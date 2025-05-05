# app/main.py

from fastapi import FastAPI
from app.schema import IrisInput
import joblib
import numpy as np

app = FastAPI()

# Cargar modelo entrenado
model = joblib.load("iris_model.pkl")

@app.get("/")
def root():
    return {"mensaje": "API para clasificar flores con modelo de IA"}

@app.post("/predict")
def predict_species(data: IrisInput):
    input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(input_data)[0]
    species = ["setosa", "versicolor", "virginica"]
    return {"prediccion": species[prediction]}
