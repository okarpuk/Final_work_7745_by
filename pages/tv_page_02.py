from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    price_slider_1 = "//*[@id='filter-range-price']/span[1]"
    price_slider_2 = "//*[@id='filter-range-price']/span[2]"
    brands_dropdown = driver.find_element(By.XPATH, "//*[@id='catalog-filter-form']/div[3]/div[2]/div[8]/label")
    checkbox_lg = driver.find_element(By.XPATH,
                                      "//*[@id='catalog-filter-form']/div[3]/div[2]/div[10]/div/div/div/div[10]/label/span[1]/span")
    checkbox_diagonal = driver.find_element(By.XPATH,
                                            "//*[@id='catalog-filter-form']/div[5]/div[3]/div[6]/label/span[1]")
    checkbox_screen_technology = driver.find_element(By.XPATH,
                                                     "//*[@id='catalog-filter-form']/div[6]/div[3]/div[2]/label/span[1]/span")
    checkbox_screen_resolution = driver.find_element(By.XPATH,
                                                     "//*[@id='catalog-filter-form']/div[7]/div[3]/div[3]/label/span[1]/span")
    confirm_filter_button = driver.find_element(By.XPATH, "//*[@id='catalog-filter-form']/div[33]/button[1]")

    add_to_cart_button = driver.execute_script("return document.querySelector('.action-btn--btn-buy');")
    cart_button = driver.find_element(By.XPATH, "//a[@id='cart-link']")








    # Getters
    def get_add_to_cart_button_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_1)))

    def get_add_to_cart_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_2)))

    def get_add_to_cart_button_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_3)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_about_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_button)))

# Actions
    def click_add_to_cart_button_1(self):
        self.get_add_to_cart_button_1().click()
        print("Add to cart button 1 clicked")

    def click_add_to_cart_button_2(self):
        self.get_add_to_cart_button_2().click()
        print("Add to cart button 2 clicked")

    def click_add_to_cart_button_3(self):
        self.get_add_to_cart_button_3().click()
        print("Add to cart button 3 clicked")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Cart button clicked")

    def click_menu_button(self):
        self.get_menu_button().click()
        print("Menu button clicked")

    def click_about_button(self):
        self.get_about_button().click()
        print("About button clicked")

# Methods
    def select_product_1(self):
        self.get_current_url()
        self.click_add_to_cart_button_1()
        self.click_cart_button()
        self.get_current_url()

    def select_product_2(self):
        self.get_current_url()
        self.click_add_to_cart_button_2()
        self.click_cart_button()
        self.get_current_url()

    def select_product_3(self):
        self.get_current_url()
        self.click_add_to_cart_button_3()
        self.click_cart_button()
        self.get_current_url()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu_button()
        self.click_about_button()
        self.get_current_url()
        self.assert_url('https://saucelabs.com/')
