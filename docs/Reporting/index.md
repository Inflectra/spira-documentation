# Reporting Overview
Spira provides a large number of report views that can be used to create custom reports, graphs, or analyses. This is in addition to built-in "standard" reports that can always be accessed from the reporting pages of the application.

Report views can always be accessed via OData, or via the Spira administration console for system admins or report admins.

There are as many custom needs for reporting as there are end users, or more. By combining the data in the different report views together, along with powerful tools to display that data (like XSLT, OData, or spreadsheets), you can find out almost anything you want about your Spira application using these report views.

In this reporting section of our docs we have a number of useful links:
- tutorials about how to get started with Spira's built in [custom reports](./Custom-Report-Tables.md) and [custom graphs](./Custom-Graph-Tutorial.md)
- a tutorial about [how to use OData with Spira](./OData-Tutorial.md)
- reference information about all of the [custom report tables](./Custom-Report-Tables.md), including names, fields, and primary keys
- XXX information below


## Artifacts
Almost every artifact is made up of data from multiple sources. The 

## Essential Traceability
This is a collection of report view that capture traceability between artifacts. It focuses on Requirements, Test Cases, Test Runs, and Incidents.

XXX Do not have a full ER diagram because XXX

=== "Key Report Tables"
    **Requirements**

    - [Requirements](./Custom-Report-Tables.md/#requirements)
    - [Requirement Steps](./Custom-Report-Tables.md/#requirement-steps)
    - [Requirement Types](./Custom-Report-Tables.md/#requirement-types)
    - [Requirement TestCases](./Custom-Report-Tables.md/#requirement-test-case-coverage)
    - [Requirement Incidents](./Custom-Report-Tables.md/#requirement-incidents)

    **Test Cases**

    - [Test Cases](./Custom-Report-Tables.md/#test-cases)
    - [Test Steps](./Custom-Report-Tables.md/#test-steps)
    - [Test Case Folders](./Custom-Report-Tables.md/#test-case-folders)
    - [Test Case Incidents](./Custom-Report-Tables.md/#test-case-incidents)
    - [Test Case Types](./Custom-Report-Tables.md/#test-case-types)

    **Test Runs**

    - [Test Runs](./Custom-Report-Tables.md/#test-runs)
    - [Test RunSteps](./Custom-Report-Tables.md/#test-run-steps)
    - [Test Run Incidents](./Custom-Report-Tables.md/#test-run-incidents)

    **Incidents**

    - [Incidents](./Custom-Report-Tables.md/#incidents)
    - [Incident Priorities](./Custom-Report-Tables.md/#incident-priorities)
    - [Incident Severities](./Custom-Report-Tables.md/#incident-severities)
    - [Incident Statuses](./Custom-Report-Tables.md/#incident-statuses)
    - [Incident Types](./Custom-Report-Tables.md/#incident-types)

=== "Tips"
    - Requirement Steps are relevant only when the requirement has scenario steps associated with it.
    - Consolidated tables exist for RequirementIncidents, RequirementTestCases, TestCaseIncidents, TestRunIncidents to bring information related to requirements, test cases, and incidents efficiently.
    - Test Runs represent the snapshot of test case or test set. Details of the steps inside a test case execution is captured in TestRunSteps.
    - TestCaseFolders table contains information of test cases grouped in the test case folder hierarchy.
    - Requirement Type are at the template level and contain types of requirements.
    - Components lend a business lens to the way the requirements are organized for product delivery.
    - Releases are timeboxed intervals that represent the projects within the products.
    - The Spira interface will not show deleted artifacts. To suppress them in custom queries, use the Is_Deleted = "False" on the artifacts where this field is supported.
    - The Spira interface may support hierarchical definitions which may not be required in the custom reports. In such cases, use the Is_Summary = "False" on the artifacts where this field is supported.


=== "Table Connections"
    ``` mermaid
    erDiagram  
    R_Requirements }o--o{ R_RequirementTestCases : rq_key
    R_TestCases }o--o{ R_RequirementTestCases : tc_key

    R_TestCases }o--o{ R_TestCaseIncidents : tc_key
    R_Incidents }o--o{ R_TestCaseIncidents : in_key

    R_Requirements }o--o{ R_RequirementIncidents : rq_key
    R_Incidents }o--o{ R_RequirementIncidents : in_key

    R_Requirements {
        rq_key REQUIREMENT_ID
    }
    R_TestCases {
        tc_key TEST_CASE_ID
    }
    R_Incidents {
        in_key INCIDENT_ID
    }
    R_RequirementIncidents {
        rq_key REQUIREMENT_ID
        in_key INCIDENT_ID
    }
    R_TestCaseIncidents {
        in_key INCIDENT_ID
        tc_key TEST_CASE_ID
    }
    R_RequirementTestCases {
        rq_key REQUIREMENT_ID
        tc_key TEST_CASE_ID
    }
    ```


    ``` mermaid
    erDiagram
    R_Requirements ||--o{ R_RequirementSteps : REQUIREMENT_ID
    R_RequirementTypes ||--|{ R_Requirements : REQUIREMENT_TYPE_ID
    ```

    ``` mermaid
    erDiagram
    R_TestCases ||--o{ R_TestSteps : TEST_CASE_ID
    R_TestCases ||--o{ R_TestCaseFolders : TEST_CASE_FOLDER_ID
    R_TestCases ||--|{ R_TestCaseTypes : TEST_CASE_TYPE_ID
    ```

    ``` mermaid
    erDiagram
    R_IncidentPriorities ||--|{ R_Incidents : PRIORITY_ID
    R_IncidentSeverities ||--o{ R_Incidents : SEVERITY_ID
    R_IncidentStatuses ||--|{ R_Incidents : INCIDENT_STATUS_ID
    R_IncidentTypes ||--|{ R_Incidents : INCIDENT_TYPE_ID
    ```
