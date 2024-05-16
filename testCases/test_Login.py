from PageObject.Search import Search

class TestLogin:
    def test_Login_001(self,setUp):
        driver = setUp
        driver.get("https://www.google.com")

