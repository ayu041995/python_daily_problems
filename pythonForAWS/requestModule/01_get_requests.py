import requests

r  = requests.get("https://www.codewithharry.com")
# print(r.text)

with open("index.html","w") as f:
    f.write(r.text)