from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from features.steps.menu_navigation import open_menu_item
from features.steps.page_verification import wait_for_element_load

use_step_matcher("parse")


def is_logged_in(browser):
    """
    Brings the session to the Login page and inquires whether
    the "logout" element is present.
    :param browser: carries session.
    :return: True if we find the "logout" button.
    """
    if browser.title != "info":
        open_menu_item(browser, "Login")
    try:
        browser.find_element_by_id("logout")
    except NoSuchElementException:
        return False
    return True


def is_form_open(browser, form_name):
    """
    Checks if the given 'form_name' is an ID on the current page.
    :param browser:
    :param form_name:
    :return: Aborts test if form isn't found.
    """
    try:
        browser.find_element_by_id(form_name)
    except NoSuchElementException:
        assert False, "Not able to find " + form_name


def logout(browser):
    try:
        browser.find_element_by_id("logout")
    except NoSuchElementException:
        assert False, "Unable to logout"

    find_form(browser).submit()
    wait_for_element_load(browser, By.ID, "login")


def login(context):
    try:
        context.browser.find_element_by_id("login")
    except NoSuchElementException:
        assert False, "Unable to login"

    valid_email_account = "test.email@clueride.com"
    enter_credentials(context, valid_email_account).submit()
    wait_for_element_load(context.browser, By.ID, "logout")


@step('I see a "{form_name}" form')
def step_impl(context, form_name):
    """
    :param form_name: ID of the div element containing the form.
    :type context: behave.runner.Context
    """
    is_form_open(context.browser, form_name)


def find_form(browser):
    try:
        form = browser.find_element_by_xpath('//form')
    except NoSuchElementException:
        assert False, "Not able to open form"
    return form


def enter_credentials(context, email_account):
    form = find_form(context.browser)
    try:
        email_wrapper = form.find_element_by_name('email')
        email_field = email_wrapper.find_element_by_tag_name('input')
        email_field.send_keys(email_account)
    except NoSuchElementException:
        assert False, "Not able to open email field"

    try:
        password_wrapper = form.find_element_by_name('password')
        password_field = password_wrapper.find_element_by_tag_name('input')
        password_field.send_keys("unchecked")
    except NoSuchElementException:
        assert False, "Not able to open password field"
    return form


@when("I enter my username and password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    valid_email_account = "test.email@clueride.com"
    context.form = enter_credentials(context, valid_email_account)


@step("Click Login")
def step_impl(context):
    """
    :type context: behave.runner.Context

    Coupled to the "I enter my username and password" above
    """
    context.form.submit()


@step('I wait to see a "logout" form')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    wait_for_element_load(context.browser, By.ID, "logout")


@step("I make sure I'm logged out")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if is_logged_in(context.browser):
        logout(context.browser)


@when("I enter bad username and password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    invalid_email_account = "invalid@clueride.com"
    context.form = enter_credentials(context, invalid_email_account)



@then("I see failed login message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass