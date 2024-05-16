from selenium import webdriver
from selenium.webdriver.common.by import By

class Search:
    textbox_Search_xpath = "//*[@class='gLFyf'']"


    def __init__(self,setUp):
        driver = setUp

    def search_withdata(self):
        driver = webdriver.Chrome()
        driver.find_element(By.XPATH,Search.textbox_Search_xpath).send_keys("Amazon")
        