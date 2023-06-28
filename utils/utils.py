import pytest
import re
from playwright.sync_api import expect

expect_timeout=25000

class Utils:

    def verify_url(page, expected_url):
        expect(page).to_have_url(re.compile(expected_url), timeout=expect_timeout)
    

    def verify_page_title(page, expected_url):
        expect(page).to_have_title(re.compile(expected_url), timeout=expect_timeout)