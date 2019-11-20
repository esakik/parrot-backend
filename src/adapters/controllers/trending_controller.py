from flask import Blueprint, request

from src.adapters.controllers.handlers.handler import handle_success
from src.request_objects.trending.get_trending_request import GetTrendingRequest
from src.use_cases.trending.impl.get_trending_use_case import GetTrendingUseCase

trending = Blueprint("trending", __name__, url_prefix="/trending")


@trending.route("/list", methods=["GET"])
def trending_list():
    if request.method == "GET":
        limit = request.args.get("limit")
        offset = request.args.get("offset")

        req = GetTrendingRequest(limit, offset)
        get_trending = GetTrendingUseCase()

        res = get_trending.handle(req)

        return handle_success(res)
