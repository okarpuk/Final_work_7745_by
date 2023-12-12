from base.base_class import Base

class Last_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def create_screenshot(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.screenshot()