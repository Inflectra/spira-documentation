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
    - **artifactNames**: an object with artifact names localized to the end user's settings. Keys are Artifact type IDs & values are the localized names. Relevant mappings can be seen [here](./SpiraApps-Reference.md/#artifact-types)
    - **artifactTypes**: An object with the artifact names in english as keys & the artifact type IDs as the value. This is essentially the reverse of artifactNames. 
    - **requirementStatuses**: An object with the requirement statuses lookups - keys are the names of the statuses in english & the value is the Status ID. Relevant mappings can be seen [here](./SpiraApps-Reference.md/#requirement-statuses) 
    - **releaseStatuses**: An object with release status lookups - keys are the names of the release statuses in english in camelcase. Relevant mappings can be seen [here](./SpiraApps-Reference.md/#release-statuses)
    - **testCaseStatuses**: An object with test case status lookups - keys are the names of the test cases statuses in english in camelcase. Relevant mappings can be seen [here](./SpiraApps-Reference.md/#test-case-statuses)

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

=== "Parameters"
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

    //Uses JS Fetch API - returns the body of the API call already serialized to JSON or JSON Array   
    let asAPromise: Promise<ResponseBody> = spiraAppManager.executeApiAsync(
        "mySpiraApp",
        "7.0",
        "PUT",
        url,
        updatedIncidentBody
    );
    ```


## AWS Bedrock API Calls
SpiraApps can make API calls to the Amazon Web Services (AWS) Generative Artificial Intelligence (GenAI) platform known as [AWS Bedrock](https://aws.amazon.com/bedrock). Since AWS uses a proprietary authentication system called SignatureV4, we have provided a special helper method to make these API calls easier.

The **executeAwsBedrockRuntime** function call makes a REST API call to the AWS Bedrock Runtime service. It uses an AWS Access Key and Access Key Secret. The latter needs to be stored as a secure setting.

=== "Parameters"
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

=== "Available Actions"
    ??? note "**displayErrorMessage(message: string)**" 
        Shows an error message to the user 
    ??? note "**displaySuccessMessage(message: string)**" 
        Shows a success message to the user
    ??? note "**displayWarningMessage(message: string)**" 
        Shows a warning message to the user
    ??? note "**hideMessage()**" 
        Hides any currently displayed message. This is useful when a SpiraApp needs to show a message during an operation, but hide after the operation is complete. 

=== "Example Usage"

    ```js
    spiraAppManager.displayErrorMessage("The operation could not complete due to the following error: " + errorMessage);

    spiraAppManager.displaySuccessMessage("The operation completed successfully!");
    
    spiraAppManager.displayWarningMessage("The operation completed but please note the following warning: " + warningMessage);
    
    spiraAppManager.hideMessage();
    ```


## Menus
SpiraApps can create [menu entries](./SpiraApps-Overview.md/#menus) on [relevant pages](./SpiraApps-Reference.md/#pages). If a menu entry's action is to run a JavaScript function, then the SpiraApp needs to register the function to call when the menu entry is clicked. A SpiraApp cannot use the "action" field in the manifest to set the function to run because the code for the SpiraApp is in an IIFE. Therefore the SpiraApp code has to register the function on initiation.

Use the `registerEvent_menuEntryClick` function on the spiraAppManager to register the function to execute when a menu entry is clicked.

=== "Parameters"
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
There are a number of events that a SpiraApp can register against. This allows SpiraApps to take specific actions at relevant times based on the wider flow on the page. Most have no return value & do not use any returned values from the callback, unless otherwise specified. Function signatures are meant to match TypeScript type syntax.

=== "Details Pages"

    ??? note "registerEvent_dataSaved(handler: (operation: string, newId: number) => void)" 
        Registers an event handler on a details page to trigger when the main form data is saved. 

        - **handler**:
            - **operation**: Proprietary string detailing what kind of save was done - undefined for normal saves, but can be new, redirect (IN, RK only), or close when doing complex saves
            - **artifactId**: If the operation created a new artifact, it's ID is put here. Always paired with the redirect or new operation, depending on whether the artifact has a separate redirect operation.
    
    ??? note "registerEvent_loaded(handler: (dontClearMessages: boolean) => void)"
        Registers an event handler on the details page to trigger when the main form data is loaded. This will be triggered each time the data is refreshed, including switching between artifacts without a full page load.

        - **handler**:
            - **dontClearMessages**: Whether or not the page load being performed should clear any displayed errors native to Spira. Unlikely to be meaningful for a SpiraApp.
    
    ??? note "registerEvent_dataFailure(handler: (errorMessage: PluginRestException) => void)"
        Registers an event handler on the details page form manager for when data is not saved correctly. 

        - **handler**:
            - **PluginRestException**: Object containing an exceptionType & message property
    
    ??? note "registerEvent_operationReverted(handler: (statusId: number, isOpen: boolean) => void)" 
        Registers an event handler on the details page form manager for when a status change is reverted back. 

        - **handler**:
            - **statusId**: ID of the status this operation is reverting to
            - **isOpen**: Whether or not the status being reverted to is open (if supported by artifact)
    
    ??? note "registerEvent_dropdownChanged(fieldName: string, <br> handler: (oldValue: string, newValue: string) => boolean): boolean" 
        Registers an event handler on the [specified dropdown field](./SpiraApps-Reference.md/#available-field-names) for when its value changes. 

        - **fieldName**: name of the artifact field this should listen to changes on
        - **handler**: 
            - **oldValue**: the value a dropdown had selected prior to user input
            - **newValue**: the value a dropdown is changing to based on user input
            - **return**: False to reject the transition & return the dropdown to the original value
        - **return**: False if the SpiraAppManager could not find the field or otherwise was unable to mount the event listener 
    
    ??? note "registerEvent_gridLoaded(gridId: string, handler: () => void)" 
        Registers an event handler to trigger when a [specific grid](./SpiraApps-Reference.md#available-grid-ids) is loaded. A grid is loaded on page load, refresh, after a cancelled edit, and after a successful grid update/edit.

        - **gridId**: [ID of the relevant grid](./SpiraApps-Reference.md#available-grid-ids)
        - **handler**: Callback for doing any setup which requires a grid on a details page to be loaded 
    
    ??? note "registerEvent_dataPreSave(handler: (operation: string) => void)" 
        Registers an event handler on a details page to trigger after a user has started a save operation, but before the save is submitted to the database. 

        - **handler**:
            - **operation**: Proprietary string detailing what kind of save was done - undefined for normal saves, but can be new, redirect (IN, RK only, for new artifact creation), or close when doing complex saves

=== "All Pages"
    ??? note "registerEvent_windowLoad(handler: () => void)" 
        Registers an event handler to run on full page load (e.g. to load a dashboard widget on page load). Note that while the page may be fully loaded, some data or logic on the page may still be processing or loading.

        - **handler**: Callback to perform any setup for the SpiraApp that requires window load, such as mounting other events or interacting with the page

=== "Dashboards"
    ??? note "registerEvent_dashboardUpdated(handler: () => void)" 
        Registers an event handler on dashboard pages with a release dropdown when it is changed. This can be useful when a user changes the release on the product dashboard or product reporting page.

        - **handler**: Callback to perform actions or update a SpiraApp widget based on the newly applied release filter. The new releaseId will need to be retrieved separately - not passed as an argument.

=== "Examples"

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
            //arbitrarily block any attempts to select a value with an ID above 20
            //Would be more useful to pull some configuration from a product setting related to these behaviors, but this example is simple
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
The helper function `createComboDialog` creates a modal dialog box where users can choose a value from a dropdown list, and then trigger an action in a SpiraApp based off that choice.

=== "Parameters"

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


## User Permission Checks
The SpiraAppManager provides a number of helpers to let SpiraApps better understand the current context of the user. Some of these have been discussed above. The following functions provide checks that can be useful in building up a SpiraApp's logic.

=== "Available Checks"
    ??? note "canViewArtifactType(artifactTypeId: number)" 
        Returns true if the current user can **view** the specified [artifact type](./SpiraApps-Reference.md/#artifact-types) for the current product.

        - **artifactTypeId**: ID of the artifact type we want to check permissions for 

    ??? note "canCreateArtifactType(artifactTypeId: number)"
        Returns true if the current user can **create** the specified [artifact type](./SpiraApps-Reference.md/#artifact-types) for the current product. 
        
        - **artifactTypeId**: ID of the artifact type we want to check permissions for 
    ??? note "canModifyArtifactType(artifactTypeId: number)" 
        Returns true if the current user can **modify** the specified [artifact type](./SpiraApps-Reference.md/#artifact-types) for the current product. 

        - **artifactTypeId**: ID of the artifact type we want to check permissions for 

=== "Example"

    ```js
    spiraAppManager.canViewArtifactType(1); // returns true if the user can view requirements in this product

    spiraAppManager.canCreateArtifactType(2); // returns true if the user can create test cases in this product

    spiraAppManager.canModifyArtifactType(3); // returns true if the user can modify incidents in this product
    ```

## Format Helpers

=== "Explanation"
    ??? note "formatDate(isoDate: string)" 
        Formats an ISO 8601 datetime into a user friendly date format/timezone based on the user's cultural settings in Spira.

        - **isoDate**: String of a date in ISO 8601 format (how Spira provides it from the server)
    ??? note "formatDateTime(isoDate: string)" 
        Formats an ISO datetime into a user friendly datetime format/timezone based on the user's cultural settings in Spira.

        - **isoDate**: String of a date in ISO 8601 format (how Spira provides it from the server)
    ??? note "formatCustomFieldName(propertyNumber: number)" 
        Returns the custom property field name in the form `Custom_01` for a passed in property number

        - **propertyNumber**: Field # of the custom property we want the field name of (for [getDataItemField & updateFormField functions](./SpiraApps-Manager.md/#page-actions))
    ??? note "convertHtmlToPlainText(htmlTemplate: string)" 
        Returns a plain text string for a passed in HTML string (all tags and relevant syntax is removed)
    
        - **htmlTemplate**: Template string of some HTML to remove markup from. Useful for grabbing information from descriptions or rich text custom properties.
    ??? note "sanitizeHtml(htmlToSanitize: string)"
        Returns a safe to use and display string based on a provided string. Any SpiraApp that displays rich text should always pass the text through this function before displaying to the user to avoid XSS risks 

        - **htmlToSanitize**: String of HTML which is going to be rendered to the DOM from user input, such as in a dashboard widget rendering the description of an artifact

=== "Example"

    ```js
    spiraAppManager.formatDate("1993-05-16T14:48:00.000Z"); // returns "5/16/1993" if the user's culture is en-US

    spiraAppManager.formatDateTime("1993-05-16T14:48:00.000Z"); // returns "5/16/1993 10:48:00 AM" if the user's culture is en-US

    spiraAppManager.formatCustomFieldName(5); // returns "Custom_07"

    spiraAppManager.convertHtmlToPlainText("<p>Hello World</p>"); // returns "Hello World"

    spiraAppManager.sanitizeHtml("<image/src/onerror=prompt(8)>"); // returns "&lt;image/src/onerror=prompt(8)&gt" 
    ```

## Local Storage
Local storage is a way to store semi-persistent data in the user's browser. SpiraApps have access to a single storage location with data stored as a string. The storage can be retrieved, updated, or deleted. The storage is accessed via helper functions that use a string provided by a SpiraApp.
Do not use this for storing secure information.

=== "Explanation"
    ??? note "getLocalData(storageKey: string) => string" 
        Retrieves the local storage object for this user, on this browser, for this SpiraApp. 

        - **storageKey**: Key to store the data in. Must contain the APP_GUID for key uniqueness.
        - **returns**: The data as a string, stored at that key, if any
    
    ??? note "setLocalData(storageKey: string, data: any)" 
        Sets or updates the local storage entry for this app guid. Takes the app guid (string) as the first parameter, and data to be put in localStorage as the second parameter (string).
    
        - **storageKey**: Key the data is stored in. Must contain the APP_GUID for key uniqueness.
        - **data**: Any data, as per localStorage restrictions. This data will be saved as a string. Complex types like objects will have .ToString called on them by the localStorage API, likely resulting in unintended outcomes. 
    
    ??? note "removeLocalData(storageKey: string)"
        Deletes the information stored in a given key. 

        - **storageKey**: Key to remove from localStorage. Must contain the APP_GUID for key uniqueness.

=== "Best Practices"
    Always use your APP_GUID as a prefix / suffix of the local storage keys your SpiraApp uses to avoid conflicts with other SpiraApps. Define these keys as constants at the top of the JS file. 
    
    Your SpiraApp will likely not be distributed by Inflectra if you fail to follow this rule, since it puts localStorage based functionality of Spira & other SpiraApps at risk.

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


