import pytest
from playwright.sync_api import Page, expect
from pages.progress_bar_page import ProgressBarPage


@pytest.fixture(scope="function", autouse=True)
def before_each(progress_bar_page: ProgressBarPage):
    progress_bar_page.navigate()
    yield

def test_result_is_equal_to_0_when_progress_bar_reaches_to_75_percent(progress_bar_page: ProgressBarPage) -> None:
    progress_bar_page.start_button.click()
    progress_bar_page.progress_bar_with_75_percent.wait_for()
    progress_bar_page.stop_button.click()
    expect(progress_bar_page.result_label).to_contain_text("Result: 0")
