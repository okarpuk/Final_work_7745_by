import time
import pytest
from selenium import webdriver
from pages.cart_page_03 import Cart_page
from pages.my_main_page_01 import Login_page
from pages.tv_page_02 import Main_page

#@pytest.mark.order(3)
def test_buy_product_1(set_up):
    driver = webdriver.Chrome()
    print("\nTest 1 started")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_1()

    cp = Cart_page(driver)
    cp.confirm_product()

    print("Test 1 finished")
    time.sleep(3)
    driver.quit()

#@pytest.mark.order(1)
def test_buy_product_2():
    driver = webdriver.Chrome()
    print("\nTest 2 started")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_2()

    cp = Cart_page(driver)
    cp.confirm_product()

    print("Test 2 finished")
    time.sleep(3)
    driver.quit()

#@pytest.mark.order(2)
def test_buy_product_3():
    driver = webdriver.Chrome()
    print("\nTest 3 started")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_3()

    cp = Cart_page(driver)
    cp.confirm_product()

    print("Test 3 finished")
    time.sleep(3)
    driver.quit()