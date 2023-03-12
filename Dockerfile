FROM python:3.11

RUN apt-get update

# * create a working directory(app) for the Docker image and container
WORKDIR /app

# * install needed libs
COPY requirements/ requirements/
RUN pip install --upgrade pip
# * for deploy use only base requirements
RUN pip3 install -r requirements/base.txt

COPY src/ .

# * expose port and run the app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--port=8000", "--host", "0.0.0.0"]