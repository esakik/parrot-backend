from http import HTTPStatus

from flask import jsonify


def handle_success(data):
    message = "Success!"
    return jsonify({"message": message, "data": data}), HTTPStatus.OK


def handle_validation_error(e):
    return jsonify({"message": e.message}), HTTPStatus.BAD_REQUEST


def handle_unauthorized_error(e):
    return jsonify({"message": e.message}), HTTPStatus.UNAUTHORIZED


def handle_unexpected_error(e):
    return jsonify({"message": e.message}), HTTPStatus.INTERNAL_SERVER_ERROR
