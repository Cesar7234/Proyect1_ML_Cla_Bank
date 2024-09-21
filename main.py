from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# Definir la estructura de los datos de entrada usando Pydantic
class PredictionInput(BaseModel):
    age: int
    education: int
    housing: int
    contact: int
    month: int
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: int

# Cargar el modelo entrenado
def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

# Crear la aplicación FastAPI
app = FastAPI()

# Cargar el modelo al iniciar la aplicación
model = load_model('model.pkl')

# Endpoint de bienvenida
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de predicción"}

# Endpoint para hacer predicciones
@app.post("/predict")
def predict(input_data: PredictionInput):
    # Convertir los datos de entrada en un DataFrame
    input_df = pd.DataFrame([input_data.dict()])
    
    # Hacer predicción
    prediction = model.predict(input_df)
    
    # Devolver la predicción
    return {"would_open_term_deposit_acount": int(prediction[0])}
