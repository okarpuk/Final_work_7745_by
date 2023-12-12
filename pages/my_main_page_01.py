from selenium.webdriver.support.select import Select

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_page(Base):
    url = 'https://www.7745.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    enter_button = "//div[@id='logon-link']/div[2]"
    selector_registration = "//div[@class='open-logon open-login']//div//select[@name='prefix']"
    user_name = "//div[@class='open-logon open-login']//div//input[@id='login-modal-input-login']"
    user_password = "//div[@class='open-logon open-login']//div//input[@id='password']"
    enter_2_button = "div[class='open-logon open-login'] div input[value='Войти']"     #CSS SELECTOR !!!!!!!!
    tv_button = "//a[@class='header-categories__item'][contains(text(),'Телевизоры')]"

    # Getters
    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_selector_registration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selector_registration)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_enter_2_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.enter_2_button)))

    def get_tv_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_button)))


# Actions
    def click_enter_button(self):
        self.get_enter_button().click()
        print("Enter button clicked")

    def click_selector_registration(self):
        self.get_selector_registration().click()
        se = Select(self.get_selector_registration)
        for item in se.options:
            if item.text == 'e-mail':
                item.click()
                break
        print("Email registration type selected")







    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("User name entered")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Password entered")















    def authorization(self):
        self.driver.get(self.url)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Products")