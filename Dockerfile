FROM python:3.11-slim

# Container User
RUN useradd --create-home --shell /bin/bash python
USER python
WORKDIR /home/python

# Package
COPY requirements.txt /home/python
RUN pip install -r requirements.txt

# Application File
COPY app.py /home/python

# Setting PATH
ENV PATH="/home/python/.local/bin:$PATH"

# Port
EXPOSE 80

# Worker Count = 1, run by uvicorn
CMD ["fastapi", "run", "app.py", "--port", "80"]