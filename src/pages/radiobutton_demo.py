from framework.base_page import BasePage
from locators.locators import Locators

class RadiobuttonDemo(BasePage):
    def click_male_btn(self):
        self.click_element(Locators.radio_btn_male)

    def click_female_btn(self):
        self.click_element(Locators.radio_btn_female)

    def click_get_checked_value_btn(self):
        self.click_element(Locators.get_checked_button)

    def get_checked_message(self):
        return self.get_text(Locators.checked_message)

    
