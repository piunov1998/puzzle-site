FROM python:3.10

COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

COPY . /app

WORKDIR /app

CMD python3 app.py
