from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import os
import time
#from webdriver_manager.firefox import GeckoDriverManager
#driver = webdriver.Firefox(service=serv(GeckoDriverManager().install()))


firefox_driver = os.path.join(os.getcwd(), 'Drivers', 'geckodriver.exe')
serv = Service(firefox_driver)
opts = Options()
#opts.add_argument('--headless')

browser = webdriver.Firefox(opts, serv)
browser.get('https://hudle.in/venues/willingdon-sports-club/539638')


search_form = browser.find_element(By.ID, 'identifier')
#search_form.send_keys('9821092425')
search_form.submit()
time.sleep(3)
print(browser.current_url)
print(browser.title)
results = browser.find_elements(By.CLASS_NAME, 'results--main')
#print(results.text)
#results = browser.find_elements_by_class_name('result')
#print(Results[0].text)

print('done')
