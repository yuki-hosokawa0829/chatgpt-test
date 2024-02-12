#from python:3.11
FROM python:3.11-slim
WORKDIR /app
COPY ./app.py /app
COPY ./requirements.txt /app
COPY ./.env /app
RUN pip install -r requirements.txt
RUN mkdir log
EXPOSE 7860
CMD ["python", "app.py"]