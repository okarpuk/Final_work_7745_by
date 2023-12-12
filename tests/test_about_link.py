import time
from selenium import webdriver
from pages.my_main_page_01 import Login_page
from pages.tv_page_02 import Main_page

def test_about_link():
    driver = webdriver.Chrome()
    print("Test started")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    time.sleep(3)
