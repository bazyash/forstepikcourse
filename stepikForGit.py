import os
import time
from selenium import webdriver

# path to the driver
driver_path = r"C:\Users\Temp\pythonStepik\curs2\87.0.4280.88\chromedriver.exe"

urls = {
    'Success': "http://suninjuly.github.io/registration1.html",
    'Fail': "http://suninjuly.github.io/registration2.html"
        }

try:

    if os.path.exists(driver_path):
        # use special driver file
        browser = webdriver.Chrome(driver_path)
    else:
        # use driver from Windows PATH
        browser = webdriver.Chrome()

    # loop over all urls
    for result, url in urls.items():

        print(f'This attempt should end with {result}')

        # open page
        browser.get(url)

        # find all required fields
        #required_inputs = browser.find_elements_by_tag_name("input[type=text]:required")

        # find 3 required fields: First name, last name, email
        # search for label by text and then take the following element of the same level
        first_name_input = browser.find_element_by_xpath('//label[contains(text(), "First name")]/following-sibling::*[1][self::input]')
        last_name_input = browser.find_element_by_xpath('//label[contains(text(), "Last name")]/following-sibling::*[1][self::input]')
        email_input = browser.find_element_by_xpath('//label[contains(text(), "Email")]/following-sibling::*[1][self::input]')
        required_inputs = [first_name_input, last_name_input, email_input]

        # fill the form
        for input in required_inputs:
            input.send_keys("Мой ответ")

        # find and click button to submit form
        button = browser.find_element_by_xpath('//button[text()="Submit"]')
        button.click()
        time.sleep(1)

        # define expected and actual text
        welcome_text = browser.find_element_by_tag_name('h1').text
        expected_text = "Congratulations! You have successfully registered!"

        # final verification
        assert welcome_text == expected_text

finally:
    time.sleep(5)
    browser.quit()
