from behave import *
from selenium.common.exceptions import NoSuchElementException

use_step_matcher("parse")


@then('I see the "{page_title}" page')
def step_impl(context, page_title):
    """
    :type context: behave.runner.Context
    :param page_title: Title of the page we're verifying
    """
    print('Page Title: ', context.browser.title, "\n")
    assert context.browser.title == page_title, \
        "expected " + page_title + " but got " + context.browser.title


@step('I see a "{badge_name}" badge')
def step_impl(context, badge_name):
    """
    :param badge_name: expected badge name.
    :type context: behave.runner.Context
    """
    try:
        element = context.browser.find_element_by_id('badges')
        print(element.text)
        assert badge_name in element.text, 'Expected ' + badge_name + ' but found ' + element.text
    except NoSuchElementException:
        print("No element found")

