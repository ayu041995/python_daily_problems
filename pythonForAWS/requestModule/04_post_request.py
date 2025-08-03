import requests

r = requests.post('https://httpbin.org/post?a=b', data={'ayushi': 'jaiswal'})

print(r.text)