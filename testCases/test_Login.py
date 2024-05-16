import pytest
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class", autouse=True)
def setUp():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

class TestLogin(softest.TestCase):
    def test_Login_001(self,setUp):
        driver = setUp
        driver.get("https://www.google.com")
        # actualTitle = driver.title
        # self.soft_assert(self.assertEqual, actualTitle, 'Googlelkj ', 'Title does not match')
        # if actualTitle == "Googlelkj ":
        #     print("Test is Passed")
        # else:
        #     print("Test is failed")
        # self.assert_all()

    # def test_Login_002(self):
    #     driver = webdriver.Chrome()
    #     driver.get("https://www.google.com")
