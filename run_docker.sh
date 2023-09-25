docker build -t my-flask-app -f Dockerfile .
docker container run -p 5000:5000 my-flask-app