from grpclib.client import Channel
from quart import Quart
from quart import render_template

from bookstore.lib.green import GreenColors
from bookstore.lib.green import GreenStub
from bookstore.lib.recommendations import BookCategory
from bookstore.lib.recommendations import RecommendationsStub


app = Quart(__name__)


async def rec() -> dict:
    recommendations_channel = Channel(host="127.0.0.1", port=50051)
    service = RecommendationsStub(recommendations_channel)
    response = await service.recommend(user_id=1, category=BookCategory.MYSTERY, max_results=3)
    recommendations_channel.close()

    return response.to_dict()


async def green() -> dict:
    green_channel = Channel(host="127.0.0.1", port=50052)
    service = GreenStub(green_channel)
    response = await service.green()
    green_channel.close()
    print(response.to_dict())
    return response.to_dict()


@app.route("/favicon.ico")
async def fav() -> None:
    return "ok", 200


@app.route("/")
@app.route("/<color>")
async def hello(color: str = "modern") -> None:
    res = await rec()
    green_color = await green()
    res["color"] = green_color["hexadecimal"][0]["hexdict"][GreenColors[color.upper()].value]
    return await render_template("homepage.html", **res)


if __name__ == "__main__":
    app.run(debug=True)
