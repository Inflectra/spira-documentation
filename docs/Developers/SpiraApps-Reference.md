# SpiraApps Developer Reference
This page provides reference information for multiple parts of SpiraApp development. Separate reference information about the [manifest](./SpiraApps-Manifest.md) is also available.

## Manifest Lookups
There are a number of places in the manifest file where lookups are required. The different lookups and what they relate to are listed below.

### Setting types
The following IDs are allowed for the settingTypeId property for system admin settings and product admin settings. Not all of these are currently supported, and some are not available in system settings.

| ID  | Setting Type                   | Product Settings | System Settings |
| --- | ------------------------------ | ---------------- | --------------- |
| 1   | Plain text                     | Y                | Y               |
| 2   | Rich text (html)               | Y                | Y               |
| 3   | ArtifactCustomProperty         | Y                |                 |
| 4   | Integer                        | Y                | Y               |
| 5   | ArtifactStatusSingleSelect     | Y                |                 |
| 6   | ArtifactStatusMultiSelect      |                  |                 |
| 7   | ArtifactStandardField          | Y                |                 |
| 8   | ArtifactFlexibleCustomProperty |                  |                 |
| 9   | Multi line plain text          | Y                | Y               |
| 10  | Boolean                        | Y                | Y               |

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

| ID  | Page                  | Supports columns |
| --- | --------------------- | ---------------- |
| 1   | TestCaseList          | Y                |
| 2   | TestCaseDetails       | N                |
| 3   | TestRunList           | Y                |
| 4   | TestRunDetails        | N                |
| 5   | ReleaseDetails        | N                |
| 6   | RiskList              | Y                |
| 7   | RiskDetails           | N                |
| 8   | RequirementList       | Y                |
| 9   | RequirementDetails    | N                |
| 10  | ReleaseList           | Y                |
| 11  | TestSetList           | Y                |
| 12  | TestSetDetails        | N                |
| 13  | TaskList              | Y                |
| 14  | TaskDetails           | N                |
| 15  | DocumentList          | Y                |
| 16  | DocumentDetails       | N                |
| 17  | AutomationHostList    | Y                |
| 18  | AutomationHostDetails | N                |
| 19  | IncidentList          | Y                |
| 20  | IncidentDetails       | N                |

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

## SpiraApp Manager Lookups
### Available Grid IDs
The following gridIDs are available when calling the `spiraAppManager.gridIds` [function](./SpiraApps-Manager.md/#properties).

- requirementSteps
- riskMitigations
- testCaseTestSteps

### Available Field Names
The following field names are available when calling various [page functions](./SpiraApps-Manager.md/#page-actions) related to artifact details pages like getDataItemField or updateFormField. 

=== "Automation Hosts"
    - AutomationHostId
    - Custom_01...Custom_99
    - Description
    - IsActive
    - LastUpdateDate
    - Name
    - Token
    
=== "Documents"
    - AttachmentId
    - AuthorId
    - CurrentVersion
    - Custom_01...Custom_99
    - Description
    - DocumentStatusId
    - DocumentTypeId
    - DocumentVersions
    - EditedDate
    - EditorId
    - Filename
    - Filetype
    - ProjectAttachmentFolderId
    - Size
    - Tags
    - UploadDate

=== "Incidents"
    - ActualEffort
    - BuildId
    - ClosedDate
    - CompletionPercent
    - ComponentIds
    - CreationDate
    - Custom_01...Custom_99
    - Description
    - DetectedReleaseId
    - EstimatedEffort
    - IncidentId
    - IncidentStatusId
    - IncidentTypeId
    - LastUpdateDate
    - Name
    - OpenerId
    - OwnerId
    - PriorityId
    - ProgressId
    - ProjectedEffort
    - RemainingEffort
    - Resolution
    - ResolvedReleaseId
    - SeverityId
    - StartDate
    - Tags
    - VerifiedReleaseId

=== "Releases"
    - AvailableEffort
    - AvailablePoints
    - CountPassed
    - CreationDate
    - CreatorId
    - Custom_01...Custom_99
    - DaysNonWorking
    - Description
    - EndDate
    - LastUpdateDate
    - Name
    - OwnerId
    - PercentComplete
    - PlannedEffort
    - PlannedPoints
    - ReleaseId
    - ReleaseStatusId
    - ReleaseTypeId
    - RequirementCount
    - RequirementPoints
    - ResourceCount
    - StartDate
    - Tags
    - TaskActualEffort
    - TaskCount
    - TaskEstimatedEffort
    - TaskProjectedEffort
    - TaskRemainingEffort
    - VersionNumber

=== "Requirements"
    - AuthorId
    - ComponentId
    - CoverageCountTotal
    - CreationDate
    - Custom_01...Custom_99
    - Description
    - EstimatedEffort
    - EstimatePoints
    - ImportanceId
    - IsSummary
    - LastUpdateDate
    - Name
    - OwnerId
    - TaskCount
    - ReleaseId
    - RequirementId
    - RequirementStatusId
    - RequirementTypeId
    - Tags
    - TaskActualEffort
    - TaskEstimatedEffort
    - TaskProjectedEffort
    - TaskRemainingEffort

=== "Risks"
    - ClosedDate
    - ComponentId
    - CreationDate
    - CreatorId
    - Custom_01...Custom_99
    - Description
    - LastUpdateDate
    - Name
    - OwnerId
    - ReleaseId
    - ReviewDate
    - RiskExposure
    - RiskId
    - RiskImpactId
    - RiskProbabilityId
    - RiskStatusId
    - RiskTypeId
    - Tags
    - Title

=== "Tasks"
    - ActualEffort
    - CompletionPercent
    - ComponentId
    - CreationDate
    - CreatorId
    - Custom_01...Custom_99
    - Description
    - EndDate
    - EstimatedEffort
    - LastUpdateDate
    - Name
    - OwnerId
    - ProgressId
    - ProjectedEffort
    - ReleaseId
    - RemainingEffort
    - RequirementId
    - RiskId
    - StartDate
    - Tags
    - TaskId
    - TaskPriorityId
    - TaskStatusId
    - TaskTypeId

=== "Test Cases"
    - ActualDuration
    - AuthorId
    - AutomationChanged
    - AutomationDocumentFolderId
    - AutomationDocumentId
    - AutomationDocumentTypeId
    - AutomationEngineId
    - AutomationFileIcon
    - AutomationLink
    - AutomationScript
    - AutomationType
    - AutomationVersion
    - ComponentIds
    - CreationDate
    - Custom_01...Custom_99
    - Description
    - EstimatedDuration
    - ExecutionDate
    - ExecutionStatusId
    - IsSuspect
    - IsTestSteps
    - LastUpdateDate
    - Name
    - OwnerId
    - ReleaseId
    - Tags
    - TestCaseId
    - TestCasePriorityId
    - TestCaseStatusId
    - TestCaseTypeId

=== "Test Runs"
    - ActualDuration
    - AutomationHostId
    - BuildId
    - Custom_01...Custom_99
    - Description
    - EndDate
    - EstimatedDuration
    - ExecutionStatusId
    - Name
    - ProjectId
    - ReleaseId
    - RunnerMessage
    - RunnerName
    - RunnerTestName
    - Tags
    - TestCaseId
    - TestRunId
    - TestRunTypeId
    - TestSetId
    - TesterId

=== "Test Sets"
    - ActualDuration
    - AutomationHostId
    - BuildExecuteTimeInterval
    - CreationDate
    - CreatorId
    - Custom_01...Custom_99
    - Description
    - EstimatedDuration
    - ExecutionDate
    - ExecutionStatusId
    - IsAutoScheduled
    - LastUpdateDate
    - Name
    - OwnerId
    - PlannedDate
    - RecurrenceId
    - ReleaseId
    - Tags
    - TestCaseReleaseId
    - TestConfigurationSetId
    - TestRunTypeId
    - TestSetId
    - TestSetStatusId
					
### Available Data Properties
The following data properties are available when calling various [page functions](./SpiraApps-Manager.md/#page-actions) related to artifact details pages like getDataItemField or updateFormField. 

A given field may have data and metadata of multiple types, such as a label & an ID. in these cases, the field has multiple data properties for it's different components. This resource will summarize how to access these pieces of information on the details page as a SpiraApp developer & where to expect to find specific information available on artifact details pages.

If you are unsure what is available, network requests in browser dev tools can be filtered by Form_Retrieve on details pages to capture the relevant response. the d.Fields object in the response contains field names as it's keys, and the values for a given field are the data properties available. This document is not an exhaustive list.

=== "textValue"
    This data property contains the string information about a field. 

    This is the relevant database property for text, rich text, and multi-select based fields & if changed, will change the relevant data in the database upon save.
        
    ??? note "Example use cases"
        - The name & description of artifacts as raw text are stored in this property (Including markup in rich text fields)
        - Multi-select value IDs are stored here, where this contains a string with a comma separated list of integers, where the integers are the IDs of each selected value (Available values & label mappings are stored in lookups data property)


=== "intValue"
    This data property contains integer based data. Some fields may be integer based in the database, but are displayed differently via their UI controls. All single select dropdowns use integers for their underlying ID values. Often times, the int value is the "real" database value, but is not what gets displayed to the end user within Spira's UI.

    This is the relevant database property for single select dropdowns and effort values & if changed, will change the relevant data in the database upon save.

    ??? note "Example use cases"
        - ID of a single item selected for a dropdown property 
        - Effort values (Stored as number of minutes)
        - Integer custom property values


=== "dateValue"
    This data property contains dates. 
    ??? note "Example use cases"
        - Start and End dates of artifacts
        - Last executed dates for tests

    This is the relevant database property for all dates & if changed, will change the relevant data in the database upon save (Creation & last update dates cannot be updated this way)

=== "caption"
    This data property contains the captions for the fields as displayed in the UI, localized to the user's language settings. This could be used for refering to the name of specific fields, such as "Owner" from the field OwnerId in a displayed message.

=== "lookups" 
    This data property contains an object of potential values for dropdowns with the relevant ID as the objects' keys & their label values as the objects' values. Users and release fields never have this information here. For most standard fields, this options information is not stored here. Keys start with "k" followed by an integer, and the integer is the relevant ID (k must be removed to use the value). Cases where this is available:
    
    - Custom property fields of type list or multi-list 
    - Components on the incident details page

=== "tooltip"
    This data property contains tooltips information & sometimes alternate text formatting of certain data fields.

    ??? note "Example Use Cases"
        - Date fields have a user friendly string localized to the relevant culture's formatting
        - Multi-select properties which are disabled have the list of selected items labels stored here as a 

=== "Workflow Properties"
    This is not a data property in itself, but it makes more sense to group these under the workflow category. The following are boolean properties that indicate specific workflow or custom property constraints for a specific field. Relevant data properties:

    - editable
    - required
    - hidden


## Available resources
### Inflectra Javascript helpers
Each Javascript contents for a SpiraApp is embedded on the relevant page wrapped in an IIFE block and set to use strict. The SpiraApp code is also prepended to include access to useful constants:

- `spiraAppManager`: an instance of a helper class, described more below
- `APP_GUID`: string of the SpiraApp's guid

You can read the contents of these constants, but cannot write to them.

Additionally, if a SpiraApp has any relevant settings these are stored in the `SpiraAppSettings` object. The settings for a SpiraApp can be accessed with `SpiraAppSettings[APP_GUID]`. This will store key/values based on each relevant setting and its `name` field as specific in the manifest. Product settings are loaded onto all product specific pages. System settings are loaded onto the My Page.

### spiraAppManager
The [spiraAppManager](./SpiraApps-Manager.md) is a helper class that provides a wide range of useful functions and operations to SpiraApps. Read its reference material [here](./SpiraApps-Manager.md).

### SpiraAppSettings
SpiraApp admins can store settings at the [system](./SpiraApps-Manifest.md/#system-admin-settings) and [product level](./SpiraApps-Manifest.md/#product-admin-settings). These allow admins to configure the SpiraApp and also set information that the SpiraApp can access. These settings are stored in a special on page resource called `SpiraAppSettings`. 

You can access the settings specific to your SpiraApp in JavaScript by calling `SpiraAppSettings[APP_GUID]`. This will provide a full JSON object of all relevant settings. Secure settings are not accessible client-side - these are designed for credentials storage to make external API calls.

The different settings are accessible in the following places (note that not all settings are available in all places)

| Spira Location         | System Settings                   | Product Settings                  |
| ---------------------- | --------------------------------- | --------------------------------- |
| Product artifact pages |                                   | :material-checkbox-marked-circle: |
| Product home page      |                                   | :material-checkbox-marked-circle: |
| Product reporting      |                                   | :material-checkbox-marked-circle: |
| My Page                | :material-checkbox-marked-circle: |                                   |

### Third party Javascript libraries
The following third party Javascript libraries and tools are available to SpiraApps:

- React v16.14
- Mustache

Spira provides a number of resources that SpiraApps can use to provide rich, powerful, and seamless user experiences. These are designed to provide developers a comprehensive and developer-friendly toolset to create SpiraApps that can (and should) feel like native Spira features.

### Inflectra CSS helpers
HTML elements added to the page for a SpiraApp (like a menu or widget) is wrapped in a containing div that has the guid of the SpiraApp as a property. Any CSS added onto the page for the SpiraApp is nested with this same property on the page. This means the SpiraApp CSS cannot change any CSS elsewhere on the page

[Inflectra's Unity CSS library](https://github.com/Inflectra/inflectra-unity-css-library) is available to SpiraApps. While it exists within Spira, the basics and its classes are available to help you plan and review your css on GitHub.


### Spira Artifact Images
The following images are available for SpiraApps to access to help enhance the appearance of any UX. Use the [baseThemeUrl](./SpiraApps-Manager.md/#properties) property from the SpiraAppManager to aid in retrieval. Note that all of the images below are in SVG format and in the "Images" folder. 

- artifact-UseCaseStep.svg
- artifact-AutomationHost.svg
- artifact-Baseline.svg
- artifact-Build.svg
- artifact-Capability.svg
- artifact-CapabilitySummary.svg
- artifact-Configuration.svg
- artifact-Document.svg
- artifactHighlight-planningBoard.gif
- artifactHighlight-risk.gif
- artifactHighlight-risk.png
- artifactHighlight-sourceCode.gif
- artifactHighlight-task.gif
- artifact-Incident.svg
- artifact-Iteration.svg
- artifact-Planning.svg
- artifact-PlanningBoard.svg
- artifact-PortfolioMilestone.svg
- artifact-ProgramMilestone.svg
- artifact-Project.svg
- artifact-PullRequest.svg
- artifact-Release.svg
- artifact-RepositoryTest.svg
- artifact-Requirement.svg
- artifact-RequirementStep.svg
- artifact-RequirementSummary.svg
- artifact-Resource.svg
- artifact-Revision.svg
- artifact-Revision-Add.svg
- artifact-Revision-Delete.svg
- artifact-Risk.svg
- artifact-RiskMitigation.svg
- artifact-SourceCode.svg
- artifact-StrategicOutcome.svg
- artifact-Task.svg
- artifact-TestCase.svg
- artifact-TestCaseNoSteps.svg
- artifact-TestConfigurationSet.svg
- artifact-TestLink.svg
- artifact-TestRun.svg
- artifact-TestSet.svg
- artifact-TestStep.svg
- artifact-UseCase.svg
- FolderOpen.svg
- Folder.svg
- product-TaraVault.svg
- org-Administration.svg
- org-Component.svg
- org-Enterprise.svg
- org-Portfolio.svg
- org-Program-outline.svg
- org-Project-outline.svg
- org-spiraApp.svg
- org-Template-outline.svg
- product-SpiraPlan.svg
- product-SpiraTeam.svg
- product-SpiraTest.svg

### Third party CSS libraries
The following third party CSS libraries are available to SpiraApps:

- FontAwesome 6 pro: available as embedded fonts referenced [using css styles](https://docs.fontawesome.com/web/add-icons/how-to#add-icons-to-html) 


