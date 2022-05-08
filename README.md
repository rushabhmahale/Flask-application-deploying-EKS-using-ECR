# Flask-application-deploying-EKS-using-ECR


## Flask:
Flask is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.

## What is EKS(Elastic Kubernetes Service):
Amazon Elastic Kubernetes Service (Amazon EKS) is a managed Kubernetes service that makes it easy for you to run Kubernetes on AWS and on-premises. Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.

## What is ECR:
Amazon Elastic Container Registry (Amazon ECR) is an AWS managed container image registry service that is secure, scalable, and reliable. Amazon ECR supports private repositories with resource-based permissions using AWS IAM. This is so that specified users or Amazon EC2 instances can access your container repositories and images.

## What we will do:
- Create a flask application 
- Create Dockerfile and push to ECR (Elastic Container Registry)
- Create manifest for deploying application in EKS (Elastic Kubernetes Service) here the cluster will be private 

## Steps to be followed:
## Step1 Create a flask application <br>
  first we will create Ec2 instance :- 
- Choose an Amazon Machine Image (AMI)
- Choose an Instance Type, choose Next: Configure Instance Details.
- Configure Instance Details
- Choose Next: Add Storage.
- Next: Add Tags.
- Next: Configure Security Group.
- Review and Launch.<br>
<b> Ready to go </b> <br>
 [Link to Create Ec2 instance](https://docs.aws.amazon.com/efs/latest/ug/gs-step-one-create-ec2-resources.html)
 
![image](https://user-images.githubusercontent.com/63963025/167152381-3eb0b21d-7a17-4f26-894c-d56a10ad29f2.png)

-  Connect the machine via ssh 

```
sudo su 
```
-  Install Docker inside machine <br>
 [Link to Installtion Docker in Amazon Linux](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html)
![image](https://user-images.githubusercontent.com/63963025/167154337-861f9cd4-9178-46cf-83e3-32cdc18f30fe.png)

- create a directory and create app for a flask application 
```
yum update -y 
```
```
mkdir flask
cd flask/
vi app.py
```
![image](https://user-images.githubusercontent.com/63963025/167246415-d552ab3e-269e-4906-95c9-9b0434fee7e3.png)

- [Link to app.py file](*)
```
pip3 install flask 
```
![image](https://user-images.githubusercontent.com/63963025/167154877-0781f2dc-149f-48b6-a932-18a833f50e78.png)

- run the python application for testing 
```
python3 app.py
```
![image](https://user-images.githubusercontent.com/63963025/167158639-d965d2f7-0d25-405d-a70e-8fd947cade1d.png)


- open new tab and (curl localhost ip:127.0.0.1:5000)
![image](https://user-images.githubusercontent.com/63963025/167158711-86223ad1-2f0e-43f0-be9d-393ccabdefcb.png)


- lets create Dockerfile and append our Flask application and create Dockerimage <br>
- [Link to Dockerfile](*) <br>
![image](https://user-images.githubusercontent.com/63963025/167260396-deff0104-d4c0-4457-9433-7f001b477472.png)



- Also create requirements.txt 
- [Link to requirements.txt](*) <br>
![image](https://user-images.githubusercontent.com/63963025/167260437-4b2b4098-8873-438b-a41b-01f7950fca5c.png)


- Create virtualenv to run flask application
 use this command 
 ```
 python3 -m venv flaskpython
 ```

## Step2 create Docker Image 
- current directory 
```
docker build -t flaskapp:v1 .
```
<b>or</b> <br> 
- different directory 
```
docker build -t flaskapp:v1 /home/ec2-user/flask
```
![image](https://user-images.githubusercontent.com/63963025/167162123-6251818f-8ce2-48b6-bafa-8090080b099c.png)

- install httpd (apache)
```
yum install httpd -y
```
- Test docker image before uplaoding to ECR 
 
```
docker run -it -p 8080:8080  flaskapp:v1
```
![image](https://user-images.githubusercontent.com/63963025/167284670-1574d07f-24e4-4d3c-b84c-3d6ecb128462.png)

- Go to EC2--> Left hand side there is option call--> Security group (change firewall rule) edit inbound rules allow custom port number 8080
![image](https://user-images.githubusercontent.com/63963025/167284743-9e378802-acca-4350-bfb2-f44c074dab1e.png)

- copy the external ip of your vm and attach port number to external ip eg:- http://<external ip of vm>:8080/ <br>
  ![image](https://user-images.githubusercontent.com/63963025/167284827-a56ce54f-0ecd-4aed-8466-17441a1300b0.png)
- paste the ip to your browser with port number 8080 (http://<external ip of vm>:8080/) <br>
![image](https://user-images.githubusercontent.com/63963025/167284771-d3876e27-19e8-41dc-84b0-c6c18f97ba84.png)

## Step3 

