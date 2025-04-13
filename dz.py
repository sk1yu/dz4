import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        url = 'https://bank.gov.ua/'  
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        
        usd_element = soup.find('td', text='USD')
        if usd_element:
            rate = usd_element.find_next_sibling('td').text
            return float(rate.replace(',', '.'))
        else:
            raise Exception("Курс USD не найден.")

    def convert_to_usd(self, amount):
        return amount / self.usd_rate

if __name__ == "__main__":
    converter = CurrencyConverter()
    amount = float(input("Введите сумму в гривнах: "))
    usd_amount = converter.convert_to_usd(amount)
    print(f"Это эквивалентно {usd_amount:.2f} USD")
