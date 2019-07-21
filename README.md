# LAFB-project

## Architecture
### Original Architecture
Below is the architectural design for the LAFB application in its original state.
![Original architecture](/documentation/original_architecture.png) 

### New Architecture
The new architectural design for the updated application is shown below.
![New architecture](/documentation/new_architecture.png)
Service (port): description
*	Mongo (port 27017): the database
*	Db_Connector (port 5001): communicates with the mongo database
*	Prize_Generator (port 5002): When an account is created this service is responsible for generating a prize, sending HTTP GET request to the notification_server if someone wins a prize and HTTP POST request to the db_connector when an account is created
*	Notification_Server (port 9000): a notification is sent here when a member has won a prize
*	Server (port 8084): communicates to the three micro-services - Number_Generator, Text_Generator, Prize_Generator
*	Number_Generator (port 9017):  microservice responsible for generating the numbers of an account number i.e. AH12345678
*	Text_Generator (port 9018): microservice responsible for generating the letters of an account number i.e. AH12345678
*	Static Website (port 8089): sends HTTP POST requests to the server when an account is created
*	Nginx (port 80): this re-directs traffic to the appropriate location (i.e. Static_Website and Server)

## CI Pipeline
![Pipeline image](/documentation/pipeline_image.png)
Above is the CI pipeline, when a user makes a change to the source code and pushes it to a global repository in Github, a webhook will detect this change and trigger a Jenkins job which will rebuild the images and push them to Dockerhub.  The images of each deployment are now updated in the Swarm enabling seamless changes to the application without disruption to the service provided. (For example, the value of one of the rewards can be changed, and when it is pushed the implementation will be reflected on the application.)
