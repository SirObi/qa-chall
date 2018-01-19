*** Settings ***
| # this is the only place where we have to hard-code a path;
| # when config.py is loaded it will alter the path to include
| # the resources folder.
| Variables | ../resources/config.py
|
| Library   | PageObjectLibrary
| Library   | Selenium2Library
| Library   | Process
|
| Suite Setup | Start webapp and open browser
| Suite Teardown | Stop webapp and close all browsers

*** Variables ***
| ${BROWSER} | chrome

*** Keywords ***
| Stop webapp and close all browsers
| | Terminate all processes
| | Close all browsers

| Start webapp and open browser
| | open browser | ${CONFIG.root_url} | ${BROWSER}

*** Test Cases ***
| User browses main products on mobile device
| | [Setup] | Go to page | HomePage
| | I am using a device of size | 550 | 550 |
| | I swipe through main products section
| | I see the appropriate product
