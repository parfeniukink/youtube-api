FROM python:3.7
RUN pip install pipenv
RUN mkdir /code
COPY Pipfile* /code/
WORKDIR /code
RUN pipenv install --system --deploy --ignore-pipfile
ADD . /code/
