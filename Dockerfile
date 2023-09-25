# base image
FROM python:3.11.5-bullseye 
# which container the app is running in
WORKDIR /app
# copy requirements.txt into /app
COPY requirements.txt .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt 
# copy everything into /app
COPY . .
# set the environment var for port
ENV FLASK_RUN_HOST=0.0.0.0
# expose the port
EXPOSE 5000
# command to start the app
CMD ["flask", "run"]