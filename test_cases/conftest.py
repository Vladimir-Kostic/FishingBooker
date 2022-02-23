import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# chrome_options = Options()
# chrome_options.add_experimental_option("prefs", {
#     "profile.default_content_setting_values.notifications": 2
# })
chrome_service = Service(ChromeDriverManager().install())
firefox_service = Service(GeckoDriverManager().install())
edge_service = Service(EdgeChromiumDriverManager().install())


@pytest.fixture(autouse=True, scope="class")
def setup(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome(
            service=chrome_service)
    elif browser == "firefox":
        driver = webdriver.Firefox(service=firefox_service)
    elif driver == "edge":
        driver = webdriver.Edge(service=edge_service)
    else:
        print("Provide valid browser")
    driver.get(
        "https://fishingbooker:QAFBTest@qahiring.dev.fishingbooker.com/charters/view/19612")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(autouse=True, scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            os.environ["REPORT_DIRECTORY"] = ".\\reports"
            report_directory = os.environ.get("REPORT_DIRECTORY")
            file_name = (item.name + ".png")
            destination_file = os.path.join(report_directory, file_name)
            driver_fixture = item.funcargs["request"]
            driver_fixture.cls.driver.save_screenshot(destination_file)
            extra.append(pytest_html.extras.image(destination_file))
            extra.append(pytest_html.extras.html(
                "<div>Additional HTML </div>"))
        report.extra = extra


def pytest_configure(config):
    config._metadata["Project name"] = "FishingBooker"
    config._metadata["Module name"] = "Booking and payment"
    config._metadata["Tester"] = "Vladimir Kostic"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


def pytest_html_report_title(report):
    report.title = " 4 hour trip booking"
