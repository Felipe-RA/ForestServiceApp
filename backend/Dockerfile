FROM python:3.12
# latest stable version of python as 18/11/2023 https://devguide.python.org/versions/#versions

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
