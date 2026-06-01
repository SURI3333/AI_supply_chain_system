from fastapi import APIRouter
from app.services.risk_service import get_risk

router = APIRouter(prefix="/risk")

@router.get("/")
def risk():
    return get_risk()