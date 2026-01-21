# calculation functions
#for example

def predict_score(data: dict):
    score = sum(len(str(v)) for v in data.values()) 
    return {"score": score, "status": "success"}