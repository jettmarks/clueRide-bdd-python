import time

from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from features.steps.page_verification import wait_for_element_load

use_step_matcher("parse")

field_element = None


def click_named_button_within_named_group(browser, group_style_name, button_name):
    """
    Sends the click event against the named button within the group with the given style name.
    :param browser:
    :param group_style_name:
    :param button_name:
    :return:
    """
    try:
        button_group = browser.find_element_by_class_name(group_style_name)
    except NoSuchElementException:
        assert False, "Unable to find " + group_style_name

    found_button = False
    for button in button_group.find_elements_by_class_name("button-inner"):
        if button.text == button_name:
            found_button = True
            button.click()
            print("Clicked the button " + button_name)
    assert found_button, "Unable to find button named " + button_name

    # time.sleep(0.3)


@step('I Click the alert\'s "{button_name}" button')
def step_impl(context, button_name):
    """
    :param button_name: User-visible string on the desired button.
    :type context: behave.runner.Context
    """
    group_name = "alert-button-group"
    click_named_button_within_named_group(context.browser, group_name, button_name)
    wait_for_element_load(context.browser, By.CLASS_NAME, "label")


@step('I Click the edit form\'s "{button_name}" button')
def step_impl(context, button_name):
    """
    :param button_name: User-visible string on the desired button.
    :type context: behave.runner.Context
    """
    group_name = "form-buttons-row"
    click_named_button_within_named_group(context.browser, group_name, button_name)
    wait_for_element_load(context.browser, By.CLASS_NAME, "label")


@step('I Click the image edit\'s "{button_name}" button')
def step_impl(context, button_name):
    """
    :param button_name: User-visible string on the desired button.
    :type context: behave.runner.Context
    """
    group_name = "image-edit"
    click_named_button_within_named_group(context.browser, group_name, button_name)
    wait_for_element_load(context.browser, By.ID, "image-capture")
    # Bugs me that this is required after having waited for other items on page to be visible.
    time.sleep(0.5)


@step('I enter "{entry_text}" into the "{field_type}" field labeled "{label_name}"')
def step_impl(context, entry_text, field_type, label_name):
    """
    :param entry_text: Text to be entered into the field.
    :param field_type: 'input', 'select', 'textarea', etc.
    :param label_name: What the user sees as the name of the field.
    :type context: behave.runner.Context
    """
    global field_element
    if field_element is None:
        assert False, "Make sure the field labeled " + label_name + " can be found before attempting to enter text"
        # raise
    else:
        field_element.click()
        wait_for_element_load(context.browser, By.CLASS_NAME, "alert-radio-group")
        time.sleep(2)

    try:
        # option_group = context.browser.find_element_by_class_name("alert-radio-group")
        button_list = context.browser.find_elements_by_class_name("alert-radio-button")
    except NoSuchElementException:
        assert False, "Unable to find option group"

    if button_list:
        # Unable to use this because 'option_group' isn't the browser 'select' element
        # Select(option_group).select_by_visible_text(entry_text)
        for button in button_list:
            if entry_text in button.find_element_by_class_name("alert-radio-label").text:
                button.click()

    time.sleep(2)


def get_label_element(browser, label_name):
    try:
        label_element_list = browser.find_elements_by_class_name("label")
    except NoSuchElementException:
        assert False, "Unable to find 'label' class on page " + browser.title

    return [label for label in label_element_list if label.text == label_name][0]


@step('I see the "{field_type}" field labeled "{label_name}"')
def step_impl(context, field_type, label_name):
    """
    :param field_type: 'input', 'select', 'textarea', etc.
    :param label_name: What the user sees as the name of the field.
    :type context: behave.runner.Context

    Algorithm is to find the label_name matching the field, and then search
    the parent for the matching field_type.
    """
    label_element = get_label_element(context.browser, label_name)

    global field_element

    try:
        field_element = label_element.parent.find_element_by_tag_name(field_type)
    except NoSuchElementException:
        assert False, "Unable to find " + field_type + " field on element labeled " + label_element.text
    except:
        assert False, "Something else happened"
    finally:
        print(field_element.text)


@step('I see the "{field_type}" class labeled "{label_name}"')
def step_impl(context, field_type, label_name):
    """
    :param field_type: 'input', 'select', 'textarea', etc.
    :param label_name: What the user sees as the name of the field.
    :type context: behave.runner.Context

    Algorithm is to find the label_name matching the field, and then search
    the parent for the matching field_type.
    """
    label_element = get_label_element(context.browser, label_name)

    global field_element

    try:
        field_element = label_element.parent.find_element_by_class_name(field_type)
    except NoSuchElementException:
        assert False, "Unable to find " + field_type + " class on element labeled " + label_element.text
    except:
        assert False, "Something else happened"
    finally:
        print(field_element.text)


@step('I see the text "{entry_text}" in the "{field_type}" field labeled "{label_name}"')
def step_impl(context, entry_text, field_type, label_name):
    """
    :type context: behave.runner.Context
    :param entry_text: Text to be entered into the field.
    :param field_type: 'input', 'select', 'textarea', etc.
    :param label_name: What the user sees as the name of the field.
    """
    global field_element
    try:
        entry_element = field_element.find_element_by_class_name("select-text")
    except NoSuchElementException:
        assert False, "Unable to find text"

    assert entry_element.text == entry_text, "Expected " + entry_text + " but found " + entry_element.text

    time.sleep(2)


@when('I set the Test Marker\'s "{field_in}" to "{name_in}"')
def step_impl(context, field_in, name_in):
    """
    :param field_in:
    :param name_in:
    :type context: behave.runner.Context
    """
    context.execute_steps(u"""
    When I find the Test Marker
    And Click found Marker
    And I see the "Editing:" page
    And I see the "select" field labeled "{field}"
    And I enter "{name}" into the "select" field labeled "{field}"
    And I Click the alert's "OK" button
    And I see the "Editing:" page
    And I see the text "{name}" in the "select" field labeled "{field}"
    And I Click the form's "Save" button
    """.format(field=field_in, name=name_in))


@step('I list all items in the select field labeled "{label}"')
def step_impl(context, label):
    """
    :param label: The user-visible Label on the select field.
    :type context: behave.runner.Context
    """
    context.execute_steps(u"""
    When I find the Test Marker
    And Click found Marker
    And I see the "Editing:" page
    And I see the "select" field labeled "{field}"
    """.format(field=label))

    global field_element
    field_element.click()

    select_elements = context.browser.find_elements_by_xpath(
        '//div[contains(@class,"alert-radio-group")]//div[contains(@class,"alert-radio-label")]')
    context.select_list = []
    for element in select_elements:
        context.select_list.append(element.text)
