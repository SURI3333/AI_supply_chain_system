from fastapi import APIRouter
from app.services.simulation_service import simulate

router = APIRouter(prefix="/simulate")

@router.get("/")
def simulate_route(demand_increase: float, delay: int):
    return simulate(demand_increase, delay)