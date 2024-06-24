# Tutorial: Creating a SpiraApp
In this tutorial, you’ll create a SpiraApp that:
* Runs on the Requirement Details page
* Uses product settings
* Replaces specific words when you save the Requirements description
* … (add something that uses a button)
* Add a column on the list page
* Add a widget

## Prerequisites
* Node.js (the latest LTS version).
* A github account
* git installed on your computer (github desktop is helpful as well)
* Familiarity with the basic development process for a SpiraApp, listed [here](https://spiradoc.inflectra.com/Developers/SpiraApps-Overview/).

## Create Your Manifest
The manifest is the heart of your SpiraApp. It contains all of the information that describes what your SpiraApp is and where it will run within a user’s Spira web application. 

Create a new folder for your SpiraApp and create a new file in it called "manifest.yaml"

(Optionally create a local git repository in this folder and publish to github to keep a backup of all your work. You will have to create a repository on github to submit your SpiraApp for approval, so this follows best practices. Once the repository is created, immediately create a new branch and do your development there, leaving the main branch mostly untouched. This makes it very simple to make a pull request for the official submission process later.)

Our SpiraApp will be very simple but we still need a complete manifest, so open your manifest file in your preferred code editor and copy and paste the following:

``` yaml
guid: 00000000-0000-0000-0000-000000000000
name: myFirstSpiraApp
caption: My first SpiraApp
summary: A word replacer SpiraApp
description: The aim of this SpiraApp is to show a basic word replacer proof of concept
productSummary: A word replacer SpiraApp
productDescription: The aim of this SpiraApp is to show a basic word replacer proof of concept
author: My Company
url: https://mycompany.com/help/spirapps/word-replacer
license: MIT License
copyright: Copyright My Company
version: 1.0
```

An additional "icon: data:image/svg+xml;file://{filename.svg}" line is optional, so we are not going to include it for now. 

Make sure to replace the value for "guid" with a newly generated GUID so your app has a unique identifier when you test and publish it. Using two SpiraApps with the same GUID could cause unexpected bugs.

Now we’re going to add another entry at the bottom of our manifest that will tell it to load a custom script on the Requirement details page:

``` yaml
pageContents:
  - pageId: 9
    name: mySpiraAppCode
    code: file://requirement.js
productSettings:
  - settingTypeId: 1 
    name: wordsToReplace
    caption: Words to Replace
    position: 1
    placeholder: pc, laptop, tablet
    tooltip: Enter a comma-separated list of words that will be replaced
  - settingTypeId: 1
    name: replacementWord
    caption: Replacement Word
    position: 2
    placeholder: device
```


## Create Your Script File
Now that you have linked requirement.js in your manifest, it’s time to actually create it. Create a new file called "requirement.js" in the same directory as your manifest and open it in a code editor.
This javascript file will do a very simple task at first: showing a short message to the user about the current artifact.

``` javascript
spiraAppManager.registerEvent_loaded(runOnRequirementLoaded);

function runOnRequirementLoaded(b) {
  var name = spiraAppManager.getDataItemField("Name", "textValue");
  var description = spiraAppManager.getDataItemField("Description","textValue");

  spiraAppManager.displaySuccessMessage(`You are viewing Requirement: ${name}, with description: ${description} `);
}
```

## Building Your SpiraApp
Before you can test your new SpiraApp, you have to create a development build of it. To do that, first use git to clone the SpiraApp package generator to your computer. Then follow the setup instructions listed on the package generator’s README. 

Build your SpiraApp by opening the terminal within the folder of your local repository of the package generator and running this command, replacing MySpiraApp with the path to your SpiraApp folder and BundleStorage to the folder you want to put the generated .spiraapp file in. 

``` bash
npm run build --input="C:\MySpiraApp" --output="C:\BundleStorage"
```

## Installing Your SpiraApp
In order to install your SpiraApp, you must be a System Administrator. First, turn on developer mode in General Settings under the System heading in the System: Admin Home. Then go to the SpiraApps page in System: Admin Home and upload the .spiraapp package file at the bottom. Its name should have appeared in the list of SpiraApps above the upload area, click the red X button on its row to enable it.

## Testing Your SpiraApp
Now that you have installed your SpiraApp, go to the product you want to test it in and go to that product’s SpiraApps page. Enable it there and then navigate to Requirements. When you click on a requirement, immediately on loading the page you should see a popup message with the name and description of the requirement. It should look something like this:

(INSERT SCREENSHOT FROM TEST HERE)


## Using the REST API
Let’s add some more code to the requirements.js file to replace the words given in the SpiraApp’s product settings. This makes use of the Spira REST API, which you can access the documentation of in the Web Services page from System: Admin Home. 

``` javascript
spiraAppManager.registerEvent_dataSaved(runOnRequirementSaved);

function runOnRequirementSaved() {
  if (SpiraAppSettings[APP_GUID] && SpiraAppSettings[APP_GUID].wordsToReplace && 
  SpiraAppSettings[APP_GUID].replacementWord) {
    var productId = spiraAppManager.projectId;
    var requirementId = spiraAppManager.artifactId;
    var url = `projects/${productId}/requirements/${requirementId}`;
    spiraAppManager.executeApi(
      "myFirstSpiraApp",
      "7.0",
      "GET",
      url,
      null,
      requirementRetrieve_Success,
      requirementRetrieve_Failure
    );
  }
}

function requirementRetrieve_Success(requirement) {
  var wordsToReplace = SpiraAppSettings[APP_GUID].wordsToReplace.split(",");
  wordsToReplace = wordsToReplace.map(str => "\b" + str.strip() + "\b");
  wordsToReplace = wordsToReplace.join("|");
  replacementRegExp = new RegExp(`/${wordsToReplace}/`, "gi");
  var replacement = SpiraAppSettings[APP_GUID].replacementWord;
  var newDescription = requirement.Description.replaceAll(replacementRegExp, replacement);
  requirement.Description = newDescription;
  spiraAppManager.executeApi(
    "myFirstSpiraApp",
    "7.0",
    "PUT",
    url,
    JSON.stringify(requirement),
    requirementUpdate_Success,
    requirementUpdate_Failure
  );
}

function requirementUpdate_Success() {
  // reload the form so the user sees the updated description
  spiraAppManager.reloadForm();
}

function requirementRetrieve_Failure(e) {
  spiraAppManager.displayErrorMessage("Error retrieving requirement data: " + e);
}

function requirementUpdate_Failure(e) {
  spiraAppManager.displayErrorMessage("Error updating requirement data: " + e);
}
```

Now is a good time to rebuild your .spiraapp package, install the new version in your test product, and test your changes to make sure everything works as expected. Make sure you enter values for the product settings "Words to Replace" and "Replacement Word" so that your code has the information it needs.

Next we’ll add a button on the requirement details page to create a new 
