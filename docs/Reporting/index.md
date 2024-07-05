# Reporting Overview
Spira provides a large number of report views that can be used to create custom reports, graphs, or analyses. This is in addition to built-in "standard" reports that can always be accessed from the reporting pages of the application.

Each report view shows a specific slice of data in the application. Some views will be easy to understand, like the main incident table, as the data will look very similar to what you can see in the application itself. Other views are focused on how artifacts link together, or provide additional information about their metadata - by themselves these can take longer to work out how to use in reports. 

Report views can always be accessed via OData, or via the Spira administration console for system admins or report admins.

There are as many custom needs for reporting as there are end users, or more. By combining the data in the different report views together, along with powerful tools to display that data (like XSLT, OData, or spreadsheets), you can find out almost anything you want about your Spira application using these report views. 

These docs provide a number of resources to help you learn, understand, and develop your own custom reports and graphs:

- tutorials about how to get started with Spira's built in [custom reports](./Custom-Report-Tables.md) and [custom graphs](./Custom-Graph-Tutorial.md)
- a tutorial about [how to use OData with Spira](./OData-Tutorial.md)
- reference information about all of the [custom report tables](./Custom-Report-Tables.md), including names, fields, and primary keys
- [Tips and tricks](#reporting-tips-and-tricks) to remember when making custom queries for report
- Explanations about how report views fit together and how they be used to give you meaningful insights (below) 

    - [Artifacts](#artifact-views)
    - [Traceability](#essential-traceability)

!!! info "Entity Relationship Diagrams"
    In this guide we do not provide complete ER diagrams. With over 80 views, such a diagram would not be user friendly. We will explore ways to provide more expert level ways to use our report views, but believe that once SQL expert users are familiar with the views available, they will be able to intuitively work out how the views can connect together.

## Reporting Tips and Tricks
- Spira does not show **deleted artifacts** to users, but some may still be in the database. By default these are accessible to report views. To ignore deleted artifacts, make sure to always add `IS_DELETED = False` to your query.
- Every artifact is made up of **data from multiple sources**. The application shows all of this data in a seamless way to users. Report views will often also combine this information. For example, a task has an assigned owner. The database only saves the ID of the user, but the custom report view for tasks shows both the user's ID and their name. Before you start building a complex query joining lots of views together, the information you want may already be available out the box. Where you need more information, you can "bolt on" extra views
- For many artifacts, certain properties are set at the **product template level**. These properties, like types and custom properties, all have dedicated views to get the raw data about that template, if required.
- Other data about artifacts, particularly releases, tags, and components, are set at the **product level**. Again, there are dedicated views to get this raw product level data, to bring into your queries if needed
- In databases, you **link data together with joins**. Joins are very powerful and come in a few different types. When you make a join you have to tell the computer how to join the two views together. You do this by specifying which field in one view links to which field in the second view. For example, you can link a list of users, to a list of incidents they have made by joining the user ID field for the user to the author ID field of the incidents
- There are a number of different **types of join** that you can use to do different things:

    - INNER JOIN: Returns only the rows where there is a match in both tables based on the specified join condition.
    - LEFT OUTER JOIN (or LEFT JOIN): Returns all rows from the left table, and the matched rows from the right table; if there's no match, the result is NULL on the right side.
    - RIGHT OUTER JOIN (or RIGHT JOIN): Returns all rows from the right table, and the matched rows from the left table; if there's no match, the result is NULL on the left side.
    - FULL OUTER JOIN (or FULL JOIN): Returns all rows when there is a match in either the left or right table records.


## Artifact Views
### Requirements
=== "Key Report Tables"
    - [Requirements](./Custom-Report-Tables.md/#requirements)
    - [Requirement Steps](./Custom-Report-Tables.md/#requirement-steps)
    - [Requirement Types](./Custom-Report-Tables.md/#requirement-types)

=== "Tips"
    - Requirement Steps are relevant only when the requirement type support steps
    - In Spira requirements are organized hierarchically. 
    
        - Any requirement with children has the IS_SUMMARY field set to True. 
        - There is a special field called "INDENT_LEVEL", which is used to map out the hierarchy organized alphabetically. Each indent level is represented by 3 letters (AAA, then AAB, then AAC, etc). 
        - First root requirement's indent level = "AAA"
        - Second root requirement's indent level = "AAB"
        - First root requirement's first child's indent level = "AAAAAA",
        - Second root requirement's third child's indent level = "AABAAC",

=== "Table Connections"
    ``` mermaid
    erDiagram
    R_Requirements ||--o{ R_RequirementSteps : rq_key
    R_RequirementTypes ||--|{ R_Requirements : type_key

    R_Requirements {
        rq_key REQUIREMENT_ID
    }
    R_RequirementTypes {
        type_key REQUIREMENT_TYPE_ID
    }
    ```

### Test Cases
=== "Key Report Tables"
    - [Test Cases](./Custom-Report-Tables.md/#test-cases)
    - [Test Steps](./Custom-Report-Tables.md/#test-steps)
    - [Test Case Folders](./Custom-Report-Tables.md/#test-case-folders)
    - [Test Case Types](./Custom-Report-Tables.md/#test-case-types)
    - [Test Runs](./Custom-Report-Tables.md/#test-runs)
    - [Test RunSteps](./Custom-Report-Tables.md/#test-run-steps)

=== "Table Connections"
    ``` mermaid
    erDiagram
    R_TestCases ||--o{ R_TestSteps : case_key
    R_TestCases ||--o{ R_TestRunSteps : runstep_key
    R_TestCases ||--o{ R_TestCaseFolders : folder_key
    R_TestCases ||--|{ R_TestCaseTypes : type_key
    R_TestCases ||--o{ R_TestRuns : case_key
    R_TestRuns ||--o{ R_TestRunSteps : run_key

    R_TestCases { 
        case_key TEST_CASE_ID
    }
    R_TestSteps { 
        step_key TEST_STEP_ID
        case_key TEST_CASE_ID
    }
    R_TestCaseFolders { 
        folder_key TEST_CASE_FOLDER_ID
    }
    R_TestCaseTypes { 
        type_key TEST_CASE_TYPE_ID
    }
    R_TestRuns {
        run_key TEST_RUN_ID
        case_key TEST_CASE_ID
    }
    R_TestRunSteps {
        run_key TEST_RUN_ID
        case_key TEST_CASE_ID
        runstep_key TEST_RUN_STEP_ID
    }
    ```

## Incidents
=== "Key Report Tables"
    - [Incidents](./Custom-Report-Tables.md/#incidents)
    - [Incident Priorities](./Custom-Report-Tables.md/#incident-priorities)
    - [Incident Severities](./Custom-Report-Tables.md/#incident-severities)
    - [Incident Statuses](./Custom-Report-Tables.md/#incident-statuses)
    - [Incident Types](./Custom-Report-Tables.md/#incident-types)

=== "Table Connections"
    ``` mermaid
    erDiagram
    R_IncidentPriorities ||--|{ R_Incidents : pr_key
    R_IncidentSeverities ||--o{ R_Incidents : se_key
    R_IncidentStatuses ||--|{ R_Incidents : st_key
    R_IncidentTypes ||--|{ R_Incidents : tp_key

    R_IncidentPriorities {
        pr_key PRIORITY_ID
    }
    R_IncidentSeverities {
        se_key SEVERITY_ID
    }
    R_IncidentStatuses {
        st_key INCIDENT_STATUS_ID
    }
    R_IncidentTypes {
        tp_key INCIDENT_TYPE_ID
    }
    ```

## Essential Traceability
This is a collection of report views that capture traceability between key product artifacts. It focuses on Requirements, Test Cases, Test Runs, and Incidents.

=== "Key Report Tables"
    **Requirements**

    - [Requirements](./Custom-Report-Tables.md/#requirements)
    - [Requirement TestCases](./Custom-Report-Tables.md/#requirement-test-case-coverage)
    - [Requirement Incidents](./Custom-Report-Tables.md/#requirement-incidents)

    **Test Cases**

    - [Test Cases](./Custom-Report-Tables.md/#test-cases)
    - [Test Case Incidents](./Custom-Report-Tables.md/#test-case-incidents)

    **Test Runs**

    - [Test Run Incidents](./Custom-Report-Tables.md/#test-run-incidents)

    **Incidents**

    - [Incidents](./Custom-Report-Tables.md/#incidents)


=== "Table Connections"
    ``` mermaid
    erDiagram  
    R_Requirements }o--o{ R_RequirementTestCases : rq_key
    R_TestCases }o--o{ R_RequirementTestCases : tc_key

    R_TestCases }o--o{ R_TestCaseIncidents : tc_key
    R_Incidents }o--o{ R_TestCaseIncidents : in_key

    R_Requirements }o--o{ R_RequirementIncidents : rq_key
    R_Incidents }o--o{ R_RequirementIncidents : in_key

    R_TestRuns }o--o{ R_TestRunIncidents : tr_key
    R_Incidents }o--o{ R_TestRunIncidents : in_key

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
    R_TestRuns {
        tr_key TEST_RUN_ID
    }
    R_Incidents {
        tr_key TEST_RUN_ID
        in_key INCIDENT_ID
    }
    ```
