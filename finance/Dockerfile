

FROM python:3.10

# Установка pipenv
RUN pip install pipenv
COPY Pipfile Pipfile.lock .env ./
WORKDIR /finance
COPY . .

# Установка зависимостей
RUN pipenv install


