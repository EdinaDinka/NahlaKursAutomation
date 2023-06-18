from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from pages.page import Page

class HomePage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        username_field_locator = (By.ID, "user-name")
        wait_username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))
        wait_username_field.click()
        wait_username_field.clear()
        wait_username_field.send_keys(username)

        password_field = self.selenium_driver.find_element(By.ID, "password")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.selenium_driver.find_element(By.ID, "login-button")
        login_button.click()