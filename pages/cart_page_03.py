from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart_page(Base):

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

# LOCATORS
    actual_word = "div[class='cart-form-section__header open-popup jc--n'] h2"
    plus_one_product_button = "//button[normalize-space()='+']"
    user_type_radiobutton = "//*[@id='svelte-page']/div/div[1]/div[4]/div[1]/label[2]/span/span[1]"
    unp_field = "//*[@id='cart[org][UNP]']"
    organization_name_field = "//*[@id='cart[org][name]']"
    delete_button = "//button[@title='Удалить из заказа']"
    profile_icon = "//div[@class='svg-icon header-icon__icon--person']"

# GETTERS
    def get_actual_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.actual_word)))

    def get_plus_one_product_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plus_one_product_button)))

    def get_user_type_radiobutton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_type_radiobutton)))

    def get_unp_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.unp_field)))

    def get_organization_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.organization_name_field)))

    def get_delete_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_button)))

    def get_profile_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_icon)))

# ACTIONS
    def click_plus_one_product_button(self):
        self.get_plus_one_product_button().click()
        print("Plus one product button clicked")

    def click_user_type_radiobutton(self):
        self.get_user_type_radiobutton().click()
        print("User type chosen")

    def input_unp(self, unp_number):
        self.get_unp_field().send_keys(unp_number)
        print("UNP entered")

    def input_organization_name(self, organization):
        self.get_organization_name_field().send_keys(organization)
        print("Organization name entered")

    def click_delete_button(self):
        self.get_delete_button().click()
        print("Product deleted")

    def click_profile_icon(self):
        self.get_profile_icon().click()
        print("Entered to profile")

# METHODS
    def confirm_offer(self):
        self.get_current_url()
        self.assert_url('https://7745.by/cart')
        self.assert_page_text(self.get_actual_word(), "Способ доставки")
        self.click_plus_one_product_button()
        self.screenshot()
        self.click_user_type_radiobutton()
        self.input_unp("12121212")
        self.input_organization_name("My test organization")
        self.screenshot()
        self.driver.execute_script("window.scrollBy(0, -800);") #Другие способы прокручивания страницы до элемента не работают
        self.click_delete_button()
        self.click_profile_icon()
