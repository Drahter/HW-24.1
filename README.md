# Learning service

Project created for learning purposes.

## Install 

The instruction assume that you have already installed [Docker](https://docs.docker.com/installation/) and [Docker Compose](https://docs.docker.com/compose/install/). 



    
    git clone https://github.com/Drahter/HW-24.1.git

## How to get up and running

Once you've cloned the project to your host we can now start our demo project. Easy! Navigate to the directory in which you cloned the project. Run the following commands from this directory 

    docker-compose up -d --build

The  docker-compose command will pull the images from Docker Hub and then link them together based on the information inside the docker-compose.yml file. This will create ports, links between containers, and configure applications as requrired. After the command completes we can now view the status of our stack

    docker-compose ps