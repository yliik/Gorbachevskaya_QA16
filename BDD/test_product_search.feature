Feature: Product Search
  As a user
  I want to be able to search for products
  So that I can find the desired items easily

  Scenario: Search for a product
    Given the user is on the 21vek.by homepage
    When the user searches for "Телевизоры"
    Then the search results page is displayed