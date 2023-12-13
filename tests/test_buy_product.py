import time
from selenium import webdriver
# from pages.cart_page_03 import Cart_page
# from pages.last_page import Last_page
from pages.login_page_01 import Login_page
from pages.tv_page_02 import Tv_page


# from pages.tv_page_02 import Main_page
# from pages.user_info_page_04 import User_info_page

def test_buy_product():
    driver = webdriver.Chrome()
    print("Test started")

    login = Login_page(driver)
    login.authorization()

    tp = Tv_page(driver)
    tp.select_tv()
    #
    # cp = Cart_page(driver)
    # cp.confirm_product()
    #
    # uip = User_info_page(driver)
    # uip.confirm_user_info()
    #
    # pp = Payment_page(driver)
    # pp.click_finish_button()
    #
    # lp = Last_page(driver)
    # lp.create_screenshot()

    time.sleep(5)
