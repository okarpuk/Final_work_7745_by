from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class User_info_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# LOCATORS
    profile_exit_button = "//a[@class='btn btn-orange btn-orange--bordered']"

# GETTERS
    def get_profile_exit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_exit_button)))

# ACTIONS
    def click_profile_exit_button(self):
        self.get_profile_exit_button().click()
        print("Profile exit button clicked")

# METHODS
    def exit_from_profile(self):
        self.click_profile_exit_button()
        self.get_current_url()
        self.assert_url('https://7745.by/')