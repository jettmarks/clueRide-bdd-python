from behave import *
from selenium.common.exceptions import NoSuchElementException

use_step_matcher("parse")

temp_profile = {
    "sub": "google-oauth2|115646561365354495360",
    "given_name": "Bike",
    "family_name": "Angel",
    "nickname": "bikeangel.atl",
    "name": "Bike Angel",
    "picture": "https://lh6.googleusercontent.com/-sbXJYcO2EBY/AAAAAAAAAAI/AAAAAAAAAAc/86jPiXVs-ZE/photo.jpg",
    "locale": "en",
    "updated_at": "2018-01-15T17:18:09.113Z",
    "email": "bikeangel.atl@gmail.com",
    "email_verified": True,
    "user_metadata": {}
}


def find_target_link(context, link_text):
    """
    :param context:
    :param link_text:
    :return:
    """
    try:
        target_element = context.browser.find_element_by_partial_link_text(link_text)

    except NoSuchElementException:
        raise

    return target_element


@when('I click the "{link_text}" link')
def step_impl(context, link_text):
    """
    :type context: behave.runner.Context
    :param link_text: What the user sees as the text of the Link.
    """
    find_target_link(context, link_text).click()


@step('I see a link to "{link_text}"')
def step_impl(context, link_text):
    """
    :type context: behave.runner.Context
    :param link_text: What the user sees as the text of the Link.
    """
    find_target_link(context, link_text)
