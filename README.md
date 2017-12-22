# CaptainScarlet

Bagbatch Website

## Install or Update GAE on C9

* Alt-T
* cd ..
* rm -r google_appengine
* wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.65.zip
* unzip google_appengine_1.9.65.zip
* rm google_appengine_1.9.65.zip 

To run on Cloud9 use:

    ``` python ../google_appengine/dev_appserver.py ./web_app/ --enable_host_checking=false ```
    
To run on Cloud9 with access to the admin interface use:
    
    ``` python ../google_appengine/dev_appserver.py ./web_app/ --enable_host_checking=false --host=0.0.0.0 --port=8080 --admin_host=0.0.0.0 --admin_port=8081 ```
    
Not all the ports are available to use be 8081 is so it needs to be set explicitly.

## App Engine Standard Flask Hello World

This sample shows how to use [Flask](http://flask.pocoo.org/) with Google App Engine Standard.

Before running or deploying this application, install the dependencies using [pip](http://pip.readthedocs.io/en/stable/):

    ``` pip install -t lib -r requirements.txt ```

## Settings

The application settings are stored in the Datastore, so visit https://console.cloud.google.com/datastore to adjust the settings.
