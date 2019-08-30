import urllib.request
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + "!@#$%^&*()"
random.seed = (os.urandom(1024))

attackURL = "<receiver-url>"

dummyData = json.loads(open("dummyData.json").read())

for userData in dummyData:
    randomValues = "".join(random.choices(string.digits))
    username = userData.lower() + randomValues + "@mail.ru"
    password = "".join(random.choice(chars) for i in range(8))
    urllib.request.post(attackURL, allow_redirects=False, data={
        <request-data>
    })

