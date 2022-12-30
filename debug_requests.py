#!/usr/bin/env python3
import requests

import logging
import http.client

# enable logging
logging.getLogger("requests.packages.urllib3").setLevel(logging.DEBUG)
http.client.HTTPConnection.debuglevel = 1
requests.get("http://httbin.org/ip")

# disable logging
http.client.HTTPConnection.debuglevel = 0
requests.get("http://httbin.org/ip")

"""
kmille@linbox:learning-python python log_requests.py
send: b'GET /ip HTTP/1.1\r\nHost: httbin.org\r\nUser-Agent: python-requests/2.28.1\r\nAccept-Encoding: gzip, deflate, br\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n'
reply: 'HTTP/1.1 429 Too Many Requests\r\n'
header: cache-control: max-age=0, private, must-revalidate
header: connection: close
header: content-length: 17
header: date: Fri, 30 Dec 2022 10:01:14 GMT
header: server: nginx
header: set-cookie: sid=e57179b2-8828-11ed-a007-be05f76a02e1; path=/; domain=.httbin.org; expires=Wed, 17 Jan 2091 13:15:21 GMT; max-age=2147483647; HttpOnly
"""
