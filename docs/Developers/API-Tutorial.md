# Using the Spira REST API
## Overview
The Spira products (SpiraTest, SpiraTeam, and SpiraPlan) include SOAP and REST API services with your subscription. This guide explains how to use the Spira REST API version 7 (hereafter 'API'), from the basic operations to the advanced ones, so you can effectively integrate your applications with Spira.

## Documentation and Service URL
Before we start, we need to figure what is the endpoint of the API service for your Spira instance. Typically, it should be:

`https://{Spira_instance_URL}/Services/v7_0/RestService.svc/`

where {Spira_instance_URL} is the address you use to access Spira. For most cloud customers, it is usually `company-name.spiraservice.net`. On-prem customers use different, customized instance URLs. If you are unsure about it, please check with your system administrator. Similarly, the API documentation is available at:

`https://{Spira_instance_URL}/Services/v7_0/RestService.aspx`

Save this address for your future reference, as it contains the complete list and description of operations available in this version. Alternatively, you can find both your API endpoint and documentation by going to Integration > Web Services in Spira. Then, under <i>Version 7.0</i>, in the REST row, click the link that leads to the documentation page. The base URL of your instance is shown in the first topic.

## Request Headers
For every request made to the Spira API, you must provide a valid username and API Key. Learn how to activate and get your API Key [here](http://spiradoc.inflectra.com/HowTo-Guides/Users-profile-management/#how-to-get-or-make-your-rss-token-or-api-key). The following table summarizes all the parameters you should include when sending requests to the API:

| Header        | Description|
| ------------- | --------------------------|
| username      | Your Spira username|
| api-key       | Your Spira API Key. Remember to include the curly brackets. Example: `{00000000-0000-0000-0000-000000000000}`.|
| Accept        | This defines what format the response from the server should have. JSON format is supported so use `Accept: application/json`|
| Content-Type  | This defines the format of the request payload data sent to the server. For POST and PUT methods use `Content-Type: application/json`|

## Available Methods
=== "GET"

    GET methods are used to retrieve data from Spira. They usually require the workspace ID (product, program, portfolio) and/or the artifact ID, which must be provided in the request URL.

    === "REQUEST"
        !!! example "Example: Retrieving Task #2 from Product #1"
            <i>Remember to replace the instance URL, project ID (1), Task ID (2), username (my_username), and API Key ({000...000})</i>
            ```json
            GET https://my-company.spiraservice.net/Services/v7_0/RestService.svc/projects/1/tasks/2?username=my_username&api-key={00000000-0000-0000-0000-000000000000}
            Accept: application/json
            ```

    === "RESPONSE"
        !!! example "Example: Retrieving Task #2 from Product #1"
            ```json
            {
                "TaskId": 2,
                "TaskStatusId": 3,
                "TaskTypeId": 1,
                "TaskFolderId": 3,
                "RequirementId": 4,
                "ReleaseId": 8,
                "ReleaseGuid": null,
                "ComponentId": 1,
                "CreatorId": 2,
                "OwnerId": 2,
                "CreatorGuid": null,
                "OwnerGuid": null,
                "TaskPriorityId": 1,
                "Name": "Create book object insert method",
                "Description": "Code the business object that inserts a new book row in the database",
                "CreationDate": "2023-11-13T17:09:14.620Z",
                "LastUpdateDate": "2024-01-31T17:09:14.620Z",
                "StartDate": "2024-01-30T17:09:14.620Z",
                "EndDate": "2024-01-31T17:09:14.620Z",
                "CompletionPercent": 100,
                "EstimatedEffort": 300,
                "ActualEffort": 320,
                "RemainingEffort": 0,
                "ProjectedEffort": 320,
                "TaskStatusName": "Completed",
                "TaskTypeName": "Development",
                "OwnerName": "Fred Bloggs",
                "TaskPriorityName": "1 - Critical",
                "ProjectName": "Library Information System (Sample)",
                "ReleaseVersionNumber": "1.0.0.0.0001",
                "RequirementName": "Ability to add new books to the system",
                "RiskId": null,
                "ProjectId": 1,
                "ProjectGuid": null,
                "ArtifactTypeId": 6,
                "ConcurrencyDate": "2023-11-13T17:09:14.620Z",
                "CustomProperties": null,
                "IsAttachments": false,
                "Tags": null,
                "Guid": null
            }
            ```

=== "POST"
    POST methods are used to create new data in Spira as well as advanced search operations. They usually require the `Accept` and `Content-Type` headers and the workspace ID (product, program, portfolio). The server returns the new artifact ID if the operation is successful.
    
    === "REQUEST"
        !!! example "Example: Creating a new Tasks from Product #1"
            <i>Remember to replace the instance URL, project ID (1), username (my_username), and API Key ({000...000})</i>
            ```json
            POST https://my-company.spiraservice.net/Services/v7_0/RestService.svc/projects/1/tasks?username=my_username&api-key={00000000-0000-0000-0000-000000000000}
            content-type: application/json
            Accept: application/json
            
            {
                "Name": "My new task",
                "TaskStatusId": 1
            }
            ```
    === "RESPONSE"
        !!! example "Example: Creating a new Tasks from Product #1"
            <i>Note that the newly created Task has the ID 49 in the system.</i>
            ```json
            {
                "TaskId": 49,
                "TaskStatusId": 1,
                "Name": "My new task",
                "CompletionPercent": 0,
                "ProjectId": 1
            }
            ```

=== "PUT"
    PUT methods are used to update existing data in Spira. They usually require the `Accept` and `Content-Type` headers, the workspace ID (product, program, portfolio), and sometimes the artifact ID that must be provided in the request URL. To update artifacts in Spira, you must provide a valid `ConcurrencyDate` value in the request body, to avoid concurrency issues. Send a GET request to the server to retrieve the target artifact, copy the value of the `ConcurrencyDate` field, and use it in the PUT request body. If the request is successful, the server returns only the HTTP code 200 and no data.

    !!! example "Example: Updating the Task #49 of Product #1"
        <i>Remember to replace the instance URL, project ID (1), username (my_username), and API Key ({000...000})</i>
        ```json
        PUT https://my-company.spiraservice.net/Services/v7_0/RestService.svc/projects/1/tasks?username=my_username&api-key={00000000-0000-0000-0000-000000000000}
        content-type: application/json
        Accept: application/json
            
        {
            "TaskId": 49,
            "TaskStatusId": 2,
            "Name": "My updated task",
            "Description": "This is the new description.",
            "ConcurrencyDate": "2023-11-13T17:09:14.620Z",
            "CompletionPercent": 50,
            "OwnerId": 2,
            "ProjectId": 1
        }
        ```

=== "DELETE"
    DELETE methods are used to remove existing data from Spira. They usually require the workspace ID (product, program, portfolio), and the artifact ID that must be provided in the request URL. If the request is successful, the server returns only the HTTP code 200 and no data.

    !!! example "Example: Removing the Task #49 of Product #1"
        <i>Remember to replace the instance URL, project ID (1), Task ID (49), username (my_username), and API Key ({000...000})</i>
        ```json
        DELETE https://my-company.spiraservice.net/Spira/Services/v7_0/RestService.svc/projects/1/tasks/49?username=my_username&api-key={00000000-0000-0000-0000-000000000000}
        ```

## Spira API and Postman
TODO

## Pagination

Some Spira GET API operations can return a huge amount of data, which can lead to timeouts and connection issues. To better handle this scenario, pagination parameters are required for some operations when making requests to the server. They are:


- **start_row** : The record starting number. This parameter starts at 1.
- **number_of_rows** : The maximum number of records to return. The bigger the number, the more time it takes for the request to be processed. If you are seeing timeout errors, reduce this value and make more requests to retrieve the data.

    !!! example "Example: Retrieving all new tasks added in the product #1 since 01/01/2021"
        <i>Remember to replace the instance URL, project ID (1), username (my_username), and API Key ({000...000})</i>
        Using page size of 10 records.<br>
        Page 1: Records 01 to 10  
        ```json
        GET https://my-company.spiraservice.net/Services/v7_0/RestService.svc/projects/1/tasks/new?creation_date=2021-01-01T00:00:00.000&start_row=1&number_of_rows=10&username=my_username&api-key={00000000-0000-0000-0000-000000000000}
        ```
        Page 2: Records 11 to 20  
        ```json
        GET https://my-company.spiraservice.net/Services/v7_0/RestService.svc/projects/1/tasks/new?creation_date=2021-01-01T00:00:00.000&start_row=11&number_of_rows=10&username=my_username&api-key={00000000-0000-0000-0000-000000000000}
        ```
        Page 3: Records 21 to 30  
        ```json
        GET https://my-company.spiraservice.net/Services/v7_0/RestService.svc/projects/1/tasks/new?creation_date=2021-01-01T00:00:00.000&start_row=21&number_of_rows=10&username=my_username&api-key={00000000-0000-0000-0000-000000000000}
        ```
        and so on...<br>
        When the end of the list is reached, the system returns an empty result:
        ```json
        []
        ```

## User Roles and Security

In order to retrieve, create, edit, or delete data in Spira through the API, the user must have authorization to perform the requested operation. Spira checks this against:

- The user access level in the workspace (system admin, program owner/member) and/or
- The user role in the workspace for the given artifact

!!! info "If you are seeing 'Access Denied' error messages in the API"
    First, verify if the provided credentials are correct and the user is not locked out. Then, make sure the provided credentials have enough authority to perform the operation in Spira. You can check if the user's role for the given product allows performing the operation against the given artifact, and if the user is a system administrator, a program member or owner, depending on the requirements of the target operation.

## Custom Properties
TODO

## Filtering
TODO
https://www.inflectra.com/Support/Ticket/71169.aspx

## Use Cases

Following, there are a few common use cases related to the Spira API:


### Create an Incident and Set Custom Properties
TODO
TYPE RELEASE https://www.inflectra.com/Support/Ticket/88169.aspx

### Add a new Document Version
TODO

### Record an Automated Test Run Result
TODO

### Associate XX to YY
TODO

### Add TestCase to Release
TODO
https://www.inflectra.com/Support/Ticket/66096.aspx

### Custom Lists
TODO

### Add new users to the system
TODO

## Common Error Messages
If something goes wrong with your request, the system will return the error code 404 and a message describing the error. Following are the most common error messages and how to solve them:

TODO
-You need to be a Product Administrator to use this function!
Method not allowed - https://www.inflectra.com/Support/Ticket/70993.aspx
-Access Denied
-Unable to connect Using Postman: https://www.inflectra.com/Support/Ticket/70905.aspx
-Unable to locate requested artifact

## Learn More
The following articles explores different use cases for the Spira API:

[GET an automated test script using Spira's REST API](https://www.inflectra.com/Support/KnowledgeBase/KB346.aspx)

[Using the Spira REST API to Remove Test Cases from a Test Set](https://www.inflectra.com/Support/KnowledgeBase/KB684.aspx)

[Using the Spira REST API to Remove Test Cases from a Test Set](https://www.inflectra.com/Support/KnowledgeBase/KB590.aspx)

[Using the Spira Reports API](https://www.inflectra.com/Support/KnowledgeBase/KB494.aspx)