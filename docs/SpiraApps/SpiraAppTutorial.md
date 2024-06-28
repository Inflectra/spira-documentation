# Tutorial: Creating a SpiraApp
In this tutorial, you’ll create a SpiraApp that:
* Runs on the Requirement Details page
* Uses product settings
* Replaces specific words when you save the Requirements description
* Adds a Quick Link button on the Requirement Details page
* Add a widget to the product page
* Add a column on the list page

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
summary: A Tutorial SpiraApp
description: The aim of this SpiraApp is to show off multiple functionalities of SpiraApps
productSummary: A Tutorial SpiraApp
productDescription: The aim of this SpiraApp is to show off multiple functionalities of SpiraApps
author: My Company
url: https://mycompany.com/help/spiraapps/tutorial
license: MIT License
copyright: Copyright Inflectra
version: 1.0
```

An additional "icon: data:image/svg+xml;base64,file://filename.svg" line is optional, so we are not going to include it for now. 

**Replace the value for "guid" with a newly generated GUID** so your app has a unique identifier when you test and publish it. Using two SpiraApps with the same GUID could cause unexpected bugs.

Now we’re going to add another entry at the bottom of our manifest that will tell it to load a custom script on the Requirement details page:

``` yaml
pageContents:
  - pageId: 9
    name: mySpiraAppCode
    code: file://requirement.js
```

Let's define the product settings we need now so we can use them later in development. Add this to your manifest as well:

``` yaml
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
Before you can test your new SpiraApp, you have to create a development build of it. To do that, first use git to clone the SpiraApp package generator to your computer in a different directory. Then follow the setup instructions listed on the package generator’s README. 

To build your SpiraApp, open the terminal within the package generator folder and run the command below, replacing MySpiraApp with the path to your SpiraApp folder and BundleStorage to the folder you want to put the generated .spiraapp file in. 

``` bash
npm run build --input="C:\MySpiraApp" --output="C:\BundleStorage"
```

## Installing Your SpiraApp
In order to install your SpiraApp, you must be a System Administrator. First, turn on developer mode in General Settings under the System heading in the System: Admin Home. Then go to the SpiraApps page in System: Admin Home and upload the .spiraapp package file at the bottom. Its name should have appeared in the list of SpiraApps above the upload area, now click the red X button on its row to enable it for your system.

## Testing Your SpiraApp
Now that you have installed your SpiraApp, go to the product you want to test it in and go to General Settings > SpiraApps. Enable it there and then navigate to Requirements. When you click on a requirement, immediately on loading the page you should see a popup message with the name and description of the requirement. It should look something like this:

![Popup on requirement details page with the requirement name and description](img\tutorial-requirement-popup.png)


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
  wordsToReplace = wordsToReplace.map(str => "\\b" + str.trim() + "\\b");
  wordsToReplace = wordsToReplace.join("|");
  var replacementRegExp = new RegExp(`${wordsToReplace}`, "gi");
  var replacement = SpiraAppSettings[APP_GUID].replacementWord;
  var newDescription = requirement.Description.replaceAll(replacementRegExp, replacement);
  var productId = spiraAppManager.projectId;
  var url = `projects/${productId}/requirements`;
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

## Adding a Home Page Widget
Next we’ll add a widget on the Product Home page to show the most recently created incident.

First we need to add the widget to our manifest.yaml file.

``` yaml
dashboards:
  - dashboardTypeId: 1
    name: Latest Incident
    isActive: true
    description: Displays the most recently created incident
    code: file://widget.js
```

Next we have to implement the code to render the widget in a new file, widget.js. We are going to use the HTML rendering library Mustache to fill in the widget template. First assign the widget elementId and the template to global constants.

``` javascript
const elementId = APP_GUID + "_content";
const template = `
{{^hasItems}}
    <p class="alert alert-info">Sorry, there is no data to display</p>
{{/hasItems}}
{{#hasItems}}
    <table class="WidgetGrid" role="grid" style="width:100%">
        <tr role="rowHeader">
            <th> colspan="2">Name</th>
            <th>Type</th>
            <th>Created By</th>
            <th>Date Created</th>
        <tr>
        {{#dataItems}}
            <tr role="row">
                <td>
                    <img src="{{ icon }}" class="w4 h4"></img>
                </td>
                <td>
                    <a class="has-tooltip" href=" {{ incUrl }}">
                        {{ name }}
                        <div class="is-tooltip">[RQ:{{ reqID }}]</td>
                    </a>
                </td>
                <td>{{ type }}</td>
                <td>{{ creator }}</td>
                <td>
                    <span title="{{ datetime }}">{{ date }}</span>
                </td>
            <tr>
        {{/dataItems}}
    </table>
{{/hasItems}}`;
```

Then we need to write the functions that will fill this template with the latest incident. This code should go right after the template in widget.js.

``` javascript
spiraAppManager.registerEvent_windowLoad(loadIncident);
spiraAppManager.registerEvent_dashboardUpdated(loadIncident);

function loadIncident() {
    const REQ_TYPE_ID = 1;
    const canViewReqs = spiraAppManager.canViewArtifactType(REQ_TYPE_ID);

    if (!canViewReqs) {
        var rendered = `<p class="alert alert-info">You are not able to view this data.</p>`;
        document.getElementById(elementId).innerHTML = rendered;
    }
    else {
        var projectId = spiraAppManager.projectId;
        var url = `projects/${projectId}/incidents`;
        spiraAppManager.executeApi(
            'myFirstSpiraApp', 
            '7.0',
            'GET', 
            url, 
            null, 
            loadIncidentSuccess,
            loadIncidentFailure);
    }
}

function loadIncidentSuccess(incidents) {
    let model = {
        dataItems: []
    }
    incidents = incidents.slice(0,1)

    incidents.forEach(incident => {
        var creationDate = '';
        var creationDateTime = '';
        if (incident.CreationDate) {
            creationDate = spiraAppManager.formatDate(incident.CreationDate);
            creationDateTime = spiraAppManager.formatDateTime(incident.CreationDate);
        }
        var item = {
            incId: incident.IncidentId,
            incUrl: `${spiraAppManager.baseUrl}${spiraAppManager.projectId}/Incident/${incident.IncidentId}.aspx`,
            icon: `${spiraAppManager.baseThemeUrl}Images/artifact-Incident.svg`,
            name: incident.Name,
            type: incident.IncidentTypeName,
            creator: incident.OpenerName,
            date: creationDate,
            datetime: creationDateTime
        };
        model.dataItems.push(item);
    })

    model.hasItems = model.dataItems.length ? true : false;

    var rendered = Mustache.render(template, model);
    document.getElementById(elementId).innerHTML = rendered;
}

function loadIncidentFailure(status, error) {
    spiraAppManager.displayErrorMessage(`Latest Incident widget: ${status} - ${error}`);
}
```

## Adding a Button to Requirement Details Page

Next we're going to add a button that goes to an arbitrary link given in product settings to the requirement details page.
First, let's add the product setting to our manifest.yaml, as another item under the "productSettings:" key:

``` yaml
# other settings are right above this line!
  - settingTypeId: 1
    name: quickLink
    caption: Quick Link
    position: 3
    placeholder: https://www.inflectra.com/
```

Then we need to add the button to the requirement details page with a new "menu:" entry at the bottom of our manifest. As mentioned in the SpiraApps Documentation, we can use Font Awesome classes for our icons, or .svg's bundled with your app.

``` yaml
menus:
  - pageId: 9
    caption: Quick Links
    icon: fa-regular fa-globe-pointer
    isActive: true
    entries:
    - name: link
      caption: Follow Link
      tooltip: Follow the link specified in product settings
      icon: fa-regular fa-globe-pointer
      isActive: true
      actionTypeId: 2
      action: followLink
```

Finally, we add code to the bottom of requirement.js to handle the button being pressed. We check if the SpiraApp's settings exist first, because if nothing has been entered in settings the object will not be defined.

``` javascript
spiraAppManager.registerEvent_menuEntryClick(
  APP_GUID, 
  "followLink", 
  followLink
  );

function followLink() {
  if (SpiraAppSettings[APP_GUID] && SpiraAppSettings[APP_GUID].quickLink) {
    spiraAppManager.setWindowLocation(SpiraAppSettings[APP_GUID].quickLink);
  } else {
    spiraAppManager.displayErrorMessage("No quick link found in product settings");
  }
}
```

## Adding a Column to Requirement List Page

Next up on our list is adding a custom data column on the Requirement List page.

First, the entry in our manifest.yaml:

``` yaml
pageColumns:
  - pageId: 8
    name: number
    caption: Number
    template: file://requirement.html
```

Next, the html file to represent the data in each row of the column. Here we use {project_id} and {artifact_id}, which will be filled in automatically when the column is shown on the page.

``` html
<p>
  {project_id}_{artifact_id}
</p>
```

## Final Testing

Now you should look through each page where we added functionality and verify that everything is working as expected.

First we need to do our setup by filling in the SpiraApp's product settings. Write a few words in the "Words to Replace" field, a single one in "Replacement Word", and whatever link you would like in "Quick Link".


Then let's test requirements. On the Requirement List page, you should see an extra column on the right side that has the title "Number". Each entry should contain the current project id and the requirement id for each requirement in the list. 

![Number column between ID and Edit with several requirement rows](img\tutorial_column_test.png)

When you click on a requirement, you should see a message immediately appear at the top of the screen, telling you the name and description of the requirement.

Click the X to dismiss the message, and you should see the Quick Links button in the top right of the menu.

![Top menu of requirements page including Tools, Email, Subscribe, and then Quick Links](img\tutorial-requirement-button.png)

Click "Quick Links" and then "Follow Link" and you should see the page you listed in your product settings. Now go back to the requirement page and let's test the word replacement feature.  Type in a few different words in the requirement description, including some that you put in the "Words to Replace" setting. Save the requirement and you should see that some of the words have been replaced!

Then navigate to your product page and add the SpiraApp's custom widget.

![Add/Remove items screen with three highlighted items: "SpiraApp Widgets (1)" and then "Latest Incident" checkbox, and then "Add" button](img\tutorial-addwidget.png)

Then refresh the page and you should see the latest incident listed in the widget, like below.

![Widget with title "Latest Incident" containing a grid with Headers: "Name", "Type", "Created By", and "Date Created". The grid contains a single row with data: (incident icon) "Add a widget to tutorial app", "Enhancement", blank field, and "6/26/2024"](img\tutorial-widget-incident.png)

Clicking the name of the incident should bring you to it's details page, ending our test of the Tutorial SpiraApp! If you had any difficulties with this tutorial or want extra help, email us at support@inflectra.com.
