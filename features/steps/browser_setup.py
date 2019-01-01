import time

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


@given("Registered Device")
def step_impl(context):
    """
    This stuffs a set of valid tokens into storage on a "new" device.
    This simulates a device which had been registered in the past.
    :type context: behave.runner.Context
    """
    open_application(context)
    script = """localStorage.setItem('expires_at',JSON.stringify((86400 * 1000) + new Date().getTime()));"""
    context.browser.execute_script(script)


def assemble_token_script(user_key):
    token_map = {
        'invitedUser': "invitedUser",
        'declinedUser': "declinedUser",
        'acceptedInviteUser': "acceptedInviteUser",
        'noInviteUser': "noInviteUser",
        'multiInviteUser': "multiInviteUser",
    }

    return """localStorage.setItem(
      'access_token', 
      JSON.stringify('""" \
           + token_map.get(user_key, "unknownUser") \
           +"""')
    );"""


def reload(context):
    script = """location.reload();"""
    context.browser.execute_script(script)


@given('Device registered to "{user_key}"')
def step_impl(context, user_key):
    """
    :type context: behave.runner.Context
    :param user_key: str representing the key for a specific user's account.
    """
    open_application(context)
    time.sleep(int(1))
    script = assemble_token_script(user_key)
    context.browser.execute_script(script)
    time.sleep(int(1))
    # reload appears to be working better than the open_application
    # open_application(context)
    reload(context)
    time.sleep(int(2))



