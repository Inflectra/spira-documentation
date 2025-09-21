# Integrating with PyTest
!!! abstract "Compatible with SpiraTest, SpiraTeam, SpiraPlan"

This section describes how to use Spira in conjunction with python's pytest unit testing framework. The Spira pytest plugin enables the automated sending of unit test results from pytest to Spira with a specified Test Case, and (optionally), a release and/or test set as well.

## Installing the pytest plugin
This section outlines how to install the Spira plugin for pytest. It assumes that you already have a working installation of Spira v6.0 or later. If you have an earlier version of Spira you will need to upgrade to at least v6.0 before trying to use this plugin. You will also need to have Python (with pip) and pytest version 3.0 or later.

To obtain the latest version of the Spira plugin, simply run the following command: `pip install pytest-spiratest`

This command will install the latest version of the plugin straight from the [Python Package Index](https://pypi.org/project/pytest-spiratest/) (PyPI). Once the Spira plugin is successfully installed, all you need to do is configure the extension, then you can begin testing!

## Configuring the pytest plugin
This section outlines how to configure the Spira plugin for pytest. It assumes that you are familiar with pytest, and already have some working tests configured.

Here is a sample test file:

```python
import pytest

# Function we are testing
def add(num1, num2):
  return num1 + num2

# Successful test
def test_add_1():
  assert add(1, 1) == 2

# Failed test
def test_add_2():
  assert add(2, 1) == 2

# Failed test
def test_add_3():
  assert add(4, 1) == 6
```

Note how test_add_2 is used in the configuration file discussed below.

In your test root folder (the folder you run the pytest command from), create a file named "spira.cfg" with the following:

```cfg
[credentials]
# Following are required

url = localhost/Spira
username = fredbloggs
token = {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXXX}
project_id = 1

# Following are optional:
release_id = 5
test_set_id = 1

[test_cases]
# Assigned to the rest
default = 20
# Test case for a specific function
test_add_2 = 22
```

For the plugin to work, you must have both settings groups (credentials and test_cases) with the following in the credentials group:

- **url**: The base url to your Spira installation, without a '/' at the end.
- **username**: The username you use to sign into Spira.
- **token**: Your RSS Token. Found in your profile page as the "RSS Token" field, you must have RSS Feeds enabled for this to work.
- **project_id**: The ID of the project you would like the test runs to be sent to
- **release_id**: OPTIONAL -- Use if you would like to associate the test run with a release.
- **test_set_id**: OPTIONAL -- Use if you would like to associate the test run with a test set.

Under the test_cases group, put the following:

- **default**: The default test case ID for functions without an assigned test case
- **\<function name>** - Used to override the default setting for a function's test case ID in Spira. Only include the function name, without the parentheses. 

**NOTE**: If your functions are in a class then add the class before the function name - for example `MyClass.myFunction`. The plugin is case insensitive.

Once you have filled out all of the configurations, you are all set to go!

Running the pytest (or py.test) command will run your unit tests, send the data to Spira, and show the results to you. Here is an example of the test_add_3 function inside Spira:

![](img/Integrating_with_PyTest_16.png)

## Have Questions or Need Assistance?
If you are an Inflectra customer, please contact our customer support at:

- Email: support@inflectra.com
- Help Desk: https://www.inflectra.com/Support/

Otherwise, please feel free to post a question on our public forums:

- [Test Case Integration Forum](https://www.inflectra.com/Support/Forum/integrations/unit-testing/List.aspx)