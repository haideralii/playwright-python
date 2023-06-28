import pytest
from playwright.sync_api import Page, expect
from pages.class_attribute_page import ClassAttributePage


@pytest.fixture(scope="function", autouse=True)
def before_each(class_attribute_page: ClassAttributePage):
    class_attribute_page.navigate()
    yield


def test_click_a_button_with_primary_class_and_accept_popup(page: Page, class_attribute_page: ClassAttributePage) -> None:
    page.on("dialog", lambda dialog: dialog.accept())
    class_attribute_page.primary_button.click()
