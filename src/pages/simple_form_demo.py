from framework.base_page import BasePage
from locators.locators import Locators


class SimpleFormDemo(BasePage):
    def enter_message(self, text):
        self.set_text(Locators.message_field, text)

    def click_show_message(self):
        self.click_element(Locators.show_message_button)

    def get_text_form1(self):
        return self.get_text(Locators.div_message_id)

    def enter_value_a(self, value):
        self.set_text(Locators.val_a, value)
    def enter_value_b(self, value):
        self.set_text(Locators.val_b, value)
    def calculate(self):
        self.click_element(Locators.get_total_btn)
    def get_total(self):
        return self.get_text(Locators.dsp_value)
