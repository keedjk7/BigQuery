import requests
from bs4 import BeautifulSoup


def get_set100_data():
    url = 'https://www.set.or.th/th/market/index/set100/overview'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find index value
    index_value_element = soup.find('div', class_='value text-white mb-0 me-2 lh-1 stock-info')
    index_value = index_value_element.text.strip()

    # Find highest bid price
    highest_bid_price_element = soup.find('div', class_='d-block quote-market-high me-auto border-0')
    highest_bid_price_span = highest_bid_price_element.find('span', class_='ms-2')
    highest_bid_price = highest_bid_price_span.text.strip()

    return index_value, highest_bid_price


index_value, highest_bid_price = get_set100_data()
print("SET100 Index Value:", index_value)
print("SET100 Highest Bid Price:", highest_bid_price)



