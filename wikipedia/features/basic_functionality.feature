Feature: Basic functionality

  As a user
  I would like to be able to search for and browse Wikipedia articles
  So that I can get the information I need quickly

  Scenario: User searches for articles related to phrase
    Given I am on the home page
    When I for the phrase 'furry rabbits'
    Then I see a list of results
      And I see a search suggestion

  Scenario: User follows search suggestion
    Given I see a search suggestion
    When I click on the search suggestion
    Then I see a list of results
      And the number of results is 20

  Scenario: User opens article from results list
    Given I see a list of results
    When I click on the first result
    Then I see an article page
      And I see a title
      And I see a table of contents

  Scenario: User changes language
    Given I see an article page
    When I go to 'Main page' in the navigation
      And I change the language to 'German'
    Then I see the website URL is 'de.wikipedia.org'
