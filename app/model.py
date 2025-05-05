# app/model.py

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_and_save_model():
    # Cargar datos
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)

    # Entrenar modelo
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Guardar modelo entrenado
    joblib.dump(model, "iris_model.pkl")

if __name__ == "__main__":
    train_and_save_model()
