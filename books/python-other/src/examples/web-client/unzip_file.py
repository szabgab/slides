import zipfile

path = "developer_survey_2019.zip"
zf = zipfile.ZipFile(path)
zf.extractall()
