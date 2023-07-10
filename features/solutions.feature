Feature: Set of scenarios to check https://sperasoft.com/solutions/ page

Scenario: The page opens successfully
	Given User opens the page https://sperasoft.com/solutions/
	Then The company logo is shown
	And Both headers have correct text

Scenario: Page content sections
	Given User opens the page https://sperasoft.com/solutions/
	When User scrolls down to a 'Live services' section
	Then The right text description is shown in 'Live services' section
	When User scrolls down to a 'NOC' section
	Then The right text description is shown in 'NOC' section
	When User scrolls down to a 'eCommerce' section
	Then The right text description is shown in 'eCommerce' section
	When User srolls down to a 'DevOps' section
	Then The right text description is shown in 'DevOps' section
	When User srolls down to a 'QE' section
	Then The right text description is shown in 'QE' section

Scenario: 'Contact us' pop up check
	Given User opens the page https://sperasoft.com/solutions/
	When User clicks on 'Contact us' field
	Then The form for requests should be shown
	