FROM python:3.9-slim

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

# RUN export $(cat ../.env | xargs)

RUN python -m pip cache purge
RUN pip install -r requirements.txt

WORKDIR /app

RUN mkdir images
RUN mkdir resources
COPY ./src ./src 
COPY ./resources/openapi/swagger.yaml ./resources/openapi/swagger.yaml
COPY ./api_utils.py .
COPY ./main.py .
COPY ./resources/google-cred-ocr.json ./google-cred-ocr.json

CMD ["python", "main.py"]
