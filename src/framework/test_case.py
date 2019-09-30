import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType

from locators.locators import Locators


class TestCase(unittest.TestCase):
    # driver = None

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls) -> None:
        selenium_hub_url = os.getenv('SELENIUM_HUB_URL', 'http://127.0.0.1:4444/wd/hub')
        browser = os.getenv('BROWSER', 'chrome')

        cap = {'browserName': browser, 'javascriptEnabled': True}
        cls.driver = webdriver.Remote(
            command_executor=selenium_hub_url,
            desired_capabilities=cap)

    @allure.step("Launch site")
    def launch_site(self, url):
        self.driver.get(url)
        self.takeScreenshot("Launch_site: " + url)

    @allure.step("Verify Title loaded")
    def verify_page_loaded(self, page):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(Locators.page_title_locator))
        self.takeScreenshot("Title loaded")

    def takeScreenshot(self, title):
        allure.attach(self.driver.get_screenshot_as_png(), title, attachment_type=AttachmentType.PNG)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
