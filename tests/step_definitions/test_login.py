from behave import given, when, then
from pages.login_page import LoginPage
import configparser

config = configparser.ConfigParser()
config.read("configs/config.properties")

@given("the user is on the login page")
def step_user_on_login_page(context):
    """
    Step to navigate to the login page.
    """
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()

@when("the user logs in with valid credentials")
def step_user_logs_in(context):
    """
    Step to log in using valid credentials from the configuration file.
    """
    username = config.get("Credentials", "USERNAME")
    password = config.get("Credentials", "PASSWORD")
    context.login_page.login(username, password)

@then("the user should be logged in successfully")
def step_user_logged_in_successfully(context):
    """
    Step to verify that the user is logged in by checking for an element on the inventory page.
    """
    assert context.login_page.is_logged_in(), "Login failed!"

@then("click on logout button")
def step_user_logged_out_successfully(context):
     """
    Step to verify that the user is logged out after clicking on log out button.
    """
     context.login_page.logout()