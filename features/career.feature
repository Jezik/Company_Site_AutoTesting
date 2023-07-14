Feature: Set of scenarious to check https://sperasoft.com/career/ page

Scenario: The page opens successfully
	Given User opens the page https://sperasoft.com/career/
	Then The displayed url is correct
	And The company logo is shown
	
Scenario: Page content checks
	Given User opens the page https://sperasoft.com/career/
	Then The big header 'Join #Sperasoft' is shown
	And The section 'Jobs at Sperasoft' is shown
	
Scenario: Internal site navigation
	Given User opens the page https://sperasoft.com/career/
	When User clicks on a 'About us' link
	Then The page https://sperasoft.com/about/ is shown
	When User return to previous page
	And User clicks on 'Sperasoft bootcamp' link
	Then The page https://sperasoft.com/career/bootcamp/ is opened
	When User return to previous page
	And User clicks on 'Sperasoft news' link
	Then The page https://sperasoft.com/news/ is opened
	
Scenario: Jobs at Sperasoft section checks
	Given User opens the page https://sperasoft.com/career/
	Then The section 'Jobs at Sperasoft' is shown
	When User picks from drop down list city Warsaw
	Then There are only jobs for Warsaw shown
	When User clicks on job header
	Then The job description openes in on a new page	
	