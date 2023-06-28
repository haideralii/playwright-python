import pytest
from playwright.sync_api import Page, expect
from pages.text_input_page import TextInputPage


@pytest.fixture(scope="function", autouse=True)
def before_each(text_input_page: TextInputPage):
    text_input_page.navigate()
    yield


def test_button_text_gets_updated_on_entering_text_in_field_and_clicking_button(text_input_page: TextInputPage) -> None:
    text = "New Button Text"
    text_input_page.my_text_field.fill(text)
    text_input_page.update_button.click()
    expect(text_input_page.update_button).to_contain_text(text)
