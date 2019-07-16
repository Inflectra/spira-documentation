# Integrating with PyUnit

## Installing the PyUnit Extension

This section outlines how to install the SpiraTest Extension for PyUnit
onto a workstation so that you can then run automated PyUnit tests
against a Python application and have the results be recorded as test
runs inside SpiraTest. It assumes that you already have a working
installation of SpiraTest v2.3 or later, and a working Python
development environment. If you have an earlier version of SpiraTest you
will need to upgrade to at least v2.3 before trying to use this
extension.

To obtain the version of the PyUnit extension that is compatible with
your version of SpiraTest, you simply need to log-in as a project-level
administrator to SpiraTest, go to the Administration home page and
download the PyUnit Extension compressed archive (.zip). This process is
described in the *SpiraTest Administration Guide* in more detail.

-   Note: there are two versions of the PyUnit extension, one compatible
with Python 2.x, and one compatible with Python 3.x. Please make
sure you use the correct version.

The PyUnit extension is provided as a set of Python source files that
can be imported into your existing unit tests to add the SpiraTest
reporting functionality. Once you have downloaded the Zip archive, you
simply need to uncompress it into a folder of your choice on your local
system (e.g. C:\\Program Files\\SpiraTest\\PyUnit Extension)

Now to use the extension within your test cases, you need to first make
sure that the folder is added to the Python *PYTHONPATH*. The method for
doing this is dependent on the platform you're using, so please refer to
the documentation on [python.org](http://www.junit.org) for details on
the appropriate method for your platform. As an example, on a Windows
platform, the folder would be added to the PYTHONPATH by typing the
following:

set PYTHONPATH=%PYTHONPATH%; C:\\Program Files\\SpiraTest\\PyUnit
Extension

Once you have completed this step, you are now ready to begin using your
PyUnit test fixtures with SpiraTest.

## Using PyUnit with SpiraTest

The typical code structure for a PyUnit test fixture coded in Python is
as follows:

import random

import unittest

\# sample PyUnit test case

class TestSequenceFunctions(unittest.TestCase):

def setUp(self):

self.seq = range(10)

def testshuffle(self):

\# make sure the shuffled sequence does not lose any elements

random.shuffle(self.seq)

self.seq.sort()

self.assertEqual(self.seq, range(10))

def testchoice(self):

element = random.choice(self.seq)

self.assert\_(element in self.seq)

def testfail(self):

self.assertEqual(1, 2, \"1==2 Should fail\")

def testsample(self):

self.assertRaises(ValueError, random.sample, self.seq, 20)

for element in random.sample(self.seq, 5):

self.assert\_(element in self.seq)

suite =
unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)

testResult = unittest.TextTestRunner(verbosity=2).run(suite)

The Python class is marked as a PyUnit test fixture by inheriting from
the unittest.TestCase base class, and the individual test methods are
identified by using the 'test' prefix, with special setUp() and
tearDown() methods reserved for the respective purposes. When you open
up the class in a PyUnit runner or execute from the command line it
loads all the test classes and executes all the methods marked with
'test...' in turn.

Each of the Assert statements is used to test the state of the
application after executing some sample code that calls the
functionality being tested. If the condition in the assertion is true,
then execution of the test continues, if it is false, then a failure is
logged and PyUnit moves on to the next test method.

So, to use SpiraTest with PyUnit, each of the test cases written for
execution by PyUnit needs to have a corresponding test case in
SpiraTest. These can be either existing test cases that have manual test
steps or they can be new test cases designed specifically for automated
testing and therefore have no defined test steps. In either case, the
changes that need to be made to the PyUnit test fixture for SpiraTest to
record the PyUnit test run are illustrated below:

import random

import unittest

import spiratestextension

\# sample PyUnit test case

class TestSequenceFunctions(unittest.TestCase):

def setUp(self):

self.seq = range(10)

def testshuffle\_\_2(self):

\# make sure the shuffled sequence does not lose any elements

random.shuffle(self.seq)

self.seq.sort()

self.assertEqual(self.seq, range(10))

def testchoice\_\_3(self):

element = random.choice(self.seq)

self.assert\_(element in self.seq)

def testfail\_\_4(self):

self.assertEqual(1, 2, \"1==2 Should fail\")

def testsample\_\_5(self):

self.assertRaises(ValueError, random.sample, self.seq, 20)

for element in random.sample(self.seq, 5):

self.assert\_(element in self.seq)

suite =
unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)

testResult = unittest.TextTestRunner(verbosity=2).run(suite)

releaseId = 1

testSetId = 1

spiraTestExtension = spiratestextension.SpiraTestExtension()

spiraTestExtension.projectId = 1

spiraTestExtension.server = \"localhost\"

spiraTestExtension.port = 80

spiraTestExtension.ssl = False

spiraTestExtension.path = \"SpiraTest\"

spiraTestExtension.userName = \"fredbloggs\"

spiraTestExtension.password = \"PleaseChange\"

spiraTestExtension.recordResults(TestSequenceFunctions, testResult,
releaseId, testSetId)

Firstly, each of the individual test methods is appended with two
underscores followed by the ID of the corresponding test case in
SpiraTest. So for example testshuffle() is now testshuffle\_\_2() as it
maps to test case TC00002 inside SpiraTest.

Second, at the end of the test run, the testResults object generated by
the test run is passed to a special SpiraTestExtension() class via the
recordResults() method. This class takes the results from the test run
and uses it to generate the web-service messages that are sent to
SpiraTest to communicate the test results.

The following attributes need to be set on the instance of the
SpiraTestExtension() object so that the extension can access the
SpiraTest repository:

**spiraTestExtension.projectId** -- The ID of the project inside
SpiraTest (this can be found on the project homepage in the "Project
Overview" section)

**spiraTestExtension.server** - The name of the web server that
SpiraTest is installed on

**spiraTestExtension.port** -- The port used to access SpiraTest over
the network (typically 80 unless you have a custom port setup)

**spiraTestExtension.ssl** -- This should be set to False for HTTP and
True for HTTPS

**spiraTestExtension.path** -- The path to SpiraTest on your webserver
(typically just 'SpiraTest')

**spiraTestExtension.userName** - A valid username for the instance of
SpiraTest that has access to the project specified above

**spiraTestExtension.password** - A valid password for the user
specified above

In addition, when calling the recordResults() method, you should also
pass the Release ID and the Test Set ID which is used to tell SpiraTest
which release and/or test set to associate the test execution with.

The Release ID can be found on the releases list page (click on the
Planning \> Releases tab) -- just remove the RL prefix from the number
as well as any leading zeros. Similarly, the Test Set ID can be found on
the test set list page (click on the Testing \> Test Sets tab) -- just
remove the TX prefix from the number as well as any leading zeros. If
you don't want to associate the test run with a specific release or test
set, just use the special value -1 to indicate N/A.

Now all you need to do is save your code, launch PyUnit, run the test
fixtures as you would normally do, and when you view the test cases in
SpiraTest, you should see a PyUnit automated test run displayed in the
list of executed test runs:

![](img/Integrating_with_PyUnit_14.png)




Clicking on one of the PyUnit test runs will bring up a screen that
provides information regarding what PyUnit test method failed, what the
error was, together with the associated code stack-trace:

![](img/Integrating_with_PyUnit_15.png)




Congratulations... You are now able to run PyUnit automated tests and
have the results be recorded within SpiraTest. The sample test fixture
[testsequencefunctions.py]{.underline} is provided with the
installation.

