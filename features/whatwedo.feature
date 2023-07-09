Feature: Set of scenarios to check https://sperasoft.com/whatwedo/ page

Scenario: The page opens successfully
	Given User opens the page https://sperasoft.com/whatwedo/
	Then The company logo is shown
	And The header is shown with a correct text

Scenario: Page content sections
	Given User opens the page https://sperasoft.com/whatwedo/
	When User scrolls down to a 'Game Development' section
	Then The right text description is shown in 'Game Development' section
	When User scrolls down to a 'Game porting' section
	Then The right text description is shown in 'Game porting' section
	When User scrolls down to a 'Engineering' section
	Then The right text description is shown in 'Engineering' section
	When User scrolls down to a 'Creative' section
	Then The right text description is shown in 'Creative' section
	
Scenario: Internal site links checks
	Given User opens the page https://sperasoft.com/whatwedo/
	When User scrolls down to a 'Game Development' section
	And User clicks on 'View all Games' button
	Then The page https://sperasoft.com/games/ is opened
	When User return back to whatwedo page
	And User scrolls down to a 'Creative' section
	And User clicks on 'Portfolio' button
	Then The https://sperasoft.com/whatwedo/portfolio/ page is opened

Scenario: Request more info form checks
	Given User opens the page https://sperasoft.com/whatwedo/
	When User scrolls down to a 'Engineering' section
	And User clicks on 'Request more info' button
	Then The the pop-up with the request form is shown

Scenario: Company certifications section checks
	Given User opens the page https://sperasoft.com/whatwedo/
	When User scrolls down to 'Company certifications' section
	Then The correct list of certifications is shown
