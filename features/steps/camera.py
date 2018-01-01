from behave import *

use_step_matcher("re")


@step("I see camera is open")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass