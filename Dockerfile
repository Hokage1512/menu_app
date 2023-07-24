FROM python:3.11-slim

RUN mkdir /menu_app

COPY requirements.txt /menu_app/requirements.txt

COPY . /menu_app

RUN pip install -r /menu_app/requirements.txt --no-cache-dir

WORKDIR /menu_app

EXPOSE 8000

CMD ["python", "main.py"]