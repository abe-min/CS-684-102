Sprint 2: Automated unit test report

The following manual test cases are executed every time a new feature is added

March 08 2022 


|**Unit Test ID**|**Unit Test Name**|**Unit Test Category**|**Unit Test Methodology**|**Results**|
| :- | :- | :- | :- | :- |
|URL\_01|test\_home\_url\_resolve|URL|Python Unit Tests|Fail|
|URL\_02|test\_user\_registration|URL|Python Unit Tests|Fail|
|URL\_03|test\_user\_settings|URL|Python Unit Tests|Fail|
|View\_01|test\_home\_view|View|Python Unit Tests|Fail|
|View\_02|test\_register\_view|View|Python Unit Tests|Fail|
|View\_03|test\_settings\_view|View|Python Unit Tests|Fail|
|Forms\_01|test\_registration\_form|Forms|Python Unit Tests|Fail|
|Forms\_02|test\_registration\_form\_no\_data|Forms|Python Unit Tests|Fail|
|Forms\_03|test\_login\_form|Forms|Python Unit Tests|Fail|
|Forms\_04|test\_settings\_form|Forms|Python Unit Tests|Fail|

(mindbenders-newsfeed-app) (base) abrehammindaye@Abrehams-MacBook-Pro user\_management % python manage.py test Users

System check identified no issues (0 silenced).

EEEE

\======================================================================

ERROR: Users.tests.test\_forms (unittest.loader.\_FailedTest)

\----------------------------------------------------------------------

ImportError: Failed to import test module: Users.tests.test\_forms

Traceback (most recent call last):

`  `File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/unittest/loader.py", line 436, in \_find\_test\_path

`    `module = self.\_get\_module\_from\_name(name)

`  `File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/unittest/loader.py", line 377, in \_get\_module\_from\_name

`    `\_\_import\_\_(name)

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/GitHub/CS-684-102/mindbenders-newsfeed-app/user\_management/Users/tests/test\_forms.py", line 2, in <module>

`    `from users.forms import RegisterForm, LoginForm, UpdateProfileForm

ModuleNotFoundError: No module named 'users'


\======================================================================

ERROR: Users.tests.test\_models (unittest.loader.\_FailedTest)

\----------------------------------------------------------------------

ImportError: Failed to import test module: Users.tests.test\_models

Traceback (most recent call last):

`  `File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/unittest/loader.py", line 436, in \_find\_test\_path

`    `module = self.\_get\_module\_from\_name(name)

`  `File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/unittest/loader.py", line 377, in \_get\_module\_from\_name

`    `\_\_import\_\_(name)

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/GitHub/CS-684-102/mindbenders-newsfeed-app/user\_management/Users/tests/test\_models.py", line 2, in <module>

`    `from users.models import Profile

ModuleNotFoundError: No module named 'users'


\======================================================================

ERROR: Users.tests.test\_urls (unittest.loader.\_FailedTest)

\----------------------------------------------------------------------

ImportError: Failed to import test module: Users.tests.test\_urls

Traceback (most recent call last):

`  `File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/unittest/loader.py", line 436, in \_find\_test\_path

`    `module = self.\_get\_module\_from\_name(name)

`  `File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/unittest/loader.py", line 377, in \_get\_module\_from\_name

`    `\_\_import\_\_(name)

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/GitHub/CS-684-102/mindbenders-newsfeed-app/user\_management/Users/tests/test\_urls.py", line 4, in <module>

`    `from users.views import home, RegisterView, CustomLoginView, profile

ModuleNotFoundError: No module named 'users'


\======================================================================

ERROR: Users.tests.test\_views (unittest.loader.\_FailedTest)

\----------------------------------------------------------------------

ImportError: Failed to import test module: Users.tests.test\_views

Traceback (most recent call last):

`  `File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/unittest/loader.py", line 436, in \_find\_test\_path

`    `module = self.\_get\_module\_from\_name(name)

`  `File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/unittest/loader.py", line 377, in \_get\_module\_from\_name

`    `\_\_import\_\_(name)

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/GitHub/CS-684-102/mindbenders-newsfeed-app/user\_management/Users/tests/test\_views.py", line 5, in <module>

`    `from users.models import Profile, User

ModuleNotFoundError: No module named 'users'


\----------------------------------------------------------------------

Ran 4 tests in 0.000s

FAILED (errors=4)

(mindbenders-newsfeed-app) (base) abrehammindaye@Abrehams-MacBook-Pro user\_management % 







March 13 2022 


|**Unit Test ID**|**Unit Test Name**|**Unit Test Category**|**Unit Test Methodology**|**Results**|
| :- | :- | :- | :- | :- |
|URL\_01|test\_home\_url\_resolve|URL|Python Unit Tests|Pass|
|URL\_02|test\_user\_registration|URL|Python Unit Tests|Fail|
|URL\_03|test\_user\_settings|URL|Python Unit Tests|Fail|
|View\_01|test\_home\_view|View|Python Unit Tests|Pass|
|View\_02|test\_register\_view|View|Python Unit Tests|Fail|
|View\_03|test\_settings\_view|View|Python Unit Tests|Fail|
|Forms\_01|test\_registration\_form|Forms|Python Unit Tests|Fail|
|Forms\_02|test\_registration\_form\_no\_data|Forms|Python Unit Tests|Pass|
|Forms\_03|test\_login\_form|Forms|Python Unit Tests|Fail|
|Forms\_04|test\_settings\_form|Forms|Python Unit Tests|Fail|

(SemesterLongWebApp) (base) abrehammindaye@Abrehams-MacBook-Pro mind-benders-news-feed % python manage.py test users

Creating test database for alias 'default'...

System check identified no issues (0 silenced).

FF.F.ResolverMatch(func=users.views.home, args=(), kwargs={}, url\_name=users-home, app\_names=[], namespaces=[], route=)

.ResolverMatch(func=users.views.RegisterView, args=(), kwargs={}, url\_name=users-register, app\_names=[], namespaces=[], route=register/)

.ResolverMatch(func=users.views.profile, args=(), kwargs={}, url\_name=users-profile, app\_names=[], namespaces=[], route=profile/)

..FF

\======================================================================

FAIL: test\_login\_form (users.tests.test\_forms.TestForms)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_forms.py", line 28, in test\_login\_form

`    `self.assertTrue(form.is\_valid())

AssertionError: False is not true

\======================================================================

FAIL: test\_register\_form (users.tests.test\_forms.TestForms)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_forms.py", line 14, in test\_register\_form

`    `self.assertTrue(form.is\_valid()) #checks that form is valid

AssertionError: False is not true

\======================================================================

FAIL: test\_settings\_form (users.tests.test\_forms.TestForms)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_forms.py", line 36, in test\_settings\_form

`    `self.assertTrue(form.is\_valid())

AssertionError: False is not true

\======================================================================

FAIL: test\_register\_view (users.tests.test\_views.TestViews)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_views.py", line 24, in test\_register\_view

`    `self.assertEquals(response.status\_code, 200)

AssertionError: 405 != 200

\======================================================================

FAIL: test\_settings\_view (users.tests.test\_views.TestViews)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_views.py", line 30, in test\_settings\_view

`    `self.assertEquals(response.status\_code, 200)

AssertionError: 302 != 200

\----------------------------------------------------------------------

Ran 11 tests in 0.854s

FAILED (failures=5)


March 18 2022


|**Unit Test ID**|**Unit Test Name**|**Unit Test Category**|**Unit Test Methodology**|**Results**|
| :- | :- | :- | :- | :- |
|URL\_01|test\_home\_url\_resolve|URL|Python Unit Tests|Pass|
|URL\_02|test\_user\_registration|URL|Python Unit Tests|Pass|
|URL\_03|test\_user\_settings|URL|Python Unit Tests|Pass|
|View\_01|test\_home\_view|View|Python Unit Tests|Pass|
|View\_02|test\_register\_view|View|Python Unit Tests|Pass|
|View\_03|test\_settings\_view|View|Python Unit Tests|Failure|
|Forms\_01|test\_registration\_form|Forms|Python Unit Tests|Failure|
|Forms\_02|test\_registration\_form\_no\_data|Forms|Python Unit Tests|Pass|
|Forms\_03|test\_login\_form|Forms|Python Unit Tests|Failure|
|Forms\_04|test\_settings\_form|Forms|Python Unit Tests|Failure|






\======================================================================

FAIL: test\_login\_form (users.tests.test\_forms.TestForms)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_forms.py", line 28, in test\_login\_form

`    `self.assertTrue(form.is\_valid())

AssertionError: False is not true

\======================================================================

FAIL: test\_register\_form (users.tests.test\_forms.TestForms)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_forms.py", line 14, in test\_register\_form

`    `self.assertTrue(form.is\_valid()) #checks that form is valid

AssertionError: False is not true

\======================================================================

FAIL: test\_settings\_form (users.tests.test\_forms.TestForms)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_forms.py", line 36, in test\_settings\_form

`    `self.assertTrue(form.is\_valid())

AssertionError: False is not true

\======================================================================

FAIL: test\_settings\_view (users.tests.test\_views.TestViews)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_views.py", line 30, in test\_settings\_view

`    `self.assertEquals(response.status\_code, 200)

AssertionError: 302 != 200

\----------------------------------------------------------------------

Ran 11 tests in 0.452s

FAILED (failures=4)

March 21 2022


|**Unit Test ID**|**Unit Test Name**|**Unit Test Category**|**Unit Test Methodology**|**Results**|
| :- | :- | :- | :- | :- |
|URL\_01|test\_home\_url\_resolve|URL|Python Unit Tests|Pass|
|URL\_02|test\_user\_registration|URL|Python Unit Tests|Pass|
|URL\_03|test\_user\_settings|URL|Python Unit Tests|Pass|
|View\_01|test\_home\_view|View|Python Unit Tests|Pass|
|View\_02|test\_register\_view|View|Python Unit Tests|Pass|
|View\_03|test\_settings\_view|View|Python Unit Tests|Failure|
|Forms\_01|test\_registration\_form|Forms|Python Unit Tests|Failure|
|Forms\_02|test\_registration\_form\_no\_data|Forms|Python Unit Tests|Pass|
|Forms\_03|test\_login\_form|Forms|Python Unit Tests|Failure|
|Forms\_04|test\_settings\_form|Forms|Python Unit Tests|Failure|

(SemesterLongWebApp) (base) abrehammindaye@Abrehams-MacBook-Pro mind-benders-news-feed % python manage.py test users

Creating test database for alias 'default'...

System check identified no issues (0 silenced).

FF.F.ResolverMatch(func=users.views.home, args=(), kwargs={}, url\_name=users-home, app\_names=[], namespaces=[], route=)

.ResolverMatch(func=users.views.RegisterView, args=(), kwargs={}, url\_name=users-register, app\_names=[], namespaces=[], route=register/)

.ResolverMatch(func=users.views.profile, args=(), kwargs={}, url\_name=users-profile, app\_names=[], namespaces=[], route=profile/)

...F

\======================================================================

FAIL: test\_login\_form (users.tests.test\_forms.TestForms)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_forms.py", line 29, in test\_login\_form

`    `self.assertTrue(form.is\_valid())

AssertionError: False is not true

\======================================================================

FAIL: test\_register\_form (users.tests.test\_forms.TestForms)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_forms.py", line 15, in test\_register\_form

`    `self.assertTrue(form.is\_valid()) #checks that form is valid

AssertionError: False is not true

\======================================================================

FAIL: test\_settings\_form (users.tests.test\_forms.TestForms)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_forms.py", line 37, in test\_settings\_form

`    `self.assertTrue(form.is\_valid())

AssertionError: False is not true

\======================================================================

FAIL: test\_settings\_view (users.tests.test\_views.TestViews)

\----------------------------------------------------------------------

Traceback (most recent call last):

`  `File "/Users/abrehammindaye/Desktop/Spring 2022/CS-684/SemesterLongWebApp/mind-benders-news-feed/users/tests/test\_views.py", line 30, in test\_settings\_view

`    `self.assertEquals(response.status\_code, 200)

AssertionError: 302 != 200

\----------------------------------------------------------------------

Ran 11 tests in 0.745s

FAILED (failures=4)


