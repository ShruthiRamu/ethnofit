# Ethnofit

## Using Docker Image
docker stop ethnofit-app

docker container rm ethnofit-app

docker  build . -t ethnofit-app:latest --no-cache=true

docker run -d --name ethnofit-app -p 8080:8080 ethnofit-app

http://localhost:8080/

## Using The App In Local

streamlit run demo_app/main.py

## To get inside the docker 

docker exec -it ethnofit-app bash

