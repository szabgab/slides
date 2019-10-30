import re

email = "foo@bar.com"

m = re.search(r'\w[\w.-]*\@([\w-]+\.)+(com|net|org|uk|hu|il)', email)
if (m):
    print('match')


m = re.search(r'''
                \w[\w.-]*               # username
                \@
                ([\w-]+\.)+             # domain
                (com|net|org|uk|hu|il)  # gTLD
                ''', email, re.VERBOSE)
if (m):
    print('match')
