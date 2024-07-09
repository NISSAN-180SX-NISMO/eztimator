from dataclasses import dataclass
from abc import ABC
from typing import Dict


@dataclass
class Response(ABC):
    success: bool
    info: Dict[str, str]


@dataclass
class DataBaseResponse(Response):
    pass


@dataclass
class HttpResponse(Response):
    status_code: int
