import requests

res = requests.get('http://httpbin.org/headers',
        headers = {
            'User-agent'  : 'Internet Explorer/2.0',
            'SOAPAction'  : 'http://www.corp.net/some/path/CustMsagDown.Check',
            'Content-type': 'text/xml'
        }
    )
print(res.text)

# {
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Type": "text/xml",
#     "Host": "httpbin.org",
#     "Soapaction": "http://www.corp.net/some/path/CustMsagDown.Check",
#     "User-Agent": "Internet Explorer/2.0"
#   }
# }

