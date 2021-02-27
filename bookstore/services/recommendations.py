import asyncio
import logging
import random
from sys import exit
from typing import NoReturn

from grpclib.server import Server

from bookstore.lib.recommendations import BookCategory
from bookstore.lib.recommendations import BookRecommendation
from bookstore.lib.recommendations import RecommendationResponse
from bookstore.lib.recommendations import RecommendationsBase


log = logging.getLogger(__name__)

books_by_category = {
    BookCategory.MYSTERY: [
        BookRecommendation(id=1, title="The Maltese Falcon"),
        BookRecommendation(id=2, title="Murder on the Orient Express"),
        BookRecommendation(id=3, title="The Hound of the Baskervilles"),
    ],
    BookCategory.SCIENCE_FICTION: [
        BookRecommendation(
            id=4, title="The Hitchhiker's Guide to the Galaxy"
        ),
        BookRecommendation(id=5, title="Ender's Game"),
        BookRecommendation(id=6, title="The Dune Chronicles"),
    ],
    BookCategory.SELF_HELP: [
        BookRecommendation(
            id=7, title="The 7 Habits of Highly Effective People"
        ),
        BookRecommendation(
            id=8, title="How to Win Friends and Influence People"
        ),
        BookRecommendation(id=9, title="Man's Search for Meaning"),
    ],
}


class RecommendationService(RecommendationsBase):
    """Book recommendation call override"""

    async def recommend(self, *, user_id: int = 0, category: "BookCategory" = 0, max_results: int = 0) -> RecommendationResponse:
        books_for_category = books_by_category[category]
        num_results = min(max_results, len(books_for_category))
        books_to_recommend = random.sample(
            books_for_category, num_results
        )

        return RecommendationResponse(recommendations=books_to_recommend)


async def close() -> NoReturn:
    log.info("Service stopped")
    exit(0)


async def start_server() -> NoReturn:
    HOST = "127.0.0.1"
    PORT = 50051
    server = Server([RecommendationService()])

    await server.start(HOST, PORT)
    await server.wait_closed()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    try:
        log.info("Recommendations service started")
        loop.run_until_complete(start_server())

    except KeyboardInterrupt:
        loop.run_until_complete(close())
