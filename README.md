# Automated Terraform Deployment Documentation

## Purpose
This documentation provides an overview of deploying a Retail Banking Application container utilizing Jenkins to manage 2 Jenkins Agents running on 2 EC2 instances one of which is running Terraform to deploy a Docker image to the other. The goal is to create the necessary Terraform files with specific components and set up Jenkins for continuous integration, enabling the deployment of an application as a container across an App Load Balancer.

## Issues
No Issues encountered 

## Steps

### Step 1: Docker Image Creation
1. On an instance with Docker already installed. I created a Dockerfile and then made an image from the Deployment 7 repository. I made sure to have the image connected to my RDS database.
2. I pushed the image previously created to my docker hub repository.
   
### Step 2: Terraform Edits
  I changed the following resources to reflect the correct deployment names and tags for the Banking Application to function.
  ```
main.tf:
- #Cluster name
- #Task Definition: Family
- container_definitions:
    - name
    - image
    - containerPort
- execution_role_arn
- task_role_arn
- #ECS Service name
- container_name
- container_port

ALB.tf
- #Traget Group name
- port
- #Application Load Balancer name

```
### Step 3: Create Terraform files to build the infrastructure for 3 instances running Jenkins Terraform and Docker respectively. 
1. I created a main.tf file that would create 3 instances on a default VPC and include the following dependencies: 
```
Instance 1:
- Jenkins, software-properties-common, add-apt-repository -y ppa:deadsnakes/ppa, python3.7, python3.7-venv, build-essential, libmysqlclient-dev, python3.7-dev
Instance 2:
- Docker, default-jre, software-properties-common, add-apt-repository -y ppa:deadsnakes/ppa, python3.7, python3.7-venv, build-essential, libmysqlclient-dev, python3.7-dev
Instance 3:
- Terraform and default-jre
```
2. During this stage, I implemented a JenkinsManagerInstall.sh, DockerInstall.sh, and TerraformInstall.sh script in the User Data tags. That script will install the dependencies and enable Jenkins, Docker, and Terraform to their respective instances.
 
3. I observed the VPC.tf file and made sure the resources below were created: 
    - 2 AZ's
    - 2 Public Subnets
    - 2 Private Subnets
    - 1 NAT Gateway
    - 2 Route Table
    - Security Group Ports: 8000
    - Security Group Ports: 80
4. I observed the Terraform resources in the main.tf and ALB.tf and made sure the resources below were created: 
```
- aws_ecs_cluster
- aws_cloudwatch_log_group
- aws_ecs_task_definition
- aws_ecs_service
- aws_lb_target_group
- aws_alb
- aws_alb_listener
```
### Step 4: Edited the Jenkinsfile
1. Added my Docker Hub credentials to the Jenkinsfile.
2. Added my Bank App image name to the Jenkinsfile.

### Step 5: Added Credentials to Jenkins Manager
1. I generated an Access Token from my Docker Hub.
2. Entered in username and token into Jenkins global credentials.
3. When entering my username and password enter your Dockerhub username into the ID section.
4. Added AWS Access Key and Secret Key to the credentials under "secret text"
   
### Step 6: Made Jenkins agents
1. Followed these Steps to make an agent for the Docker instance:
    - Select "Build Executor Status"
    - Click "New Node"
    - Choose a node name that will correspond with the Jenkins agent defined in our Jenkins file
    - Select permenant Agent
    - Create the node
    - Use the same name for the name field
    - Enter "/home/ubuntu/agent1" as the "Remote root directory"
    - Use the same name for the labels field
    - Click the dropdown menu and select "only build jobs with label expressions matching this node"
    - Click the dropdown menu and select "launch agent via SSH"
    - Enter the public IP address of the instance you want to install the agent on, in the "Host" field
    - Click "Add" to add Jenkins credentials
    - Click the dropdown menu and select "select SSH username with private key"
    - Use the same name for the ID field 
    - Use "ubuntu" for the username
    - Enter directly & add the private key by pasting it into the box
    - Click "Add" and select the Ubuntu credentials
    - Click the dropdown menu and select "non verifying verification strategy"
    - Click save & check in Jenkins UI for a successful installation by clicking "Log"
  2. Repeat the steps above to make a second agent for the Terraform Instance.  
    
### Step 5: Jenkins Multibranch Pipeline
1. I downloaded the Docker Pipeline plugin on Jenkins
1. Create a Jenkins multibranch pipeline.
2. Run the Jenkinsfilev.

### Step 6: Application Testing
1. Check the application utilizing the Load Balancer URL.
2. Observed the application running.

## FAQ

### Is your infrastructure secure? if yes or no, why?

### What happens when you terminate 1 instance? Is this infrastructure fault-tolerant?

### Which subnet were the containers deployed in? 

  
### System Diagram
![image](Deployment6-IMG/DEP6.png)

### Optimization
To make this deployment more efficient, I would implement the following:

1. **Implement Autoscaling:** Set up auto-scaling groups for EC2 instances to automatically adjust the number of instances based on traffic demands.


# Bank App US-east-1a
![image](Deployment6-IMG/1stBankServer.png)
# Bank App US-east-1b
![image](Deployment6-IMG/2ndBankServer.png)
# Bank App US-west-2a
![image](Deployment6-IMG/3rdBankServer.png)
# Bank App US-west-2b
![image](Deployment6-IMG/4thBankServer.png)
# Jenkins Credential Failure
![image](Deployment6-IMG/mainbranchfailed.png)
# West Branch Successful Deploy
![image](Deployment6-IMG/westbranchdeployed.png)
# Load Balancer East
![image](Deployment6-IMG/loadbalancereast.png)
# Load Balancer West
![image](Deployment6-IMG/loadbalancerwest.png)
