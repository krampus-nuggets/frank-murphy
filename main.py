import urllib.request
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = '<request-receiver>'

dummyData = json.loads(open('dummyData.json').read())

