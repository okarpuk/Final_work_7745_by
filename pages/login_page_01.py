import time

from selenium.webdriver import Keys

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    user_login = "//div[@class='open-logon open-login']//div//input[@id='login-modal-input-login']"
    user_password = "//div[@class='open-logon open-login']//div//input[@id='password']"
    enter_2_button = "div[class='open-logon open-login'] div input[type='submit']"
    # enter_2_button = "//button[normalize-space()='Войти']"

    tv_button = "//a[@class='header-categories__item'][contains(text(),'Телевизоры')]"

    # Getters
    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_selector_registration(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selector_registration)))

    def get_user_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_login)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_enter_2_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.enter_2_button)))

    def get_tv_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tv_button)))

# Actions
    def click_enter_button(self):
        self.get_enter_button().click()
        print("First enter button clicked")

    def click_selector_registration(self):
        self.get_selector_registration().click()
        Select(self.get_selector_registration()).select_by_visible_text("e-mail")

    def input_user_login(self, user_name):
        self.get_user_login().send_keys(user_name)
        print("User login entered")

    def input_user_password(self, password):
        self.get_user_password().send_keys(password)
        # self.get_user_password().send_keys(Keys.RETURN)
        time.sleep(12)
        print("User password entered")

    def click_enter_2_button(self):
        self.get_enter_2_button().click()
        print("Second enter button clicked")
        time.sleep(10)

    def click_tv_button(self):
        self.get_tv_button().click()
        print("TV button clicked")

    def authorization(self):
        self.driver.get(self.url)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.click_selector_registration()
        self.input_user_login("final_project_test@mail.ru")
        self.input_user_password("1A.2b.3c.4d")
        self.click_enter_2_button()
        self.click_tv_button()
        # self.assert_word(self.get_main_word(), "Products")