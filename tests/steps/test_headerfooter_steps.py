# tests/steps/test_homepage_steps.py

from pytest_bdd import given, when, then, scenarios, parsers
from playwright.sync_api import Page, expect

# IMPORTING THE LOCATORS DIRECTLY
from locators.headerfooter_locators import HomeLocators

# Map all scenarios in the feature file to this steps file
scenarios('headerfooter.feature')

# --- GIVEN STEP ---

@given("the user is on the automation testing practice home page")
def user_is_on_home_page(page: Page):
    """Navigate to the home page URL."""
    page.goto(HomeLocators.BASE_URL)
    page.wait_for_load_state("load")

# --- THEN STEPS ---

@then(parsers.parse('the page title should be {expected_title}'))
def verify_page_title(page: Page, expected_title):
    """Verifies the browser tab title."""
    expect(page).to_have_title(expected_title)

@then(parsers.parse('the main header {expected_main_header} should be visible'))
def verify_main_header(page: Page, expected_main_header):
    """Verifies the text and visibility of the main blog header using the imported locator."""

    # Locate the element using the imported locator string
    main_header_locator = page.locator(HomeLocators.MAIN_HEADER)

    # 1. Assert the main header is visible
    expect(main_header_locator).to_be_visible()

    # 2. Assert the text content matches
    expect(main_header_locator).to_have_text(expected_main_header)

@then(parsers.parse('the sub header {expected_sub_header} should be visible'))
def verify_sub_header(page: Page, expected_sub_header):
    """Verifies the text and visibility of the sub blog header using the imported locator."""

    # Locate the element using the imported locator string
    sub_header_locator = page.locator(HomeLocators.SUB_HEADER)

    # 1. Assert the sub header is visible
    expect(sub_header_locator).to_be_visible()

    # 2. Assert the text content matches
    expect(sub_header_locator).to_have_text(expected_sub_header)
    