from selenium.webdriver.common.by import By


# constans
class Constants():
    driver = r"C:\Users\afinapd\PycharmProjects\Portfolio\chromedriver\chromedriver.exe"
    baseURL = "https://www.cermati.com/gabung"


# locators
class LocatorsElements():
    FIELD_EMAIL = (By.ID, "email")
    ALERT_EMAIL = (By.XPATH, "//div[2]/div/div[2]/div/div/div")

    FIELD_PASSWORD = (By.ID, "password")
    ALERT_PASSWORD = (By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/div[3]/div[2]/div/div")

    FIELD_CONFIRM_PASSWORD = (By.ID, "confirm-password")
    ALERT_CONFIRM_PASSWORD = (By.XPATH, "//div[4]/div[2]/div/div")

    FIELD_FIRST_NAME = (By.ID, "first-name")
    ALERT_FIRST_NAME = (By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/div[5]/div[1]/div/div/div/div")

    FIELD_LAST_NAME = (By.ID, "last-name")
    ALERT_LAST_NAME = (By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/div[5]/div[2]/div/div/div/div")

    FIELD_MOBILE_PHONE = (By.ID, "mobile-phone")
    ALERT_MOBILE_PHONE = (By.XPATH, "//div[6]/div/div/div")

    FIELD_RESIDENCE_CITY = (By.ID, "residence-city")
    ALERT_RESIDENCE_CITY = (By.XPATH, "//div[7]/div/div[2]/div/div")

    AUTOCOMPLETE_CITY = (By.CSS_SELECTOR, ".autocomplete-list-item")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, ".btn")

    ASSERT_HEADER = (By.CSS_SELECTOR, ".text-header")
    ASSERT_ALERT_DESCRIPTION = (By.CSS_SELECTOR, ".alert-danger > .alert-description")
