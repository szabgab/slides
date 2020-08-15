import os

for env in sorted(os.environ.keys()):
    print(f"{env:25} = {os.environ[env]}")



def test_anything():
    pass
