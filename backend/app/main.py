from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import forecast, risk, optimize, anomaly, simulation

app = FastAPI(title="AI Supply Chain System")

# ✅ CORS FIX (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ ROUTES
app.include_router(forecast.router)
app.include_router(risk.router)
app.include_router(optimize.router)
app.include_router(anomaly.router)
app.include_router(simulation.router)

@app.get("/")
def root():
    return {"message": "API Running"}
