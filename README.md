# API de Predicción de Marketing Bancario

Este proyecto utiliza un modelo de Machine Learning para predecir si un cliente aceptará una oferta bancaria basado en varios factores. El modelo fue entrenado usando un clasificador Random Forest, y se expone mediante una API creada con FastAPI para recibir solicitudes de predicción en tiempo real.

## Estructura del Proyecto

El proyecto está dividido en tres scripts:

1. **Feature Pipeline (feature_pipeline.py)**: 
   - Carga los datos crudos.
   - Realiza el preprocesamiento y selección de características utilizando la información mutua.
   - Guarda las características y los objetivos preprocesados.

2. **Training Pipeline (training_pipeline.py)**: 
   - Carga las características preprocesadas.
   - Entrena el modelo Random Forest.
   - Guarda el modelo entrenado como un archivo `.pkl`.

3. **Batch Inference Pipeline (inference_pipeline.py)**: 
   - Carga el modelo entrenado.
   - Proporciona predicciones basadas en las características proporcionadas a través de una solicitud POST a la API.

## Uso de la API

### Instalar dependencias
Primero, debes instalar las dependencias listadas en `requirements.txt`:

```bash
pip install -r requirements.txt

Ejecutar el servidor
Para ejecutar el servidor de la API localmente:
uvicorn main:app --reload

Esto levantará el servidor en http://127.0.0.1:8000.

Realizar una predicción
Puedes enviar una solicitud POST a la API con los datos de entrada en formato JSON. Ejemplo:

{
  "age": 45,
  "education": 3,
  "housing": 1,
  "contact": 2,
  "month": 5,
  "duration": 350,
  "campaign": 2,
  "pdays": 999,
  "previous": 1,
  "poutcome": 1
}

Usa curl para hacer una solicitud POST:
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"age": 45, "education": 3, "housing": 1, "contact": 2, "month": 5, "duration": 350, "campaign": 2, "pdays": 999, "previous": 1, "poutcome": 1}'

Respuesta de la API
La API devolverá una predicción en formato JSON:

{
  "prediction": 0
}

Requerimientos del Proyecto
Python 3.8+
FastAPI
scikit-learn
pandas
numpy
Uvicorn (para ejecutar el servidor FastAPI)

Cómo contribuir
Haz un fork del repositorio.
Crea una rama nueva (git checkout -b feature/nueva-funcionalidad).
Realiza los cambios y haz un commit (git commit -am 'Agrega nueva funcionalidad').
Haz un push a la rama (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.

Licencia
Este proyecto está bajo la Licencia MIT.