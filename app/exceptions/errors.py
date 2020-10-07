from flask_rebar.errors import HttpJsonError


class AppError(HttpJsonError):
    http_status_code, default_message = 430, "Error with custom status code"

    def __init__(self, status_code, message):
        self.http_status_code = status_code
        self.default_message = message
