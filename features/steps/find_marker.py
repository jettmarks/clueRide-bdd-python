import time
from behave import *
from selenium.common.exceptions import NoSuchElementException

use_step_matcher("re")

test_marker = None


@step("I find the Test Marker")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        broken_marker_list = context.browser.find_elements_by_class_name('awesome-marker-icon-darkred')
    except NoSuchElementException:
        assert False, "Unable to find test marker; No dark red markers"

    # for marker in broken_marker_list:
    #     print(marker.get_attribute("title"), "\n")

    if broken_marker_list:
        global test_marker
        test_marker = [marker for marker in broken_marker_list if marker.get_attribute("title") == " : 13"][0]
    else:
        assert False, "Unable to find test marker; Node '13' not present"


@step("Click found Marker")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    test_marker.click()
    time.sleep(2)


@step("I read the Location Type")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I see an icon matching the Location Type")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('I read the "(.+)"')
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    pass


@step('I see the "(?P<Icon>.+)" matches')
def step_impl(context, Icon):
    """
    :type context: behave.runner.Context
    :type Icon: str
    """
    pass