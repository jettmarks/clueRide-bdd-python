from behave import *
from selenium.common.exceptions import NoSuchElementException

use_step_matcher("parse")


def elements_child_contains_matching_text(element, text):
    """
    Returns true if the given element's child wraps the given text.
    The Text can either be part of the element itself or wrapped in a
    child <span> element -- both are checked to cover alternate
    implementations of the ion-button.
    :param element: which may be parent element for a span with the text.
    :param text: Text to be matched (case insensitive contains).
    :return: true if the text matches either the element or its span child.
    """
    if (str.upper(text)) in str.upper(element.text):
        return True

    try:
        child_element = element.find_element_by_tag_name("span")

    except NoSuchElementException:
        return False

    return str.upper(text) in str.upper(child_element.text)


def find_button_by_name(context, button_name):
    """
    Ionic Button specific since the element with the "button" tag is the
    parent for the element with the button text.
    :param context: session context.
    :param button_name: Text that the user sees on the button.
    :return: Button element that matches; throws exception if not found
    """
    button_list = context.browser.find_elements_by_tag_name("button")
    if len(button_list) == 0:
        raise Exception("No Buttons Found")

    match_list = [element for element in button_list if elements_child_contains_matching_text(element, button_name)]
    if len(match_list) == 0:
        raise Exception("No matching Button Found (" + button_name + ")")

    return match_list


@then('I see the "{button_name}" button')
def step_impl(context, button_name):
    """
    :param button_name: Text that the user sees on the Button.
    :type context: behave.runner.Context
    """
    try:
        find_button_by_name(context, button_name)
        pass

    except Exception:
        raise


@step('I click the "{button_name}" button')
def step_impl(context, button_name):
    """
    :param button_name: Text that the user sees on the Button.
    :type context: behave.runner.Context
    """
    try:
        button = find_button_by_name(context, button_name)
        button[0].click()
        pass

    except Exception:
        raise
