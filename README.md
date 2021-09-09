# Project

## Installation
```shell
virtualenv .venv -p /usr/bin/python3
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```shell
python manage.py runserver 0.0.0.0:8000
```

## Docker Build
```shell
docker-compose up -d --build
```

## Docker Push Repo
```shell
docker tag <IMAGE ID> <USERNAME>/<REPOSITORY>:<TAG> 
docker push <USERNAME>/<REPOSITORY>:<TAG> 
docker run -e TZ=Asia/Bangkok -d -p 5000:5000 <IMAGE ID>
```
