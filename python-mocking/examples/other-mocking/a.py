import requests

#r = requests.get('http://httpbin.org/status/500')
#print(r.status_code)

r = requests.get('http://httpbin.org/cookies/set/name/FooBar')
print(r.status_code)
print(r.text)
print(r.cookies)


cookies = dict(cookies_are='working')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(r.status_code)
print(r.text)
print(r.cookies)

