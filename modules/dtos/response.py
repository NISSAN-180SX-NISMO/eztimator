from dataclasses import dataclass
from abc import ABC
from modules.aliases.aliases import InfoStruct


@dataclass
class Response(ABC):
    success: bool
    info: InfoStruct


@dataclass
class DataBaseResponse(Response):
    pass


@dataclass
class HttpResponse(Response):
    status_code: int
