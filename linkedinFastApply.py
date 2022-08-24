from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class LinkedInEasyApply():
    def setUp(self):
        self.driver = webdriver.Chrome()

    def loadBrowser(self, url):
        driver = self.driver
        driver.get(url)

    def WriteElement(self, by, search, value):
        box = self.driver.find_element(by, search)
        if (box is None):
            pass
        box.send_keys(value)

    def search(self, keyword, location):
        self.WriteElement(self, By.XPATH, '', keyword)
        self.WriteElement(self, By.XPATH, '', location)
