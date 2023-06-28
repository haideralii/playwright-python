from playwright.sync_api import Page


class DynamicTablePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.chrome_cpu_percent_column = page.locator(
            '[role="table"] [role="rowgroup"] [role="row"]:has-text("chrome") [role="cell"]:has-text("%")')
        self.yellow_label = page.locator(".bg-warning")

    def navigate(self) -> None:
        self.page.goto("/dynamictable")

    def get_chrome_cpu_percentage_from_table(self) -> None:
        value_in_percent = self.chrome_cpu_percent_column.inner_text()
        value_without_percent_sign = value_in_percent.replace("%", "")
        return float(value_without_percent_sign)

    def get_chrome_cpu_percentage_in_yellow_label(self) -> None:
        percent_value_in_yellow_label = self.yellow_label.inner_text()
        value_without_label = percent_value_in_yellow_label.replace("Chrome CPU: ", "")
        value_without_percent = value_without_label.replace("%", "")
        return float(value_without_percent)
