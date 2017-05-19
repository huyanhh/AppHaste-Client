# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import os
import dictionary_builder
import logging
import datetime

curr_time = datetime.datetime.now().strftime("%Y-%m-%d")
#filename='../logs/{}.log'.format(curr_time),
logging.basicConfig(
                    filemode='a',
                    format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.WARNING)
logging.getLogger('app').setLevel(logging.INFO)

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

def applyGreenhouse(logger):
    form_id = ["first_name", "last_name", "email",
               "phone", "job_application_location"]

    form_values = ["Huyanh", "Hoang", "huyanhh@uci.edu",
                   "5626661609", "Irvine, California, United States"]

    inputs = []
    for i, text in zip(form_id, form_values):
        element = browser.findElementByID(i)
        # bug in pychrome? if cant find element it overrides previous element if didnt check for 0
        if element:
            inputs.append(True)
            browser.sendTextToElement(text, element)

    if len(inputs) == 0:
        logging.error("None of the standard inputs filled, saving application: {}".format(browser.driver.current_url))

    try:
        file_element = browser.findElementByID("file")
        file_path = "/Users/huyanh/Documents/dont_go_in_here/mesos-scraper/samples/HuyanhHoang-Resume.pdf"
        file_element.send_keys(file_path)
    except AttributeError:
        logging.error('File upload error, element does not exist')

    custom = browser.findElementByID("custom_fields")
    field = browser.findElementByTag("div", custom)
    siblings = browser.findSiblingsElements()
    for element in siblings:
        label = browser.findElementByTag("label", element)
        if "*" in label.text:
            question = dictionary_builder.check_question(phrase=label.text, kw_dict=keyword_dict)
            if question:
                answer = questions_dict[question]
                input_box = browser.findElement(element=label, css="input[type=text]")
                if not input_box:
                    dropdown = browser.findElementByTag("select", label)
                    if dropdown:
                        select = Select(dropdown)
                        logger.info("Dropdown found")
                        if "Yes" in dropdown.text and "No" in dropdown.text:
                            logger.info("yes/no question found")
                            select.select_by_visible_text(answer)
                        else:
                            logger.info("not a yes/no question")
                            logger.info('Questions: {}'.format(select.options))
                            select.select_by_index(1)
                            logger.info('Selected "{}"'.format(select.first_selected_option))
                    else:
                        logger.error("Neither dropdown or input (No tags found)")
                else:
                    try:
                        input_box.send_keys(answer)
                    except:
                        logger.error("Element isn't valid")
            else:
                logging.warning('Question not in graph, saving: {}'.format(label.text))
                dictionary_builder.save_question(label.text, browser.driver.current_url)
    logger.info("Finished answering questions")
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

# browser.quit()

if __name__ == '__main__':
    logger = logging.getLogger('app')
    logger.info('\n --------NEW SESSION--------')
    from pyChrome import PyChrome
    browser = PyChrome()
    keyword_dict = dictionary_builder.build_dict('../keywords.txt')
    questions_dict = dictionary_builder.build_dict('../questions.txt')
    logger.info('Using keyword dict: {}'.format(keyword_dict))
    logger.info('Using questions dict: {}'.format(questions_dict))

    greenhouse = []
    greenhouse = ["https://boards.greenhouse.io/embed/job_app?for=zocdoc&token=122726&b=https://www.zocdoc.com/about/careers/",
                  "https://boards.greenhouse.io/acquia/jobs/645684",
                  "https://boards.greenhouse.io/betterment/jobs/13624?gh_jid=13624",
                  "https://boards.greenhouse.io/6sense/jobs/238123",
                  "https://boards.greenhouse.io/checkr/jobs/163433?gh_jid=163433",
                  "https://boards.greenhouse.io/yext/jobs/573036",
                  "https://boards.greenhouse.io/acorns/jobs/126365?gh_jid=126365",
                  "https://boards.greenhouse.io/asana/jobs/613752?gh_src=bso7t51#.WRdFY1PyvOQ"
                  "https://boards.greenhouse.io/embed/job_app?for=amino&t=lwpnt21&token=504429&b=https://amino.com/careers/504429/"]
    # greenhouse.append("https://boards.greenhouse.io/6sense/jobs/238123")
    for link in greenhouse:
        browser.open(link)
        applyGreenhouse(logger)
        browser.newTab()
        browser.rightTab()

    logger.info('--------END SESSION--------')