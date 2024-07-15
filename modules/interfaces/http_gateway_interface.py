from __future__ import annotations

from abc import ABC, abstractmethod
from modules.dtos.response import Response
from settings import Settings


class HttpGatewayInterface(ABC):
    @abstractmethod
    async def get_info(self, key: str, cfg: Settings.Http) -> Response:
        pass
