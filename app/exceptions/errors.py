from flask_rebar.errors import HttpJsonError


class AppError(HttpJsonError):
    http_status_code, default_message = 430, "Error with custom status code"


class AppImageProcessingError(HttpJsonError):
    http_status_code, default_message = 421, "Failed to process image."
