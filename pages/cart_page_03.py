from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# LOCATORS
    plus_one_product_button = "//button[normalize-space()='+']"
    dropdown_date = "//*[@id='svelte-page']/div/div[1]/div[2]/div[5]/div/span/div/select"
    need_call_radiobutton = "//*[@id='svelte-page']/div/div[1]/div[6]/div[1]/div/label[2]/span/input"
    delete_button = "//button[@title='Удалить из заказа']"
    profile_icon = "//div[@class='svg-icon header-icon__icon--person']"



# GETTERS
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))








# Actions
    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Checkout button clicked")

    def confirm_product(self):
        self.click_checkout_button()
        self.get_current_url()