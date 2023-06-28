from playwright.sync_api import Page


class ProgressBarPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.start_button = page.locator("#startButton")
        self.stop_button = page.locator("#stopButton")
        self.progress_bar_with_75_percent = page.locator(
            '#progressBar[aria-valuenow="75"]')
        self.result_label = page.locator("#result")

    def navigate(self) -> None:
        self.page.goto("/progressbar")
