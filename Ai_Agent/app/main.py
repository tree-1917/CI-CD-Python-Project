# === libs === # 
from fastapi import FastAPI 
from app.routes import model1_route

# == App
app = FastAPI(
        title="Health Mate ML API", 
        description="API for ML Model", 
        version="0.0.1"
        )

# == Routes 
app.include_router(model1_route.router)

