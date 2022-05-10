# Sprint 3 Test Plan

Project: News Feed Application


**Purpose**

The purpose of this document is to outline the test strategy and overall test approach for the News Feed Application project. This includes test methodologies, test cases, resources required, and estimated schedule.

**1. Introduction**

`	`1.1 Test objectives

The objective of the test suite is to provide adequate coverage metrics, requirements validation, and system quality data such that sufficient data is provided for those making the decision to release.

`	`1.2 Extent of tests

The tests referenced herein are written to validate Integration tests.


**2. Test Setup**

`	`2.1 Test Items

- Category Tab
- Category Links
- Home article view
- Pagination
- News articles From Preference Settings

2.2 Features to be tested

- Category Tab
  - The landing page shall have a links (or tabs) to select the articles displayed
- Category Links
  - The “Home” link will display articles from the categories chosen in the settings page
- Home article view
  - Upon signing in, the landing page will display articles for the “Home” link
- Pagination
  - The list of articles  will support pagination
- News articles From Preference Settings
  - News user API returns the articles from the user’s settings


2.3 Testing approach  

`		`Manual Integration Testing

A series of integration test cases will be executed for each new feature in section 2.1. Each integration test case will validate the added feature within its respective module.  	

**3. Pass/Fail criteria**

Each test case will have its own corresponding pass/fail criteria that the test engineer will need to confirm during testing. Please see more details in Sprint 3 Test Cases
