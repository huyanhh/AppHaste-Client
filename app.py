# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utility import record
#
# driver = webdriver.Chrome('./bin/chromedriver')
# driver.get("http://www.google.com")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

from pyChrome import PyChrome

browser = PyChrome()
# url = "https://boards.greenhouse.io/6sense/jobs/238123"
url = "https://jobs.lever.co/21/1c62cece-d385-4b79-a36e-5cb30cd1e9f0/apply"
browser.open(url)
# browser.scrollDown()
# form_id = ["first_name", "last_name", "email",
#            "phone", "job_application_location"]
# form_values = ["Huyanh", "Hoang", "huyanhh@uci.edu",
#                "5626661609", "Irvine, California, United States"]
#
# zipped = zip(form_id, form_values)
# for i, text in zipped:
#     element = browser.findElementByID(i)
#     browser.sendTextToElement(text, element)

# attach_element = browser.findElementByXPath("#main_fields > div:nth-child(11) > div > div.link-container > a:nth-child(1)")
# browser.clickElement(attach_element)
# file_element = browser.findElementByID("file")
# attach_element.send_keys("/Users/huyanh/Documents/#job\ apps/Resume/Awesome-CV/HuyanhHoang-Resume.pdf")
# attach_element.send_keys(Keys.RETURN)

form_id = ["name", "email",
        "phone", "urls[LinkedIn]"]
form_values = ["kek kek", "kkek@uci.edu",
            "5626661609", "http://linkedin.com/in/kek"]

for i, text in zip(form_id, form_values):
    element = browser.findElementByName(i)
    browser.sendTextToElement(text, element)

file_element = browser.findElementByID("resume-upload-input")
# file_element.send_keys("/Users/huyanh/Documents/#job\ apps/Resume/Awesome-CV/HuyanhHoang-Resume.pdf")

submit = browser.findElement(element=None, id=None, name=None, classname="template-btn-submit")
browser.clickElement(file_element)
# browser.clickElement(submit)