import requests

def calc(expr):
    url = "http://api.mathjs.org/v1/?expr=%s" % expr
    r = requests.get(url)
    if r.text != "":
        return r.text
    if r.text == "undefined":
        return "Méo biết!"
    return "Méo hiểu!"
