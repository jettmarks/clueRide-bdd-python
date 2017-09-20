import time
from behave import *
from selenium.common.exceptions import NoSuchElementException

use_step_matcher("parse")


@step('I see a "{form_name}" form')
def step_impl(context, form_name):
    """
    :param form_name: ID of the div element containing the form.
    :type context: behave.runner.Context
    """
    try:
        form_div = context.browser.find_element_by_id(form_name)
        print(form_div.text, "\n")
    except NoSuchElementException:
        assert False, "Not able to find " + form_name


@when("I enter my username and password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        context.form = context.browser.find_element_by_xpath('//form')
    except NoSuchElementException:
        assert False, "Not able to open form"

    try:
        email_wrapper = context.form.find_element_by_name('email')
        email_field = email_wrapper.find_element_by_tag_name('input')
        # email_field.click()
        email_field.send_keys("test.email@clueride.com")
    except NoSuchElementException:
        assert False, "Not able to open email field"

    try:
        password_wrapper = context.form.find_element_by_name('password')
        password_field = password_wrapper.find_element_by_tag_name('input')
        # password_field.click()
        password_field.send_keys("unchecked")
    except NoSuchElementException:
        assert False, "Not able to open password field"


@step("Click Login")
def step_impl(context):
    """
    :type context: behave.runner.Context

    Coupled to the "I enter my username and password" above
    """
    context.form.submit()
    time.sleep(2)
