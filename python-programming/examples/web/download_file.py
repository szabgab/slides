import requests
import shutil

url = "https://code-maven.com/public/developer_survey_2019.zip"
filename = "developer_survey_2019.zip"

res = requests.get(url, stream=True)
print(res.status_code)
if res.status_code == 200:
    with open(filename, 'wb') as fh:
        res.raw.decode_content
        shutil.copyfileobj(res.raw, fh)
