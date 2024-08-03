# Release Notes for Spira v8
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