# Project of robot explorer with Raspberry Pi 

## Backed
This is the backend of the project. It is a REST API that allows to control the robot and to get the data from the sensors.

### Installation
To install the backend, you need to install the dependencies with the following command:
```bash
pip install -r requirements.txt
```

### Usage
To launch the backend, you need to run the following command:
```bash
python3 server.py
```

### API
The API url is: http://localhost:5000/api/v1.0/

## Docker
Build image
```bash
docker build -f backend/Dockerfile -t backend_tracking .
```

Run image
```bash
docker run -it --rm --privileged -p 8000:8000 backend_tracking
```
