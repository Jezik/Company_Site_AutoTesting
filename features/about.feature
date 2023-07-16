Feature: Set of scenarious to check https://sperasoft.com/about/ page

Scenario: The page opens successfully
	Given User opens the page https://sperasoft.com/about/
	Then The displayed url of 'About' page is correct
	And The company logo is shown

Scenario: Check page content
	Given User opens the page https://sperasoft.com/about/
	When User scrolls down to a 'World Class Gaming Studio' section
	Then The right text description is shown in 'World Class Gaming Studio' section
	When User scrolls down to a 'Our clients' section
	Then User can see the list of main partners
	When User clicks on 'View all' button
	Then User can see the whole list of partners
	
Scenario: Check information about Leadership team
	Given User opens the page https://sperasoft.com/about/
	When User scrolls down to a 'Leadership team' section
	Then User can see the list of all company's top managers
	When User clicks on 'Read more' button
	Then The page https://sperasoft.com/about/executives/ is opened
	And The correct header for this page is shown
