import time
from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from features.steps.page_verification import wait_for_element_load

use_step_matcher("parse")


def open_menu(browser):
    try:
        menu_element = browser.find_element_by_xpath("//button[@menutoggle]")
    except NoSuchElementException:
        assert False, "Unable to find the Menu to open"

    menu_element.click()
    time.sleep(.1)


def open_menu_item(browser, menu_item):
    open_menu(browser)
    element = browser.find_element_by_xpath('//button//ion-label[contains(., "' + menu_item + '")]/..')
    element.click()


@step('I select "{menu_item}" menu item')
def step_impl(context, menu_item):
    """
    :param menu_item: User-visible label for the menu item.
    :type context: behave.runner.Context
    """
    open_menu_item(context.browser, menu_item)
    time.sleep(.1)


@when("I revisit the application")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.execute_script("""location.reload()""")


def wait_for_map_loaded(context):
    wait_for_element_load(context.browser, By.ID, "map")
    wait_for_element_load(context.browser, By.CLASS_NAME, "awesome-marker")


def open_map(context):
    # Find the form element
    try:
        context.form = context.browser.find_element_by_xpath('//form')
    except NoSuchElementException:
        assert False, "Not able to open form"

    try:
        email_wrapper = context.form.find_element_by_name('email')
        email_field = email_wrapper.find_element_by_tag_name('input')
        email_field.send_keys("test.email@clueride.com")
    except NoSuchElementException:
        assert False, "Not able to open email field"

    try:
        password_wrapper = context.form.find_element_by_name('password')
        password_field = password_wrapper.find_element_by_tag_name('input')
        password_field.send_keys("unchecked")
    except NoSuchElementException:
        assert False, "Not able to open password field"

    context.form.submit()
    wait_for_element_load(context.browser, By.ID, "logout")

    context.browser.execute_script("""location.reload()""")


def on_opening_page(page_title):
    return page_title == "info" or page_title == "ClueRide Location Editor"


@given('the "Map" page has been opened')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Open the application
    context.browser.get("http://localhost:8100/")
    time.sleep(0.1)

    if context.browser.title == "ClueRide Location Editor":
        wait_for_element_load(context.browser, By.ID, "login")

    if context.browser.title == "info":
        open_map(context)
    else:
        if context.browser.title != "Map":
            print("Expected info page, but found " + context.browser.title);
            assert False, "Unable to reach Login page"

    wait_for_map_loaded(context)


@when("I refresh the map page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.execute_script("""location.reload()""")
    wait_for_map_loaded(context)
