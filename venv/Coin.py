from selenium import webdriver
from CoinInfo import CoinInfo

import time
driver_path = '/Users/mac/0_Dev/PythonProjects/get_coin/chromedriver'

driver = webdriver.Chrome(driver_path)
driver.get('http://luka7.net/')
time.sleep(3)

search_kewords = ['BTC', 'XRP']
coin_infos = []

for coin in search_kewords :
    coin_row = driver.find_element_by_css_selector('.{}'.format(coin))
    coin_name = coin_row.find_element_by_css_selector('.coin').text
    coin_usd = coin_row.find_element_by_css_selector('.usd').text
    coin_krw = coin_row.find_element_by_css_selector('.krw').text
    coin_price_diff = coin_row.find_element_by_css_selector('.minus').text

    coin_info = CoinInfo(coin_name, coin_usd, coin_krw, coin_price_diff)
    coin_infos.append(coin_info)

driver.close()