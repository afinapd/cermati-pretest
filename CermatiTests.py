__author__ = 'Afina P'

import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import ValidationData
from CermatiLocators import Constants, LocatorsElements
from CermatiPage import CermatiPage


class EnvironmentSetup(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=Constants.driver)
        self.driver.get(Constants.baseURL)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, timeout=30)
        self.action = webdriver.ActionChains(self.driver)
        self.CermatiPage = CermatiPage(self.driver)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_scenario_signup(self):
        self.CermatiPage.input_all_field("afnpd03@gmail.com", "test1234", "test1234", "Afina", "Putri Dayanti",
                                         "085772610027", "Kota Jakarta Timur")
        self.CermatiPage.submit()

    def test_validation_email(self):
        self.CermatiPage.validationData(ValidationData.validEmail, ValidationData.invalidEmail,
                                        LocatorsElements.FIELD_EMAIL, LocatorsElements.ALERT_EMAIL, 'email',
                                        'alertMessage')

    def test_validation_password(self):
        # password
        self.CermatiPage.validationData(ValidationData.validPassword, ValidationData.invalidPassword,
                                        LocatorsElements.FIELD_PASSWORD, LocatorsElements.ALERT_PASSWORD, 'password',
                                        'alertMessage')
        self.driver.find_element(*LocatorsElements.FIELD_PASSWORD).send_keys("test1234")
        # confirm password
        self.CermatiPage.validationData(ValidationData.validPassword, ValidationData.invalidConfirmPassword,
                                        LocatorsElements.FIELD_CONFIRM_PASSWORD,
                                        LocatorsElements.ALERT_CONFIRM_PASSWORD,
                                        'password', 'alertMessage')

    def test_validation_first_name(self):
        self.CermatiPage.validationData(ValidationData.validName, ValidationData.invalidName,
                                    LocatorsElements.FIELD_FIRST_NAME, LocatorsElements.ALERT_FIRST_NAME, 'name',
                                    'alertMessage')

    def test_validation_last_name(self):
        self.CermatiPage.validationData(ValidationData.validName, ValidationData.invalidName,
                                    LocatorsElements.FIELD_LAST_NAME, LocatorsElements.ALERT_LAST_NAME, 'name',
                                    'alertMessage')

    def test_validation_mobile_phone(self):
        self.CermatiPage.validationData(ValidationData.validMobilePhone, ValidationData.invalidMobilePhone,
                                        LocatorsElements.FIELD_MOBILE_PHONE, LocatorsElements.ALERT_MOBILE_PHONE, 'mobilePhone',

                                        'alertMessage')
