from behave import *
from selenium.common.exceptions import NoSuchElementException

use_step_matcher("parse")


@step("I see Registered as Test Account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        name_element_list = context.browser.find_elements_by_class_name('profile-summary.name')
    except NoSuchElementException:
        assert False, "Unable to find User's Registered Name"

    assert len(name_element_list) == 1, "Wrong number of Registered Names"
    pass


@step('I see the registered address "{email_text}"')
def step_impl(context, email_text):
    """
    :param context: behave.runner.Context
    :param email_text: String representing the email address to match
    """
    try:
        email_span = context.browser.find_element_by_tag_name("span")
    except NoSuchElementException:
        assert False, "Unable to find Span with email address"

    print(email_span.get_attribute("value"))
    assert email_span.get_attribute("value") is not None, "Email address not populated"
    assert email_text in email_span, "Email Address (" + email_span + ") doesn't match expected value (" + email_text + ")"

    pass