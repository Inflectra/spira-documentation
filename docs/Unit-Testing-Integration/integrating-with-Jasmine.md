# Integrating with Jasmine

Jasmine is a behavior-driven development framework for testing JavaScript code. It does not depend on any other JavaScript frameworks. It does not require a DOM. And it has a clean, obvious syntax so that you can easily write tests.

Some key features of Jasmine are:

* Fast- Low overhead, jasmine-core has no external dependencies.
* Batteries Included - Comes out of the box with everything you need to test your code.
* NodeJS and Browser - Run your browser tests and Node.js tests with the same framework.

The [Spira Reporter for Jasmine](https://www.npmjs.com/package/jasmine-spiratest) will integrate JasmineJS with Spira. It will create a test run in Spira for each test spec executed in Jasmine.

## Setting up the integration
Install the integration by running `npm i jasmine-spiratest` in the root directory of your tests. Inside each test spec file, import the SpiraReporter with `var SpiraReporter = require('jasmine-spiratest')` then put the line `jasmine.getEnv().addReporter(new SpiraReporter(spiraCredentials));` where spiraCredentials is an object of the format below. You can see a full sample test spec at the bottom of this page.

```
{
    "url": "https://doctor/SpiraPlan",
    "username": "fredbloggs",
    "token": "{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}",
    "projectId": 1,
    "releaseId": 1,
    "testSetId": 1,
    "testCases": {
        "default": 20,
        "should multiply correctly": 21,
        "should solve exponents and logarithms correctly": 16
    }
}
```

Fields are required unless otherwise noted.

| Field       | Description |
|-------------|-------------|
| url         | The root URL of your SpiraTest instance without a '/' at the end |
| username    | The username you use to sign into SpiraTest |
| token       | Your RSS Token. Found in your profile page as the RSS Token field. You must have RSS Feeds enabled for this to work |
| projectId   | The ID of the product you would like the Test Runs to be filed under |
| releaseId   | OPTIONAL - Use if you would like to associate created test runs with a release |
| testSetId   | OPTIONAL - Use if you would like to associated created test runs with a test set |
| testCases   | Must contain the default field within it and, optionally, specific test cases for a given test spec name |
| default     | Inside the testCases field, this is the ID of the default test case mapped to a created test run |
| <spec_name> |	OPTIONAL - Use as many times as you would like to map a the created test run for a spec to a particular test case in SpiraTest. Note that capitalization, special characters and spaces are ignored both in testCases and the spec itself |
Once you have added the SpiraReporter to the jasmine environment in each file as described above, you are all set!

## Using the SpiraTest Reporter
Run `npm test` or however you ran jasmine before and you should see test runs created in the product you specified.

## Sample Test Spec with SpiraTest Integration
```
describe("Test having two specs", () => {
    var SpiraReporter = require('jasmine-spiratest');
 
    jasmine.getEnv().addReporter(new SpiraReporter({
        "url": "https://doctor/SpiraPlan",
        "username": "fredbloggs",
        "token": "{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}",
        "projectId": 1,
        "releaseId": 1,
        "testSetId": 1,
        "testCases": {
            "default": 20,
            "equality works": 21,
            "addition works": 16
        }
    }));
 
    describe("Test basic JavaScript", () => {
        it("Equality works...", () => {
            expect(2).toEqual(2);
        });
        it("Addition works", () => {
            expect(3 + 2).toEqual(5);
        });
        it("Multiplication works", () => {
            expect(4 * 5).toEqual(20);
        });
    });
});
```