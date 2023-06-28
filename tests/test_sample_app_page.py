import pytest
import os

from playwright.sync_api import Page, expect
from pages.sample_app_page import SampleAppPage


@pytest.fixture(scope="function", autouse=True)
def before_each(sample_app_page: SampleAppPage):
    sample_app_page.navigate()
    yield

@pytest.mark.only
def test_login_with_correct_username_and_password(sample_app_page: SampleAppPage) -> None:
    user_name = os.getenv('SAMPLE_APP_USERNAME')
    password = os.getenv('SAMPLE_APP_PASSWORD')
    sample_app_page.enter_username(user_name)
    sample_app_page.enter_password(password)
    sample_app_page.click_login_button()
    expect(sample_app_page.login_status_txt).to_contain_text(
        "Welcome, " + user_name)


def test_login_with_incorrect_username_and_password(sample_app_page: SampleAppPage) -> None:
    user_name = "incorrect"
    incorrect_password = "wrong123"
    sample_app_page.enter_username(user_name)
    sample_app_page.enter_password(incorrect_password)
    sample_app_page.click_login_button()
    expect(sample_app_page.login_status_txt).to_contain_text(
        "Invalid username/password")
