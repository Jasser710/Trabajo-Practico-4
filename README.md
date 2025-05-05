# Clasificación de Flores con FastAPI y Modelo de IA

Este proyecto implementa una API REST usando FastAPI que permite predecir la especie de una flor Iris utilizando un modelo de aprendizaje automático (RandomForestClassifier) previamente entrenado.

## Estructura del proyecto

- app/main.py: define la API y los endpoints.
- app/model.py: script que entrena el modelo y lo guarda como iris_model.pkl.
- app/schema.py: esquema de entrada para la predicción usando Pydantic.
- iris_model.pkl: archivo generado con el modelo entrenado.
- Dockerfile: permite contenerizar la aplicación.
- .github/workflows/train_model.yml: workflow de GitHub Actions para reentrenar el modelo automáticamente.
- requirements.txt: dependencias del proyecto.

## Uso de la API

### Endpoint principal

POST /predict: recibe los datos de una flor y devuelve su especie predicha.

Ejemplo de entrada (JSON):

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

Ejemplo de salida:

{
  "prediccion": "setosa"
}

### Endpoint de prueba

GET /: retorna un mensaje básico para verificar que la API está activa.

## Variables de entrada del modelo

- sepal_length (float)
- sepal_width (float)
- petal_length (float)
- petal_width (float)

## Salida del modelo

- prediccion: especie de la flor (setosa, versicolor o virginica)

## Instrucciones para correr localmente

1. Clonar el repositorio:

git clone https://github.com/Jasser710/Trabajo-Practico-4.git  
cd nombre-del-repositorio

2. Crear un entorno virtual (opcional pero recomendado):

python -m venv venv  
source venv/bin/activate  (En Windows: venv\Scripts\activate)

3. Instalar dependencias:

pip install -r requirements.txt

4. Entrenar el modelo (opcional si ya existe iris_model.pkl):

python model.py

5. Ejecutar la API:

uvicorn main:app --reload

## Automatización con GitHub Actions

El proyecto incluye un flujo de trabajo en .github/workflows/train_model.yml que:

- Se ejecuta automáticamente al hacer push a main.
- Reentrena el modelo desde cero usando model.py.
- Usa un secret (DUMMY_SECRET) para simular el uso seguro de credenciales.

## Docker

La imagen de la API está lista para ser construida con Docker. Comando de ejemplo:

docker build -t iris-api .  
docker run -d -p 8000:8000 iris-api

## Autor

Jasser Palacios  
https://github.com/Jasser710
