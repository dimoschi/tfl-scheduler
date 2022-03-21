import json
from typing import List
from urllib.parse import urljoin

import requests

from app import crud, schemas
from app.api import deps
from app.core.config import settings

TFL_BASE_URL = settings.TFL_BASE_URL

DB = next(deps.get_db())


class Line:
    def __init__(self, lines=List[str], *args, **kwargs) -> None:
        self.lines = lines
        self.url_ready_lines = ",".join(self.lines)
        self.base_url = urljoin(TFL_BASE_URL, "Line/")

    def _store_to_DB(self, results: list) -> None:
        for result in results:
            line = crud.line.get(db=DB, id=result["id"])
            line_in = schemas.LineInDB(
                id=result["id"],
                name=result["name"],
                line_statuses=result["lineStatuses"],
                route_sections=result["routeSections"],
                disruptions=result["disruptions"],
                mode_id=result["modeName"],
                created=result["created"],
                modified=result["modified"],
            )
            if not line:
                crud.line.create(db=DB, obj_in=line_in)
            else:
                crud.line.update(db=DB, db_obj=line, obj_in=line_in)

    def get_basic_info(self) -> list:
        url = urljoin(self.base_url, f"{self.url_ready_lines}")
        response = requests.get(url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        self._store_to_DB(parsed_response)
        return parsed_response

    def get_route(self, service_type: str) -> list:
        url = urljoin(
            self.base_url,
            f"{self.url_ready_lines}/Route?serviceTypes={service_type}",
        )
        response = requests.get(url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        # Store results in DB
        return parsed_response

    def get_statuses(self, detail: bool = False) -> list:
        url = urljoin(self.base_url, f"{self.url_ready_lines}/Status?{detail}")
        response = requests.get(url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        # Store results in DB
        return parsed_response

    def get_distractions(self) -> list:
        url = urljoin(self.base_url, f"{self.url_ready_lines}/Disruption")
        response = requests.get(url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        # Store results in DB
        return parsed_response

    def get_arrivals(self) -> list:
        url = urljoin(self.base_url, f"{self.url_ready_lines}/Arrivals")
        response = requests.get(url)
        parsed_response = json.loads(response.content.decode("utf-8"))
        # Store results in DB
        return parsed_response
