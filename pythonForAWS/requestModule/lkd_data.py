import requests

def get_daf_data(token):
    url = "https://httpbin.org/get"
    try:
         r = requests.get(url)
         return r.json()
    except:
        -1

print(get_daf_data(""))
