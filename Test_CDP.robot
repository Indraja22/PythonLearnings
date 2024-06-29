*** Settings ***
Library    SeleniumLibrary
Library    cdp_lib.py
Library    cdp_print_page.py

*** Keywords ***
Offline Status
    
    Open Browser    https://www.costco.com/    Chrome
    # Cdp Responsiveness
    Wait Until Element Is Visible    id:search-field
    Input Text    id:search-field    iPhone 15
    Print Pdf Preview
    Click Element    xpath://input[@id='search-field']//parent::span//following-sibling::button[contains(@class,'search-ico-button')]
    # Set Offline Status
    Reload Page 

*** Test Cases ***
CDP
    Offline Status
    Capture Page Screenshot    EMBED
    Close Browser
