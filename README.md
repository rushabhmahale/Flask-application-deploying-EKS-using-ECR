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
- Step1 Create a flask application 
Here i am using AWS Cloud shell (become sudo user)
```
sudo su 
```
- create a directory and create app for a flask application 
```
yum update -y 
```
```
mkdir flask
cd flask/
vi app.py
```
![image](https://user-images.githubusercontent.com/63963025/167089349-a55a8525-f3ac-44be-ba99-0b60496e3b62.png)

![image](https://user-images.githubusercontent.com/63963025/167089449-75e3eac9-8468-4cb2-9a83-e35dcb78afdb.png)
```
pip3 install flask 
```
![image](https://user-images.githubusercontent.com/63963025/167089636-89348f79-ff88-4f7e-bb0d-cf12098c785f.png)

- run the pyhon application for testing 
```
python3 app.py
```
![image](https://user-images.githubusercontent.com/63963025/167090424-82501564-dcbd-4e58-9a4f-ddd61c7fee3c.png)

- open new tab and (curl localhost ip:127.0.0.1:5000)
![image](https://user-images.githubusercontent.com/63963025/167090570-5dc43815-d532-49b2-981a-50984811f708.png)

- lets create Dockerfile and append our Flask application and create Dockerimage

- same folder /home/cloudshell-user/flask Create Dockerfile




