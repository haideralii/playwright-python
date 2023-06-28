import pytest
from playwright.sync_api import Page, expect
from pages.dynamic_table_page import DynamicTablePage

@pytest.fixture(scope="function", autouse=True)
def before_each(dynamic_table_page: DynamicTablePage):
    dynamic_table_page.navigate()
    yield


def test_compare_chrome_cpu_value_from_table_with_value_in_the_yellow_label(dynamic_table_page: DynamicTablePage) -> None:
    chrome_cpu_value_in_table = dynamic_table_page.get_chrome_cpu_percentage_from_table()
    chrome_cpu_value_in_yellow_label = dynamic_table_page.get_chrome_cpu_percentage_in_yellow_label()
    assert chrome_cpu_value_in_table == chrome_cpu_value_in_yellow_label
