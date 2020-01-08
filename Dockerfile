FROM python:3.7


MAINTAINER AturX <pywizard6261@gmail.com>

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app/main.py" ]