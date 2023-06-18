from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from pages.page import Page

class ProductsPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.inventory_list_selector = (By.CLASS_NAME, "inventory_item")
        self.add_to_cart_btn = ".//div[3]/button"
       #self.add_to_cart_btn = "//div/button"
        self.inventory_name = ".//a/div"


    def is_at_page(self):
       page_title_locator = (By.CLASS_NAME, "title") 
       wait_page_text = self.wait.until(EC.visibility_of_element_located(page_title_locator))

       page_text = wait_page_text.text
       return page_text

    
    def add_items(self, number_of_items): # this method takes first two product items
        item_list = self.selenium_driver.find_elements(*self.inventory_list_selector)
        #item_list = (By.CLASS_NAME, "inventory_item")
        
        names_list = [] 
        for item in range(number_of_items - 1):
            add_cart_button = item_list[item].find_element_by_xpath(*self.add_to_cart_btn)
            #add_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
            add_cart_button.click()
            get_item_locator = item_list[item].find_element_by_xpath(*self.inventory_name)
            get_item_text = get_item_locator.text
            names_list.append(get_item_text)  
        return names_list 
    
    def open_cart(self):
        cart_locator = (By.CLASS_NAME, "shopping_cart_link")
        wait_cart_link = self.wait.until(EC.element_to_be_clickable(cart_locator))
        wait_cart_link.click()


