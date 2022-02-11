# Spira Test Runner add-in for Excel 365

This add-in lets you retrieve your assigned Test Cases and Test Sets for a specific product in SpiraTest®, SpiraTeam®, or SpiraPlan® application (hereafter referred to as SpiraPlan). You can run your tests straight away or later. When you are ready you can send your test executions back to SpiraPlan. This addin works with Microsoft Excel 2016+, Excel in the cloud (via a web browser), and Excel on iPad OS.


## Installation 

To install the add-in:

* Go to the **insert** tab in Excel
* Click on **"Get Add-Ins"** and in the window that opens navigate to the **store** tab
* Search for **"Spira** or **SpiraPlan**. 
* When you see the correct add-in **"Test Runner"** developed by Inflectra, click on the "Add" button associated with it.
* You should now see the SpiraPlan icon labeled "SpiraPlan Test Runner" in your home tab. Click on it to begin.


## Connecting to SpiraPlan
Open the add-in from the ribbon and fill in the login form panel on the right of your Excel screen. If you are using Excel in the browser, make sure your SpiraPlan is accessible over the internet.

![SpiraPlan add-in login screen](img/test-runner-log-in-screen.png)

* **Your SpiraPlan URL:** The web address that you use to access SpiraPlan in your browser. Use the web address you use to access SpiraPlan in your browser. This is usually of the form 'http://company.spiraservice.net'. Make sure you remove any suffixes from the address (e.g. Default.aspx or "/")
* **Your Username:** This is the exact same username you use to log in to SpiraPlan. (Not Case Sensitive)
* **Enter your RSS token:** You can find or generate this from your user profile page inside SpiraPlan - "{ExampleRSS}". Make sure to include the curly braces and *make sure to hit Save after generating a new RSS token.*

If there is a problem connecting to SpiraPlan you will be notified with an error message.

After you have logged in click **Logout** to close your connection with SpiraPlan and take you back to the add-in's login page.

## Retrieving Tests from SpiraPlan

After successfully logging in to the application, you'll need to get the Test Cases and/or Test Sets assigned to you from SpiraPlan. Select a product to retrieve the data from and click on 'Get from Spira'. 

![SpiraPlan add-in main screen](img/test-runner-main-screen.png)

You should see the Test Cases and their Test Steps on the Spreadsheet. Please note that the spreadsheet contains only Test Cases with Test Steps and Test Sets type 'Manual' assigned to you. The spreadsheet template has a few different columns:

![SpiraPlan add-in spreadsheet data](img/test-runner-spreadsheet.png)

**'Send to Spira' Log**: This column will bring important information from the SpiraPlan server. Here, you can see warning, error, and success messages. Remember to always check this column after sending data to SpiraPlan to check if the operation was successful or not.

**Case ID and Step ID**: Respectively, the IDs of the Test Case and the Test Step in SpiraPlan. You can't edit this field.

**Test Case Name**: The name of the Test Case in SpiraPlan.

**Associated Release**: The release associated with the Test Case in SpiraPlan.

**Set ID**: If the Test Case came from a Test Step assigned to you, you should see its ID in this field. Otherwise, it will remain blank.

**Set Case Unique ID**: This is the Test-Set, Test Case unique ID i.e.: the ID of the Test Case inside a Test Set in SpiraPlan.

**Test Step Description/Test Step Expected Result/Test Step Sample Data**: This field brings the text description/expected result/sample data of the Test Step in SpiraPlan.

**Execution Status**: The execution status of that test step. It should be selected drop the dropdown list. This field will be sent to SpiraPlan.

**Actual Result**: The long description of the actual result experienced during testing. If you want it formatted, you need to add HTML tags such as `<b>` for bold. This field will be sent to SpiraPlan.

**Incident Name** : If you want to log an incident associated with the test failure, enter the name of the incident here. The description of the incident will be automatically populated with the Test Step Description, Expected Result, and Actual Result.


## Running Tests

In the spreadsheet, you can see different cell colors. Each of them has a different meaning:

- <span style="color:gray">**Gray:**</span> means you can't edit the cell, it's a protected field.
- <span style="color:green">**Green:**</span> means you are encouraged to populate this cell, as the changes will reflect in SpiraPlan.
- <span style="background-color: #000000; color:white" >**White:**</span></span> means it is an optional field.
- <span style="color:red">**Red:**</span> means there was an error in the artifact. Check the 'Send to Spira' Log column to read the error message.

To run the tests, fill all the green (and optionally the white) cells of each row, accordingly. You can also save the spreadsheet and run the Test Cases later (see the session 'Offline Testing').


## Uploading Tests

Now that all the necessary data is populated in the spreadsheet, you can upload the results to SpiraPlan. There are two ways of doing it, depending on whether you just retrieved the test cases or if they are stored in a previously saved spreadsheet.

### Online Testing

This session assumes you just retrieved the Test Cases from SpiraPlan (the add-in is still running) and now want to upload your results to SpiraPlan. In that case, just click the button 'Send to Spira' and wait until the operation is complete. If everything goes well, you will see the Test Run and (optionally) Incident IDs in the 'Send to Spira' Log column. If there's any error, instead you will see red cells and error messages. Check the FAQ session to see how to fix it.


### Offline Testing

Assuming that you decided to save the spreadsheet and populate the fields later (there's no need to have access to the internet when doing it), to upload the data to SpiraPlan:

1. Open the saved spreadsheet - make sure the Test Run fields are filled
2. Open and log in to the add-in
3. Select the product you originally chose to generate the template - it is not possible to save the Test Runs in a different product
4. Click on 'Use Current Sheet'
5. Now, click on 'Send to Spira' to upload your results.

Check the FAQ session in case you see any error message.


## Frequently Asked Questions

Following are answers to questions related to common errors you may face when using the add-in.

**1. Right after providing my SpiraPlan credentials and clicking 'Log in', I see the error message **

`Error: Request has been terminated Possible causes: the network is offline, Origin is not allowed by Access-Control-Allow-Origin, the page is being unloaded, etc.`

**how to solve this issue?**

First, make sure your credentials are correct. You can re-generate your RSS / API Key by going to your user page in SpiraPlan. Always remember to click 'Save' after re-generating your RSS key. If the problem persists, ask your SpiraPlan administrator to check the SpiraPlan API CORS configuration (in SpiraPlan: Admin menu > System > Security Settings > Allowed Domains) to see if it is accepting connections from the add-in domain.


**2. When importing data from a spreadsheet previously saved on my computer, I'm seeing error message(s). How to solve it?**

Following is the list of possible error messages when importing a spreadsheet into the add-in and how to solve them:

`Error: The selected product does not match the Spreadsheet data.`

Solution: You cannot run Tests from one product to another. In the add-in, select the same product of the saved spreadsheet and try again.

`Error: Database sheet is missing.`

Solution: Your spreadsheet is missing required data. You have to re-import the data from the product. Never delete/rename any worksheet from the spreadsheet.

`Error: There are columns missing in the spreadsheet.`

Solution: Your worksheet is missing required data. You have to re-import the data from the product. Never delete/rename any column from the worksheet.

`Error: Invalid Test Case detected: missing Test Step(s).`

Solution: Your worksheet is missing Test Case data. You have to re-import the data from the product. You can delete Test Cases from the worksheet, but make sure to not leave Test Sets with no Test Cases or Test Cases with no Test Steps.

**3. Right after clicking on 'Send to Spira', I see a Test Case red row and an error message at its first column saying**

`Invalid Execution Statuses: This TestCase contains an invalid execution statuses combination.`

**how to solve this issue?**

If there are a 'Not Run' Test Step in the Test Case, it is required to have at least one failed Test Step (Failed/Blocked/Caution) in the same Test Case. Make sure your Test Steps match this condition and try again.

**4. Right after clicking on 'Send to Spira', I see a Test Step red row and an error message at its first column saying**

`Missing Actual Result: This TestStep needs to have an Actual Result, since it failed.`

**how to solve this issue?**

It is required for all the failed Test Steps (Failed/Blocked/Caution) to have the Actual Result column filled. Make sure your failed Test Steps match this condition and try again.

**5. Right after clicking on 'Get from Spira' or 'Send to Spira', the add-in hangs on a loading screen for a long time and nothing happens. How to solve this issue?**

Make sure you are not editing any cell when clicking on any add-in button. Excel does not allow add-ins to modify the spreadsheet when in editing mode. To solve this issue, simply click on any blank cell or press the ESC key. If it still does not work, check your internet connection and try again.