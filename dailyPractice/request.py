import requests
import json

url = 'https://dummyjson.com/users'

response = requests.get(url)

if response.status_code == 200: 
    data = response.json()

    for i in  data["users"]:
        user_id = i["id"]
        age = i["age"]
        first_name = i["firstName"]
        address = i["address"]
        print(first_name,address)
        if age > 25:
            print(first_name,age)
    first_names = [j["firstName"] for j in data["users"]]
    print(sorted(first_names))






