import requests

def get_data(url):

    response = requests.get(url)

    fh = response.json()
    public_repo = fh.get('public_repos')
    followers = fh.get('followers')
    total = public_repo + followers

    return total

print(get_data("https://api.github.com/users/lambda"))

# b'{"login":"lambda","id":37398,"node_id":"MDQ6VXNlcjM3Mzk4","avatar_url":"https://avatars.githubusercontent.com/u/37398?v=4","gravatar_id":"","url":"https://api.github.com/users/lambda","html_url":"https://github.com/lambda","followers_url":"https://api.github.com/users/lambda/followers","following_url":"https://api.github.com/users/lambda/following{/other_user}","gists_url":"https://api.github.com/users/lambda/gists{/gist_id}","starred_url":"https://api.github.com/users/lambda/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/lambda/subscriptions","organizations_url":"https://api.github.com/users/lambda/orgs","repos_url":"https://api.github.com/users/lambda/repos","events_url":"https://api.github.com/users/lambda/events{/privacy}","received_events_url":"https://api.github.com/users/lambda/received_events","type":"User","user_view_type":"public","site_admin":false,"name":"Brian Campbell","company":null,"blog":"https://hachyderm.io/@unlambda","location":"Vermont, US","email":null,"hireable":true,"bio":null,"twitter_username":"unlambda","public_repos":50,"public_gists":26,"followers":45,"following":4,"created_at":"2008-11-30T21:03:27Z","updated_at":"2025-07-11T02:54:17Z"}'


# https://api.github.com/users/lambda
# public_repos=50 followers=45
# total repos and followers: 95
# call this api programatically
# get response to variable
# extract two fields public_repos and followers
# prind out the names of these two fields and corresponding values
# and sum these. two vaules up and pring total
 