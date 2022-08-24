from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time


class LinkedInEasyApply():
    # xpath list
    XPATH_keywordbox = '//*[@id="JOBS"]/section[1]/input'
    XPATH_locationbox = '//*[@id="JOBS"]/section[2]/input'
    XPATH_locationboxclearbutton = '//*[@id="JOBS"]/section[2]/button'
    XPATH_europaacceptterms = '//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[1]'
    XPATH_searchbutton = '//*[@id="main-content"]/section[1]/div/section/div[2]/button[2]'

    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()

    # helper begin
    def WriteElement(self, by, search, value):
        box = self.driver.find_element(by, search)
        if (box is None):
            pass
        box.send_keys(value)

    def ClickElement(self, by, search):
        box = self.driver.find_element(by, search)
        if (box is None):
            pass
        box.click()
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
