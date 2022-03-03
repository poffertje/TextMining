import time
import pandas as pd 
from bs4 import BeautifulSoup
from pytest import skip
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

url = "https://www.google.com/maps/place/Domino's+Pizza+Amsterdam+Bos+En+Lommerweg/@52.3788032,4.8495339,17z/data=!3m1!4b1!4m5!3m4!1s0x47c5e26f5e6884bd:0x1b5c1b636bb56346!8m2!3d52.3788632!4d4.8517073"
driver.get(url)

driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button').click()
#to make sure content is fully loaded we can use time.sleep() after navigating to each page
time.sleep(3)

driver.find_element_by_class_name("Yr7JMd-pane-hSRGPd").click()

time.sleep(3)
# not sure about this because i have not stumbled upon paid ads in queries
# try:
#     driver.find_element(By.CLASS_NAME, "Yr7JMd-pane-hSRGPd").click()
# except Exception:
#     response = BeautifulSoup(driver.page_source, 'html.parser')
#     # Check if there are any paid ads and avoid them
#     if response.find_all('span', {'class': 'ARktye-badge'}):
#         ad_count = len(response.find_all('span', {'class': 'ARktye-badge'}))
#         li = driver.find_elements(By.CLASS_NAME, "a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd")
#         li[ad_count].click()
#     else:
#         driver.find_element(By.CLASS_NAME, "a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd").click()
#         time.sleep(5)
#     driver.find_element(By.CLASS_NAME, "Yr7JMd-pane-hSRGPd").click()
total_number_of_reviews = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[2]').text.split(" ")[0]
total_number_of_reviews = int(total_number_of_reviews.replace(',','')) if ',' in total_number_of_reviews else int(total_number_of_reviews)
#Find scroll layout
scrollable_div = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]')
#Scroll as many times as necessary to load all reviews
for i in range(0,(round(total_number_of_reviews/10 - 1))):
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', 
                scrollable_div)
        time.sleep(10)
        # print(BeautifulSoup(driver.page_source, 'html.parser'))
        print(driver.find_elements_by_class_name('ODSEW-KoToPc-ShBeI gXqMYb-hSRGPd'))

response = BeautifulSoup(driver.page_source, 'html.parser')
reviews = response.find_all('div', class_='ODSEW-ShBeI NIyLF-haAclf gm2-body-2')

def get_review_summary(result_set):
    rev_dict = {'Review Rate': [],
        'Review Time': [],
        'Review Text' : []}
    for result in result_set:
        review_rate = result.find('span', class_='ODSEW-ShBeI-H1e3jb')["aria-label"]
        review_time = result.find('span',class_='ODSEW-ShBeI-RgZmSc-date').text
        review_text = result.find('span',class_='ODSEW-ShBeI-text').text
        rev_dict['Review Rate'].append(review_rate)
        rev_dict['Review Time'].append(review_time)
        rev_dict['Review Text'].append(review_text)   
    return(pd.DataFrame(rev_dict))

get_review_summary(reviews).to_csv("dominos_reviews.csv",index=False)
