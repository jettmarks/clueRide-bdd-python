from behave import *

use_step_matcher("parse")


@when('I select "{menu_item}" menu item')
def step_impl(context, menu_item):
    """
    :type context: behave.runner.Context
    """
    element = context.browser.find_element_by_xpath('//button/**/ion-label/')
    print("Element found is ", element)


@when("I revisit the application")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.execute_script("""location.reload()""")
