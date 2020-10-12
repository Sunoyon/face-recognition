from app.app import v1_registry
from app.exceptions.errors import AppError
from app.schemas.response.health import HealthResponseSchema


@v1_registry.handles(rule="/health", method="GET", response_body_schema=HealthResponseSchema())
def get_health():
    return {"status": "OK"}
