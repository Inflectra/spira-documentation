# SpiraApps Developer Reference
This page provides reference information for multiple parts of SpiraApp development. Separate reference information about the [manifest](./SpiraApps-Manifest.md) is also available.

## Manifest Lookups
There are a number of places in the manifest file where lookups are required. The different lookups and what they relate to are listed below.

### Setting types
The following IDs are allowed for the settingTypeId property for system admin settings and product admin settings. Not all of these wil 

| ID  | Setting Type                   |
| --- | ------------------------------ |
| 1   | plain text                     |
| 2   | Rich text (html)               |
| 3   | ArtifactCustomProperty         |
| 4   | Integer                        |
| 5   | ArtifactStatusSingleSelect     |
| 6   | ArtifactStatusMultiSelect      |
| 7   | ArtifactStandardField          |
| 8   | ArtifactFlexibleCustomProperty |
| 9   | Multi line plain text          |

### Artifact Types
The list below shows the relevant IDs for different artifacts in Spira.

| ID  | Artifact Type    |
| --- | ---------------- |
| 1   | Requirement      |
| 2   | TestCase         |
| 3   | Incident         |
| 4   | Release          |
| 5   | TestRun          |
| 6   | Task             |
| 7   | TestStep         |
| 8   | TestSet          |
| 9   | AutomationHost   |
| 10  | AutomationEngine |
| 12  | RequirementStep  |
| 13  | Document         |
| 14  | Risk             |
| 15  | RiskMitigation   |

### Pages
The list below shows the relevant IDs for different pages where SpiraApps can run from. Every page below support [pageContents](./SpiraApps-Manifest.md/#page-contents) and [menus](./SpiraApps-Manifest.md/#menus), but only list pages support [columns](./SpiraApps-Manifest.md/#page-columns).

| ID  | Page               | Supports columns |
| --- | ------------------ | ---------------- |
| 1   | TestCaseList       | Y                |
| 2   | TestCaseDetails    | N                |
| 3   | TestRunList        | Y                |
| 4   | TestRunDetails     | N                |
| 5   | ReleaseDetails     | N                |
| 6   | RiskList           | Y                |
| 7   | RiskDetails        | N                |
| 8   | RequirementList    | Y                |
| 9   | RequirementDetails | N                |
| 10  | ReleaseList        | Y                |
| 11  | TestSetList        | Y                |
| 12  | TestSetDetails     | N                |
| 13  | TaskList           | Y                |
| 14  | TaskDetails        | N                |
| 15  | DocumentList       | Y                |
| 16  | DocumentDetails    | N                |

### Action Types
The list below shows the IDs for different action types.

| ID  | Page     |
| --- | -------- |
| 1   | URL      |
| 2   | Function |

### Dashboard Types
The list below shows the IDs for different dashboard pages in Spira.

| ID  | Dashboard      | Available to SpiraApps |
| --- | -------------- | ---------------------- |
| 1   | ProductHome    | Y                      |
| 2   | ProductReports | Y                      |
| 3   | MyPage         | Y                      |
| 4   | ProgramHome    | N                      |
| 5   | PortfolioHome  | N                      |
| 6   | EnterpriseHome | N                      |
| 7   | ProgramReports | N                      |


## Available resources
### Inflectra Javascript helpers
Each Javascript contents for a SpiraApp is embedded on the relevant page wrapped in an IIFE block and set to use strict. The SpiraApp code is also prepended to include access to useful constants:

- `spiraAppManager`: an instance of a helper class, described more below
- `APP_GUID`: string of the SpiraApp's guid

You can read the contents of these constants, but cannot write to them.

Additionally, if a SpiraApp has any relevant settings these are stored in the `SpiraAppSettings` object. The settings for a SpiraApp can be accessed with `SpiraAppSettings[APP_GUID]`. This will store key/values based on each relevant setting and its `name` field as specific in the manifest. Product settings are loaded onto all product specific pages. System settings are loaded onto the My Page.

### spiraAppManager
The spiraAppManager is a helper class that provides a wide range of useful functions and operations to SpiraApps.

#### spiraAppManager ids
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

#### spiraAppManager properties
The following properties are available from the spiraAppManager. They are useful for displaying UI to users, or controlling UX logic. 

=== "Explanation"
    - **myPageIsFilterByProject**: returns true if the current page is the My Page and the user is viewing the current product only (not all products). Otherwise it returns false (boolean)
    - **baseUrl**: returns the base url of the Spira instance (string). This can be used to programmatically generate internal URLs to an artifact or page
    - **baseThemeUrl**: returns the base theme url for the Spira instance (string). This can be used to retrieve and display SVG assets such as artifact icons
    - **currentUtcOffset**: returns the user's offset from UTC (string)
    - **currentCulture**: returns the name of the user's chosen culture setting (string)
    - **productType**: returns the product type installed (string). The value will be one of "SpiraTest", "SpiraTeam", or "SpiraPlan".
    - **gridIds**: returns an object with keys for names of each relevant grid, and values for their matching ID (object). This is useful if the SpiraApp needs to interact with a grid (for instance to refresh its data). Available grid values are:

        - requirementSteps

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

    const stepsGridId = spiraAppManager.gridIds.requirementSteps; // e.g. "cplMainContent_grdScenarioSteps" 
    ```

#### spiraAppManager external REST calls
=== "Explanation"
executeRest
executeRest_success
executeRest_failure

=== "Example"

#### spiraAppManager internal REST calls
=== "Explanation"
executeApi

=== "Example"


#### spiraAppManager notification handlers
=== "Explanation"
displayErrorMessage
displaySuccessMessage
displayWarningMessage
hideMessage

=== "Example"


#### spiraAppManager menu handlers
=== "Explanation"
registerEvent_menuEntryClick

=== "Example"


#### spiraAppManager events listeners
=== "Explanation"
registerEvent_windowLoad
registerEvent_dataSaved
registerEvent_loaded
registerEvent_dataFailure
registerEvent_operationReverted
registerEvent_dashboardUpdated

=== "Example"


#### spiraAppManager page actions
=== "Explanation"
reloadForm
updateFormField
getDataItemField
reloadGrid
setWindowLocation

=== "Example"



#### spiraAppManager UX generator
=== "Explanation"
createComboDialog

=== "Example"



#### spiraAppManager logic helpers
=== "Explanation"
canViewArtifactType
canCreateArtifactType
canModifyArtifactType

=== "Example"



#### spiraAppManager format helpers
=== "Explanation"
formatDate
formatDateTime
formatCustomFieldName

=== "Example"


#### spiraAppManager localStorage
=== "Explanation"
getLocalData
setLocalData
removeLocalData

=== "Example"



### Third party Javascript libraries
The following third party Javascript libraries and tools are available to SpiraApps:

- React v16.14
- Mustache

Spira provides a number of resources that SpiraApps can use to provide rich, powerful, and seamless user experiences. These are designed to provide developers a comprehensive and developer-friendly toolset to create SpiraApps that can (and should) feel like native Spira features.

### Inflectra CSS helpers
HTML elements added to the page for a SpiraApp (like a menu or widget) is wrapped in a containing div that has the guid of the SpiraApp as a property. Any CSS added onto the page for the SpiraApp is nested with this same property on the page. This means the SpiraApp CSS cannot change any CSS elsewhere on the page

The following CSS libraries and properties are available to SpiraApps:

- Inflectra CSS utility library
- Spira theming variables for light and dark mode
- theme images 

### Third party CSS libraries
The following third party CSS libraries are available to SpiraApps:

- FontAwesome 6 pro: available as embedded fonts referenced [using css styles](https://docs.fontawesome.com/web/add-icons/how-to#add-icons-to-html) 


