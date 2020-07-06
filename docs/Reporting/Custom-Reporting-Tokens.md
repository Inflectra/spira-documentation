# Tokens for Custom Reporting

## Introduction
When creating custom reports or custom graphs, you can use special tokens in your query. These are evaluated during the generation of the report or graph to make sure that your report is dynamically limited to the specific context the user is in when they run the report. These are listed below.

You do not have to use these tokens. You can hard code a report to query only against a specific value that the token would return dynamically (eg set the ProjectId to 1 rather than to the current ProjectId of the product the user is in). You can also exclude that part of the query entirely, so that the report will include all the items in the entire system, with no restriction by a token / that field.


## Available Tokens

- **${ProjectId}**: limits the data to items in the current product only (a "product" in the tool is referred to as a "Project" in the database)
- **${ProjectGroupId}**: limits the data to items in the current program only (a "program" in the tool is referred to as a "ProjectGroup" in the database)
- **${ReleaseId}**: limits the data to a specific single release (selected via a dropdown)
- **${ReleaseAndChildIds}**: limits the data to a specific release and all of its 'active' children (selected via a dropdown)

## More details about ${ReleaseId}
This token limits the data to the release selected in the release dropdown. For custom graphs this is the dropdown on the main reporting page. For custom reports, this dropdown is shown at the bottom of the report configuration page in a section called "Custom Section Filters". 

If "All Releases" is selected, custom graphs/reports using this token display no data. If a specific release is selected, then the graph will display data for that release only.

Example query:

``` sql
select R.EXECUTION_STATUS_NAME, COUNT (R.TEST_RUN_ID) as COUNT
from SpiraTestEntities.R_TestRuns as R
where R.PROJECT_ID = ${ProjectId} and R.RELEASE_ID = ${ReleaseId}
group by R.EXECUTION_STATUS_NAME
```

## More details about ${ReleaseAndChildIds}
This token limits the data to the selected release **and to data from that release's children**. 

If "All Releases" is selected data against all active releases in the current product will be returned. For example, if your custom graph shows requirements by release, with "All Releases" selected, the graph will show any requirement with an active release set on the release field (which matches the list of releases in the release dropdown). In other words, requirements with no release set will not be included.

If a specific release is selected that does not have any active children data for that release only will be returned. 

If a release with active children is selected data for that release and all of its active children (ie any children shown in the release dropdown at the top of the page) will be returned.

**Please note**: an "active" release is one with a status of Planned, In Progress, or Completed.

Example query (note the use of "in" before the token): 

``` sql
select R.EXECUTION_STATUS_NAME, COUNT (R.TEST_RUN_ID) as COUNT
from SpiraTestEntities.R_TestRuns as R
where R.PROJECT_ID = ${ProjectId} and R.RELEASE_ID in {${ReleaseAndChildIds}}
group by R.EXECUTION_STATUS_NAME
```
