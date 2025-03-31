FROM python:3.11-slim
COPY requirements.txt /

RUN pip3 install -r requirements.txt

RUN mkdir /src
WORKDIR /src
COPY . /src/
CMD ["waitress-serve", "--host=0.0.0.0", "--port=5000", "app:app"]
EXPOSE 5000