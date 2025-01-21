# Release Notes for Spira v8

## Version 8.7 (February 2025)
!!! info "Summary"

??? success "New Features"
    * **Cross-Cutting Functionality**
        - Enhance the history tab and product admin history details to display difference highlighting for text fields, to make it easier for people to see exactly what has changed and how [RQ:5102]

    * **My Timesheet**

        - As a developer, I can see the last time that a timesheet's status was changed, to help me better manage my timesheets [RQ:4964]
        - As a developer with timesheet approvals enabled, I cannot delete a timesheet that has been approved, to ensure the integrity of data a manager has reviewed [RQ:4974]
        - As a developer with timesheet approvals enabled, I cannot edit a timesheet that has been approved, to ensure the integrity of data a manager has reviewed [RQ:4975]
        - As a developer with timesheet approvals enabled, I can edit a timesheet that has been rejected, so I can correct any issues a manager has flagged [RQ:4970]
        - As a developer with timesheet approvals enabled, I can resubmit a previously rejected timesheet, to get the timesheet re-reviewed by a manager [RQ:4971]
        - As a developer with timesheet approvals enabled, I can see any comment added to any timesheet, for my records [RQ:4977]
        - As a developer, I can filter the list of my timesheets using "advanced filters", to help me quickly find the data I need [RQ:5117]
        - As a developer, I can see a list in a grid of all of my timesheets, so can easily explore my timesheets [RQ:4965]

    * **Timesheet Managers**

        - As a timesheet manager with approvals enabled, I can navigate to the enterprise level timesheets list page, so I can access the page as needed [RQ:5044]
        - As a timesheet manager with approvals enabled, I can access an enterprise level timesheet list page, so I can view all timesheets submitted for approval [RQ:5045]
        - As a timesheet manager with approvals enabled, I can view a list of all timesheets submitted for approval, so I can review relevant timesheets [RQ:5046]
        - As a timesheet manager with approvals enabled, I can filter the list of timesheets by owner & dates using "advanced filters", to help me quickly find the data I need [RQ:5094]
        - As a timesheet manager with approvals enabled, I can sort the list of timesheets by relevant columns, to help me quickly find the data I need [RQ:5047]
        - As a timesheet manager with approvals enabled, I can export the current list of timesheets as a CSV file, to help me do more detailed analysis outside of Spira [RQ:5048]
        - As a timesheet manager with approvals enabled, I can view all details about a timesheet submitted for approval, so I can inspect each relevant timesheet [RQ:5049]
        - As a timesheet manager with approvals enabled, I can approve a timesheet submitted for approval, to formally approve and lock the timesheet [RQ:5050]
        - As a timesheet manager with approvals enabled, I can reject a timesheet submitted for approval, to request the developer makes changes [RQ:5051]

    * **Timesheet APIs**

        - As an API user, I can update a timesheet using the Spira APIs, to help me automate timesheet work [RQ:5031]
        - As an API user, I can create timesheet entries using the Spira APIs, to help me automate timesheet work [RQ:5032]
        - As an API user, I can update timesheet entries using the Spira APIs, to help me automate timesheet work [RQ:5033]
        - As an API user, I can retrieve timesheet status data using the Spira APIs, to help me automate timesheet work [RQ:5034]
        - As an API user, I can retrieve all my timesheets using the Spira APIs, to help me automate timesheet work [RQ:5036]
        - As an API user, I can retrieve a filtered list of paginated timesheet entries using the Spira APIs, to help me automate timesheet work [RQ:5040]
        - As an API user, I can delete relevant timesheets using the Spira APIs, to help me automate timesheet work [RQ:5041]
        - As an API user, I can delete relevant timesheet entries using the Spira APIs, to help me automate timesheet work [RQ:5042]

    * **Product Artifacts**

        - Improve the user experience of deleting artifact folders via the sidebar by giving users more information about the impacts and making the act of deletion more purposeful [RQ:5074]
        - Improve the user experience of deleting test case folders from the list by giving users more information about the impacts and making the act of deletion more purposeful [RQ:5095]
        - Improve the user experience of deleting Test Set folders from the list by giving users more information about the impacts and making the act of deletion more purposeful [RQ:5096]
        - Improve the user experience of deleting Task folders from the list by giving users more information about the impacts and making the act of deletion more purposeful [RQ:5097]
    
    * **SpiraApps**

    - Add support to SpiraApps to [retrieve the list of artifacts currently selected](../Developers/SpiraApps-Manager.md/#page-actions) in a list (using the function getGridSelectedItems) [RQ:5116]
    - As a SpiraApp developer, I can save [system level storage data](../Developers/SpiraApps-Manager.md/#storage) for my SpiraApp on [installation](../Developers/SpiraApps-Manifest.md/#storage), to enable richer user experiences [RQ:5057]
    
        * **[SpiraApps Storage: create](../Developers/SpiraApps-Manager.md/#storage)**

            - As a SpiraApp developer, I can create system storage data for my SpiraApp, to enable richer user experiences [RQ:5066]
            - As a SpiraApp developer, I can create user storage data for my SpiraApp, to enable richer user experiences [RQ:5067]
            - As a SpiraApp developer, I can create product storage data for my SpiraApp, to enable richer user experiences [RQ:5068]
            - As a SpiraApp developer, I can create product with user storage data for my SpiraApp, to enable richer user experiences [RQ:5053]
            
        * **[SpiraApps Storage: retrieve a single value for a key](../Developers/SpiraApps-Manager.md/#storage)**

            - As a SpiraApp developer, I can retrieve a single system storage value for my SpiraApp, to enable richer user experiences [RQ:5055]
            - As a SpiraApp developer, I can retrieve a single user storage value for my SpiraApp, to enable richer user experiences [RQ:5075]
            - As a SpiraApp developer, I can retrieve a single product storage value for my SpiraApp, to enable richer user experiences [RQ:5076]
            - As a SpiraApp developer, I can retrieve a single product and user storage value for my SpiraApp, to enable richer user experiences [RQ:5077]
        
        * **[SpiraApps Storage: retrieve multiple storage items for specific scenarios](../Developers/SpiraApps-Manager.md/#storage)**

            - As a SpiraApp developer, I can retrieve all system storage data for my SpiraApp, to enable richer user experiences [RQ:5069]
            - As a SpiraApp developer, I can retrieve all user storage data for my SpiraApp, to enable richer user experiences [RQ:5080]
            - As a SpiraApp developer, I can retrieve all product storage data for my SpiraApp, to enable richer user experiences [RQ:5079]
            - As a SpiraApp developer, I can retrieve all product with user storage data for my SpiraApp, to enable richer user experiences [RQ:5078]
        
        * **[SpiraApps Storage: update a single value for a key](../Developers/SpiraApps-Manager.md/#storage)**

            - As a SpiraApp developer, I can update system storage data for my SpiraApp, to enable richer user experiences [RQ:5054]
            - As a SpiraApp developer, I can update user storage data for my SpiraApp, to enable richer user experiences [RQ:5071]
            - As a SpiraApp developer, I can update product storage data for my SpiraApp, to enable richer user experiences [RQ:5072]
            - As a SpiraApp developer, I can update product with user storage data for my SpiraApp, to enable richer user experiences [RQ:5073]
        
        * **[SpiraApps Storage: delete a single item](../Developers/SpiraApps-Manager.md/#storage)**

            - As a SpiraApp developer, I can delete a single system storage item for my SpiraApp, to enable richer user experiences [RQ:5056]
            - As a SpiraApp developer, I can delete a single user storage item for my SpiraApp, to enable richer user experiences [RQ:5089]
            - As a SpiraApp developer, I can delete a single product storage item for my SpiraApp, to enable richer user experiences [RQ:5088]
            - As a SpiraApp developer, I can delete a single product with storage item for my SpiraApp, to enable richer user experiences [RQ:5087]
        
        * **[SpiraApps Storage: delete all by a filter](../Developers/SpiraApps-Manager.md/#storage)**

            - As a SpiraApp developer, I can delete all system storage data for my SpiraApp, to enable richer user experiences [RQ:5090]
            - As a SpiraApp developer, I can delete all user storage data for my SpiraApp, to enable richer user experiences [RQ:5093]
            - As a SpiraApp developer, I can delete all product storage data for my SpiraApp, to enable richer user experiences [RQ:5092]
            - As a SpiraApp developer, I can delete all product with user storage data for my SpiraApp, to enable richer user experiences [RQ:5091]
            - As a SpiraApp developer, I can delete all product with any user storage data for my SpiraApp, to enable richer user experiences [RQ:5098]

??? bug "Bug fixes and enhancements"
    - Allow users to view history detail records that happened prior to an artifact being deleted [IN:10215]
    - Convert adding an artifact to the timesheet from a 2 step process to a 1 step process, by immediately creating the row when it is selected from the dropdown [IN:10317]
    - Do not let TaraVault users create new repositories of type Subversion, and display a message on the TaraVault Configuration page to this effect [IN:10547]
    - Fix system admins, who are not also timesheet managers, from being able to update other users' timesheets via the API [IN:10545]
    - Fix the API to retrieve an individual timesheet throwing an error when requesting a timesheet that does not exist [IN:10507]
    - Fix the label under the My Timesheet grid to always show and to be called "Last Update" [IN:10572]
    - Fix the my timesheet grid to properly updated the disabled state of timesheet rows, after you switch timesheets using the calendar control [IN:10436]
    - Fix timesheets not being fully editable or able to be deleted when timesheet approvals are disabled, regardless of the timesheet's status [IN:10410]
    - Improve performance when refreshing the test case parameters hierarchy (by an estimated 45%) [IN:10306]
    - Improve the performance of inserting a new requirement [IN:7974]
    - Improve the SpiraApp reloadGrid function to allow it to refresh the full artifact list grid [IN:10565]
    - Log the initial database version in the installer's log file when performing any upgrade task [IN:10387]
    - Prevent drag and drop mouse operations on time inputs on my timesheet, to ensure times are always correctly recorded [IN:10424]
    - Return the user's MFA status in v7 API calls that return user information, to provide this useful extra information to API end users [IN:10396]

## Version 8.6 (December 2024)
!!! info "Summary"
    Users can now create [timesheets](../Spira-User-Manual/Timesheets.md/#my-timesheet) in the past, delete timesheets, or download them as CSV files for offline analysis or records. With approvals enabled, users can also submit timesheets for approval (full feature set coming in early 2025). <span class="pill">SpiraTeam</span> <span class="pill">SpiraPlan</span>

    Ahead of full timesheet approval workflows, system admins can enable or disable [system-wide approvals](../Spira-Administration-Guide/System.md/#general-settings), and flag specific users as [timesheet managers](../Spira-Administration-Guide/System-Users.md/#edit-an-existing-user), to help them prepare for future functionality. <span class="pill">SpiraPlan</span>

??? success "New Features"
    * **My Timesheet** <span class="pill">SpiraTeam</span> <span class="pill">SpiraPlan</span>

        - As a developer, I can [download](../Spira-User-Manual/Timesheets.md/#downloading) the data in a timesheet to a CSV file, to help me track and analyze my time [RQ:4942]
        - As a developer, I can [create a timesheet for any past date range](../Spira-User-Manual/Timesheets.md/#my-timesheet), so I can record my historical work correctly [RQ:4944]
        - As a developer, I can easily [delete an artifact row](../Spira-User-Manual/Timesheets.md/#deleting) from a timesheet, so I can easily correct data entered by mistake [RQ:4947]
        - As a developer, I can [delete a whole timesheet](../Spira-User-Manual/Timesheets.md/#deleting), so I can easily correct data entered by mistake [RQ:4948]
    
    * **As a developer, I can submit and manage my timesheets to get them approved by a manager, to officially record my time** <span class="pill">SpiraPlan</span>

        - As a developer with [timesheet approvals enabled](../Spira-User-Manual/Timesheets.md/#my-timesheet-approvals), I can see the status of any timesheet, to help me manage my timesheets [RQ:4963]
        - As a developer with [timesheet approvals enabled](../Spira-User-Manual/Timesheets.md/#my-timesheet-approvals), I can submit any draft timesheet for approval, to get my timesheet reviewed by a manager [RQ:4969]
        - As a developer with [timesheet approvals enabled](../Spira-User-Manual/Timesheets.md/#my-timesheet-approvals), I cannot edit a timesheet that has been submitted for approval, to ensure the manager works from the correct data [RQ:4972]
        - As a developer with [timesheet approvals enabled](../Spira-User-Manual/Timesheets.md/#my-timesheet-approvals), I cannot delete a timesheet that has been submitted, to ensure the integrity of data a manager has reviewed [RQ:4973]

    * **Timesheet administration** <span class="pill">SpiraPlan</span>

        - As a system admin of SpiraPlan, I can [enable timesheet approvals](../Spira-Administration-Guide/System.md/#general-settings), so people can make use of that feature or not [RQ:4961]
        - As a system admin of SpiraPlan, I can make people [timesheet managers](../Spira-Administration-Guide/System-Users.md/#edit-an-existing-user), so that they can approve timesheets as needed [RQ:4962]

    * **Timesheet API functions** <span class="pill">SpiraTeam</span> <span class="pill">SpiraPlan</span>

        - As an API user, I can create timesheets using the Spira APIs, to help me automate timesheet work [RQ:5029]
        - As an API user, I can retrieve a single timesheet using the Spira APIs, to help me automate timesheet work [RQ:5035]
        - As an API user, I can retrieve a filtered list of paginated timesheets using the Spira APIs, to help me automate timesheet work [RQ:5037]
        - As an API user, I can retrieve all timesheet entries by timesheet using the Spira APIs, to help me automate timesheet work [RQ:5039]

    * **My Page**
        - Limit the My Page assigned artifact widgets to only show artifacts from products a user is a member of [RQ:5043]

??? bug "Bug fixes and enhancements"
    - Add "N/A" status to test set, test set folder, and test case folder progress bar tooltips, to keep the execution status tooltip count consistent with the count displayed next to the artifact / folder name [IN:9984]
    - Add an api call to retrieve the total number of commits in a specific source code branch [IN:10269]
    - Add database support for SpiraApps saving storage key value pairs for fast retrieval and provider rich integration options for developers (developer side features coming in early 2025) [IN:9895]
    - Add the ability for SpiraApps to hide and show items from [dropdown lists programmatically](../Developers/SpiraApps-Manager.md/#page-actions) [IN:9575]
    - Fix certain keyboard operations not operating correctly when navigating elements, due to a bug in how the user dropdown menu handled keyboard events [IN:9943]
    - Fix filtering test runs by custom property column from the [test run tab on the test set details page](../Spira-User-Manual/Test-Set-Management.md/#test-runs) not working [IN:10178]
    - Fix potential errors when [cloning a product](../Spira-Administration-Guide/System-Workspaces.md/#product-cloning) caused by test step parameter names not being correctly checked for uniqueness [IN:7825]
    - Fix the [automated section on the test run details page](../Spira-User-Manual/Test-Run-Management.md/#test-run-details) saving incorrectly when other parts of test runs are modified [IN:8003]
    - Fix the custom dashboard types for SpiraApps potentially causing a database violation error for some users [IN:10163]
    - Improve the usability of the [product membership admin grid](../Spira-Administration-Guide/Product-Users.md) on smaller screens so it does not obscure other content [IN:9760]
    - Make the dropdown options wider on the [My Timesheet](../Spira-User-Manual/Timesheets.md/#my-timesheet) "Choose an artifact" selector [IN:10315]


## Version 8.5 (November 2024)
!!! info "Summary"
    - Following the introduction of the new [My Timesheet](../Spira-User-Manual/Timesheets.md/#my-timesheet) page, this release lets users edit or reset existing timesheet entries. <span class="pill">SpiraTeam</span> <span class="pill">SpiraPlan</span>
    - Timesheet [custom report views](../Reporting/Custom-Report-Tables.md) are now available to help you analyze timesheets across your entire organization. <span class="pill">SpiraTeam</span> <span class="pill">SpiraPlan</span>
    - [Product cloning](../Spira-Administration-Guide/System-Workspaces.md/#product-cloning) now copies over all saved filters against a product to improve the user experience. <span class="pill">SpiraTeam</span> <span class="pill">SpiraPlan</span>
    - We continue to enhance what is possible with SpiraApps and improve the [developer experience](../Developers/SpiraApps-Overview.md), based on feedback. This includes SpiraApps being able to run from the product admin settings page. <span class="pill">SpiraTeam</span> <span class="pill">SpiraPlan</span>

??? success "New Features"
    * **My Timesheet**

        - As a developer, I can edit previously recorded timesheet entries, so that I can correct them [RQ:4938]
        - As a developer, I can remove previously recorded timesheet entries by setting them to 0, so that I can correct them [RQ:4939]
        - As a developer, I can update task actual effort recorded against timesheets by editing timesheets, so that I can correct them [RQ:4940]
        - As a developer, I can update incident actual effort recorded against timesheets by editing timesheets, so that I can correct them [RQ:4941]

    * **Timesheet reporting**

        - As a report admin, I can access a custom report view for all [timesheets in the system](../Reporting/Custom-Report-Tables.md/#timesheets), to help create useful reports and analysis [RQ:4951]
        - As a report admin, I can access a custom report view for all [timesheet statuses](../Reporting/Custom-Report-Tables.md/#timesheet-statuses), to help create useful reports and analysis [RQ:4952]
        - As a report admin, I can access a custom report view for all [timesheets with their matching entries](../Reporting/Custom-Report-Tables.md/#timesheets-with-entries), to help create useful reports and analysis [RQ:4954]
        - As a report admin, I can access a custom report view for all [timesheet entries](../Reporting/Custom-Report-Tables.md/#timesheet-entries) in the system, to help create useful reports and analysis [RQ:4953]

    * **Product Cloning**

        - When doing a reset [clone of a product](../Spira-Administration-Guide/System-Workspaces.md/#product-cloning), and keeping the original template, also clone any saved filters on the product [RQ:4983]
        - When doing a full [clone of a product](../Spira-Administration-Guide/System-Workspaces.md/#product-cloning), and keeping the original template, also clone any saved filters on the product [RQ:4980]

??? bug "Bug fixes and enhancements"

    - Disable cells on My Timesheet for pre-existing rows when a user no longer has the ability to modify the related artifact [IN:10180]
    - Fix add, edit, and remove icons not displaying on the [product membership admin page](../Spira-Administration-Guide/Product-Users.md/#editing-users) at narrower page widths [IN:10169]
    - Fix data mappings for requirement, test case, and incident throwing an error on saving component mappings when a [product is cloned](../Spira-Administration-Guide/System-Workspaces.md/#product-cloning) or [created from an existing product](../Spira-Administration-Guide/System-Workspaces.md/#add-a-new-product) [IN:9982]
    - Fix list and multi-list custom properties on the test run list page and test set test runs tab being displayed as blank or numbers instead of actual values for non cross product test runs [IN:10144]
    - Fix not being able to add a tag to a new incident during test execution [IN:9997]
    
    * **SpiraApps**
    
        - Add a function to SpiraAppManager "[executeApiAsync](../Developers/SpiraApps-Manager.md/#internal-api-calls)" that returns a promise, to provide an alternative to the existing callback functionality [IN:9631]
        - Add a helper to SpiraApp javascript loaded on home pages for "[WIDGET_ELEMENT](../Developers/SpiraApps-Reference.md/#inflectra-javascript-helpers)" to provide a streamlined way for developers to interact with the widget HTML element [IN:9872]
        - Add [enums to the SpiraAppManager](../Developers/SpiraApps-Manager.md/#properties) to help developers more easily access and query data for artifact names, artifact types, requirement statuses, and test case statuses [IN:9876]
        - Add functionality to the SpiraAppsManager to return [localized Spira Artifact names](../Developers/SpiraApps-Manager.md/#properties), to provide better user experiences [IN:9812]
        - Add support for a SpiraApp [product admin setting](../Developers/SpiraApps-Manifest.md/#product-admin-settings) to show a dropdown of types for an artifact and allow admins to select a single type [IN:10124]
        - Add support for a SpiraApp [product admin setting](../Developers/SpiraApps-Manifest.md/#product-admin-settings) to show a dropdown of types for an artifact and allow admins to select multiple types [IN:10225]
        - Fix artifact status multi select [product setting type](../Developers/SpiraApps-Manifest.md/#product-admin-settings) does not working for SpiraApps on the SpiraApp product admin setting screen [IN:9766]
        - Let SpiraApps provide more dynamic experiences on the SpiraApp [product details admin page](../Spira-Administration-Guide/Product-General-Settings.md/#spiraapp-settings), with the ability to run javascript and add interactive buttons [IN:10128]
        - Transfer many SpiraApps that ship with Spira to the [marketplace](https://www.inflectra.com/Products/SpiraApps/) to improve discoverability for users [IN:10097]

## Version 8.4 (October 2024)
!!! info "Summary"
    My Timecard has been replaced with a completely new My Timesheet page. Record your work against tasks and incidents day by day to accurately track your time. This is the first in a range of upcoming time management features. <span class="pill">SpiraTeam</span> <span class="pill">SpiraPlan</span>

    On every artifact list page there is a button that lets you download the current view of the grid (with its filters and columns) as a CSV file.

    Teams functionality is now out of beta, and available for all users. <span class="pill">SpiraPlan</span>
    

??? success "New Features"
    * **[As a developer, I can track the time I spend against my assigned work on what dates, so that I can keep clear records](../Spira-User-Manual/Timesheets.md/#my-timesheet)**

        - As a developer, when I go to the "My Timesheet" page I see a grid with the current working week, so I can prepare to track my time [RQ:4835]
        - As a developer, I can add a row to the current timesheet for any incident or task assigned to me in any product, so I will be able to log my work [RQ:4836]
        - As a developer, I can add time data to any row in the current timesheet, so I can track my hours worked where [RQ:4856]
        - As a developer, I can save time data to any row in the current timesheet, so I can track my hours worked where [RQ:4837]
        - As a developer, when I update my timesheet data for a single task, then the actual effort is correctly updated on that task, so the work is logged correctly [RQ:4850]
        - As a developer, when I update my timesheet data for multiple tasks at once, then the actual effort is correctly updated on those tasks, so the work is logged correctly [RQ:4838]
        - As a developer, when I update my timesheet data for a single incident, then the actual effort is correctly updated on that incident, so the work is logged correctly [RQ:4851]
        - As a developer, when I update my timesheet data for multiple incidents at once, then the actual effort is correctly updated on those incidents, so the work is logged correctly [RQ:4839]
        - As a developer, when I update my timesheet data for tasks and incidents at the same time, then the actual effort is correctly updated on those artifacts, so the work is logged correctly [RQ:4852]
        - As a developer, I can see the total time I spent working each day on the timesheet, so I can better understand my work [RQ:4853]
        - As a developer, I can see the total time I spent working on each artifact on the timesheet, so I can better understand my work [RQ:4840]
        - As a developer, I can see the total time I spent working across the entire timesheet, so I can better understand my work [RQ:4855]
        - As a developer, I can clearly see the current date if relevant on my timesheet, so I can easily add time to today [RQ:4842]
        - As a developer, I can view my old timesheets, so that I can review and add to my previous entries [RQ:4841]
        - As a developer, I can clearly see all the columns on the timesheet, to give me an easy to use experience [RQ:4857]

    * **Add the ability for users to [download their current list page view to a CSV file](../Spira-User-Manual/Application-Wide.md/#download-as-csv)**

        - As a requirement user, I can download the current data I see on the sortable list page as a csv file [RQ:4956]
        - As a requirement user, I can download the current data I see on the hierarchical list page as a csv file [RQ:4918]
        - As a release user, I can download the current data I see on the list page as a csv file [RQ:4919]
        - As a requirement user, I can expand and collapse the hierarchical list page and then download the data I see as a CSV file [RQ:4921]
        - As a document user, I can download the current data I see on the list page as a csv file [RQ:4924]
        - As an automation host user, I can download the current data I see on the list page as a csv file [RQ:4923]
        - As a test case user, I can download the current data I see on the list page as a csv file [RQ:4933]
        - As a test configuration user, I can download the current data I see on the list page as a csv file [RQ:4934]
        - As a test run user, I can download the current data I see on the list page as a csv file [RQ:4935]
        - As a test set user, I can download the current data I see on the list page as a csv file [RQ:4936]
        - As a pull request user, I can download the current data I see on the list page as a csv file [RQ:4929]
        - As an incident user, I can download the current data I see on the list page as a csv file [RQ:4925]
        - As a task user, I can download the current data I see on the list page as a csv file [RQ:4917]
        - As a risk user, I can download the current data I see on the list page as a csv file [RQ:4922]
        - As a resource user, I can download the current data I see on the list page as a csv file [RQ:4930]
        - As a program release user, I can download the current data I see on the list page as a csv file [RQ:4920]
        - As a program incident user, I can download the current data I see on the list page as a csv file [RQ:4926]
        - As a program milestone user, I can download the current data I see on the list page as a csv file [RQ:4927]
        - As a capability user, I can download the current data I see on the list page as a csv file [RQ:4928]

??? bug "Bug fixes and enhancements"


    * **SpiraApps**:

        - Add a link at the top of the admin SpiraApps list pages to our website "marketplace" page so people can find more SpiraApps to install more easily [IN:9817]
        - Add details page pre-save event to SpiraAppManager to allow SpiraApps to modify the results of a saved form without needing to make it's own API call to do so after the original save [IN:9800]
        - Add Support for Calling [AWS Bedrock](../Developers/SpiraApps-Manager.md/#aws-bedrock-api-calls) APIs from SpiraAppManager [IN:10034]
        - Fix the boolean setting for SpiraApp settings causing a database violation error for some users who upgraded to 8.3 [IN:10145]
        - Fix the SpiraAppManager.myPageIsFilterByProject [property](../Developers/SpiraApps-Manager.md/#properties) not always returning the correct value on the My Page [IN:9765]
        - Update SpiraAppManager function(s) getDataItemField and updateFormField to handle blank data properties, to allow developers to more easily access & update the values of fields on details pages [IN:9820]
    
    * **Enhancements**:
        
        - Add event log entries when a user does an action in [Data Tools](../Spira-Administration-Guide/Product-General-Settings.md/#product-data-tools) [IN:9836]
        - Add the product name and link to the heading of the [product membership administration page](../Spira-Administration-Guide/Product-Users.md/#add-users-to-a-product) when adding new users to the product [IN:9842]
        - Move Teams out of 'Beta' so that all SpiraPlan customers can use its features without worrying about beta functions [IN:9893]
        - Update API v5, v6, and v7 to fully support cross product test sets [IN:9785]
        - Update Jira dataSync details pages "Sync Mode" label to provide a summary about the optional NoAttachments flag [IN:9862]

    * **Bug Fixes**:

        - Disable Test Case Test Step Section Edit buttons based on the Workflow to stop unauthorized users being able to edit test steps when using live loading specifically [IN:9270]
        - Fix localization not working for the column names of the grid on the Product Membership page [IN:10076]
        - Fix often not being able to move a folder into one beneath it from the folder edit dialog (as the lower folders are missing from the dropdown) [IN:9845]
        - Fix product admin [Data Tools](../Spira-Administration-Guide/Product-General-Settings.md/#product-data-tools) not fixing indentation problems found with releases [IN:9937]
        - Fix product admin [Data Tools](../Spira-Administration-Guide/Product-General-Settings.md/#product-data-tools) not fixing indentation problems found with requirements [IN:9752]
        - Fix subversion repos not supporting revisions that have the same file added or removed [IN:9931]
        - Fix Test Case Parameter Refresh potentially deleting parameters if a database error occurs [IN:9737]
        - Fix the automation host Test Run List (and counting number) not including cross product executions [IN:10120]
        - Fix the task details page sidebar showing incorrect or invalid tooltips for requirements when displaying for requirements and releases when displaying for releases (instead show no tooltip at all) [IN:9851]
        - Fix the test case details page test sets tab not showing test sets from other products that the test case is in [IN:9805]
        - Fix the test run counting number on the test Set details page not including cross product executions [IN:10121]
        - Fix the v6 and v7 SOAP APIs not correctly and consistently handling API key credentials [IN:9850]
        - Fix the v7.0 SOAP API not letting you create users if the product with ID 1 has been deleted [IN:9985]





## Version 8.3 (August 2024)
!!! info "Summary"
    - Adds database support for upcoming timesheet functionality
    - Adds and improves 15 [custom report views](../Reporting/Custom-Report-Tables.md) to help users create even more powerful reports more easily
    - New and improved German localization


??? bug "Bug fixes and enhancements"
    - **New [custom report views](../Reporting/Custom-Report-Tables.md)**
        - Add a custom report view for pending test runs [IN:3897]
        - Add a custom report view R_ArtifactAssociation_Extended that extends the normal association view to include a 'Name' column [IN:9256]
        - Add a custom report view R_RequirementIncidents_Extended that includes requirement and incident name columns [IN:9257]
        - Add a custom report view R_BuildStatus so report admins to create more useful build custom reports [IN:9311]
        - Add a custom report view for Task Folders [IN:9388]
        - Add a custom report view for R_ProjectGroup_MembershipUsers [IN:9504]
        - Add a custom report view for Requirement Importances [IN:9639]
        - Add a custom report view for Test Case Priorities [IN:9640]

    - **Improved [custom report views](../Reporting/Custom-Report-Tables.md)**
        - Update the R_TestRunIncidents custom report to include a test step and test run step id columns [IN:7461]
        - Update the R_TestCaseFolders custom report table to include HIERARCHY_LEVEL and INDENT_LEVEL columns [IN:8570]
        - Update the TestConfigurationEntries custom report view to include a PROJECT_ID column [IN:8645]
        - Update the R_RiskMitigations custom report view to include a Project_ID column [IN:9389]
        - Update the R_TestSets custom report views to include a PROJECT_IS_ACTIVE field, in addition to the PROJECT_ACTIVE_YN field [IN:9391]
        - Update the R_TestSetFolders custom report table to include HIERARCHY_LEVEL and INDENT_LEVEL columns [IN:9831]

    - **[FMEA](../SpiraApps/FMEA.md) and Risk SpiraApps**
        - Add a new Risk SpiraApp to force risk review dates to be required to be earlier than their closed dates within a project or workflow [IN:9410]
        - Correct a small typo in the FMEA SpiraApp product settings description [IN:9485]
        - Display Risk description in FMEA widget tooltip when highlighting Risk name [IN:7296]
        - Fix the FMEA SpiraApp so that selecting an incorrect custom property type does not cause problems on the Product Home Page [IN:7309]
        - Update the FMEA SpiraApp to the latest version to ensure users have access to additional features [IN:9816]
        
    - **SpiraApp developer tooling**
        - Add new functionality to the SpiraApps manager to expose a function to developers to [safely sanitize HMTL](../Developers/SpiraApps-Manager.md/#format-helpers) [IN:9629]
        - Add new functionality to the SpiraApps manager to expose a function to developers to [safely convert HMTL to plain text](../Developers/SpiraApps-Manager.md/#format-helpers) [IN:9630]
        - Add support for a boolean [setting type](../Developers/SpiraApps-Reference.md/#setting-types) for [SpiraApp product settings](../Developers/SpiraApps-Manifest.md/#product-admin-settings) [IN:9628]
        - Add support for a boolean [setting type](../Developers/SpiraApps-Reference.md/#setting-types) for [SpiraApp system settings](../Developers/SpiraApps-Manifest.md/#system-admin-settings) [IN:9767]
        - Fix artifact status single select [product setting type](../Developers/SpiraApps-Reference.md/#setting-types) not working for SpiraApps [IN:9668]

    - **Other**
        - Add enhanced database support for upcoming timesheet features, in particular around timesheet approval management [IN:9722]
        - Add the product name and link to the heading of the [product membership administration page](../Spira-Administration-Guide/Product-Users.md/#product-membership), after it was removed in 8.2.0.0 [IN:9755]
        - Fix auto-refreshing incident tab content from release and test step details pages when switching artifacts from left side menu [IN:9746]
        - Fix error messages when running background threads sometimes causing exceptions [IN:9565]
        - Fix cross product test cases in test sets not being maintained correctly after cloning a product [IN:9611]
        - Fix not being able to view a test run details page or test run report if a test set linked to a test run is soft deleted [introduced in 8.2] [IN:9823]
        - Fix test run custom properties being saved to a cross-product test case's test run using a different template to that of the test set, when creating the test run with the API [IN:9696]
        - Fix the default sort order of the [product membership page](../Spira-Administration-Guide/Product-Users.md/#product-membership) to be by Name ascending, and not userId ascending [introduced in 8.2.0.0] [IN:9735]
        - Fix the link to a test run result in the test case section on the test set details page when the test run is in another product [IN:9771]
        - Fix the test run tab for tests sets so that any test runs from other products are not editable [IN:9772]
        - Improve the error message when a test run generation failure is caused by product association revocation to let the user know the impacted product(s) or test cases [IN:9600]
        - Improve Spira's German localization with fully revised and corrected translations [IN:9740]


## Version 8.2 (July 2024)
!!! info "Summary"
    Test sets can include [test cases from multiple different products](../Spira-User-Manual/Test-Set-Management.md/#cross-product-test-cases), allowing teams to execute and report against test sets more powerfully and flexibly than ever before.
    
    The [product and team membership admin pages](../Spira-Administration-Guide/Product-Users.md/#product-membership) now provide a unified, modern, lightning fast experience. With improved performance and usability, they make managing membership a breeze, even in products with tens of thousands of members.
    
    As part of our efforts to enhance the [auditability](../Spira-Administration-Guide/System.md/#system-history-changes) and traceability of administrator activities, all changes made to a user and their profile are tracked in system history.

    Improvements to relevant list pages, make it easier to [edit and filter by tags](../Spira-User-Manual/Application-Wide.md/#tags).

    New [SpiraApp to enhance the experience of using Spira with BDD](../SpiraApps/BDD.md), including automatic syntax highlighting and generating feature files from existing requirements, tests, and risks.


??? success "New Features"
    * **User Management**

        - As a system admin, I can see a [read only history of admin changes made to user profiles in the system history](../Spira-Administration-Guide/System.md/#system-history-changes), so I can quickly audit changes to users [RQ:4807]

    * **[Product Membership](../Spira-Administration-Guide/Product-Users.md/#product-membership)**

        - As a product admin, I can easily view a list of active users who are not members of a product [RQ:4810]
        - As a product admin, I can easily add, remove, or modify team and product memberships [RQ:4811]
        - As a product admin, I can easily view, filter & sort the members of a product [RQ:4784]


    * **As a test set manager, I can [include test cases from other products in a test set](../Spira-User-Manual/Test-Set-Management.md/#cross-product-test-cases), and ensure my team can execute and report against those test sets accurately**

        - As a test set manager, I can add test cases to a test set from different products, to make the test set more powerful and useful [RQ:4806]
        - As a test set user, I can execute Test Sets with cross-product Test Cases, so I can fully complete the test sets assigned to me [RQ:4802]
        - As a test set user or manager, I can keep track of pending Test Sets with cross product Test Cases, so I can plan my work or my team's work efficiently [RQ:4803]
        - As a test manager, I can see accurate execution statuses for test cases run as part of test sets in other products, so I can fully track execution history [RQ:4804]
        - As a developer, I can use the Spira API to perform operations in Test Sets with cross product Test Cases in the same way as with those in the same product, so my integrations work consistently [RQ:4805]
        - As a reporter user, I can see the complete data from Test Sets with shared Test Cases [RQ:4808]

??? bug "Bug fixes and enhancements"
    * **[Product Membership](../Spira-Administration-Guide/Product-Users.md/#product-membership)**

        - Add the email address column on the Product Membership pages [IN:7060]
        - Improve administering large numbers of members of a product [IN:7280]
        - Fix the product membership page sometimes removing the wrong users from the project, or throwing errors when it should not [IN:9082]
    
    * **[Tags](../Spira-User-Manual/Application-Wide.md/#tags)**

        - Let users edit tags on list pages using the same dropdown control as they can on detail pages [IN:9172]
        - Let users filter tags on list pages with a dropdown control [IN:9179]
    
    - Add the ability for SpiraApps to listen for changes to [form dropdown fields](../Developers/SpiraApps-Manager.md/#page-actions) on details pages of artifacts (using a new registerEvent_dropdownChanged function) [IN:9574]
    - Automatically save the RSS Key when generating new tokens, or when turning RSS on from the [user profile page](../Spira-User-Manual/User-Product-Management.md/#my-profile) [IN:9584]
    - Automatically save the RSS Key when generating new tokens, or when turning RSS on from the [system admin edit user page](../Spira-Administration-Guide/System-Users.md/#edit-an-existing-user) [IN:9585]
    - Create source code provider configuration API endpoints to allow users with many products to set it up without needing to load the UI page for it [IN:9506]
    - Enable the field "EmailsEnabled" when system admins update users via the API [IN:9507]
    - Ensure ordering reports by custom properties works consistently across all languages [IN:9578]
    - Fix requirement statuses not being translated on the template admin [requirement status page](../Spira-Administration-Guide/Template-Requirements.md/#statuses) [IN:9503]
    - Fix the 'Generate New RSS Key' button on the [system admin user edit page](../Spira-Administration-Guide/System-Users.md/#edit-an-existing-user) to both create a new token and set RSS to enabled [IN:9599]
    - Fix upgrading to Spira v8+ not correctly updating data sync configuration files for on premise customers [IN:9653]
    - Improve the usability of the [email popup on artifact details pages](../Spira-User-Manual/Application-Wide.md/#emailing) to reduce the chance of people accidentally sending the same email multiple times [IN:9544]
    
## Version 8.1 (June 2024)
!!! info "Summary"
    In addition to using AWS CodeCommit, [AWS CodeBuild now integrates with Spira](../Build-Server-Integration/AWS-CodeBuild.md), so you can see the CodeBuild results on releases and sprints.

    As part of our efforts to enhance the [auditability](../Spira-Administration-Guide/System.md/#system-history-changes) and traceability of administrator activities, all changes to product roles are now tracked in system history.



??? success "New Features"
    - As a system admin, I can see a read only history of product role changes in the [system history](../Spira-Administration-Guide/System.md/#system-history-changes), so I can quickly audit changes to product roles [RQ:4776]

??? bug "Bug fixes and enhancements"
    - Add functionality to the SpiraApp manager so developers can [listen to grids](../Developers/SpiraApps-Manager.md/#events-handlers) loading for [requirement steps, test steps, and risk mitigations](../Developers/SpiraApps-Reference.md/#available-grid-ids) on their details pages [IN:9566]
    - Add keyboard shortcuts for risks to the keyboard shortcut reference [IN:9512]
    - Add the ability for Spira and AWS customers to record the results of [AWS CodeBuilds](../Build-Server-Integration/AWS-CodeBuild.md) (including from CodePipeline) as builds against releases/sprints [IN:9523]
    - Fix a user having a certain timezone set on their profile causing pages to load with an error [IN:9411]
    - Fix text custom properties always sorting by descending in reports (introduced in 7.12) [IN:9451]
    - Fix the [product history pages](../Spira-Administration-Guide/Product-General-Settings.md/#product-history-changes) showing product membership changed by the user changed, not the admin who made the change, when deleting the membership from the user details page [IN:9458]
    - Fix the [system history](../Spira-Administration-Guide/System.md/#system-history-changes) details screen only showing the first 15 fields changed, instead of showing all changed fields [IN:9414]
    - Fix the [system history](../Spira-Administration-Guide/System.md/#system-history-changes) list page showing a time that does not account for the admin's time-zone in tooltips for rows about changes to users [IN:9362]
    - Improve performance and compatibility by streamlining recently added indexes to tests to exclude long text fields [IN:9476]
    - Improve the label name for the [Jira data sync custom01](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md/#configure-the-plugin) field to avoid misinterpretation [IN:9277]
    - Remove keyboard shortcuts relating to the legacy planning board from the keyboard shortcut reference [IN:9511]
    - Remove the legacy planning board from the application as it is no longer needed given the new and improved main planning board [IN:9525]
    - Show our cloud customers that our SaaS solution is proudly Powered by AWS [IN:9513]
    - Update the test execution guided tours to describe the application as "Spira" not "SpiraTeam" [IN:9420]

## Version 8.0.0.1 (May 2024)

!!! bug "Bug fixes"

    - Improve handling when uploading larger SpiraApp bundles and packages [IN:9516]

## Version 8.0 (May 2024)
!!! info "Summary"
    Previously only available in SpiraPlan, now SpiraTeam users also have access to [risks and risk mitigations](../Spira-User-Manual/Risks-Management.md) to better manage their products.

    View test coverage for [requirements](../Spira-User-Manual/Requirements-Management.md/#requirement-details) and [releases](../Spira-User-Manual/Release-Management.md/#release-details) from their details pages, to make it easier than ever to assess test traceability.

    [SpiraApps](../SpiraApps/index.md) extend what is possible in Spira, addressing specific use cases. They are now open to [third party development](../Developers/SpiraApps-Overview.md), to give you far more options to tailor Spira to your needs.


??? success "New Features"
    - **SpiraApps**

        - As a system admin, I can install and manage SpiraApps created by developers with a [dedicated developer mode](../Spira-Administration-Guide/System.md/#general-settings) and features, to help me prototype and test locally developed SpiraApps [RQ:4781]
        - As a system admin, the SpiraApps [system admin list page](../Spira-Administration-Guide/System.md/#spiraapps) has an improved grid that makes it easier to review and act on installed SpiraApps [RQ:4780]
        - As a system admin, I can install officially distributed SpiraApp bundles, to allow me to enhance my organization's Spira [RQ:4787]
        - As a system admin, I can view [history entries](../Spira-Administration-Guide/System.md/#system-history-changes) for when SpiraApps are added, deleted, activated, or deactivated, to provide me with a clear audit trail for SpiraApps [RQ:4782]

??? bug "Bug fixes and enhancements"
    - Add an API call that will allow Spira to track when a data sync starts running or changes status from Not Run to In Progress [IN:8629]
    - Add more value to SpiraTeam by including full support for product [risks](../Spira-User-Manual/Risks-Management.md) [IN:9421]
    - Fix the test case folder count not updating correctly when one of its subfolder is deleted [IN:7165]
    - Fix v6 & v7 APIs to return the user's full name when getting project users (introduced in 7.13) [IN:9440]
    - Help admins get help or more information about a SpiraApp by showing the link of the SpiraApp on [their settings pages](../Spira-Administration-Guide/System.md/#spiraapp-settings) [IN:9416]
    - Improve SpiraApps for developers by requiring [API calls to third parties](../Developers/SpiraApps-Manager.md/#external-rest-calls) be made with reference to the guid and not the name of the SpiraApp [IN:9427]
    - Improve the SpiraApp developer experience with css nesting and [localStorage](../Developers/SpiraApps-Manager.md/#local-storage) support [IN:9417]
    - Show the test coverage indicator at the top of the [requirement details page](../Spira-User-Manual/Requirements-Management.md/#requirement-details) to help users see the same information the details page that they can on the list page [IN:9185]
    - Show the test coverage indicator at the top of the [release details page](../Spira-User-Manual/Release-Management.md/#release-details) to help users see the same information the details page that they can on the list page [IN:9186]
    - Update the SpiraPlan product name to use bold for "Spira" [IN:9418]
    - Upgrade the icon set used throughout the application to allow for future flexibility in icon design [IN:9296]