import requests

url = 'https://dynamic1.scrape.cuiqingcai.com/'
html = requests.get(url).text
print(html)
