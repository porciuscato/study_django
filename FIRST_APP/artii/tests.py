from django.test import TestCase

# Create your tests here.
import requests
from flask import request

url = 'http://artii.herokuapp.com/make?text='
response = requests.get('{}{}'.format(url,'SSAFY')).text
print(response)