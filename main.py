from bs4 import BeautifulSoup
import requests

def findSmartphonesCitilink():
    k = 0
    while k<17:
        html_text = requests.get(f'https://www.citilink.ru/catalog/smartfony/?p={k}').text
        soup = BeautifulSoup(html_text, 'lxml')
        smartphones_all = soup.find_all('div',
                                        class_='product_data__gtm-js product_data__pageevents-js ProductCardHorizontal js--ProductCardInListing js--ProductCardInWishlist')
        for smartphones in smartphones_all:
            phones_name = smartphones.find('a',
                                           class_='ProductCardHorizontal__title Link js--Link Link_type_default').text

            try:
                smartphones_price = smartphones.find('span',
                                                    class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price').text
            except :
                smartphones_price = 'Нет в наличии'
            print(f'''
                       Smartphone: {phones_name}
                       Price: {smartphones_price}
                       ''')

        k+=1
        print(k)

findSmartphonesCitilink()
