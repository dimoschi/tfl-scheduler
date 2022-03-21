from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import utc

from app.core.config import settings

jobstores = {"default": SQLAlchemyJobStore(url=settings.SQLALCHEMY_DATABASE_URI)}
executors = {"default": ThreadPoolExecutor(20), "processpool": ProcessPoolExecutor(5)}
job_defaults = {"coalesce": False, "max_instances": 3}
scheduler = AsyncIOScheduler(
    jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc
)
