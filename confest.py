import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

close_browser = True  # Можно отключить автоматическое зарывание браузера для дебага.


if not close_browser:
    options = Options()
    options.add_experimental_option("detach", True)

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)
    yield driver
    if close_browser:
        driver.quit()
