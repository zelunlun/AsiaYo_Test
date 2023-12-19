import requests
import sys
import json


test = sys.argv[1]
url = "http://127.0.0.1:5000/" + test 
response_post = requests.get(url=url)

print(response_post.json())



