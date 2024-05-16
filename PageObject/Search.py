from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Search:
    textbox_Search_xpath = "//*[@class='gLFyf']"
    text_searchResult_class = "wM6W7d"


    def __init__(self, setUp):
        self.driver = setUp

    def search_withdata(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,Search.textbox_Search_xpath).send_keys("Amazon")
        
    def get_results(self):
        time.sleep(2)
        results = self.driver.find_elements(By.CLASS_NAME,"wM6W7d")
        data = []
        for i in range(0,9):
            element = results[i]
            data.append(element.text)
        for i in results:
            if i.text == "amazon affiliate program":
                i.click()
                break