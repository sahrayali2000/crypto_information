from bs4 import BeautifulSoup
import requests
from crypto.models import MarketInformation


def market_info():
    url = 'https://crypto.com/price'
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    market_cap = doc.find_all(text='Market Cap')
    market = market_cap[0].parent.parent
    dd0 = market.find('dd')
    dd0 = dd0.string
    volume = doc.find_all(text='24H Volume')
    vol = volume[0].parent.parent
    dd1 = vol.find('dd')
    dd1 = dd1.string
    dominance = doc.find_all(text='Dominance')
    dom = dominance[0].parent.parent
    dd2 = dom.find('dd')
    dd2 = dd2.string
    market_information = MarketInformation()
    market_information.dominance = dd2
    market_information.volume = dd1
    market_information.market_cap = dd0
    market_information.save()


