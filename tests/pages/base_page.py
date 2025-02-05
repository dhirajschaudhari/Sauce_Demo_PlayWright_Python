import configparser
import logging
import time
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from functools import wraps

# Configure logging
logging.basicConfig(filename='logs/test_execution.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BasePage:
    """
    Base class for all pages to provide reusable Playwright interactions.
    Handles navigation, element interactions, and visibility checks.
    """
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url: str):
        """Navigates to a given URL."""
        self.page.goto(url)
    
    def fill_textbox(self, selector: str, value: str):
        """Fills a text box identified by the selector with the given value."""
        self.page.fill(selector, value)
    
    def click_button(self, selector: str):
        """Clicks a button identified by the selector."""
        self.page.click(selector)
    
    def get_element_text(self, selector: str) -> str:
        """Returns the text of an element."""
        return self.page.inner_text(selector)
    
    def is_element_visible(self, selector: str) -> bool:
        """Checks if an element is visible."""
        return self.page.is_visible(selector)

def retry_with_screenshot(retries=3):
    """
    Decorator to retry a function if it fails, capturing a screenshot on the final failure.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(self, *args, **kwargs)
                except PlaywrightTimeoutError as e:
                    logging.error(f"Attempt {attempt} failed: {str(e)}")
                    last_exception = e
                    time.sleep(1)  # Small delay before retry
            screenshot_path = f"screenshots/{func.__name__}_failure.png"
            self.page.screenshot(path=screenshot_path)
            logging.error(f"Test failed after {retries} attempts. Screenshot saved: {screenshot_path}")
            raise last_exception
        return wrapper
    return decorator