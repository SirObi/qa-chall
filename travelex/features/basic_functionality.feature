Feature: Basic functionality

  As a user
  I would like to quickly understand what Travelex offers
  So that I can buy the products I need quickly


  Scenario: User browses main products on mobile device
    Given I am on the home page
      And I am using a device of size (d_width, d_height)
    When I swipe through the main products section <x> times
    Then I should see the <x_plus_one>th product
