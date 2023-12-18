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

    def page_name_assert(self):
        page_name = self.driver.find_element(By.CSS_SELECTOR, ".bread-h1.catalog-header-news-articles")
        page_name_text = page_name.text
        print(f"PAGE NAME - {page_name_text}")
        assert page_name_text == "Личный кабинет"
        print("Page name correct")


# METHODS
    def exit_from_profile(self):
        self.get_current_url()
        self.assert_url('https://7745.by/profile/common')
        self.page_name_assert()
        self.click_profile_exit_button()
        self.get_current_url()
        self.assert_url('https://7745.by/')