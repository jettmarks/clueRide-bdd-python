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
        email_span = context.browser.find_elements_by_xpath("//page-confirm//ion-content//span")
    except NoSuchElementException:
        assert False, "Unable to find Span with email address"

    print('Found this many span elements: ', len(email_span), '\n')
    print(email_span[0].text, '\n')
    assert email_span[0].text is not None, "Email address not populated"
    assert email_text in email_span[0].text, "Email Address (" + email_span[0].text + ") doesn't match expected value (" + email_text + ")"

    pass