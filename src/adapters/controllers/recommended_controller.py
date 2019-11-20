from flask import Blueprint, request

from src.adapters.controllers.handlers.handler import handle_success
from src.request_objects.recommended.get_recommended_request import GetRecommendedRequest
from src.use_cases.recommended.impl.get_recommended_use_case import GetRecommendedUseCase

recommended = Blueprint("recommended", __name__, url_prefix="/recommended")


@recommended.route("/list", methods=["GET"])
def recommended_list():
    if request.method == "GET":
        limit = request.args.get("limit")
        offset = request.args.get("offset")

        req = GetRecommendedRequest(limit, offset)
        get_recommended = GetRecommendedUseCase()

        res = get_recommended.handle(req)

        return handle_success(res)
