from behave import *

from features.steps.login_form import is_logged_in, login

use_step_matcher("re")


@when("I open the application")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.get("http://localhost:8100/")


@then('I see a link to the "Login" page')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("Opened Page: " + context.browser.title)
    assert context.browser.title == "info"


@step("Valid Token has been set via login")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    if not is_logged_in(context.browser):
        login(context)
