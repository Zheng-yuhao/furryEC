# _An EC shopping site_
It's an EC website developed in Django.
Using Django for the backend server and Vue.js for the frontend.
## Install
`git pull git@github.com:hirrochi0211/furryEC.git`

## Description
- apps
  - user => Handling login and sign up functions.
  - order => Handling purchase functions.
  - home => Handling of processing banner images on homepage.
  - course => Handling of publishing the merchandise(In this EC site, We publish the course as merchandise).

### The packages developed by third parties used in this project（main parts）
- djangorestframework==3.10.3
- djangorestframework-jwt==1.11.0
- django-redis==5.0.0
- redis==3.5.3
- celery==5.1.2
- python-alipay-sdk==3.0.4

## Usage
`python3 manage.py runserver`

> The source for this project is being prepared for deploy, so if you want to pull the code on your local environment,
you need to modify the code in manage.py and wsgi.py, which should be set the settings file to dev(development settings file).

## Project Showcase
![Image text](https://github.com/hirrochi0211/furryEC/blob/master/furryec.gif)

