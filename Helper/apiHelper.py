import requests


def getData(url, data=None, cookie=None, method="GET"):
    if cookie is None:
        cookie = {}
    if data is None:
        data = {}
    if method == "get" or method == "GET":
        req = requests.get(url, params=data, cookies=cookie)
    else:
        req = requests.post(url, params=data, cookies=cookie)
    return req
