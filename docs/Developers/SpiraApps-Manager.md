The spiraAppManager is a helper class that provides a wide range of useful functions and operations to SpiraApps.

## IDs
The following ID fields are available from the spiraAppManager. They are useful for making internal API calls

=== "Explanation"
    - **userId**: returns the ID of the current user (integer)
    - **projectId**: returns the ID of the current product (integer)
    - **projectTemplateId**: returns the ID of the product template for the current product (integer)
    - **artifactId**: returns the ID of the current artifact (integer). Note that this will be correctly populated on details pages only, and not when creating new incidents or risks
    - **displayReleaseId**: returns the ID of the release being displayed (integer). This is used on product and reporting home pages - otherwise it is an empty string.
   
=== "Example"

    ```js
    const userId = spiraAppManager.userId; // e.g. 5

    const projectId = spiraAppManager.projectId; // e.g. 16

    const projectTemplateId = spiraAppManager.projectTemplateId; // e.g. 93

    const artifactId = spiraAppManager.artifactId; // e.g. 6

    const displayReleaseId = spiraAppManager.displayReleaseId; // e.g. 13
    ```

## Properties
The following properties are available from the spiraAppManager. They are useful for displaying UI to users, or controlling UX logic. 

=== "Explanation"
    - **myPageIsFilterByProject**: returns true if the current page is the My Page and the user is viewing the current product only (not all products). Otherwise it returns false (boolean)
    - **baseUrl**: returns the base url of the Spira instance (string). This can be used to programmatically generate internal URLs to an artifact or page
    - **baseThemeUrl**: returns the base theme url for the Spira instance (string). This can be used to retrieve and display SVG assets such as artifact icons
    - **currentUtcOffset**: returns the user's offset from UTC (string)
    - **currentCulture**: returns the name of the user's chosen culture setting (string)
    - **productType**: returns the product type installed (string). The value will be one of "SpiraTest", "SpiraTeam", or "SpiraPlan".
    - **gridIds**: returns an object with keys for names of each relevant grid, and values for their matching ID (object). This is useful if the SpiraApp needs to interact with a grid (for instance to refresh its data). Available grid values are shown [here](./SpiraApps-Reference.md/#available-grid-ids)

=== "Example"

    ```js
    const isCurrentProduct = spiraAppManager.myPageIsFilterByProject; // e.g true
    
    const riskDetailsPage = spiraAppManager.baseUrl + 
        spiraAppManager.projectId + 
        "/Risk/" + 
        spiraAppManager.artifactId + ".aspx"; 
        // e.g. "/1/Risk/2.aspx"

    const riskIcon = spiraAppManager.baseThemeUrl + "Images/artifact-Risk.svg"; // e.g. "/App_Themes/InflectraTheme/Images/artifact-Risk.svg"

    const utcOffset = spiraAppManager.currentUtcOffset; // e.g. "-05:00"

    const culture = spiraAppManager.currentCulture; // e.g. "en-US"

    const isSpiraPlan = spiraAppManager.productType == "SpiraPlan"; // e.g. true

    const stepsGridId = spiraAppManager.gridIds().requirementSteps; // e.g. "cplMainContent_grdScenarioSteps" 
    ```

## External REST calls
To make REST calls to an external service, SpiraApps should always use the spiraAppManager helper functions. The manager makes the REST call server side, avoiding any potential CORS problems and improving security for SpiraApps and end users.

The **executeRest** function call takes a large set of parameters to fully prepare the API call. This includes callback functions for success and failure of the API call.

=== "Explanation"
    - **appGuid**: the APP_GUID of the SpiraApp used to access system settings like authentication tokens (string)
    - **appName**: the name of the SpiraApp used for logging purposes only (string)
    - **method**: the verb to use for this call, with accepted values being "POST" (default), "GET", "PUT", "DELETE", "PATCH", "OPTIONS", or "MERGE" (string)
    - **url**: the full URL of the API call - tokens may be used (string)
    - **body**: body object as a string to pass with the call - tokens may be used (optional string)
    - **credentials**: (PluginCredentials object in the form of {userName: VALUE, password: VALUE }) 
    - **headers**: any additional headers required for the API call (object in the form of {keyName1: value1, keyName2: value2})
    - **successCallback**: callback function to execute on success
    - **errorCallback**: callback function to execute on failure

    Often the REST call will need a mix of data from the client and data stored in settings of the SpiraApp. Tokens can be used in the URL or body strings. These will then be replaced by any system or product settings. To add a token to the URL or body, by providing the setting name wrapped in { }. For example, `{settingApiKey}`. Make sure the SpiraApp does not use a token for a setting name that exists in both system settings and product settings - in this case the system setting will take precedence.

=== "Example"

    ```js hl_lines="16-26" linenums="1" title="myApp.js > executeRest"
    const url = "{settingBaseUrl}/myData";
    const credentials = {
        userName: "{settingUserName}",
        password: "{settingPassword}"
    };
    const headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    };
    function dataRetrieve_Success (response) { ... }
    function dataRetrieve_Failure (response) { ... }

    /* spiraAppManager.executeRest(
        appGuid, appName, method, url, body, credentials, headers, successCallback, errorCallback
    );*/
    spiraAppManager.executeRest(
        APP_GUID,
        "mySpiraApp",
        "GET",
        url,
        "",
        credentials,
        headers,
        dataRetrieve_Success,
        dataRetrieve_Failure
    );
    ```

## Internal API calls
SpiraApps are able to make API calls to Spira on behalf of the current user, to allow rich and powerful automation. Authentication of the user, including their permissions and other security checks are handled by the spiraAppManager. This makes it very easy to safely perform actions, but the SpiraApp will need to correctly handle any errors.

Note that this function is carried out client side so it does have access to any system settings.

=== "Explanation"
    - **pluginName**: name of the plugin - not currently used (string)
    - **apiVersion**: override the default API version number used (currently v6) if required (string, in the form of "6.0")
    - **method**: an allowed HTTP method (string)
    - **url**: the relative URL endpoint for the API call - the portion of the URL path from the version number(string)
    - **body**: body object as a string to pass with the call (optional string)
    - **successFunction**: callback function to execute on success
    - **errorFunction**: callback function to execute on failure

=== "Example"

    ```js hl_lines="9-17" linenums="1" title="myApp.js > executeApi"
    const updatedIncidentBody = JSON.stringify(updatedIncidentObject);
    const url = `projects/${spiraAppManager.projectId}/incidents/${spiraAppManager.artifactId}`;
    function incidentRetrieve_Success (response) { ... }
    function incidentRetrieve_Failure (response) { ... }

    /*spiraAppManager.executeApi(
        pluginName, apiVersion, method, url, body, successFunction, errorFunction
    );*/
    spiraAppManager.executeApi(
        "mySpiraApp",
        "7.0",
        "PUT",
        url,
        updatedIncidentBody,
        incidentRetrieve_Success,
        incidentRetrieve_Failure
    );
    ```


## AWS Bedrock API Calls
SpiraApps can make API calls to the Amazon Web Services (AWS) Generative Artificial Intelligence (GenAI) platform known as [AWS Bedrock](https://aws.amazon.com/bedrock). Since AWS uses a proprietary authentication system called SignatureV4, we have provided a special helper method to make these API calls easier.

The **executeAwsBedrockRuntime** function call makes a REST API call to the AWS Bedrock Runtime service. It uses an AWS Access Key and Access Key Secret. The latter needs to be stored as a secure setting.

=== "Explanation"
    - **appGuid**: the APP_GUID of the SpiraApp used to access system settings like authentication tokens (string)
    - **appName**: the name of the SpiraApp used for logging purposes only (string)
    - **accessKeyId**: the value of the AWS Access Key that should be used to make the API call (string)
    - **secretAccessKeySetting**: the name of the secure SpiraApp setting that is used to store the AWS Access Key Secret (string)
    - **region**: The name of the AWS region that should be used, if not provided, the API call will use `us-east-1` (optional string)
    - **model**: The name of the AWS Bedrock LLM model to use (string) 
    - **body**: The JSON body to be sent to the LLM model, serialized as a string (string)
    - **successCallback**: callback function to execute on success
    - **errorCallback**: callback function to execute on failure

=== "Example"

    ```js hl_lines="16-26" linenums="1" title="myApp.js > executeAwsBedrockRuntime"
    const accessKey = '...';
    const region = 'us-east-1';
    const model = 'anthropic.claude-3-haiku-20240307-v1:0';

    var body = {
        ...
    };

    function dataRetrieve_Success (response) { ... }
    function dataRetrieve_Failure (response) { ... }

    /* spiraAppManager.executeAwsBedrockRuntime(
        appGuid, appName, accessKeyId, secretAccessKeySetting, region, model, body, successCallback, errorCallback
    );*/
    spiraAppManager.executeAwsBedrockRuntime(
        APP_GUID,
        "mySpiraApp",
        accessKey,
        'access_key_secret',
        region,
        model,
        JSON.stringify(body),
        modelInvoke_Success,
        modelInvoke_Failure
    );
    ```

## Notifications
SpiraApps can show and hide messages to the user to provide them with information about the success or failure of actions taken by the SpiraApp. The different message types show different visual cues to the user. The messages are all displayed as a modal message

=== "Explanation"
    - **displayErrorMessage**: shows an error message to the user, accepting a single string from the SpiraApp
    - **displaySuccessMessage**: shows a success message to the user, accepting a single string from the SpiraApp
    - **displayWarningMessage**: shows a warning to the user, accepting a single string from the SpiraApp
    - **hideMessage**: hides the message, if any. This is useful when a SpiraApp needs to show a message during an operation, but hide after the operation is complete

=== "Example"

    ```js
    spiraAppManager.displayErrorMessage("The operation could not complete due to the following error: " + errorMessage);

    spiraAppManager.displaySuccessMessage("The operation completed successfully!");
    
    spiraAppManager.displayWarningMessage("The operation completed but please note the following warning: " + warningMessage);
    
    spiraAppManager.hideMessage();
    ```


## Menus
SpiraApps can create [menu entries](./SpiraApps-Overview.md/#menus) on [relevant pages](./SpiraApps-Reference.md/#pages). If a menu entry's action is to run a JavaScript function, then the SpiraApp needs to register the function to call when the menu entry is clicked. A SpiraApp cannot use the "action" field in the manifest to set the function to run because the code for the SpiraApp is in an IIFE. Therefore the SpiraApp code has to register the function on initiation.

Use the `registerEvent_menuEntryClick` function on the spiraAppManager to register the function to execute when a menu entry is clicked.

=== "Explanation"
    - **appGuid**: the guid of the SpiraApp as stored in APP_GUID (string)
    - **menuEntry**: the exact "name" property as set in the manifest for the specific menu entry(string, case-sensitive)
    - **handler**: function to execute

=== "Example"

    ```js hl_lines="4-8" linenums="1" title="myApp.js > registerEvent_menuEntryClick"
    function firstMenu_Click() { ... };

    //spiraAppManager.registerEvent_menuEntryClick(appGuid, menuEntry, handler)
    spiraAppManager.registerEvent_menuEntryClick(
        APP_GUID, 
        "myFirstMenuEntry", 
        firstMenu_Click
        );
    ```

## Events handlers
There are a number of events that a SpiraApp can register against. This allows SpiraApps to take specific actions at relevant times based on the wider flow on the page.

=== "Explanation"
    - **registerEvent_windowLoad**: registers an event handler to run on full page load (e.g. to load a dashboard widget on page load). Note that while the page may be fully loaded, some data or logic on the page may still be processing or loading.
    - **registerEvent_dashboardUpdated**: registers an event handler on dashboard pages when the release dropdown is changed. This can be useful when a user changes the release on the product dashboard.

    **Details page events**:

    - **registerEvent_dataSaved**: registers an event handler on a details page to trigger when the main form data is saved. When the handler is called, an operation and artifactId parameters are passed into the handler
    - **registerEvent_loaded**: registers an event handler on the details page to trigger when the main form data is loaded. When the handler is called, a boolean is provided back to the SpiraApp as a parameter, which should be ignored (internal use only). Note that this will be triggered each time the data is refreshed, including switching between artifacts without a full page load
    - **registerEvent_dataFailure**: registers an event handler on the details page form manager for when data is not saved correctly. Receives an exception message from Spira - this may be useful to help a SpiraApp debug, but should not be presented to the user.
    - **registerEvent_operationReverted**: Registers an event handler on the details page form manager for when a status change is reverted back. When the handler is called, the current status id and a boolean on if it is an open status (where relevant) are provided as parameters
    - **registerEvent_dropdownChanged**: Registers an event handler on the [specified dropdown field](./SpiraApps-Reference.md/#available-field-names) for when its value changes. When the handler is called, the old and new values are provided (as ints). The handler can block the update by returning false or an error. Note that on first registering the handler, this function returns true if the handler was registered, and false if the handler could not be registered.  
    - **registerEvent_gridLoaded**: registers an event handler to trigger when a [specific grid](./SpiraApps-Reference.md#available-grid-ids) is loaded. A grid is loaded on page load, refresh, after a cancelled edit, and after a successful grid update/edit.
    - **registerEvent_dataPreSave**: Registers an event handler on a details page to trigger after a user has started a save operation, but before the save is submitted to the database. 


=== "Example"

    ```js
    spiraAppManager.registerEvent_windowLoad(runOnWindowLoad);

    spiraAppManager.registerEvent_dashboardUpdated(runOnDashboardUpdate);

    spiraAppManager.registerEvent_dataSaved(runOnDataSaved);
    function runOnDataSaved(operation, artifactId) {
        console.log(`The ID of the artifact we are looking at is ${artifactId}`);
    };
    
    spiraAppManager.registerEvent_loaded(runOnLoaded);

    spiraAppManager.registerEvent_dataFailure(runOnDataFailure);
    function runOnDataFailure(exception) {
        console.log(`The SpiraApp cannot proceed because Spira had this problem: ${exception}`);
    };

    spiraAppManager.registerEvent_operationReverted(runOnStatusReverted);
    function runOnStatusReverted(statusId, isOpen) {
        console.log(`Current status is ${statusId} and it is ${isOpen ? "open" : "closed"}`);
    };

    spiraAppManager.registerEvent_dropdownChanged("PriorityId", runOnDropdownChange);
    function runOnDropdownChange (oldValue, newValue) {
        if (newValue > 20) {
            //arbitrarily block any attempts to set a value to above 20
            return false;
        }
    };

    spiraAppManager.registerEvent_gridLoaded(spiraAppManager.gridIds.requirementSteps, runOnGridLoaded);
    function runOnGridLoaded() {
        console.log(`The grid with id ${spiraAppManager.gridIds.requirementSteps} was (re)loaded`);
    };

    spiraAppManager.registerEvent_dataPreSave(populateDefaultEffortForNewIncidents); 
    function populateDefaultEffortForNewIncidents() {
        let incidentId = spiraAppManager.getDataItemField("IncidentId");
        let estimatedEffort = spiraAppManager.getDataItemField("EstimatedEffort");
    
        //if there is no incident id (new incident) and no estimated effort, add a default value
        if (!estimatedEffort && !incidentId) { 
            spiraAppManager.updateFormField("EstimatedEffort", null, 120);
        }
    };
    ```

## Page actions
A SpiraApp can make requests to Spira to perform certain actions on certain pages.

=== "Available Actions"
    ??? note "**reloadForm()**"
        Reloads the current main overview on a details page. 
        
        Note that doing this may interrupt a user interaction so use this with caution. It is very helpful to do if the SpiraApp updates an artifact immediately after a user saves the artifact.
    ??? note "**getDataItemField(fieldName: string, dataProperty?: string)**"
        Retrieves a single field of the currently viewed artifact on a details page. 

        - **fieldName**: The [name of a field](./SpiraApps-Reference.md/#available-field-names) of an artifact
        - **dataProperty**: The [data property](./SpiraApps-Reference.md/#available-data-properties) containing the type of information you want
    ??? note "**updateFormField(fieldName: string, dataProperty?: string, newValue: any)**" 
        Updates a field on an artifact details page.
        
        - **fieldName**: The [name of the field](./SpiraApps-Reference.md/#available-field-names) of an artifact
        - **dataProperty**: The [data property](./SpiraApps-Reference.md/#available-data-properties) containing the piece of information about this field you want to modify
        - **newValue**: The new value to set the data property to on the given field.
    ??? note "**reloadGrid(gridId: SpiraAppManager.gridIds)**" 
        Refreshes the specified grid if it exists on the page. 
        
        - **gridId**: The ID of the grid to reload (must be from the spiraAppManager.gridIds function). [Available grid ID keys](./SpiraApps-Reference.md/#available-grid-ids)
    ??? note "**setWindowLocation(URL: string)**" 
        Loads a new page in the browser.

        - **URL**: URL to navigate the user's browser to 

=== "Example Usage"

    ```js
    spiraAppManager.reloadForm();

    spiraAppManager.getDataItemField("Name", "textValue"); // returns "Fix the icon used to save"
    spiraAppManager.updateFormField("Name", "textValue", "MySpiraApp has changed the name of this task");

    spiraAppManager.reloadGrid(spiraAppManager.gridIds().requirementSteps); // Refreshes the requirement steps grid on requirement details pages

    spiraAppManager.setWindowLocation("https://inflectra.com");
    ```


## UX generator
### Dropdown list dialog
This helper function handles the creation of a UX control that allows users to interact with it freely. It creates a modal dialog box where users can choose a value from a dropdown list, and then trigger an action in a SpiraApp based off that choice.

=== "Explanation"
    The `createComboDialog` function takes the following parameters:

    - **title**: the title of the dialog (string)
    - **introText**: the introductory text, to explain to the user what to do and why (string)
    - **button**: the text to use for the OK button (string)
    - **entries**: the entries in the dropdown list (array of strings)
    - **successCallback**: callback function for when they user clicks the OK button. This function receives the selected dropdown item as its parameter.

=== "Example"

    ```js hl_lines="15-21" linenums="1"
    // provide a list of entries to show in the dropdown
    const dropdownEntries = [
        "alpha",
        "bravo",
        "charlie",
        "delta"
    ];
    // show the user the option they selected to validate our code
    function showChosenOption(chosenOption) {
        spiraAppManager.displaySuccessMessage(`You choose: ${chosenOption}`);
    }

    // this example code will run on first load
    // in reality it should be tied to a user action like a menu click
    spiraAppManager.createComboDialog(
        "MySpiraApp Dropdown",
        "Please choose one of the options from the dropdown".
        "Choose!",
        dropdownEntries,
        showChosenOption
    );
    ```


## Logic helpers
The SpiraAppManager provides a number of helpers to let SpiraApps better understand the current context of the user. Some of these have been discussed above. The following functions provide checks that can be useful in building up a SpiraApp's logic.

=== "Explanation"
    - **canViewArtifactType**: returns true if the current user can **view** the specified [artifact type](./SpiraApps-Reference.md/#artifact-types) for the current product. Takes the artifact type ID as the parameter (integer)
    - **canCreateArtifactType**: returns true if the current user can **create** the specified [artifact type](./SpiraApps-Reference.md/#artifact-types) for the current product. Takes the artifact type ID as the parameter (integer)
    - **canModifyArtifactType**: returns true if the current user can **modify** the specified [artifact type](./SpiraApps-Reference.md/#artifact-types) for the current product. Takes the artifact type ID as the parameter (integer). Note that this does not check if the actual artifact ID itself can be modified (only if they can ever modify the artifact, including limited view)

=== "Example"

    ```js
    spiraAppManager.canViewArtifactType(1); // returns true if the user can view requirements in this product

    spiraAppManager.canCreateArtifactType(2); // returns true if the user can create test cases in this product

    spiraAppManager.canModifyArtifactType(3); // returns true if the user can modify incidents in this product
    ```

## Format Helpers

=== "Explanation"
    - **formatDate**: formats an ISO datetime into the correct date format/timezone based on the user's cultural settings in Spira. Takes a datetime item as its parameter
    - **formatDateTime**: formats an ISO datetime into the correct datetime format/timezone based on the user's cultural settings in Spira. Takes a datetime item as its parameter
    - **formatCustomFieldName**: returns the custom property field name in the form `Custom_01`  for a passed in integer
    - **convertHtmlToPlainText**: returns a plain text string for a passed in HTML string (all tags and relevant syntax is removed)
    - **sanitizeHtml**: returns a safe to use and display string based on a provided string. Any SpiraApp that displays rich text should always pass the text through this function before displaying to the user to avoid XSS risks 

=== "Example"

    ```js
    spiraAppManager.formatDate("1993-05-16T14:48:00.000Z"); // returns "5/16/1993" if the user's culture is en-US

    spiraAppManager.formatDateTime("1993-05-16T14:48:00.000Z"); // returns "5/16/1993 10:48:00 AM" if the user's culture is en-US

    spiraAppManager.formatCustomFieldName(5); // returns "Custom_07"

    spiraAppManager.convertHtmlToPlainText("<p>Hello World</p>"); // returns "Hello World"

    spiraAppManager.sanitizeHtml("<image/src/onerror=prompt(8)>"); // returns "&lt;image/src/onerror=prompt(8)&gt" 
    ```

## Local Storage
Local storage is a way to store semi-persistent data in the user's browser. SpiraApps have access to a single storage location with data stored as a string. The storage can be retrieved, updated, or deleted. The storage is accessed via helper functions that use the SpiraApp guid.

=== "Explanation"
    - **getLocalData**: retrieve the local storage object for this user, on this browser, for this SpiraApp. Takes the app guid as its parameter (string)
    - **setLocalData**: sets or updates the local storage. Takes the app guid (string) as the first parameter, and a string for the data to be set as the second parameter (string).
    - **removeLocalData**: deletes all local storage for this user, in this browser, for this SpiraApp. Takes the app guid as its parameter (string)

=== "Example"

    ```js linenums="1"
    // use a single object to store all the settings in memory
    let storageData = { /* arbitrary data here */  };

    // convert the object to a string before setting it into local storage
    spiraAppManager.setLocalData(APP_GUID,JSON.stringify(storageData));

    // retrieve the data - do not forget to parse it back into JSON if needed
    storageData = JSON.parse(spiraAppManager.getLocalData(APP_GUID));

    // to update the storage, update the object in memory, then stringify it, and set it on local storage
    spiraAppManager.setLocalData(APP_GUID,JSON.stringify(storageData));

    // finally, fully remove the data
    spiraAppManager.removeLocalData(APP_GUID);
    ```


