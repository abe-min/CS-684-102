# Sprint 4 Test Plan

Project: News Feed Application


## Purpose

The purpose of this document is to outline the test strategy and overall test approach for the News Feed Application project. This includes test methodologies, test cases, resources required, and estimated schedule.

## 1. Introduction

##### 1.1 Test objectives
  The objective of the test suite is to provide adequate coverage metrics, requirements validation, and system quality data such that sufficient data is provided for those making the decision to release.

#####	1.2 Extent of tests

  The tests referenced herein are written to validate system tests


## 2. Test Setup

##### 2.1 Test Items
 
- New user sign up  
- Registered user sign in 
- Preference setting 
- Merged category articles 
- Keyword searching 
- Advanced multi keyword searching 

##### 2.2 Features to be tested

- New user sign up  
  - New users can register to use the system with credentials that meet the sign up criteria
- Registered user sign in 
  - Registered users can sign in to use the system using their correct credentials  
- Preference setting 
  - Registered users can set and save their news category preferences. This feature should only be visible to registered users
- Merged category articles 
  - For signed in users, the home page should show news articles from the categories they selected in the preferences setting. 
- Keyword searching 
  - Keyword searching should show only articles that contain the searched keyword 
- Advanced multi keyword searching 
  - Multiple keyword searching separated by AND / OR / NOT keywords should show articles which contain the searched keywords 

##### 2.3 Testing approach  

- System Testing 

  - A series of regression test cases will be executed with each new feature that’s added. Each test case will validate the system is operating end-to-end, from the front end, to the api, and to the database as designed



## 3. Pass/Fail criteria

Each test case will have it's own corresponding pass/fail criterial that the test engineer will need to confirm during testing. Please see more details in Sprint 4 Test Cases  



#### [Return to readme](README.md)


