# app/predict_schema.py

from pydantic import BaseModel
from typing import List

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
