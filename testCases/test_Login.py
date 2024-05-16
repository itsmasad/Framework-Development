from PageObject.Search import Search
import time

class TestLogin:
    def test_Login_001(self, setUp):
        driver = setUp
        driver.get("https://www.google.com")
        time.sleep(2)
        # Create an instance of the Search class
        search_page = Search(driver)
        # Call the search_withdata method
        search_page.search_withdata()
        search_page.get_results()
