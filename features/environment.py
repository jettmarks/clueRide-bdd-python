from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def before_all(context):

    # caps = DesiredCapabilities.CHROME
    # caps['loggingPrefs'] = {'performance': 'ALL'}

    try:
        context.browser = webdriver.Chrome(
            executable_path="/opt/chromedriver",
            # desired_capabilities=caps,
            service_args=["--verbose", "--log-path=/tmp/selenium/chrome.log"]
        )
    except WebDriverException:
        print("Unable to start browser, is log-path available?")
        raise
    except:
        print("This is a new one")
        raise


def after_all(context):
    context.browser.quit()