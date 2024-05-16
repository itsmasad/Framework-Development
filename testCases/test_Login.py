import softest
import pytest
from selenium import webdriver


class test_Login_Cases:
    @staticmethod
    @pytest.mark.smock()
    def test_Login_001():
        print("Test has been executed")