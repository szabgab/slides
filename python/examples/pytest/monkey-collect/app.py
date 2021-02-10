import requests

# An application that allows us to monitor keyword requency on some popular websites.
# The process:
#    - get the URLs from the database
#    - fetch the content of esch page
#    - get the frequency of keywords for each page
#    - get the precious values from the database
#    - update the database with the new values
#    - send e-mail reporting the changes.

def get_urls():
    #raise Excepton('accessing the database')
    return ['https://code-maven.com/']

def get_content(url, depth):
    #raise Exception(f'donwload content from {url}')
    return "Python Python Pytest Monkey patch Python"

def get_stats(text, limit=None):
    #raise Exception('getting stats from some text')
    return {}

def get_stats_from_db(url):
    #raise Exception('getting stats from database')
    return {}

def create_report(old, new):
    #raise Exception('create report')
    return ''

def send_report(report, subject, to):
    #raise Exception(f'send report to {to}')
    return ''

def main():
    depth = 3
    limit = 17
    boss = 'boss@code-maven.com'
    subject = 'Updated stats'
    urls = get_urls()
    for url in urls:
        content = get_content(url, depth)
        new_stats = get_stats(content, limit)
        old_stats = get_stats_from_db(url)
        report = create_report(old_stats, new_stats)
        send_report(report, subject, boss)

if __name__ == '__main__':
    main()

