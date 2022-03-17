#!/usr/bin/env python3
# pip install requests_toolbelt
from requests_toolbelt import sessions
from requests_toolbelt.utils import dump

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import requests
import http

# this is based on this blog https://findwork.dev/blog/advanced-usage-python-requests-timeouts-retries-hooks/

# non-zero value prints all request and response to stdout (without body)
#http.client.HTTPConnection.debuglevel = 1


def retry():
    session = sessions.BaseUrlSession("http://httpstat.us")
    session.verify = False

    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"],
        backoff_factor=1
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)

    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.get("/500")


def raise_for_status():
    resp = requests.get("https://httpstat.us/404")
    resp.raise_for_status()


def log_quick():
    http.client.HTTPConnection.debuglevel = 1
    requests.get("https://httpbin.org/anything")
    http.client.HTTPConnection.debuglevel = 0


def log_all():
    def log_request(resp, *args, **kwargs):
        #print(f"Hook: {resp.url}")
        data = dump.dump_all(resp)
        print(data.decode())

    session = sessions.BaseUrlSession("https://httpbin.org")
    session.hooks['response'] = [log_request, ]
    session.get("/ip")



if __name__ == '__main__':
    #retry()
    #raise_for_status()
    #log_quick()
    log_all()
