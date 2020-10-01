Application To AWS

This application is a simple example on how I would deploy to AWS from GitHub.

Project Setup
This application was built in Flask, with templates written in HTML and CSS.

The application uses Docker images for the application and a MongoDB database.

There is also a Terraform file, for setting up the Application Load Balancer. This is manually activated at the moment.

The next step would be to deploy to AWS

Local usage

To run in a local development environment, `cd` to the folder and run the Dockerimage as follows:

`docker-compose up -d`

-d brings us to detached mode, so if you want to check it is running before going further,
simply type `docker ps` to see if it is running.
