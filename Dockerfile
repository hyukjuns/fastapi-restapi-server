FROM python:3.11-slim

RUN useradd --create-home --shell /bin/bash python

USER python
WORKDIR /home/python

COPY requirements.txt .
COPY ./*.py .

RUN pip install -r requirements.txt

# Setting PATH
ENV PATH="/home/python/.local/bin:$PATH"

EXPOSE 8080

CMD ["fastapi", "run", "app.py"]