# Release Notes for Spira v9

## Version 9.4 (August 2026)
!!! info "Summary"
    Spira 9.4 focuses on performance and stability, with significant database query optimizations that improve responsiveness across the application, especially for products with large datasets and many custom properties. It also graduates [Strategic Outcomes](../Spira-User-Manual/Portfolio-Strategic-Outcomes.md) and [Portfolio Milestones](../Spira-User-Manual/Portfolio-Milestones.md) out of beta (SpiraPlan).

??? success "New Features"
    - [Portfolio Strategic Outcomes](../Spira-User-Manual/Portfolio-Strategic-Outcomes.md) and [Portfolio Milestones](../Spira-User-Manual/Portfolio-Milestones.md) are now generally available, having graduated from beta [IN:13112]
        {: .edition-spiraplan}
    - New RESTful API endpoints for handling Test Configuration Sets [IN:13129]
    - New API endpoint for updating the external key mapping of a Spira project for a data sync plugin [IN:13069]
    - Allow the Jira Server data sync to use comma-separated status values for requirement mapping [IN:13152]

??? bug "Bug fixes and enhancements"
    - Add Strategic Outcomes and Portfolio Milestones to sample Portfolios [IN:13145]
    - Fix a performance issue when products have many custom properties [IN:13116]
    - Performance enhancement for database query [IN:13192] [IN:13123] [IN:13126] [IN:13125] [IN:13132] [IN:13124] [IN:13211]
    - Fix Inflectra.ai EARS Improve Description throwing an error about electronic signatures when a Task addition triggers an unsaved Status change [IN:13074]
    - Fix access management for inactive portfolios [IN:13088]
    - Fix column sorting not working on the Strategic Outcomes list page [IN:13061]
    - Fix the missing progress bar on the Strategic Outcomes details page [IN:13096]
    - Fix inconsistent labeling between "Progress" on detail pages and "% Complete" on list pages for portfolio artifacts [IN:13097]
    - Fix the navigation sidebar row count exceeding the configured "Show Rows" threshold on Strategic Outcomes pages [IN:13105]
    - Fix Portfolio Milestone Strategic Outcomes tab not correctly loading tooltips [IN:13106]
    - Fix the Event Log Cleanup process not working correctly [IN:13008]
    - Fix upgrading to 9.3 failing for some free text indexing configurations [IN:13186]
    - Fix the installer not automatically updating installed SpiraApps to use new URL settings [IN:12878]
    - Increase the default maximum number of allowed keys in Web.config [IN:13206]

## Version 9.3 (July 2026)
!!! info "Summary"
    With new Portfolio artifacts in SpiraPlan, organizations can now better plan and manage high level goals with [Strategic Outcomes](../Spira-User-Manual/Portfolio-Strategic-Outcomes.md) and track key delivery targets with [Portfolio Milestones](../Spira-User-Manual/Portfolio-Milestones.md) across programs and products.
        {: .edition-spiraplan}

??? success "New Features"
    - Portfolio [Strategic Outcomes](../Spira-User-Manual/Portfolio-Strategic-Outcomes.md) and [Portfolio Milestones](../Spira-User-Manual/Portfolio-Milestones.md)
        {: .edition-spiraplan}

        - As a portfolio member, I can plan out the necessary work of the portfolio, linked to program capabilities and portfolio milestones, so I can ensure the portfolio objectives will be delivered [RQ:5682]
        - As a portfolio member, I can view, create, and edit strategic outcomes on a details page, so I can plan out portfolio level work needs [RQ:5685]
        - As a portfolio member, I can view, create, edit strategic outcomes on a filterable list page, so I can plan out portfolio level work needs [RQ:5683]
        - As a portfolio member, I can add or remove associations between strategic outcomes and this portfolio's program capabilities, so I can correctly organize my programs' capabilities [RQ:5686]
        - As a Portfolio member, I want to be able to make portfolio milestones to aggregate release progress and alignment at a high level across multiple program milestones [RQ:5688]
        - As a portfolio member, I can view and edit portfolio milestones on a details page, so I can plan out portfolio level work needs [RQ:5689]
        - As a portfolio member, I can view portfolio milestones on a filterable list page, so I can plan out portfolio level work needs [RQ:5691]
        - As a portfolio member, I can filter and sort the portfolio milestones list page by any available field, so that I can organize my milestones into the view I need at that moment [RQ:5694]
        - As a portfolio member, I can view portfolio milestones' program milestone start and end dates, to better manage program level timetables [RQ:5695]
        - As a portfolio member, I can add or remove associations between portfolio milestones and this portfolio's program milestones, so I can plan out the scope of the milestone [RQ:5692]
        - As a portfolio member, I can view strategic outcome associations to each portfolio milestone, to give me flexibility in seeing how the portfolio data is organized [RQ:5693]
        - As a portfolio member, I want to be able to open an Artifacts dropdown on portfolio pages to navigate to my portfolio milestones and strategic outcomes [RQ:5696]

??? bug "Bug fixes and enhancements"
    - Adds a new [Testing Setting](../Spira-Administration-Guide/Product-Planning.md/#testing-settings) to disable actual test duration recording [IN:12782]
    - Security enhancement for SpiraApps [IN:11359]

## Version 9.2 (June 2026)
??? bug "Bug fixes and enhancements"
    - Add a date selector to the data sync "Reset Sync" functionality [IN:12545]
    - Allow SpiraApps to show a popup dialog with dynamic content [RQ:9878]
    - Description improvements for the MFA enforcement feature in the application [IN:12426]
    - Fix a bug where a search dialog could cause hidden panels to appear [IN:12498]
    - Fix a bug where incident history change records for the Detected By field showed blank old and new values [IN:7592]
    - Fix a bug where the "Enable RSS Feeds" click area was oversized, causing accidental API token regeneration [IN:12562]
    - Fix a bug where users could not filter a resource view by Release [IN:12356]
    - Fix a database error when updating custom property state for an Incident Status in specific workflow configurations [IN:12729]
    - Fix a database timeout related to adding test cases to a release via the API [IN:12704]
    - Fix a permission escalation issue related to updating roles in a product [IN:12323]
    - Fix Anti-XSRF token errors when logging in via Chrome [IN:11832]
    - Fix incorrect HTTP protocol detection in certain reverse proxy configurations [IN:12732]
    - Fix project data tool API endpoints requiring incorrect permission levels [IN:12377]
    - Improve performance of recording test runs in the application [IN:12698]
    - Resolve database lock conflicts in high throughput scenarios [IN:12759]

## Version 9.1 (May 2026)
??? bug "Bug fixes and enhancements"
    
    - Add a lightweight banner to the login page to show users important Inflectra news or updates [IN:12621]
    - Documentation and Knowledge Base article updates and enhancements [IN:12479] [IN:12560] [IN:12464] [IN:12506] [IN:12558]
    - Fix a bug causing excessive log entries to be generated for test cases (introduced in 9.0) [IN:12609]
    - Fix a bug causing excessive warning entries in the notification log (introduced in 9.0) [IN:12634]
    - Fix a bug where cloning a product could fail under certain conditions [IN:12662]
    - Fix a bug where custom list API edits did not persist correctly (introduced in 9.0) [IN:12595]
    - Fix a bug where decimal custom properties did not save the precision value correctly [IN:12160]
    - Fix a bug where false notifications could be sent when reordering cards on planning boards [IN:12480]
    - Fix a bug where moving cards on the Planning Board could incorrectly update timestamps [IN:12622]
    - Fix a bug where test set execution status was not updated correctly after assigning a test run (introduced in 9.0) [IN:12601]
    - Fix a bug where the left panel could not be resized in certain views [IN:12556]
    - Fix a bug where the site could become temporarily inaccessible after an app pool restart (introduced in 9.0) [IN:12671]
    - Fix a bug with ADO Sync custom field metadata [IN:12650]
    - Fix a display issue in the Test Case Workflow condition section [IN:12297]
    - Fix a performance issue with workflow queries (introduced in 9.0) [IN:12594]
    - Improve Name and Description search behavior for Requirements and Releases, allowing users to search for exact phrases containing special characters or spaces [IN:12520]
    - Improve resilience of Data Tools jobs to transient database connection failures (introduced in 9.0) [IN:12620]
    - Update Enable 2-Step Authentication setup instructions [IN:12427]
    - Update Jira Data Sync "Time Offset" UI label for timezone clarity [IN:12493]
    - Upgrade Inflectra.ai to use newer AI models [IN:12451]

## Version 9.0.0.1 (April 2026)
??? bug "Bug fixes and enhancements"
    - Fix auto-truncation of fields not working as expected [IN:12586]
    - Fix incident workflow notifications without a defined subject have a mostly blank subject in the email [IN:12576]
    - Fix incompatible dashboard customizations for Spira 9.0 (by resetting all customizations to the defaults) [IN:12575]
    - Fix not truncating a release version number that is too long on the Release List Page [IN:12577]
    - Fix notifications for incident workflow transitions recipients [IN:12593]
    - Fix problems related to Event Log details for errors [IN:12574]
    - Fix program level planning board concurrency errors [IN:12557]
    - Fix test case history retrieval timing out for most test cases [IN:12587]
    - Fix user collection retrieval performance issue [IN:12589]
    - Fix users not being able to reset their password from the My Profile page [IN:12573]

## Version 9.0 (April 2026)
!!! info "Summary"
    With version 9 of Spira, we have upgraded much of the behind-the-scenes plumbing to improve stability and performance across the application. It also provides a solid foundation for future innovation.

    System administrators can now opt to enforce that all users logging in with a username and password (including with LDAP) also log in using a 2-Step Authentication token.

??? success "New Features"
    - Upgrade core data access infrastructure to improve performance, stability, and maintainability [RQ:5594] [RQ:5595] [RQ:5596]
    - As a system admin, I can force users to only be able to login to the application if they have MFA setup, to meet our organization's security and compliance needs [RQ:5608]

??? bug "Bug fixes and enhancements"
    - Fix a bug with custom properties in graphs [IN:12318]
    - Documentation improvements [IN:7186] [IN:11730] [IN:12192] [IN:12252] [IN:12291] [IN:12327] [IN:12343] [IN:12371] [IN:12697] [IN:12398] [IN:12423]
    - Fix a bug related to the Anti XSRF token error in Chrome under specific conditions [IN:11832]
    - Fix being unable to change the graph type view in some scenarios [IN:12300]
    - Fix being unable to filter requirements by "text field" in certain cases [IN:12359]
    - Fix endpoints being excluded from the OpenAPI documentation in edge cases [IN:12220]
    - Fix how history is recorded for test cases so that changes to the read-only "Test Steps" flag are recorded in history [IN:12004]
    - Fix left side artifact panel expansion not possible in some situations [IN:12249]
    - Fix login failure after email update for non-admin users [IN:12250]
    - Fix New Milestone page having no page title [IN:12314]
    - Fix non-admin users receiving an authorization error when attempting to delete an incident on the details page, even when they have the appropriate permissions [IN:12311]
    - Fix not being able to register an existing account to an external provider when 2-Step Authentication is enabled [IN:12386]
    - Fix the position of the follower card on artifact details pages [IN:12302]
    - Fix selection of invalid programs in planning boards [IN:12400]
    - Fix Test Execution window not fitting on the screen when there is a long description [IN:12247]
    - Fix Test Set Planned Date Calendar popup being obscured [IN:12405]
    - Fix the instant messenger occasionally showing messages in the wrong order [IN:12305]
    - Fix a bug in the My Subscribed Artifacts widget related to user permissions [IN:12006]
    - Rename Azure AD to Microsoft Entra ID throughout the application and documentation  [IN:12260] [IN:12259]
    - Improve the performance of custom filters on hierarchical Requirement lists [IN:12435]
    - Fix a bug related to retrieving capabilities using the v7 APIs for Spira [IN:12486]

