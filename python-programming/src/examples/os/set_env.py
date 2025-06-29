import os

os.system("echo hello")
os.system("echo $HOME")

os.system("echo Before $MY_TEST")
os.environ['MY_TEST'] = 'qqrq'
os.system("echo After $MY_TEST")

