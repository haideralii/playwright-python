from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.click_link = page.get_by_role("link", name="Click")
        self.text_input_link = page.get_by_role("link", name="Text Input")
        self.dynamic_table_link = page.get_by_role("link", name="Dynamic Table")
        self.sample_app_page_link = page.get_by_role("link", name="Sample App")

    def navigate(self) -> None:
        self.page.goto("/")
