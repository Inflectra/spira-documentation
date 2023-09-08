# Integrating with Jest JS

## Brief Overview
This reporter will integrate JestJS with Inflectra's ALM suite. It will create a test run in Spira for each test executed in Jest.

## Guide Basics
Unfortunately, this integration will work with SpiraTest/SpiraTeam/SpiraPlan (hereafter refered to as SpiraTest) version 5.0 and above and at least Jest 24.x. If you have an older version, you will need to update to use this reporter.

This guide assumes a basic familiarity with both SpiraTest and the Jest testing framework. 

## Setting up the integration
Install the integration by running `npm i jest-spiratest` in the root directory of your tests. Inside your `package.json` file, add the `jest` field with the format as shown below. Here is sample `package.json`.
```javascript
{
    "name": "sample",
    "scripts": {
        "test": "jest"
    },
    "jest": {
        "reporters": [
            "default",
            [
                "jest-spiratest",
                {
                    "url": "https://doctor/SpiraPlan",
                    "username": "fredbloggs",
                    "token": "{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}",
                    "projectId": 1,
                    "releaseId": 1,
                    "testSetId": 1,
                    "testCases": {
                        "default": 20,
                        "storesCorrectly": 21,
                        "javascriptWorks": 16
                    }
                }
            ]
        ]
    }
}
```
Fields are required unless otherwise noted.

| Field         | Description                                                                                                                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `url`         | The root URL of your SpiraTest instance without a '/' at the end                                                                                                                                                                              |
| `username`    | The username you use to sign into SpiraTest                                                                                                                                                                                                   |
| `token`       | Your RSS Token. Found in your profile page as the `RSS Token` field. You must have RSS Feeds enabled for this to work                                                                                                                          |
| `projectId`   | The ID of the project you would like the Test Runs to be filed under                                                                                                                                                                          |
| `releaseId`   | **OPTIONAL** - Use if you would like to associate created test runs with a release                                                                                                                                                            |
| `testSetId`   | **OPTIONAL** - Use if you would like to associated created test runs with a test set                                                                                                                                                          |
| `testCases`   | Must contain the `default` field within it and, optionally, specific test cases for a given test spec name                                                                                                                                    |
| `default`     | Inside the `testCases` field, this is the ID of the default test case mapped to a created test run                                                                                                                                            |
| `<test_name>` | **OPTIONAL** - Use *as many times as you would like* to map a the created test run to a particular test case in SpiraTest. Note that capitalization, special characters and spaces are ignored both in `testCases` *and* the test declaration |

Once you have added the SpiraReporter to jest as described above, you are all set!

## Using the SpiraTest Reporter
Actually, you don't do anything different! Just run `npm test` or however you ran jest before and you should see test runs created in the project you specified!