FROM python:3.9-slim

RUN useradd --create-home --shell /bin/bash python

USER python
WORKDIR /home/python

COPY requirements.txt .
COPY app.py .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]