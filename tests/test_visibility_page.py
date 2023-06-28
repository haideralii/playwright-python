import pytest
from playwright.sync_api import Page, expect
from pages.visibility_page import VisibilityPage


@pytest.fixture(scope="function", autouse=True)
def before_each(visibility_page: VisibilityPage):
    visibility_page.navigate()
    yield


def test_all_buttons_gets_hidden_on_clicking_hide_button(page: Page, visibility_page: VisibilityPage) -> None:
    visibility_page.hide_button.click()
    hidden_layer_with_over_lapped_btn = page.locator("button#overlappedButton#overlappedButton")
    expect(hidden_layer_with_over_lapped_btn).to_be_visible()
    expect(visibility_page.offscreen_button).to_have_class("btn btn-info offscreen")
    expect(visibility_page.opacity_zero_button).to_have_attribute("style", "opacity: 0;")
    expect(visibility_page.display_none_button).to_have_attribute("style", "display: none;")
    expect(visibility_page.removed_button).not_to_be_visible()
    expect(visibility_page.zero_width_button).to_have_class("btn btn-warning zerowidth")
    expect(visibility_page.visibility_hidden_button).to_have_attribute("style", "visibility: hidden;")