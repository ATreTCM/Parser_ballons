import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

URL = 'https://sharik.ua/catalog/folgirovannye_shary/?PAGEN_1=9'

def download_images(url, name):
    try:
        urlretrieve(url, name)
        print(f'{name} downloaded successfully')
    except Exception as e:
        print(f'Error downloading {name}: {e}')

def collect_data():
    response = requests.get(url=URL)
    soup = BeautifulSoup(response.text, 'lxml')
    ballons_img = soup.find_all('div', class_='one-item-thumb-ins')

    for ballon in ballons_img:
        img = ballon.find('img')
        url = img['src']
        name = img['alt'][11:]
        download_images('https://sharik.ua/' + url, name)

def main():
    collect_data()

if __name__ == '__main__':
    main()
