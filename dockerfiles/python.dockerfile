FROM jupyter/pyspark-notebook

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8888

#CMD [ "npm", "start" ]

