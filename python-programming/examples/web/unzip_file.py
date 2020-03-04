import zipfile

path = "developer_survey_2019.zip"
z = zipfile.ZipFile(path)
z.extractall()
