FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

# RUN pip install pycaret[full] pandas shap
RUN pip install jinja2
# RUN pip install markupsafe==2.0.1
# RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app /app
COPY ./data /data
COPY ./templates /templates

