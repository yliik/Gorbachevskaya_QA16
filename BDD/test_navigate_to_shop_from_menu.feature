Feature: Navigate to Shop
  As a user
  I want to be able to navigate to the shop page from the menu
  So that I can explore available products

  Scenario: Navigate to the shop page
    Given the user is on the 21vek.by homepage
    When the user navigates to the shop page from the menu
    Then the shop page is displayed