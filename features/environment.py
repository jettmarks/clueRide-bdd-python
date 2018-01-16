from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def before_all(context):
    LOG_PATH = "/tmp/selenium/chrome.log"

    # caps = DesiredCapabilities.CHROME
    # caps['loggingPrefs'] = {'performance': 'ALL'}

    try:
        context.browser = webdriver.Chrome(
            executable_path="/opt/chromedriver",
            # desired_capabilities=caps,
            service_args=["--verbose", "--log-path=" + LOG_PATH]
        )
    except WebDriverException:
        print("Unable to start browser, is log-path (", LOG_PATH, ") available?")
        raise
    except:
        print("This is a new one")
        raise


def after_all(context):
    context.browser.quit()