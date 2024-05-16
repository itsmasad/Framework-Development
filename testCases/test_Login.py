import softest
import pytest


class test_Login(softest.TestCase):

    def test_Login_001(self,setUp):
        driver = setUp()
        driver.implicitly_wait(3)
        driver.get("https://www.google.com")
        actualTitle = driver.title
        self.soft_assert(self.assertEqual, actualTitle, 'Google', 'Title does not match')
