from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import chromedriver_autoinstaller
import time


class LinkedInEasyApply():

    # xpath list begin
    XPATH_keywordbox = '//*[@id="JOBS"]/section[1]/input'
    XPATH_locationbox = '//*[@id="JOBS"]/section[2]/input'
    XPATH_locationboxclearbutton = '//*[@id="JOBS"]/section[2]/button'
    XPATH_europaacceptterms = '//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[1]'
    XPATH_searchbutton = '//*[@id="main-content"]/section[1]/div/section/div[2]/button[2]'
    # xpath list end

    # Do not use this path that is extracted from "chrome://version/"
    exec_path_chrome = '''C://Users//enesm//AppData//Local//Google//Chrome//User Data'''

    def setUp(self):
        chromedriver_autoinstaller.install()
        self.ch_options = webdriver.ChromeOptions()  # Chrome Options
        # Extract this path from "chrome://version/"
        self.ch_options.add_argument(
            'user-data-dir='+self.exec_path_chrome)

        self.driver = webdriver.Chrome(
            chrome_options=self.ch_options)

    # helper begin
    def WriteElement(self, by, search, value):
        box = self.driver.find_elements(by, search)
        if (box.__len__() > 0):
            box[0].send_keys(value)
            return True
        return False

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
        # Keyword Search
        self.WriteElement(
            By.XPATH, self.XPATH_keywordbox, keyword)
        time.sleep(1)
        # cancel focus
        self.ClickElement(
            By.TAG_NAME, 'body')
        # location
        self.ClickElement(
            By.XPATH, self.XPATH_locationboxclearbutton)
        time.sleep(1)
        self.WriteElement(
            By.XPATH, self.XPATH_locationbox, location)
        time.sleep(1)
        # cancel focus
        self.ClickElement(
            By.TAG_NAME, 'body')

        # send form
        self.ClickElement(
            By.XPATH, self.XPATH_searchbutton)

    def nextWorkPosition(self):
        pass

    def nextPage(self):
        pass

    def ApplyIfPossible(self):
        pass
