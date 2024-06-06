# Release Notes for Spira v8

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