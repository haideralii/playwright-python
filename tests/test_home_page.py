import pytest
from playwright.sync_api import Page, expect
from pages.class_attribute_page import ClassAttributePage
from utils.utils import Utils as utils
from pages.home_page import HomePage

HOME_PAGE_TITLE = "UI Test Automation Playground"


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page, home_page: HomePage):
    home_page.navigate()
    utils.verify_page_title(page, HOME_PAGE_TITLE)
    yield
    page.go_back()
    utils.verify_page_title(page, HOME_PAGE_TITLE)


def test_user_gets_navigated_to_click_page_on_clicking_click_link(page: Page, home_page: HomePage) -> None:
    home_page.click_link.click()
    utils.verify_url(page, ".*click")
    utils.verify_page_title(page, "Click")


def test_user_gets_navigated_to_text_input_page_on_clicking_text_input_link(page: Page, home_page: HomePage) -> None:
    home_page.text_input_link.click()
    utils.verify_url(page, ".*textinput")
    utils.verify_page_title(page, "Text Input")


def test_user_gets_navigated_to_dynamic_table_page_on_clicking_dynamic_table_link(page: Page, home_page: HomePage) -> None:
    home_page.dynamic_table_link.click()
    utils.verify_url(page, ".*dynamictable")
    utils.verify_page_title(page, "Dynamic Table")


def test_user_gets_navigated_to_sample_app_page_on_clicking_sample_app_link(page: Page, home_page: HomePage) -> None:
    home_page.sample_app_page_link.click()
    utils.verify_url(page, ".*sampleapp")
    utils.verify_page_title(page, "Sample App")
