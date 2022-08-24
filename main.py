from linkedinFastApply import LinkedInEasyApply
import time


searchword = '''C#'''
location = '''Frankfurt'''

li = LinkedInEasyApply()
li.setUp()
li.loadBrowser('https://www.linkedin.com/jobs')
time.sleep(1)
li.AcceptEuropenCookies()
time.sleep(1)
li.search(searchword, location)
time.sleep(199)
