import asyncio
import logging
import traceback
from sys import exit
from typing import NoReturn

from grpclib.server import Server

from bookstore.lib.green import GreenBase
from bookstore.lib.green import GreenColors
from bookstore.lib.green import GreenHexadecimal
from bookstore.lib.green import GreenResponse


log = logging.getLogger(__name__)

green_colors = GreenHexadecimal(
    hexdict={
        GreenColors.MODERN: "#9eeb34",
        GreenColors.MOLDY: "#7a8c61",
        GreenColors.PASTEL: "#3af281",
    }
)


class GreenService(GreenBase):
    """Green call override"""

    async def green(self, *args: tuple) -> GreenResponse:
        log.info("requested the green colors")

        return GreenResponse(hexadecimal=green_colors)


async def close() -> NoReturn:
    log.info("Service stopped")
    exit(0)


async def start_server() -> NoReturn:
    HOST = "127.0.0.1"
    PORT = 50052
    server = Server([GreenService()])

    await server.start(HOST, PORT)
    await server.wait_closed()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    try:
        log.info("Recommendations service started")
        loop.run_until_complete(start_server())

    except KeyboardInterrupt:
        loop.run_until_complete(close())

    except Exception:
        log.critical(traceback.format_exc())
        loop.run_until_complete(close())
