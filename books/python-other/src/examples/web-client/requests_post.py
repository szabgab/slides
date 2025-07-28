import requests

payload = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cus="http://www.corp.net/Request.XSD">
    <soapenv:Header/>
    <soapenv:Body>
       <cus:CustMsagDown.Check>
           <cus:MainCustNum>327</cus:MainCustNum>
           <cus:SourceSystem></cus:SourceSystem>
       </cus:CustMsagDown.Check>
    </soapenv:Body>
</soapenv:Envelope>
'''

res = requests.post('http://httpbin.org/post',
    headers = {
        'User-agent'  : 'Internet Explorer/2.0',
        'SOAPAction'  : 'http://www.corp.net/some/path/CustMsagDown.Check',
        'Content-type': 'text/xml'
    },
    data = payload,
)
print(res.headers['content-type'])
print(res.text)

