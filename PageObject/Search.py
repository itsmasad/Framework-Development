from selenium import webdriver
from selenium.webdriver.common.by import By

class Search:
    textbox_Search_xpath = "//*[@class='gLFyf']"


    def __init__(self, setUp):
        self.driver = setUp

    def search_withdata(self):
        self.driver.find_element(By.XPATH,Search.textbox_Search_xpath).send_keys("Amazon")
        