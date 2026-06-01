from fastapi import APIRouter
from app.services.anomaly_service import get_anomalies

router = APIRouter(prefix="/anomaly")

@router.get("/")
def anomaly():
    return get_anomalies()