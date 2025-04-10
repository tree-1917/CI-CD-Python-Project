# === libs === # 
import pickle 

# == Load Model Function
async def load_model(path: str): 
    """Method To Load models logic"""
    with open(path, "rb") as f: 
        return pickle.load(f)


