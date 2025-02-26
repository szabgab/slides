import re

email = "foo@bar.com"

m = re.search(r'\w[\w.-]*\@([\w-]+\.)+(com|net|org|uk|hu|il)', email)
if (m):
    print('match 1')


# To make the regex more readable we can break it into rows and add comments:
m = re.search(r'''
                \w[\w.-]*               # username
                \@
                ([\w-]+\.)+             # domain
                (com|net|org|uk|hu|il)  # gTLD
                ''', email, re.VERBOSE)
if (m):
    print('match 2')


# Improvement to make the code *after* the regex more readable using named captures
m = re.search(r'(?P<username>\w[\w.-]*)\@(?P<domain>[\w-]+\.)+(?P<gtld>com|net|org|uk|hu|il)', email)


# Both, use named captures and also break it up to rows.
m = re.search(r'''
              (?P<username>\w[\w.-]*)
              \@
              (?P<domain>[\w-]+\.)+
              (?P<gtld>com|net|org|uk|hu|il)   # I only handle a few because this is just an example
              ''', email, re.VERBOSE)


