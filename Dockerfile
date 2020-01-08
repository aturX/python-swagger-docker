FROM python:3.7


MAINTAINER AturX <pywizard6261@gmail.com>

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt && python setup.py install

COPY . .

CMD [ "python", "./app/main.py" ]