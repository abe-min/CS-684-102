***Sprint 3: manual integration test report 04/1/2022***


|**Test CaseID**|**Description**|**Test Steps**|**Pre-requistes**|**Author**|**Test Method**|**Test Result**|
| :- | :- | :- | :- | :- | :- | :- |
|IT1|The landing page shall have a links (or tabs) to select the articles displayed|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p>|<p>1. Add hyperlink tags to home.html</p><p>2. Add new endpoints for each category in urls.py </p>|Abreham|Manual|Fail|
|IT2|The “Home” link will display articles from the categories chosen in the settings page|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p>3. Sign in with registered credentials </p><p>4. Navigate to Settings and select preferred articles </p><p>5. Save choices and navigate to home page </p>|1. Modify the home view function in views.py to pass a category based on user selection |Amulya |Manual|Fail|
|IT3|Upon signing in, the landing page will display articles for the “Home” link|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p>3. Sign in using registered credentials </p>|1. Add redirect lookup logic to automatically navigate to the homepage after user sign in |Sri|Manual|Fail|
|IT4|The list of articles  will support pagination|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p></p>|<p>1. Add pagination to HTML using bootstrap </p><p>2. Separate results into multiple pages </p>|Amulya|Manual|Fail|
|IT5|News user API returns the articles from the user’s settings|1. Using postman test GET request at address[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/>news/{user}|1. Convert existing view into a REST API |Abreham|Manual|Fail|
***Sprint 3: manual integration test report 04/2/2022***

|**Test CaseID**|**Description**|**Test Steps**|**Pre-requistes**|**Author**|**Test Method**|**Test Result**|
| :- | :- | :- | :- | :- | :- | :- |
|IT1|The landing page shall have a links (or tabs) to select the articles displayed|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p>|<p>1. Add hyperlink tags to home.html</p><p>2. Add new endpoints for each category in urls.py </p>|Abreham|Manual|Pass|
|IT2|The “Home” link will display articles from the categories chosen in the settings page|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p>3. Sign in with registered credentials </p><p>4. Navigate to Settings and select preferred articles </p><p>5. Save choices and navigate to home page </p>|1. Modify the home view function in views.py to pass a category based on user selection |Amulya |Manual|Fail|
|IT3|Upon signing in, the landing page will display articles for the “Home” link|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p>3. Sign in using registered credentials </p>|1. Add redirect lookup logic to automatically navigate to the homepage after user sign in |Sri|Manual|Pass|
|IT4|The list of articles  will support pagination|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p></p>|<p>1. Add pagination to HTML using bootstrap </p><p>2. Separate results into multiple pages </p>|Amulya|Manual|Fail|
|IT5|News user API returns the articles from the user’s settings|1. Using postman test GET request at address[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/>news/{user}|1. Convert existing view into a REST API |Abreham|Manual|Fail|

***Sprint 3: manual integration test report 04/9/2022***

|**Test CaseID**|**Description**|**Test Steps**|**Pre-requistes**|**Author**|**Test Method**|**Test Result**|
| :- | :- | :- | :- | :- | :- | :- |
|IT1|The landing page shall have a links (or tabs) to select the articles displayed|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p>|<p>1. Add hyperlink tags to home.html</p><p>2. Add new endpoints for each category in urls.py </p>|Abreham|Manual|Pass|
|IT2|The “Home” link will display articles from the categories chosen in the settings page|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p>3. Sign in with registered credentials </p><p>4. Navigate to Settings and select preferred articles </p><p>5. Save choices and navigate to home page </p>|1. Modify the home view function in views.py to pass a category based on user selection |Amulya |Manual|Fail|
|IT3|Upon signing in, the landing page will display articles for the “Home” link|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p>3. Sign in using registered credentials </p>|1. Add redirect lookup logic to automatically navigate to the homepage after user sign in |Sri|Manual|Pass|
|IT4|The list of articles  will support pagination|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p></p>|<p>1. Add pagination to HTML using bootstrap </p><p>2. Separate results into multiple pages </p>|Amulya|Manual|Fail|
|IT5|News user API returns the articles from the user’s settings|1. Using postman test GET request at address[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/>news/{user}|1. Convert existing view into a REST API |Abreham|Manual|Fail|


***Sprint 3: manual integration test report 04/11/2022***

|**Test CaseID**|**Description**|**Test Steps**|**Pre-requistes**|**Author**|**Test Method**|**Test Result**|
| :- | :- | :- | :- | :- | :- | :- |
|IT1|The landing page shall have a links (or tabs) to select the articles displayed|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p>|<p>1. Add hyperlink tags to home.html</p><p>2. Add new endpoints for each category in urls.py </p>|Abreham|Manual|Pass|
|IT2|The “Home” link will display articles from the categories chosen in the settings page|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p>3. Sign in with registered credentials </p><p>4. Navigate to Settings and select preferred articles </p><p>5. Save choices and navigate to home page </p>|1. Modify the home view function in views.py to pass a category based on user selection |Amulya |Manual|Fail|
|IT3|Upon signing in, the landing page will display articles for the “Home” link|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p>3. Sign in using registered credentials </p>|1. Add redirect lookup logic to automatically navigate to the homepage after user sign in |Sri|Manual|Pass|
|IT4|The list of articles  will support pagination|<p>1. Run local server</p><p>2. Navigate to[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/></p><p></p>|<p>1. Add pagination to HTML using bootstrap </p><p>2. Separate results into multiple pages </p>|Amulya|Manual|Fail|
|IT5|News user API returns the articles from the user’s settings|1. Using postman test GET request at address[ ](http://127.0.0.1:8000/)<http://127.0.0.1:8000/>news/{user}|1. Convert existing view into a REST API |Abreham|Manual|Fail|




















