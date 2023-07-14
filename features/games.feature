Feature: Set of scenarios to check https://sperasoft.com/games/ page

Scenario: The page opens successfully
	Given User opens the page https://sperasoft.com/games/
	Then The displayed url is correct
	And The company logo is shown
	
Scenario: Check the list of the most important titles
	Given User opens the page https://sperasoft.com/games/
	Then User can see the correct list of top games/
	
Scenario: Check the 'Creative' section
	Given User opens the page https://sperasoft.com/games/
	When User scrolls down to 'Creative' header
	Then User can see the correct list of games in 'Creative' section
	
Scenario: Check the 'Sports' section
	Given User opens the page https://sperasoft.com/games/
	When User scrolls down to 'Sports' header
	Then User can see the correct list of games in 'Sports' section
	
Scenario: Check the 'Action/Shooter' section
	Given User opens the page https://sperasoft.com/games/
	When User scrolls down to 'Action/Shooter' header
	Then User can see the correct list of games in 'Action/Shooter' section
	And Each image has correct caption
	