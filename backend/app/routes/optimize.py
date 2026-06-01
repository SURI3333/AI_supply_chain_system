from fastapi import APIRouter
from app.services.optimization_service import optimize

router = APIRouter(prefix="/optimize")

@router.get("/")
def optimize_route(stock: float, demand: float):
    return optimize(stock, demand)