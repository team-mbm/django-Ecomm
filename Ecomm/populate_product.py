"""
populate product db
with post requests (only if you are admin/superuser)
"""
from __future__ import print_function
import json, os, sys
from requests.auth import HTTPBasicAuth
import requests
products_data = json.loads(open("./payload.json").read())
try:
    EMAIL = os.getenv('ADMIN_EMAIL')
    PASSWORD = os.getenv('ADMIN_PASSWORD')
except Exception as envexception:
    print ("export ADMIN_EMAIL & ADMIN_PASSWORD in current env")
    print (envexception)
    sys.exit(1)
for data in products_data:
    resp = requests.post("http://localhost:8000/api/product/", data=data,
                         auth=HTTPBasicAuth(EMAIL, PASSWORD))
    print (data['title'], resp)
