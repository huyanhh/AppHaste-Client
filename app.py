# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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

def applyGreenhouse(logger, file_path):
    current_url = browser.driver.current_url
    logger.info('Starting at page: {}'.format(current_url))
    form_id = ["first_name", "last_name", "email",
               "phone", "job_application_location"]

    form_values = ["Huyanh", "Hoang", "huyanhh@uci.edu",
                   "5626661609", "Irvine, California, United States"]

    inputs = []
    # TODO: potential bug: id isnt there but the values are by name i.e. pinterest
    for i, text in zip(form_id, form_values):
        element = browser.findElementByID(i)
        # bug in pychrome? if cant find element it overrides previous element if didnt check for 0
        if element:
            inputs.append(True)
            browser.sendTextToElement(text, element)

    # for now we hard code the click.
    location = browser.findElementByID('job_application_location')
    # if location not found then it will use the previous item found, PyChrome issue
    if location:
        browser.sendTextToElement('Irvine, California, United States', location)
        location_item = browser.findElementByClass('ui-menu-item')
        browser.findElementByTag('div', location_item).click()

    if len(inputs) == 0:
        logging.error("None of the standard inputs filled, saving application: {}".format(current_url))
        dictionary_builder.save_question(current_url, "Standard inputs not filled")
    try:
        file_element = browser.findElementByID("file")
        file_element.send_keys(file_path)
    except AttributeError:
        logging.error('File upload error, element does not exist')

    custom = browser.findElementByID("custom_fields")
    field = browser.findElementByTag("div", custom)
    siblings = browser.findSiblingsElements()
    for element in siblings:
        label = browser.findElementByTag("label", element)
        if label and "*" in label.text:
            # check if the question exists in our dictionary
            question = dictionary_builder.check_question(phrase=label.text.split("\n")[0], kw_dict=keyword_dict)
            if question:
                answer = questions_dict[question]
                answers = questions_dict[question].split("|")
                input_box = browser.findElement(element=label, css="input[type=text]")
                if not input_box:
                    dropdown = browser.findElementByTag("select", label)
                    if dropdown:
                        select = Select(dropdown)
                        logger.info("Dropdown found")
                        if "Yes" in dropdown.text and "No" in dropdown.text:
                            try:
                                logger.info("Yes/No question found")
                                select.select_by_visible_text(answer)
                            except NoSuchElementException:
                                logger.error('Could not fill out yes/no question: {}'.format(dropdown.text))
                        else:
                            logger.info("Not a Yes/No question")
                            logger.info('Questions: {}'.format(select.options))

                            def find_answer():
                                for _i, option in enumerate(select.options):
                                    for answer in answers:
                                        if answer in option.text:
                                            select.select_by_index(_i)
                                            return answer
                                return 0
                            if not find_answer():
                                select.select_by_index(1)
                                logger.info('Nothing in dict, selecting "{}"'.format(select.first_selected_option))
                    elif browser.findElementByTag('label', label):  # find the direct child label
                        find_checkbox()
                    else:
                        logger.error("Neither dropdown nor input (No tags found)")
                else:
                    try:
                        input_box.send_keys(answer)
                    except:
                        logger.error("Element isn't valid")
            else:
                question_to_save = label.text.split('\n')[0]
                logging.warning('Question not in graph, saving: {}'.format(question_to_save))
                dictionary_builder.save_question(current_url, 'Question not in graph', question_to_save)
        else:
            logger.warning('Label does not exist or not required')
    logger.info("Finished answering questions")
    try:
        WebDriverWait(browser.driver, 5).until(
            expected_conditions.text_to_be_present_in_element((By.ID, 'resume_filename'), 'HuyanhHoang-Resume.pdf')
        )
    except TimeoutException:
        logger.error('Resume was not uploaded, save file here')
        dictionary_builder.save_question(current_url, 'Resume not uploaded')
        return 0

    # submit = browser.findElementByID("submit_app")
    # page = browser.findElementByTag('html')
    # browser.clickElement(submit)
    # logger.info('Clicked')
    # # might be better to watch for a specific element, because form might not be submitted?
    # try:
    #     WebDriverWait(browser.driver, 5).until(
    #         expected_conditions.staleness_of(page)
    #     )
    #     assert current_url != browser.driver.current_url, 'Fatal: Application URL equals Confirmation URL after submit'
    #     logger.info('Confirmation page, {}'.format(browser.driver.current_url))
    #     return 1
    # except TimeoutException:
    #     logger.error('URL didn\'t change, save file here: {}'.format(current_url))
    #     dictionary_builder.save_question(current_url, 'Resume not uploaded')
    #     return 0

def find_checkbox():
    siblings = browser.findSiblingsElements()
    for sublabel in siblings:
        if 'other' in sublabel.text.lower():
            browser.findElementByTag('input', sublabel).click()

def not_required(label):
    return label and "*" not in label.text

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
    keyword_dict = dictionary_builder.build_dict('../keywords.csv')
    questions_dict = dictionary_builder.build_dict('../questions.csv')
    logger.info('Using keyword dict: {}'.format(keyword_dict))
    logger.info('Using questions dict: {}'.format(questions_dict))


    # file_path = "C:\\Users\\brian\\Desktop\\Test.txt"
    file_path = "/Users/huyanh/Documents/dont_go_in_here/mesos-scraper/samples/HuyanhHoang-Resume.pdf"
    assert os.path.isfile(file_path), 'not a valid path'
    assert file_path.endswith('.pdf'), 'not a pdf'

    greenhouse_urls = dictionary_builder.parse_urls('../samples/urls.csv')
    print(greenhouse_urls)
    # test_url = "https://boards.greenhouse.io/mozilla/jobs/695728"
    # test_url = "http://localhost:8000"
    #greenhouse = ['https://boards.greenhouse.io/autogravitycorporation/jobs/218041#.WOhP0hLyvUJ']
    # greenhouse = [test_url]
    # browser.open(greenhouse[0])
    # applyGreenhouse(logger, file_path=file_path)


    applied = 0
    for link in greenhouse_urls:
        browser.open(link)
        applied += applyGreenhouse(logger, file_path)
    logger.info('Successfully applied to {} out of {} companies'.format(applied, len(greenhouse_urls)))


    logger.info('--------END SESSION--------')


