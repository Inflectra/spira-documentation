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
Spira provides a number of resources that SpiraApps can use to provide rich, powerful, and seamless user experiences. These are designed to provide developers a comprehensive and developer-friendly toolset to create SpiraApps that can (and should) feel like native Spira features.

### Third party libraries
The following third party libraries and tools are available to SpiraApps

- React v16.14
- Mustache
- FontAwesome 6 pro: available as embedded fonts referenced [using css styles](https://docs.fontawesome.com/web/add-icons/how-to#add-icons-to-html) 

### Inflectra libraries
- Inflectra CSS utility library
- Spira theming variables for light and dark mode

## SpiraApp helper class
- SpiraApp helper functions
- Make internal API calls to Spira
- Make external API calls
