#Application To AWS

This application is a simple example on how I deploy to AWS from GitHub.

#Project Setup
This application was built in Flask, with templates written in HTML and CSS.

The application uses Docker images for the application and a MongoDB database.

There is a pipeline set up on this, allowing for integration with GitHub. Whenever a branch is pulled to Main, the 
pipeline is triggered and deployment to AWS begins.

There is also a Terraform file, for setting up the Application Load Balancer. This is manually activated at the moment.