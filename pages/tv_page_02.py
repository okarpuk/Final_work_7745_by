from selenium.webdriver import ActionChains

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tv_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    price_slider_1 = "//*[@id='filter-range-price']/span[1]"
    price_slider_2 = "//*[@id='filter-range-price']/span[2]"
    brands_dropdown = "//*[@id='catalog-filter-form']/div[3]/div[2]/div[8]/label"
    checkbox_lg = "//*[@id='catalog-filter-form']/div[3]/div[2]/div[10]/div/div/div/div[10]/label/span[1]/span"
    checkbox_diagonal = "//*[@id='catalog-filter-form']/div[5]/div[3]/div[6]/label/span[1]"
    checkbox_screen_technology = "//*[@id='catalog-filter-form']/div[6]/div[3]/div[2]/label/span[1]/span"
    checkbox_screen_resolution = "//*[@id='catalog-filter-form']/div[7]/div[3]/div[3]/label/span[1]/span"
    confirm_filter_button = "//*[@id='catalog-filter-form']/div[33]/button[1]"
    add_to_cart_button = "//*[@id='panel']/div[1]/div[4]/div/div[2]/div[2]/div[6]/div[1]/div[1]/div/div[2]/div[2]/div[1]/button"
    cart_button = "//a[@id='cart-link']"

# Getters
    def get_price_slider_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_1)))

    def get_price_slider_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_2)))

    def get_brands_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brands_dropdown)))

    def get_checkbox_lg(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_lg)))

    def get_checkbox_diagonal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_diagonal)))

    def get_checkbox_screen_technology(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_screen_technology)))

    def get_checkbox_screen_resolution(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_screen_resolution)))

    def get_confirm_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_filter_button)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))


# Actions
    def move_price_slider_1(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_price_slider_1()).move_by_offset(20, 0).release().perform()
        print("Slider 1 moved")

    def move_price_slider_2(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_price_slider_2()).move_by_offset(-50, 0).release().perform()
        print("Slider 2 moved")

    def click_brands_dropdown(self):
        self.get_brands_dropdown().click()
        print("Brands dropdown clicked")

    def click_checkbox_lg(self):
        self.get_checkbox_lg().click()
        print("LG checkbox selected")



    # def execute_script(self, param, param1):
    #     self.execute_script("arguments[0].click();", self.get_checkbox_diagonal())
    #     print("Diagonal selected")




    # def click_checkbox_diagonal(self):
    #     # self.get_checkbox_diagonal().click()
    #     self.driver.execute_script("arguments[0].click();", self.get_checkbox_diagonal())
    #     print("Diagonal selected")

    # def click_checkbox_diagonal(self):
    #     self.get_checkbox_diagonal().location_once_scrolled_into_view
    #     self.get_checkbox_diagonal().click()

    def click_checkbox_diagonal(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_checkbox_diagonal()).perform()
        self.get_checkbox_diagonal().click()








    # Methods

    def select_tv(self):
        self.move_price_slider_1()
        self.move_price_slider_2()
        self.click_brands_dropdown()
        self.click_checkbox_lg()
        self.click_checkbox_diagonal()




        # self.assert_url('https://saucelabs.com/')

