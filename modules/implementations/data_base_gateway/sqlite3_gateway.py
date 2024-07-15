import aiosqlite

from modules.dtos.response import Response
from modules.interfaces.data_base_gateway_interface import DataBaseGatewayInterface
from settings import Settings


class SQLiteDataBaseAsyncGateway(DataBaseGatewayInterface):
    def __init__(self, db_file_path: str, username: str = None, password: str = None):
        self._db_file_path = db_file_path
        self._username = username  # todo need?
        self._password = password  # todo need?
        self._connection = None

    async def get_info(self, key: str, cfg: Settings.DataBase) -> Response:
        try:
            async with aiosqlite.connect(self._db_file_path) as db:
                cursor = await db.cursor()
                await cursor.execute(f"SELECT * FROM ? WHERE key = ?", (cfg.table, key,))
                row = await cursor.fetchone()

                if row:
                    columns = [description[0] for description in cursor.description]
                    info = {columns[i]: row[i] for i in range(len(columns))}
                    return Response(success=True, info=info)
                else:
                    return Response(success=False, info={"error": f"Key '{key}' not found in table '{cfg.table}'"})

        except aiosqlite.Error as e:
            return Response(success=False, info={"error": f"aiosqlite error: {str(e)}"})
