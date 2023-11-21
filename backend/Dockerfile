FROM python:3.11
# latest stable version of python as 18/11/2023 https://devguide.python.org/versions/#versions
# which is explicitly compatible with fastapi  and over 65.3% of the 360 popular packages https://pyreadiness.org/3.11/

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
