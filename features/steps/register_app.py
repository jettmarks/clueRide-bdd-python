from behave import *
from features.steps.browser_setup import reload

use_step_matcher("parse")


@step("Application is unregistered -- and refreshed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    script = """localStorage.removeItem('expires_at');
       localStorage.removeItem('access_token');"""
    context.browser.execute_script(script)
    reload(context)
    # open_application(context)
    pass
