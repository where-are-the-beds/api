## This project allows user to track availability of beds in the US

### Technologies Used
```
Docker: Lightweight virtual machine
Flask: Lightweight web application framework
```

### Running the application locally
```
docker build . --tag where-are-the-beds-backend
docker run --rm -it -p80:80 where-are-the-beds-backend
```
Once the backend is up, open another terminal and run `curl localhost/beds`

### Debugging 
```
docker exec -it <container-id> /bin/sh
Alpine only have sh unlike ubuntu which runs in /bin/bash 
```