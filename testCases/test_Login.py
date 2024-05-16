from PageObject.Search import Search
from testData.data import Google_data
import time

class TestLogin:
    def test_Login_001(self, setUp):
        driver = setUp
        driver.get(Google_data.BaseURL)
        time.sleep(2)
        # Create an instance of the Search class
        search_page = Search(driver)
        # Call the search_withdata method
        search_page.search_withdata()
        search_page.get_results()
