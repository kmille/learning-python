#!/usr/bin/env python3
import requests

import logging
import http.client


#URL = "http://httbin.org/ip"
URL = "https://heise.de"


def do():
    requests.get(URL)
    print("done")


# enable logging
logging.getLogger("requests.packages.urllib3").setLevel(logging.DEBUG)
http.client.HTTPConnection.debuglevel = 1
do()

# disable logging
http.client.HTTPConnection.debuglevel = 0
do()

"""
kmille@linbox:learning-python python debug_requests.py
send: b'GET / HTTP/1.1\r\nHost: heise.de\r\nUser-Agent: python-requests/2.28.1\r\nAccept-Encoding: gzip, deflate, br\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n'
reply: 'HTTP/1.1 301 Moved Permanently\r\n'
header: Server: nginx
header: Date: Fri, 30 Dec 2022 10:04:34 GMT
header: Content-Type: text/html; charset=iso-8859-1
header: Content-Length: 229
header: Connection: keep-alive
header: X-Cobbler: servo65.heise.de
header: X-Pect: The Spanish Inquisition
header: X-Clacks-Overhead: GNU Terry Pratchett
header: X-42: DON'T PANIC
header: Location: https://www.heise.de/
header: Strict-Transport-Security: max-age=604800
send: b'GET / HTTP/1.1\r\nHost: www.heise.de\r\nUser-Agent: python-requests/2.28.1\r\nAccept-Encoding: gzip, deflate, br\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n'
reply: 'HTTP/1.1 200 OK\r\n'
header: Server: nginx
header: Date: Fri, 30 Dec 2022 10:04:32 GMT
header: Content-Type: text/html; charset=UTF-8
header: Last-Modified: Fri, 30 Dec 2022 10:04:32 GMT
header: Content-Encoding: gzip
header: Age: 1
header: Accept-Ranges: bytes
header: Strict-Transport-Security: max-age=15768000
header: x-frame-options: DENY
header: X-XSS-Protection: 1; mode=block
header: X-Content-Type-Options: nosniff
header: X-Hacc-Refreshed:
header: Vary: Accept-Encoding, X-Export-Format, X-Export-Agent, X-Export-IAP
header: Cache-Control: no-store
header: Content-Length: 105689
header: Connection: keep-alive
done
done
"""
