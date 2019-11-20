from flask import Blueprint

from src.adapters.controllers.handlers.handler import handle_validation_error, handle_unexpected_error
from src.exception.errors import ValidationError, UnexpectedError

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(ValidationError)
def validation_error(error):
    return handle_validation_error(error)


@errors.app_errorhandler(UnexpectedError)
def unexpected_error(error):
    return handle_unexpected_error(error)
