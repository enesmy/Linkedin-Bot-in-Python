from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import chromedriver_autoinstaller
import time


class LinkedInEasyApply():

    # xpath list begin

    # when you logged in. this option is disabled
    # XPATH_keywordbox = '//*[@id="JOBS"]/section[1]/input'
    # XPATH_locationbox = '//*[@id="JOBS"]/section[2]/input'

    XPATH_locationboxclearbutton = '//*[@id="JOBS"]/section[2]/button'
    XPATH_europaacceptterms = '//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[1]'
    XPATH_searchbutton = '//*[@id="main-content"]/section[1]/div/section/div[2]/button[2]'
    # xpath list end

    # classNames
    CLASSNAME_searchboxLabel = 'jobs-search-box__keywords-label'

    # Do not use this path that is extracted from "chrome://version/"
    exec_path_chrome = '''C://Users//enesm//AppData//Local//Google//Chrome//User Data'''

    # send key speed
    send_key_speed = 0.1

    def setUp(self):
        chromedriver_autoinstaller.install()
        self.ch_options = webdriver.ChromeOptions()  # Chrome Options
        # Extract this path from "chrome://version/"
        self.ch_options.add_argument(
            'user-data-dir='+self.exec_path_chrome)

        self.driver = webdriver.Chrome(
            chrome_options=self.ch_options)

        # Maximum size
        self.driver.maximize_window()

    # helper begin
    def WriteElement(self, by, search, value):
        box = self.driver.find_elements(by, search)
        if (box.__len__() > 0):
            self.send_keys(box[0], value)
            return True
        return False

    def send_keys(self, box, value):
        for character in value:
            box.send_keys(character)
            time.sleep(self.send_key_speed)  # pause for selected seconds

    def ClickElement(self, by, search):
        command = self.driver.find_elements(by, search)
        if (command.__len__() > 0):
            command[0].click()
            return True
        return False
    # helper end

    def loadBrowser(self, url):
        driver = self.driver
        driver.get(url)

    def AcceptEuropenCookies(self):
        self.ClickElement(
            By.XPATH, self.XPATH_europaacceptterms)

    def search(self, keyword, location):
        # activate searchbox and location box
        self.ClickElement(
            By.CLASS_NAME, self.CLASSNAME_searchboxLabel)
        time.sleep(1)
        self.send_keys(self.driver.switch_to.active_element, keyword)
        self.driver.switch_to.active_element.send_keys(Keys.TAB)
        time.sleep(1)
        self.send_keys(self.driver.switch_to.active_element, location)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        pass

    def nextWorkPosition(self):
        pass

    def nextPage(self):
        pass

    def ApplyIfPossible(self):
        pass
