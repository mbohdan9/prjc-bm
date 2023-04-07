from fastapi import FastAPI
from joblib import load
from pydantic import  BaseModel, constr


text_complexity_model = load('/model/text_complexity_model.joblib')

def get_prediction(excerpt):
    x = [excerpt]
    y = text_complexity_model.predict(x)[0]
    return {'target': y}

app = FastAPI()


class ModelParams(BaseModel):
    excerpt: constr(min_length=1)


@app.post("/predict")
def predict(params: ModelParams):
    return get_prediction(params.excerpt)
 
