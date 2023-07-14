Feature: Set of scenarious to check https://sperasoft.com/news/ page

Scenario: The page opens successfully
	Given User opens the page https://sperasoft.com/news/
	Then The displayed url is correct
	And The company logo is shown
	
Scenario: Page content check
	Given User opens the page https://sperasoft.com/news/
	Then User can see the header for the latest article
	When User scrolls down to the second article
	Then User can see the header for the second article
	When User scrolls down to the third article
	Then User can see the header for the third article
	When User clicks on the the header of the third article
	Then The full artcile is shown on a new page