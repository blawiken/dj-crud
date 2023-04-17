FROM python:3.11

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

COPY . /src

ENV SECRET_KEY=890fdfNJDFsad223218!sddlfm432)sadasd12
ENV ALLOWED_HOSTS=127.0.0.1

WORKDIR src

RUN python manage.py migrate

EXPOSE 8888

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stocks_products.wsgi"]