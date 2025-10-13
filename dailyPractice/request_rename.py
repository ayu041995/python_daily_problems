import requests
import json


url = 'https://dummyjson.com/users'

data = requests.get(url)
fh = data.json()

id = fh["users"]["id"]

print(id)

# for i in fh["users"]:
#     id = i["id"]
#     # print(id)
#     department = i["company"]["department"]
#     print(department)



