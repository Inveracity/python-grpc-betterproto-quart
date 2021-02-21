from grpclib.client import Channel
from quart import Quart
from quart import render_template

from bookstore.lib.recommendations import BookCategory
from bookstore.lib.recommendations import RecommendationsStub


app = Quart(__name__)


async def rec() -> dict:
    channel = Channel(host="127.0.0.1", port=50051)
    service = RecommendationsStub(channel)
    response = await service.recommend(user_id=1, category=BookCategory.MYSTERY, max_results=3)
    channel.close()
    return response.to_dict()


@app.route("/")
async def hello() -> None:
    res = await rec()
    return await render_template("homepage.html", **res)


if __name__ == "__main__":
    app.run(debug=True)
