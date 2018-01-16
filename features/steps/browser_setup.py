from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def open_application(context):
    """
    Shared function for opening the app.
    :param context:
    :return:
    """
    context.browser.get("http://localhost:8100")


@given("first access for a device")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Application has been opened")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    open_application(context)


@step("Valid Token has been set")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.config.userdata["test_token"], "The config parameter `test_token` needs to be defined"
    # print("What we got: ", context.config.userdata["test_token"], "\n")
    token = "'" + context.config.userdata["test_token"] + "'"
    script = """localStorage.setItem('_ionicstorage/_ionickv/token.key',""" + token + """);"""
    context.browser.execute_script(script)


@when("I wait for Map to load")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("waiting for map to load\n")
    try:
        WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.ID, "map"))
        )
    finally:
        print("Did not find map\n")




