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
| User searches for articles related to phrase
| | [Setup] | Go to page | HomePage
| | I search for the phrase | furry rabbits
| | The current page should be | ResultsPage
| | Wait for condition  | return document.title == "furry rabbits - Search results - Wikipedia"
| | I see a list of results
| | I see a search suggestion

| User follows search suggestion
| | I see a search suggestion
| | I click on the search suggestion
| | I see a list of results
| | the number of results is |  20

| User opens article from results list
| | I see a list of results
| | I click on the first result
| | The current page should be | ArticlePage
| | Wait for condition  | return document.title == "Rabbit Bandini Productions - Wikipedia"
| | I see a title
| | I see a table of contents

| User changes language
| | The current page should be | ArticlePage
| | I go to main page
| | I change the language to  | de
| | Location should contain   | de.wikipedia.org

| | Stop webapp and close all browsers
