FROM python:3.6-slim
COPY ./requirements.txt /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
COPY ./app.py /deploy/
EXPOSE 80
ENTRYPOINT ["python", "app.py"]

