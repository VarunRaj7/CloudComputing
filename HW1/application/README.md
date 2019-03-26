#HW01 Web Application

##Left-truncatable and Right-truncatable Prime Numbers
________________________________________________________________________________________________________________________________________

Table of Contents:

I. What are Truncatable Prime Numbers?

II. How python is setup in wsgi server and hosted behind Apache2

III. Enabling HTTPS
________________________________________________________________________________________________________________________________________

I. What are Truncatable Prime Numbers?

The number 3797 is both left-truncatable and right-truncatable prime number. Being prime itself, it is possible to continously remove digits from left to right, and remain prime at each stage: 3797, 379, 37,3.Hence, left-truncatable prime number. Similarly we can work from right to left: 3797, 797, 97 and 7, and call it as a right-truncatable number too.

Project Problem Statement from: https://projecteuler.net/problem=37

Python Help:https://www.geeksforgeeks.org/python/
            https://www.tutorialspoint.com/index.htm

Flask Help:https://www.tutorialspoint.com/flask/index.htm

II.How python is setup in wsgi server and hosted behind Apache2

1. Installation steps:

Install Apache2 webserver and modwsgi

$ sudo aptitude install apache2 apache2.2-common apache2-mpm-prefork apache2-utils libexpat1 ssl-cert

$ sudo apt-get install libapache2-mod-wsgi

2. Change the location of the flask app to /var/www/html

3. In the application create the .wsgi file with the code below:

            import sys
            sys.path.insert(0, '/var/www/html/application')

            from home import app as application

In the secondline of this code , the location of the application is provided and the last line indicates that the app variable is      taken from home.py and aliasing in the application namespace.

4. Configuring Apache: go to the file /etc/apache2/sites-enabled/000-default.conf and add the following code

       WSGIDaemonProcess application threads=5
       WSGIScriptAlias / /var/www/html/applicatio/app.wsgi

       <Directory application>
       WSGIProcessGroup home
       WSGIApplicationGroup %{GLOBAL}
       Order deny,allow
       Allow from all
       </Directory>
  
This code will capture all the requests on your server and redirect them to the WSGI file that we just created. The WSGI file is then
  sending the request onto the Flask application which produces a HTTP response.

5. Restart the server:

  $ sudo a2enmod wsgi

  $ /etc/init.d/apache2 restart

Sources: https://www.jakowicz.com/flask-apache-wsgi/
          https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/
          https://askubuntu.com/questions/484183/apache-django-and-mod-wsgi/484188#484188

III. To enable HTTPS:

1. Create a copy of home.py as home1.py so as to resolve error due to name duplicates error in wsgi daemon definition.

2. Copy the default-ssl.conf from /etc/apache2/sites-available to etc/apache2/sites-enable

3. Open the following code in the VirtualHost tag under the DocumentRoot:  
 
            WSGIDaemonProcess home1 threads=5
            WSGIScriptAlias / /var/www/html/application/app.wsgi

4. In the same file following the following code in the directory tag: 

            WSGIProcessGroup home1
            WSGIApplicationGroup %{GLOBAL}
            
5. Copy the following files from the /etc/apache2/mods-available to /etc/apache2/mods-enabled to enable these modules:

socache_shmcb.load

ssl.conf

ssl.load

5. Restart the server.

Now, the HTTPS port is enabled.

Credits: Akshay

Project HTTPS Link:

https://ec2-52-14-93-71.us-east-2.compute.amazonaws.com/home

##Thank you 
