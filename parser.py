import requests
from bs4 import BeautifulSoup
from urllib.request import *



def collect_data():

    response = requests.get(url = 'https://sharik.ua/catalog/folgirovannye_shary/?PAGEN_1=9')
    soup = BeautifulSoup(response.text, 'lxml')
    ballons_img = soup.find_all('div', class_="one-item-thumb-ins")
  

    for ballon in ballons_img:
        
        f = ballon.find('img')
        url = str(f['src'])
        name = str(f['alt'][11:])
        try:
            urlretrieve('https://sharik.ua/'+url,name)
            print(name,'ok')
        except:
            continue
       

def main():
    collect_data()


if __name__ == '__main__':
    main()