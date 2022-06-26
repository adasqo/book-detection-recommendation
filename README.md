# Book detector project setup
This readme file will present the way to set-up project and run it locally on your machine with use of Docker.
## Prerequisites
### Package installment
In order to run the project, make sure you downloaded the following tools:
- [Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-debian-10) to run containers with working program.
- [Docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-debian-10) to start and manage all docker containers.
### Google Cloud setup
Project uses [Google OCR Vision OCR API](https://cloud.google.com/vision/docs/ocr) for text recognition. In order to run the program, you need to have a Google Cloud account (free to start and use for 3 months), create project, enable API and create OCR Vision API key. For more information, [see](https://cloud.google.com/vision/docs/setup) and follow this instruction to do all described steps.
## Setup
### Setup you Google Cloud API key
In order for application to start, move you Google Cloud API key (generated in previous step) to /server/resources/ directory and rename it to *google-cred-ocr.json*. (Important: never pull your key to the repo with git push!).
### Export environmental variabls
For your project root directory, run ```export $(cat .env | xargs)``` in your terminal to export all environmental variables from .env file. 
### Start application
Start application with ```docker-compose up``` ran from your root project directory. Go to [localhost](http://localhost) to use application.