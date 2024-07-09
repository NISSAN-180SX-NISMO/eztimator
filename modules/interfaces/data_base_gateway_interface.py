from __future__ import annotations

from abc import ABC, abstractmethod
from modules.dtos.response import Response


class DataBaseGatewayInterface(ABC):
    @abstractmethod
    async def get_info(self, key: str, table: str) -> Response:
        pass
