from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Core element locators
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")
    DOBBY_CHAT_CANVAS = (By.XPATH, "//*[contains(@id, 'dobby') or contains(@class, 'dobby') or contains(@id, 'chat')]")

    def click_login(self):
        self.click_element(self.LOGIN_LINK)

    def click_signup(self):
        self.click_element(self.SIGNUP_LINK)

    def verify_menu_item_visible(self, item_name):
        locator = (By.XPATH, f"//*[contains(text(), '{item_name}')]")
        return self.find(locator).is_displayed()

    def is_dobby_present(self):
        try:
            return len(self.find_all(self.DOBBY_CHAT_CANVAS)) > 0
        except:
            return False
