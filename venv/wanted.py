from WantedInfo import WantedInfo
from selenium import webdriver
import time

driver_path = '/Users/mac/0_Dev/PythonProjects/get_coin/chromedriver'
url = 'https://www.wanted.co.kr/wdlist/518/678?country=kr&job_sort=job.latest_order&years=0&locations=all'
driver = webdriver.Chrome(driver_path)
driver.get(url)
wanted_jobs = []
url_list = []
time.sleep(3)

datas = driver.find_element_by_css_selector('ul.clearfix')
companies = datas.find_elements_by_class_name('body')
urls = datas.find_elements_by_tag_name('a')

for url in urls :
    detail_link = url.get_property('href')
    url_list.append(detail_link)
i = 0
for company in companies :
    position_name = company.find_element_by_class_name('job-card-position').text
    name = company.find_element_by_class_name('job-card-company-name').text
    location = company.find_element_by_class_name('job-card-company-location').text
    reward = company.find_element_by_class_name('reward').text
    url = url_list[i]
    i += 1
    wanted_jobs.append(WantedInfo(name, location,position_name, reward, url))

print(len(wanted_jobs))
for job in wanted_jobs :
    print(job.name)

driver.close()