# python image
FROM python:3.6

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

# copy objects to the image
COPY ./model_objects /app
COPY flask_app.py ./flask_app.py
# install nltk packages
RUN python3 -c "import nltk;nltk.download('stopwords');nltk.download('punkt')"

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["flask_app.py" ]