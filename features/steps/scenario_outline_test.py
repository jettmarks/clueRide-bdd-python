from behave import *

use_step_matcher("re")


@given("I have populated the Examples")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for key in [1, 2, 3]:
        context.active_outline.add_row([str(key), 'value' + str(key)], key+10)


@when('I have a "(?P<key>.+)", I print a "(?P<value>.+)"')
def step_impl(context, key, value):
    """
    :type context: behave.runner.Context
    :type key: str
    :type value: str
    """
    print(key + ": " + value)
