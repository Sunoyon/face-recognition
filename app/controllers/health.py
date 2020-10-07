from app.app import v1_registry
from app.exceptions.errors import AppError
from app.schemas.response.health import HealthResponseSchema


@v1_registry.handles(rule="/health", method="GET", response_body_schema=HealthResponseSchema())
def get_health():
    return {"status": "OK"}


@v1_registry.handles(rule="/error_1", method="GET")
def get_error_1():
    raise AppError(msg="This is error with custom status code")


@v1_registry.handles(rule="/error_2", method="GET")
def get_error_2():
    err = AppError(msg="This is error with custom status code")
    err.http_status_code = 421
    raise err
