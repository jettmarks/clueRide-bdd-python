from behave import *
from selenium.common.exceptions import NoSuchElementException

use_step_matcher("parse")


@given('Email with name "{email_file_name}" has been received')
def step_impl(context, email_file_name):
    """
    :param email_file_name: Name of the Email's file on disk.
    :type context: behave.runner.Context

    """
    fullPath = "file:///home/jett/PycharmProjects/testData/emailReceived/" + email_file_name + ".html"
    print ("Name of the File to find: ", fullPath, "\n")

    context.browser.get(fullPath)


@when('I open the link for "{link_name}"')
def step_impl(context, link_name):
    """
    :param link_name: The text within the link that we want to open.
    :type context: behave.runner.Context
    """
    print ("Name of the Link to load: ", link_name, "\n")

    try:
        element = context.browser.find_element_by_partial_link_text(link_name)
        print(element.text)
        assert(link_name in element.text)
        element.click()

    except NoSuchElementException:
        print("Unable to find ", link_name)
        # assert False

