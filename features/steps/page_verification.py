import time
from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

use_step_matcher("parse")


def wait_for_element_load(browser, element_type, element_id):
    """
    Pauses for up to 10 seconds to allow loading of the specific element named.
    :param browser: Browser instance of interest.
    :param element_type: One of the 'By' instances.
    :param element_id: Text representation of the element in the DOM.
    :return:
    """
    start = time.time();
    print("before wait_for_element_load (%s, %s)" %
          (element_type, element_id)
          )
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((element_type, element_id))
        )
    except:
        print("Did not find element " + element_id, "\n")

    elapsed = time.time() - start
    print("after wait_for_element_load: %f" % elapsed)


@step('I see the "{page_title}" page')
def step_impl(context, page_title):
    """
    :type context: behave.runner.Context
    :param page_title: Title of the page we're verifying
    """
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


@when('I wait for page with "{id_text}" ID')
def step_impl(context, id_text):
    """
    :param id_text: Text of the ID element expected.
    :type context: behave.runner.Context
    """
    wait_for_element_load(context.browser, By.ID, id_text)
