import softest


class TestLogin(softest.TestCase):
    
    def test_Login_001(setUp,):
        driver = setUp
        driver.implicitly_wait
        driver.get("https://www.google.com")
        actualTitle = driver.title
        softest.soft_assert(softest.assertEqual, actualTitle, "Google","Title does not match")
        # assert actualTitle == "Google "
        print("command executed")
        # if actualTitle == "Google":
        #     print("We are on correct page")
        # else:
        #     print("We are on wrong page")