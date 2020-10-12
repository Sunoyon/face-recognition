# DLIB Face Recognition Service 
A face recognition service using dlib. The service is built over flask-rebar framework.

Features:
*   Expose dlib face recognition by REST API service
*   Use of underline parameters for both detections and recognition
*   Configuration management for environments: dev/ prod/ test
*   Logger configuration
*   Error management in HTTP layer
*   DTO management
*   Containerization with docker # TODO

### Pre requisite

    python3
    build-essential 
    cmake

### Build

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