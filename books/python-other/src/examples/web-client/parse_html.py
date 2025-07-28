from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Main_Page'
res = requests.get(url)
if res.status_code != 200:
    exit(f"Error in getting the page. Status code: {res.status_code}")
html = res.content

soup = BeautifulSoup(html, features='lxml')
print(soup.title.text)

for link in soup.find_all("a", limit=3):
    print(link)
    print(link.text)
    print(link.attrs.get('href'))
    print()

print('-----------------------------------------')

forms = soup.select("#searchform")
if forms is not None:
    print(forms)
    form = forms[0] # We used an ID to search we expect to have 0 or one matches in the list
    print()
    print('Action: ', form.attrs.get('action'))

    # Search inside that element we found earlier
    for inp in form.find_all('input'):
        print('id: ', inp.attrs.get('id'))
print('-----------------------------------------')

tfa = soup.select("#mp-tfa")
if tfa is not None:
    #print(tfa)
    paras = tfa[0].select("p")
    if paras is not None:
        #print(paras)
        links = paras[0].find_all("a", limit=1)
        if links:
            print(links[0].text)
            print(links[0].attrs.get('href'))
