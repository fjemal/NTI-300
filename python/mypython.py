#!/usr/bin/python
import os
def install_django():
    print('instlling django')

def install_pip:
    os.system('sudo yum -y install python-pip')
 
def dir_create:
     os.sytem('sudo mkdir /opt/django')
     os.system('sudo chown -R ect-user /opt/django')

def install_virtualenv:
    os.system('sudo pip install virtualenv')
    os.system('virtualenv django-env')

 
def activate_virtualenv:
    os.system('source /opt/django/django-env/bin/activate')
    

    os.system(' virtualenv django-env')
    os.system('pip install django')
    os.system('sudo django-admin startporject project1')
    print('installing django')       
    print('running server')
    os.system('python manage.py runserver 0.0.0.0:8000');
    os.system(' https://docs.djangoproject.com/en/1.10/intro/tutorial01/')

install_django()    

