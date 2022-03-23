from asyncio.log import logger
from typing import Any, List

import sqlalchemy as sa
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.jobs.line import LineJob
from app.scheduler import scheduler

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=List[schemas.Task])
def read_tasks(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve tasks.
    """
    tasks = crud.task.get_multi(db, skip=skip, limit=limit)
    return tasks


# , response_model=schemas.Task
@router.post("/")
def create_task(
    *,
    db: Session = Depends(deps.get_db),
    task_in: schemas.TaskCreate,
) -> Any:
    """
    Create new task.
    In case schedule_time is missing it is executed immediately.
    """
    task = crud.task.create(db=db, obj_in=task_in)
    line = LineJob(task_id=task.id, lines=task.lines)
    job = scheduler.add_job(line.schedule_task, "date", run_date=task_in.schedule_time)
    # TODO: Get job from id and check if it exists in DB
    job = crud.job.get(db=db, id=job.id)
    if task.schedule_time and job:
        task_update = schemas.TaskUpdateInternal(job_id=job.id)
        try:
            task = crud.task.update(db=db, db_obj=task, obj_in=task_update)
        except sa.exc.IntegrityError:
            logger.warn("Job executed already")

    return task


@router.patch("/{id}", response_model=schemas.Task)
def update_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    task_in: schemas.TaskUpdate,
) -> Any:
    """
    Update a task.
    """
    task = crud.task.get(db=db, id=id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task = crud.task.update(db=db, db_obj=task, obj_in=task_in)

    # Check if schedule_time has been updated
    # and is different with the one we already have stored in DB.
    if task_in.schedule_time and (task_in.schedule_time != task.schedule_time):
        # If job_id exists in task use it to update the scheduled job,
        # else create a new job using the updated schedule_time
        if task.job_id:
            job = crud.job.get(task.job_id)
            scheduler.reschedule_job(job.id, "date", run_date=task_in.schedule_time)
        else:
            line = LineJob(task_id=task.id, lines=task.lines)
            job = scheduler.add_job(
                line.schedule_task, "date", run_date=task_in.schedule_time
            )
            task_update = schemas.TaskUpdateInternal(job_id=job.id)
            try:
                task = crud.task.update(db=db, db_obj=task, obj_in=task_update)
            except sa.exc.IntegrityError:
                logger.warn("Job executed already")
    # If schedule_time is None in PATCH and the task has a schedule time,
    # then the scheduled job must be removed.
    elif task_in.schedule_time is None and task.schedule_time:
        if task.job_id:
            job = crud.job.get(task.job_id)
            scheduler.remove_job(job.id)

    return task


@router.get("/results/{id}", response_model=List[schemas.TaskResult])
def read_task_results(*, db: Session = Depends(deps.get_db), id: str) -> Any:
    """
    Get task results by task ID.
    """
    task_results = crud.task_result.get_by_task_id(db=db, task_id=id)
    if not task_results:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_results


@router.get("/{id}", response_model=schemas.Task)
def read_task(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
) -> Any:
    """
    Get task by ID.
    """
    task = crud.task.get(db=db, id=id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{id}", response_model=schemas.Task)
def delete_task(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a task.
    """
    task = crud.task.get(db=db, id=id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    try:
        scheduler.remove_job(task.job.id)
    except AttributeError:
        task = crud.task.remove(db=db, id=id)
    return task
