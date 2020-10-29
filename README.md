# DLIB Face Recognition Service 
A face recognition service using dlib. The service is built over flask-rebar framework.

Features:
*   Expose dlib face recognition service by REST API
*   Use underline parameters in API for both detections and recognition

Packaging:
*   Environment (dev/ prod/ test) configuration support
*   Logger configuration
*   Error management in HTTP layer
*   DTO management
*   Containerization with docker 
*   Unit test support

### Pre requisite

    python3
    build-essential 
    cmake

### Build in local

    $ pip install -r requirements.txt
    
### Run in dev mode

    $ sh run.dev.sh
    
### Run in prod mode

    $ sh run.prod.sh
    
### Swagger Documentation
    
    http://localhost:5001/v1/apidocs-ui
    
### Run unit test

    $ python -m unittest tests.controllers.recognition
    $ python -m unittest tests.services.recognition
    
### Docker

    # To build the image and up the container
    $ docker-compose up --detach
    
    # To stop the container
    $ docker-compose down