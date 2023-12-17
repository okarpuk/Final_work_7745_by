from selenium import webdriver
from pages.login_page_01 import Login_page
from pages.tv_page_02 import Tv_page
from pages.cart_page_03 import Cart_page
from pages.user_info_page_04 import User_info_page

def test_buy_product(set_up):
    driver = webdriver.Chrome()

    login = Login_page(driver)
    login.authorization()

    tp = Tv_page(driver)
    tp.select_tv()

    cp = Cart_page(driver)
    cp.confirm_offer()

    uip = User_info_page(driver)
    uip.exit_from_profile()