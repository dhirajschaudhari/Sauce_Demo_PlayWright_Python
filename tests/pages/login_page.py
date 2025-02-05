from pages.base_page import BasePage, retry_with_screenshot
import configparser

class LoginPage(BasePage):
    """
    Page class for login functionality. Reads configurations and provides login automation.
    """
    config = configparser.ConfigParser()
    config.read("configs/config.properties")
    
    LOGIN_URL = config.get("URLs", "LOGIN_URL")
    USERNAME_INPUT = config.get("Selectors", "USERNAME_INPUT")
    PASSWORD_INPUT = config.get("Selectors", "PASSWORD_INPUT")
    LOGIN_BUTTON = config.get("Selectors", "LOGIN_BUTTON")
    LOGOUT_BUTTON = config.get("Selectors", "LOGOUT_BUTTON")
    INVENTORY_PAGE_INDICATOR = config.get("Selectors", "INVENTORY_PAGE_INDICATOR")
    
    def navigate(self):
        """Navigates to the login page."""
        super().navigate(self.LOGIN_URL)
    
    @retry_with_screenshot(retries=3)
    def login(self, username: str, password: str):
        """Attempts to log in with the provided username and password."""
        self.fill_textbox(self.USERNAME_INPUT, username)
        self.fill_textbox(self.PASSWORD_INPUT, password)
        self.click_button(self.LOGIN_BUTTON)
    
    def is_logged_in(self) -> bool:
        """Verifies if login was successful by checking for an element on the inventory page."""
        return self.is_element_visible(self.INVENTORY_PAGE_INDICATOR)
    
    def logout(self):
        """User logging out"""
        self.click_button(self.LOGOUT_BUTTON)