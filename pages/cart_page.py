from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from pages.page import Page

class CartPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def is_at_page(self):
       page_title_locator = (By.CLASS_NAME, "title") 
       wait_page_text = self.wait.until(EC.visibility_of_element_located(page_title_locator)) 
       page_text = wait_page_text.text
       return page_text  