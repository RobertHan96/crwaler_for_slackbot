from selenium import webdriver
import time
driver_path = '/Users/mac/0_Dev/PythonProjects/get_coin/chromedriver'

url = 'https://www.wanted.co.kr/wdlist/518/678?country=kr&job_sort=job.latest_order&years=0&locations=all'
driver = webdriver.Chrome(driver_path)
driver.get(url)
time.sleep(3)

datas = driver.find_element_by_css_selector('ul>.clearfix')
print(datas.text)

# search_kewords = ['BTC', 'XRP']
# coin_infos = []
#
# for coin in search_kewords :
#     coin_row = driver.find_element_by_css_selector('.{}'.format(coin))
#     coin_name = coin_row.find_element_by_css_selector('.coin').text
#     coin_usd = coin_row.find_element_by_css_selector('.usd').text
#     coin_krw = coin_row.find_element_by_css_selector('.krw').text
#     coin_price_diff = coin_row.find_element_by_css_selector('.minus').text
#
#     coin_info = CoinInfo(coin_name, coin_usd, coin_krw, coin_price_diff)
#     coin_infos.append(coin_info)

driver.close()