from WantedInfo import WantedInfo
from selenium import webdriver
from ProgrammersInfo import ProgrammersInfo
import time

driver_path = '/Users/mac/0_Dev/PythonProjects/get_coin/chromedriver'
url = 'https://programmers.co.kr/job?job_position%5Bmin_career%5D=&amp;job_position%5Bjob_category_ids%5D%5B%5D=3&amp;job_position%5Bjob_category_ids%5D%5B%5D=10&amp;_=1593673591520'
driver = webdriver.Chrome(driver_path)
driver.get(url)
programmers_jobs = []
time.sleep(3)

datas = driver.find_elements_by_css_selector('li.list-position-item>div.item-body')

for com in datas :
    name = com.find_element_by_css_selector('.company-name').text
    position_name = com.find_element_by_css_selector('.position-title>a').text
    url = com.find_element_by_css_selector('.position-title>a').get_property('href')
    location = com.find_element_by_css_selector('.company-info>.location').text
    min_career = com.find_element_by_css_selector('.company-info>.experience').text
    programmers_jobs.append(ProgrammersInfo(name,position_name,url,location,min_career))


print(len(programmers_jobs))
for job in programmers_jobs :
    print(job.name)

driver.close()