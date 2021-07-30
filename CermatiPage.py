import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CermatiLocators import LocatorsElements


class BasePage(object):
    def __init__(self, driver):
        self.driver=driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        self.driver.find_element(*by_locator).send_keys(Keys.ENTER)

    def delete_text(self, by_locator):
        self.driver.find_element(*by_locator).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(*by_locator).send_keys(Keys.DELETE)

class CermatiPage(BasePage):
    def input_all_field(self, email, password, confirmPassword, firstName, lastName, mobilePhone, residenceCity):
        self.enter_text(LocatorsElements.FIELD_EMAIL, email)
        self.enter_text(LocatorsElements.FIELD_PASSWORD, password)
        self.enter_text(LocatorsElements.FIELD_CONFIRM_PASSWORD, confirmPassword)
        self.enter_text(LocatorsElements.FIELD_FIRST_NAME, firstName)
        self.enter_text(LocatorsElements.FIELD_LAST_NAME, lastName)
        self.enter_text(LocatorsElements.FIELD_MOBILE_PHONE, mobilePhone)
        self.enter_text(LocatorsElements.FIELD_RESIDENCE_CITY, residenceCity)
        time.sleep(1)
        # self.click(LocatorsElements.AUTOCOMPLETE_CITY)

    def submit(self):
        self.click(LocatorsElements.SIGN_UP_BUTTON)
        time.sleep(2)
        try:
            response = self.driver.find_element(*LocatorsElements.ASSERT_HEADER).text == "Selamat Datang di Cermati!"
            if (response == True):
                print("you have successfully signed up")
            else:
                assert self.driver.find_element(*LocatorsElements.ASSERT_ALERT_DESCRIPTION).text == "Maaf, akun Anda sudah terdaftar."
                print("your account is already registered")
        except Exception as e:
            print(e)
            raise

    def validationData(self, validationDataValid, validationDataInvalid, fieldEmail, fieldAlert, email, alertMassage):
        for valid in validationDataValid:
            self.enter_text(fieldEmail, valid[email])
            elements = self.driver.find_elements(*fieldAlert)
            assert len(elements) == 0
            self.delete_text(fieldEmail)
            print('Valid - ' + valid[email])

        for invalid in validationDataInvalid:
            self.enter_text(fieldEmail, invalid[email])
            assert self.driver.find_element(*fieldAlert).text == invalid[alertMassage]
            self.delete_text(fieldEmail)
            print(self.driver.find_element(*fieldAlert).text + ' - ' + invalid[email])


