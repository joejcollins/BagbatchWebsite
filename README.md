# CaptainScarlet

Bagbatch Website

## Install GAE on C9

* Alt-T
* cd ..
* wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.57.zip
* unzip google_appengine_1.9.57.zip
* rm google_appengine_1.9.57.zip 

## To run on Cloud9 (https://c9.io) use:

```
python ./google_appengine/dev_appserver.py ./workspace/web_app/ --host=0.0.0.0  
```
    
## To run on Cloud9 with access to the admin interface use:
    
```
python ../google_appengine/dev_appserver.py ../workspace/web_app/ --host=0.0.0.0 --port=8080 --admin_host=0.0.0.0 --admin_port=8081
```

# App Engine Standard Flask Hello World

This sample shows how to use [Flask](http://flask.pocoo.org/) with Google App
Engine Standard.

Before running or deploying this application, install the dependencies using
[pip](http://pip.readthedocs.io/en/stable/):

```
pip install -t lib -r requirements.txt
```
