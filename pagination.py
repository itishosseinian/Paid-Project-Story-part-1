import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.construct-online.ch/'

headers = {
    'User-Agent': 'Mozilla/5.3 (Windows NT 10.0; Win64; x64) AppleWebKit/534.36 (KHTML, like Gecko) Chrome/93.0.4606.71 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.construct-online.ch/'
}

'''response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.text,'html.parser')

categories = soup.select('li.category a[data-depth="0"]')

data = {}

for category in categories:
    name = category.get_text(strip=True)
    href = category['href']

    data[name[3:]] = {'url': href}


with open('all_urls.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)'''


with open('all_urls.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for category,category_data in data.items():
    pages = []

    response = requests.get(category_data['url'],headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')

    num_pages = soup.select('li a.js-search-link[rel="nofollow"]')[-1]
    num_pages = num_pages.get_text(strip=True)

    try:
        num_pages = int(num_pages)
    except:
        num_pages = 1
    
    for pg in range(1, num_pages+1):

        string = f'?page={pg}'

        full_url = category_data['url'] + string
        pages.append(full_url)

    data[category]['pagination'] = pages

    print(f'{category} is done ....')


with open('all_urls2.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)




