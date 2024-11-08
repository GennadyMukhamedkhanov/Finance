FROM python:3.10
RUN pip install pipenv
WORKDIR /finance
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --ignore-pipfile
COPY . .
CMD ["pipenv", "run", "python", "manage.py", "runserver"]