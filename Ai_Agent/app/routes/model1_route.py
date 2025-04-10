# === libs === # 
from fastapi import APIRouter 
from pydantic import BaseModel
from app.utils.load_models import load_model 


# == load model
model = load_model("/app/models/model1.pkl")
router = APIRouter()

# == Input Schema 
class InputData(BaseModel):
    age: int 
    height: float 

@router.post("/predict/weight")
async def predic_weight(data: InputData):
    prediction = model.predict([[data.age, data.height]])
    return {"predicted_weight": prediction[0]}
