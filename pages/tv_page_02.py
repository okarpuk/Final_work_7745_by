import time
from base.base_class import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tv_page(Base):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

# LOCATORS
    actual_word = "h1.bread-h1"
    price_slider_1 = "//*[@id='filter-range-price']/span[1]"
    price_slider_2 = "//*[@id='filter-range-price']/span[2]"
    brands_dropdown = "div.js-show-features-block label"
    checkbox_lg = "div.catalog-filter-popover__columns_2 :nth-child(10) span.i-checkbox__faux"
    checkbox_diagonal = "[data-param='11830'] :nth-child(9) span.i-checkbox__faux"
    checkbox_screen_technology = "[data-param='11829'] :nth-child(3) span.i-checkbox__faux"
    checkbox_screen_resolution = "[data-param='11841'] :nth-child(4) span.i-checkbox__faux"
    confirm_filter_button = "//div[@class='catalog-sbf-top catalog-sbf-btnset']/button[1]" # или CSS "div.catalog-sbf-top .btn-orange"
    add_to_cart_button = "div.action-btn .btn"
    cart_button = "//a[@id='cart-link']"

# GETTERS
    def get_actual_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.actual_word)))

    def get_price_slider_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_1)))

    def get_price_slider_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_slider_2)))

    def get_brands_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.brands_dropdown)))

    def get_checkbox_lg(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkbox_lg)))

    def get_checkbox_diagonal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkbox_diagonal)))

    def get_checkbox_screen_technology(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkbox_screen_technology)))

    def get_checkbox_screen_resolution(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.checkbox_screen_resolution)))

    def get_confirm_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_filter_button)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

# ACTIONS
    def move_price_slider_1(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_price_slider_1()).move_by_offset(20, 0).release().perform()
        print("Slider min price moved")

    def move_price_slider_2(self):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_price_slider_2()).move_by_offset(-50, 0).release().perform()
        print("Slider max price moved")

    def click_brands_dropdown(self):
        self.get_brands_dropdown().click()
        print("Brands dropdown clicked")

    def click_checkbox_lg(self):
        self.get_checkbox_lg().click()
        print("LG checkbox selected")

    def click_checkbox_diagonal(self):
        self.get_checkbox_diagonal().click()
        print("Diagonal selected")

    def click_checkbox_screen_technology(self):
        self.get_checkbox_screen_technology().click()
        print("Screen technology selected")

    def click_checkbox_screen_resolution(self):
        self.get_checkbox_screen_resolution().click()
        print("Screen resolution selected")

    def click_confirm_filter_button(self):
        self.get_confirm_filter_button().click()
        print("Confifm button clicked")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Add to cart button clicked")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Cart button clicked")

# METHODS
    def select_tv(self):
        self.get_current_url()
        self.assert_url('https://7745.by/catalog/televizory')
        self.assert_page_text(self.get_actual_word(), "Телевизоры")
        self.move_price_slider_1()
        self.move_price_slider_2()
        self.click_brands_dropdown()
        self.click_checkbox_lg()
        self.driver.execute_script("window.scrollBy(0, 800);") #Другие способы прокручивания страницы до элемента не работают
        self.click_checkbox_diagonal()
        self.click_checkbox_screen_technology()
        self.click_checkbox_screen_resolution()
        self.click_confirm_filter_button()
        time.sleep(3) # Ожидания не срабатывают - выдает ошибку:  stale element not found
        self.screenshot()
        self.click_add_to_cart_button()
        self.click_cart_button()
