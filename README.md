# LAFB-project

## Architecture
### Original Architecture
Below is the architectural design for the LAFB application in its original state.

![Original architecture](/documentation/original_architecture.png) 

### New Architecture
The new architectural design for the updated application is shown below.

![New architecture](/documentation/new_architecture.png)
Service (port): description
* **Mongo (port 27017)**: the database
* **Db_Connector (port 5001)**: communicates with the mongo database
* **Prize_Generator (port 5002)**: When an account is created this service is responsible for generating a prize, sending HTTP GET request to the notification_server if someone wins a prize and HTTP POST request to the db_connector when an account is created
* **Notification_Server (port 9000)**: a notification is sent here when a member has won a prize
* **Server (port 8084)**: communicates to the three micro-services - Number_Generator, Text_Generator, Prize_Generator
* **Number_Generator (port 9017)**:  microservice responsible for generating the numbers of an account number i.e. AH*2345678*
* **Text_Generator (port 9018)**: microservice responsible for generating the letters of an account number i.e. *AH*12345678
* **Static Website (port 8089)**: sends HTTP POST requests to the server when an account is created
* **Nginx (port 80)**: this re-directs traffic to the appropriate location (i.e. Static_Website and Server)

## CI Pipeline

![Pipeline image](/documentation/pipeline_image.png)
Above is the CI pipeline, when a user makes a change to the source code and pushes it to a global repository in Github, a webhook will detect this change and trigger a Jenkins job which will rebuild the images and push them to Dockerhub.  The images of each deployment are now updated in the Swarm enabling seamless changes to the application without disruption to the service provided. (For example, the value of one of the rewards can be changed, and when it is pushed the implementation will be reflected on the application.)

## Set-up
### Prerequisites:
* Microsoft Azure account

1. Log into your Azure account
2. Navigate to the portal and open a new cloud shell

To create a Swarm with one manager node and one worker node, you will first need to create two virtual machines(VMs) to connect to each other. Both machines must have Docker installed on them.

### Creating Virtual Machines

```
az configure --defaults location=uksouth

# Creates a new resource group 
az group create --name myResourceGroup

# Creates a manager node
az vm create --resource-group myResourceGroup --name manager --image UbuntuLTS --generate-ssh-keys

# Creates a worker node
az vm create --resource-group myResourceGroup --name worker --image UbuntuLTS --generate-ssh-keys
```
You can now SSH onto your machines (e.g. ```ssh username@51.145.54.189```, where your username and ip address will be different) and install docker on both

Note: You can navigate to your VM in the portal where you will be able to locate your IP address.

### Installing docker on Linux
```
sudo apt update
sudo apt install docker.io -y

sudo usermod -aG docker $(whoami)

# You will need to restart your cloud shell ans SSH into your machine.

sudo systemctl start docker
sudo systemctl enable docker
```

### Installing docker-compose on Linux
Next install docker-compose on your manager VM.
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```
### Docker Swarm
#### Deploying Application with Docker Swarm

Before we you get started you need to download the LAFB project into your manager VM , which can be accessed from the public GitHub repository https://github.com/Thi6/LAFB-project.git
```
cd ~
git clone https://github.com/Thi6/LAFB-project.git
cd LAFB-project
```

On the Manager VM set up the Swarm cluster by running this command:
```
docker swarm init
```

To get the command that allows a worker node to join the swarm enter the following in the Manager node:
```
docker swarm join-token worker
```

To allow a worker node to join the swarm, on the worker VM run a command similar to the follwing (this is generated by the above command):
```
docker swarm join --token [TOKEN] [IP_ADDRESS]
```

 
* As we will now be managing the Swarm, make sure you are working on the manager VM.
In order to deploy this project in swarm mode, all the images needs to be created.

```
cd ~/LAFB-project
docker-compose build
```

* The stack can now be deployed, the following command creates a stack of services based on the services described in docker-compose.yaml file
```
docker stack deploy --compose-file docker-compose.yaml LAFB
```

Check that the stack is running:
```
docker stack services LAFB
```
Under the ```REPLICAS``` column, you should see ```1/1``` for all the services. This may take a while as all the images need to be pulled from the registry.

You can now see the application deployed by entering the public IP address of your manager VM into a web browser.
![Landing_page](/documentation/landing_page.png)

Note: You may need to expose the port of your Nginx container (port 80) in your portal. First find the manager VM in the portal and locate the networking section and you can add inbound ports this way. 

#### Swapping Microservice Implementations
The images below can be swapped out during deployment:
* text generation service
	- thi6/textgen:2 (default)
		- randomly generates a string of 2 uppercase characters for a user's account number
	- thi6/textgen:3
		- randomly generates a string of 3 lowercase characters for a user's account number
* number generation service
	- thi6/numgen:6 (default)
		- randomly generates a 6 digit number for a user's account number
	- thi6/numgen:8
		- randomly generates a 8 digit number for a user's account number
* prize generation service
	- thi6/prizegen:bigprize (default)
	- thi6/prizegen:smallprize

During deployment, you can swap out any of the above implementations by using the following command:
```
docker service update --image [image_name:image_tag] [service_name]
```
For example:
```docker service update --image thi6/textgen:3 LAFB_text_gen```

Note: 
You can obtain the list of service names by using this command:
```
docker service list
```
