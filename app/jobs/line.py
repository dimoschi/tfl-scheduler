import json
from typing import List
from urllib.parse import urljoin

import requests

from app import crud, schemas
from app.api import deps
from app.core.config import settings
from app.models.task_result import TaskResult

TFL_BASE_URL = settings.TFL_BASE_URL

DB = next(deps.get_db())


class LineJob:
    def __init__(self, task_id: int, lines: List[str], *args, **kwargs) -> None:
        self.lines = lines
        self.task_id = task_id
        self.url_ready_lines = ",".join(self.lines)
        self.base_url = urljoin(TFL_BASE_URL, "Line/")

    def _store_to_DB(
        self, line_result: dict, line_disruption_results: List[dict] = None
    ) -> List[TaskResult]:
        task_results = list()

        line_in = schemas.LineCreate(
            tfl_id=line_result["id"],
            tfl_name=line_result["name"],
            line_statuses=line_result["lineStatuses"],
            route_sections=line_result["routeSections"],
            disruptions=line_result["disruptions"],
            mode_id=line_result["modeName"],
            created=line_result["created"],
            modified=line_result["modified"],
        )
        line_created = crud.line.create(db=DB, obj_in=line_in)

        if line_disruption_results:
            for line_disruption_result in line_disruption_results:
                disruption_in = schemas.LineDisruptionCreate(
                    category=line_disruption_result["category"],
                    category_description=line_disruption_result["categoryDescription"],
                    type=line_disruption_result["type"],
                    description=line_disruption_result["description"],
                    affected_routes=line_disruption_result["affectedRoutes"],
                    affected_stops=line_disruption_result["affectedStops"],
                    closure_text=line_disruption_result["closureText"],
                )
                line_disruption_created = crud.line_disruption.create(
                    db=DB, obj_in=disruption_in
                )

                task_resultn_in = schemas.TaskResultCreate(
                    task_id=self.task_id,
                    line_id=line_created.id,
                    line_disruption_id=line_disruption_created.id
                    if line_disruption_created
                    else None,
                )
                task_result = crud.task_result.create(db=DB, obj_in=task_resultn_in)
                task_results.append(task_result)
        else:
            task_resultn_in = schemas.TaskResultCreate(
                task_id=self.task_id, line_id=line_created.id
            )
            task_result = crud.task_result.create(db=DB, obj_in=task_resultn_in)
            task_results.append(task_result)
        return task_results

    def _get_lines(self) -> list:
        url = urljoin(self.base_url, f"{self.url_ready_lines}")
        response = requests.get(url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        return parsed_response

    def _get_routes(self, service_type: str) -> list:
        url = urljoin(
            self.base_url,
            f"{self.url_ready_lines}/Route?serviceTypes={service_type}",
        )
        response = requests.get(url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        return parsed_response

    def _get_statuses(self, detail: bool = False) -> list:
        url = urljoin(self.base_url, f"{self.url_ready_lines}/Status?{detail}")
        response = requests.get(url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        return parsed_response

    def _get_disruptions(self) -> list:
        url = urljoin(self.base_url, f"{self.url_ready_lines}/Disruption")
        response = requests.get(url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        return parsed_response

    def _get_disruption(self, line: str) -> list:
        url = urljoin(self.base_url, f"{line}/Disruption")
        response = requests.get(url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        return parsed_response if parsed_response else None

    def _get_arrivals(self) -> list:
        url = urljoin(self.base_url, f"{self.url_ready_lines}/Arrivals")
        response = requests.get(url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        return parsed_response

    def schedule_task(self, *args, **kwargs) -> None:
        lines = self._get_lines()
        for line in lines:
            disruption = self._get_disruption(line=line["id"])
            self._store_to_DB(line, disruption)
