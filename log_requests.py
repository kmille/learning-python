#!/usr/bin/env python3
import requests
import urllib.request
import logging

logging.basicConfig()
logging.getLogger('requests.packages.urllib3').setLevel(logging.DEBUG)

http_logger = urllib.request.HTTPHandler(debuglevel=1)
opener = urllib.request.build_opener(http_logger)
urllib.request.install_opener(opener)

def http():
    requests.get("http://httbin.org/ip")
    print("done")
    urllib.request.urlopen("http://heise.de")

http()
