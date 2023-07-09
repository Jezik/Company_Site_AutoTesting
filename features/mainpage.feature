Feature: Set of scenarious for testing main page www.sperasoft.com

Scenario: Successful launch of a main page
    Given User openes main site page
    Then The url should be valid
    And The company logo should be displayed correctly

Scenario: Social media links checks
    Given User openes main site page
    When User scrolls down to Job opportunity section
    Then Links to social media appear on the right side
    When User clicks on Facebook icon
    Then Facebook company page opens in a new tab
    When User closes the tab
    And User clicks on Twitter icon
    Then Twitter company page opens in a new tab
    When User closes the tab
    And User clicks on Instagram icon
    Then Instagram company page opens in a new tab
    When User closes the tab
    And User clicks on LinkedIn icon
    Then LinkedIn company page opens in a new tab

Scenario: Internal site navigation main menu checks
    Given User openes main site page
    When User clicks on 'What we do' link
    Then The page 'Whatwedo' is opened
    When User clicks on 'Solutions' link
    Then The page 'Solutions' is opened
    When User clicks on 'Games' link
    Then The page 'Games' is opened
    When User clicks on 'About' link
    Then The page 'About' is opened
    When User clicks on 'News' link 
    Then The page 'News' is opened
    When User clicks on 'Careers' link
    Then The page 'Career' is opened

Scenario: Internal site navigation main page checks
    Given User openes main site page
    When User clicks on 'Explore' button
    Then The page 'Games' is opened
    When User presses back button in a browser
    And User scrolls down to Job opportunity section
    And User clicks on 'Learn about the company' button
    Then The page 'About' is opened 
    When User presses back button in a browser
    And User clicks on 'View all open vacancies' button
    Then The page 'Career' is opened
    When User presses back button in a browser
    And Scrolls down to Bootcamps section
    And Clicks on 'Read more' button
    Then The page 'Bootcamp' is opened

Scenario: News section of a main page checks
    Given User openes main site page
    When User scrolls down to a news section
    Then User can see four last news
    When User clicks on a specific article
    Then The new page with right content is opened

Scenario: Partners section checks
    Given User openes main site page
    When User scrolls down to a 'Our partners' section
    Then User can see appropriate list of partners
    