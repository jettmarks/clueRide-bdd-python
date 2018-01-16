import time
from behave import *


@step('I wait "{time_interval}" seconds')
def step_impl(context, time_interval):
    """
    :param time_interval: Time to wait in seconds
    :type context: behave.runner.Context
    """
    time.sleep(int(time_interval))
