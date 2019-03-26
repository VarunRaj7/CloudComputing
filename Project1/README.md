# CloudComputingProject01
## Docker Container of the Dynamic Weather Service API with UI
### Contents
1. Procedure to pull and run docker image.
2. More about the docker instance.
3. How to use the API?

### 1. Procedure to pull and run docker image.

The following are the sequence of steps to pull and run the docker container of Dynamic Weather Service API with UI developed using python-flask-uwsgi-nginx (JQuery is used to provide UI):

1. Install Docker:
        
        $ sudo yum install -y docker

2. Start the Docker Service:
       
       $ sudo service docker start

3. Pull the image using docker pull as follows:
        
        $ docker pull rayabavj/ccproject1
    
    Image Link: https://hub.docker.com/r/rayabavj/ccproject1/

4. Run the docker image:
        
        $ docker run -d --name "my_app"  -p 80:80 rayabavj/ccproject1
    
5. Check the running containers:
        
        $ docker ps
 
6. You can also check the logs:
        
        $ docker logs my_app
        
   logs content when ready:
   ![SS](https://github.uc.edu/rayabavj/CloudComputingProject01/blob/master/SS1.PNG)
   
7. When the image is successfully running, as seen in the logs, you can access the API through the browser.

      **Notice: Check in browser when app running successfully as seen in logs**

8. Stopping the running docker image
        
        $ docker stop my_app
    
### 2. How Docker Instance is built?

This docker instance is built using the file Dockerfile in link: https://github.uc.edu/rayabavj/CloudComputingProject01/blob/master/dockerfile . 

Furthermore, this docker image is based on the docker image tiangolo/uwsgi-nginx-flask:latest. This instance served as the basis upon which the docker inastance is built as seen in the first statement in the dockerfile:

        FROM tiangolo/uwsgi-nginx-flask:latest

The next statements in the docker file is just copying the required files like static, templates, python file, uwsgi file, etc. to the file app in the tiangolo/uwsgi-nginx-flask. And also, installing the required python tools RESTFUL and numpy using RUN statement in dockerfile. After creating doockerfile, use the following command to built instance:
        
        $ docker build -t rayabavj/ccproject1:latest .
               

### 3. How to use API?

This weather service api can be used to get the maximum and minimum temperature for a period of seven days given the starting date. Moreover, it compares the results from the Weather Underground data for the same data and same days.

The api is also provided with the attractive user interface as shown below:
![SS3](https://github.uc.edu/rayabavj/CloudComputing/blob/master/HW03/DynamicServiceAPI/SS3.PNG)

For more deatails about API click the following link below: 

https://github.uc.edu/rayabavj/CloudComputing/blob/master/HW03/DynamicServiceAPI/README.md
