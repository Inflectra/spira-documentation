# Tokens for Custom Reporting

## Introduction
When creating custom reports or custom graphs, you can use special tokens in your query. These are evaluated during the generation of the report or graph to make sure that your report is dynamically limited to the specific context the user is in when they run the report. These are listed below.

You do not have to use these tokens. You can hard code a report to query only against a specific value that the token would return dynamically (eg set the ProjectId to 1 rather than to the current ProjectId of the product the user is in). You can also exclude that part of the query entirely, so that the report will include all the items in the entire system, with no restriction by a token / that field.


## Tokens for Reports and Graphs

- **${ProjectId}**: limits the data to items in the current product only (a "product" in the tool is referred to as a "Project" in the database)
- **${ProjectGroupId}**: limits the data to items in the current program only (a "program" in the tool is referred to as a "ProjectGroup" in the database)


## Tokens for Graphs Only

### ${ReleaseId}
This token limits the data to the release selected in the Release dropdown on the main reporting page. 

If "All Releases" is displayed, the graph will display no data (along with an info message to users)

Example query:

``` sql
select R.EXECUTION_STATUS_NAME, COUNT (R.TEST_RUN_ID) as COUNT
from SpiraTestEntities.R_TestRuns as R
where R.PROJECT_ID = ${ProjectId} and R.RELEASE_ID = ${ReleaseId}
group by R.EXECUTION_STATUS_NAME
```

### ${ReleaseAndChildIds}
This token limits the data to the release selected in the Release dropdown on the main reporting page **and to data from that release's child sprints** (direct child sprints only). 

If "All Releases" is displayed, the graph, using this token, will correctly display information about all releases in the current product.

Example query (note the use of "in" before the token): 

``` sql
select R.EXECUTION_STATUS_NAME, COUNT (R.TEST_RUN_ID) as COUNT
from SpiraTestEntities.R_TestRuns as R
where R.PROJECT_ID = ${ProjectId} and R.RELEASE_ID in {${ReleaseAndChildIds}}
group by R.EXECUTION_STATUS_NAME
```
