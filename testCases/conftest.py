import pytest
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def setUp(softest.TestCase):
    driver = webdriver.Chrome()
    driver.maximize_window
    yield driver
    driver.quit()