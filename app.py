# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility import record
import os
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
greenhouse = []
# url = "https://boards.greenhouse.io/6sense/jobs/238123"
# url = "https://boards.greenhouse.io/checkr/jobs/163433?gh_jid=163433"
greenhouse.append("https://boards.greenhouse.io/yext/jobs/573036")
greenhouse.append("https://boards.greenhouse.io/acorns/jobs/126365?gh_jid=126365")
url = "https://boards.greenhouse.io/acorns/jobs/126365?gh_jid=126365"
# url = "https://jobs.lever.co/academia/53029c67-058c-4162-a4ec-461f21abad38/apply"
# url = "https://www.23andme.com/careers/oXNM2fwi/apply/"
# url = "http://jobs.jobvite.com/23andme/job/oXNM2fwi/apply?nl=1"
# url = "https://www.google.com"
browser.open(url)
browser.scrollDown()
### LEVER
# form_id = ["name", "email",
#            "phone"]#, "job_application_location"]
# form_values = ["Huyanh Hoang", "huyanhh@uci.edu",
#                "5626661609"]#, "Irvine, California, United States"]
#
# zipped = zip(form_id, form_values)
#
# for i, text in zip(form_id, form_values):
#     element = browser.findElementByName(i)
#     browser.sendTextToElement(text, element)
#
# file_element = browser.findElementByID("resume-upload-input")
# file_path = "/Users/huyanh/Documents/dont_go_in_here/mesos-scraper/samples/HuyanhHoang-Resume.pdf"
# file_element.send_keys(file_path)
#
# submit = browser.findElement(element=None,id=None,name=None,classname="template-btn-submit",xpath=None,tag="button",css=None,linktext=None,partialtext=None)
# browser.clickElement(submit)

### GREENHOUSE

def applyGreenhouse():
    form_id = ["first_name", "last_name", "email",
               "phone", "job_application_location"]

    form_values = ["Huyanh", "Hoang", "huyanhh@uci.edu",
                   "5626661609", "Irvine, California, United States"]

    for i, text in zip(form_id, form_values):
        element = browser.findElementByID(i)
        browser.sendTextToElement(text, element)

    file_element = browser.findElementByID("file")
    file_path = "/Users/huyanh/Documents/dont_go_in_here/mesos-scraper/samples/HuyanhHoang-Resume.pdf"
    file_element.send_keys(file_path)

    custom = browser.findElementByID("custom_fields")
    field = browser.findElementByTag("div", custom)
    siblings = browser.findSiblingsElements()
    for element in siblings:
        label = browser.findElementByTag("label", element)
        print(label.text)
        if "*" in label.text:
            input_box = browser.findElement(element=label, css="input[type=text]")
            input_box.send_keys("kek")

applyGreenhouse()
    # submit = browser.findElementByID("submit_app")

### JOBVITE

#
# try:
#     element = WebDriverWait(browser.driver, 5).until(
#         EC.visibility_of_any_elements_located((By.CLASS_NAME, "jv-careersite"))
#     )
#     print(element)
# except:
#     print("exception")

# script = "document.getElementById('file-input-0').setAttribute('style','visibility:visible;');"

# browser.driver.execute_script(script)
# file_path = "/Users/huyanh/Documents/dont_go_in_here/mesos-scraper/samples/HuyanhHoang-Resume.pdf"
# file_element.send_keys(file_path)

#browser.clickElement(submit)

# excellent
#
# file_element = browser.findElementByID("file-input-0")
# file_path = "/Users/huyanh/Documents/dont_go_in_here/mesos-scraper/samples/HuyanhHoang-Resume.pdf"
# file_element.send_keys(file_path)
