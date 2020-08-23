## This project allows user to track availability of beds in the US

### Running the application
```
docker build . --tag where-are-the-beds-backend
docker run --rm -it -p80:80 where-are-the-beds-backend
```
Once the backend is up, open another terminal and run `curl localhost/beds`