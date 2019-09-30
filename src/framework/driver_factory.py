"""
DriverFactory class
"""
import os, sys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DriverFactory():

    def __init__(self, browser='ff', browser_version=None, os_name=None):
        "Constructor for the Driver factory"
        self.browser = browser
        self.browser_version = browser_version
        self.os_name = os_name
        self.selenium_hub_url = os.getenv('SELENIUM_HUB_URL', 'http://localhost:4444')

    def get_web_driver(self, remote_flag, os_name, os_version, browser, browser_version, remote_project_name,
                       remote_build_name):
        "Return the appropriate driver"
        if (remote_flag.lower() == 'y'):
            try:
                web_driver = self.run_remote(os_name, os_version, browser, browser_version)

            except Exception as e:
                print("\nException when trying to get remote webdriver:%s" % sys.modules[__name__])
                print("Python says:%s" % str(e))

        elif (remote_flag.lower() == 'n'):
            web_driver = self.run_local(os_name, os_version, browser, browser_version)
        else:
            print("DriverFactory does not know the browser: ", browser)
            web_driver = None

        return web_driver


    def run_remote(self, os_name, os_version, browser, browser_version):
        "Run the test in selenium grid when remote flag is 'Y'"
        # Get the sauce labs credentials from sauce.credentials file
        if browser.lower() == 'ff' or browser.lower() == 'firefox':
            desired_capabilities = DesiredCapabilities.FIREFOX
        elif browser.lower() == 'ie':
            desired_capabilities = DesiredCapabilities.INTERNETEXPLORER
        elif browser.lower() == 'chrome':
            desired_capabilities = DesiredCapabilities.CHROME
        elif browser.lower() == 'opera':
            desired_capabilities = DesiredCapabilities.OPERA
        elif browser.lower() == 'safari':
            desired_capabilities = DesiredCapabilities.SAFARI
        desired_capabilities['version'] = browser_version
        desired_capabilities['platform'] = os_name + ' ' + os_version

        return webdriver.Remote(command_executor=self.selenium_hub_url,
                                desired_capabilities=desired_capabilities)

    def run_local(self, os_name, os_version, browser, browser_version):
        "Return the local driver"
        local_driver = None
        if browser.lower() == "ff" or browser.lower() == 'firefox':
            local_driver = webdriver.Firefox()
        elif browser.lower() == "ie":
            local_driver = webdriver.Ie()
        elif browser.lower() == "chrome":
            local_driver = webdriver.Chrome()
        elif browser.lower() == "safari":
            local_driver = webdriver.Safari()
        return local_driver

    def get_firefox_driver(self):
        "Return the Firefox driver"
        driver = webdriver.Firefox(firefox_profile=self.get_firefox_profile())

        return driver

    def get_firefox_profile(self):
        "Return a firefox profile"

        return self.set_firefox_profile()

    def set_firefox_profile(self):
        "Setup firefox with the right preferences and return a profile"
        try:
            self.download_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'downloads'))
            if not os.path.exists(self.download_dir):
                os.makedirs(self.download_dir)
        except Exception as e:
            print("Exception when trying to set directory structure")
            print(str(e))

        profile = webdriver.firefox.firefox_profile.FirefoxProfile()
        set_pref = profile.set_preference
        set_pref('browser.download.folderList', 2)
        set_pref('browser.download.dir', self.download_dir)
        set_pref('browser.download.useDownloadDir', True)
        set_pref('browser.helperApps.alwaysAsk.force', False)
        set_pref('browser.helperApps.neverAsk.openFile', 'text/csv,application/octet-stream,application/pdf')
        set_pref('browser.helperApps.neverAsk.saveToDisk',
                 'text/csv,application/vnd.ms-excel,application/pdf,application/csv,application/octet-stream')
        set_pref('plugin.disable_full_page_plugin_for_types', 'application/pdf')
        set_pref('pdfjs.disabled', True)

        return profile
