FROM python:3.11


COPY ./app/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

#if not mounting a volume
#COPY ./model/text_complexity_model.joblib /model/

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]



