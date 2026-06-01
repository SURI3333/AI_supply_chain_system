from fastapi import APIRouter
from app.services.forecasting_service import forecast_inventory

router = APIRouter(prefix="/forecast")

@router.get("/")
def get_forecast(days: int = 30):
    return forecast_inventory(days)