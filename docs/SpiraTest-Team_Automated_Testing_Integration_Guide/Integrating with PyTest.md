# Integrating with PyTest

This section describes how to use SpiraTest/SpiraTeam/SpiraPlan
(hereafter referred to as SpiraTest) in conjunction with python's pytest
unit testing framework. The SpiraTest-pytest plugin enables the
automated sending of unit test results from pytest to SpiraTest with a
specified Test Case, and (optionally), a release and/or test set as
well.

## Installing the pytest plugin

This section outlines how to install the SpiraTest plugin for pytest. It
assumes that you already have a working installation of SpiraTest v2.3
or later. If you have an earlier version of SpiraTest you will need to
upgrade to at least v2.3 before trying to use this plugin. You will also
need to have Python (with pip) and pytest version 3.0 or later.

To obtain the latest version of the SpiraTest plugin, simply run the
following command:

pip install pytest-spiratest

This command will install the latest version of the plugin straight from
the [Python Package Index](https://pypi.org/project/pytest-spiratest/)
(PyPI). Once the SpiraTest plugin is successfully installed, all you
need to do is configure the extension, then you can begin testing!

## Configuring the pytest plugin

This section outlines how to configure the SpiraTest plugin for pytest.
It assumes that you are familiar with pytest, and already have some
working tests configured.

Here is a sample test file:

import pytest

\# Function we are testing

def add(num1, num2):

return num1 + num2

\# Successful test

def test\_add\_1():

assert add(1, 1) == 2

\# Failed test

def test\_add\_2():

assert add(2, 1) == 2

\# Failed test

def test\_add\_3():

assert add(4, 1) == 6

Note how test\_add\_2 is used in the configuration file discussed below.

In your test root folder (the folder you run the pytest command from),
create a file named "spira.cfg" with the following:

\[credentials\]

\# Following are required

url = localhost/SpiraTest

username = fredbloggs

token = {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXXX}

project\_id = 1

\# Following are optional:

release\_id = 5

test\_set\_id = 1

\[test\_cases\]

\# Assigned to the rest

default = 20

\# Test case for a specific function

test\_add\_2 = 22

For the plugin to work, you must have both settings groups (credentials
and test\_cases) with the following in the credentials group:

**url** -- The base url to your SpiraTest installation, without a '/' at
the end.

**username** -- The username you use to sign into SpiraTest.

**token** -- Your RSS Token. Found in your profile page as the "RSS
Token" field, you must have RSS Feeds enabled for this to work.

**project\_id** -- The ID of the project you would like the test runs to
be sent to

**release\_id** -- OPTIONAL -- Use if you would like to associate the
test run with a release.

**test\_set\_id** -- OPTIONAL -- Use if you would like to associate the
test run with a test set.

Under the test\_cases group, put the following:

**default** -- The default test case ID for functions without an
assigned test case

**\<function name\>** - Used to override the default setting for a
function's test case ID in SpiraTest. Only include the function name,
without the parentheses.

Once you have filled out all of the configurations, you are all set to
go!

Running the pytest (or py.test) command will run your unit tests, send
the data to SpiraTest, and show the results to you. Here is an example
of the test\_add\_3 function inside SpiraTest:

![](img/Integrating_with_PyTest_16.png)




