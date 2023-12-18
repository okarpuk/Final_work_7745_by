import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

# Method current URL
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL - {get_url}")

# Method assert URL
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL correct")

# Method assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Page word correct")

# Method make screenshot
    def screenshot(self):
        current_date_time = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        screenshot_name = 'screenshot' + current_date_time + '.png'
        self.driver.save_screenshot('C:\PyCharm\PycharmProjects\Final_work_7745_by\screen\\' + screenshot_name)
        print(f"SCREENSHOT '{screenshot_name}' CREATED")