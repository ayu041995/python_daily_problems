import requests
import pandas as pd

def get_user_login_data():
    url = 'https://'
    response = request.get(url)
    if response.status_code == 200:
        list1 = []
        dict1 = {}
        max_count = 0
        with open(response.content) as fh:
            user_id = fh.get("user_id")
            login = fh.get("login")
            list1.append(user_id)
            for i in list1  and :
                if i in dict1.keys():
                    dict1[i] += 1
                else:
                    dict1[i] = 1
        for i in dict1:
            if dict1[i] > max_count
            max_count = dict1[i]
        return max_count
            
            # total_count = users.count()
        # return total_count


print(get_user_login_data())