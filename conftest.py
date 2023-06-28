import pytest
from playwright.sync_api import Page, expect
from pages.class_attribute_page import ClassAttributePage
from pages.dynamic_table_page import DynamicTablePage
from pages.home_page import HomePage
from pages.progress_bar_page import ProgressBarPage
from pages.sample_app_page import SampleAppPage
from pages.text_input_page import TextInputPage
from pages.visibility_page import VisibilityPage
from dotenv import load_dotenv, find_dotenv

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def text_input_page(page: Page) -> TextInputPage:
    return TextInputPage(page)

@pytest.fixture
def dynamic_table_page(page: Page) -> DynamicTablePage:
    return DynamicTablePage(page)

@pytest.fixture
def sample_app_page(page: Page) -> SampleAppPage:
    return SampleAppPage(page)

@pytest.fixture
def visibility_page(page: Page) -> VisibilityPage:
    return VisibilityPage(page)

@pytest.fixture
def class_attribute_page(page: Page) -> ClassAttributePage:
    return ClassAttributePage(page)

@pytest.fixture
def progress_bar_page(page: Page) -> ProgressBarPage:
    return ProgressBarPage(page)

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv(find_dotenv())
