import requests 
from bs4 import BeautifulSoup

# Making a GET request 
# r = requests.get('https://www.barclaycard.co.uk/personal') 

with open('Parse_barclaycard_prettify.txt', 'r') as i:
    r = i.read()
url = []

with open('Parse_barclaycard.txt', 'w') as f:
    soup = BeautifulSoup(r, 'html.parser')
    # soup = BeautifulSoup(r.content, 'html.parser')
    
    for link in soup.find_all(['a']):

        url.append(link.get('href'))

    f.write('\n'.join(map(str, url)))
# print(soup.prettify()) 