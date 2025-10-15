from fastapi import APIRouter, status
from .models.health import Health

router = APIRouter(
    prefix='/api/ping',
    tags=['Health Check']
)

@router.get('/', response_model=Health, status_code=status.HTTP_200_OK)
def health_check() -> str:
    return Health
