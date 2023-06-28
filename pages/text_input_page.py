from playwright.sync_api import Page


class TextInputPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.my_text_field = page.get_by_role(
            "textbox", name="Set New Button Name")
        self.update_button = page.locator("#updatingButton")

    def navigate(self) -> None:
        self.page.goto("/textinput")
