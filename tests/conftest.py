import pytest
from selenium import webdriver

# @pytest.fixture()
# def set_up():
#     print("Test started")
#     driver = webdriver.Chrome()
#     url = 'https://www.saucedemo.com/'
#     self.driver.get(self.url)
#     self.driver.delete_all_cookies()
#     self.driver.maximize_window()
#     yield
#     driver.quit()
#     print("Test finished")

@pytest.fixture()
def set_up():
    print("\nTest started")
    yield
    print("\nTest finished")