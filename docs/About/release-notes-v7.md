# Release Notes for Spira v7

## Version 7.3 (December 2022)

!!! info "Summary"
    Introducing our next generation planning board for SpiraTeam and SpiraPlan. Available as a beta alongside the existing planning board, the new board has a brand new look, big new features (including swimlanes), and simpler to use than ever.

    SpiraPlan admins can create teams and assign members of a product to those teams (in beta). Currently teams are available exclusively on the beta planning board.

??? Success "New Features"

    * **[Beta Planning Board](../../Spira-User-Manual/Planning-Board/#beta-planning-board)**

        - The new beta planning board has powerful functionality with a new layout and overhauled design to let you plan work effortlessly [RQ:4286]
        * **There are useful main display modes that dictate how you use the boards**

            - The Product backlog lets managers prioritize ("groom") unplanned work items that do not have a scheduled release [RQ:4368]
            - The Release backlog lets managers review planned or in progress work items [RQ:4369]
            - The sprint backlog lets managers review work in a release and its sprint, or for a single sprint [RQ:4370]
            - When working on the release or sprint backlog there is a release dropdown [RQ:4381]

        * **The planning board makes it easy to customize how the board is organized to help you focus on the right information **

            - Users can group the board by certain fields (based on the view) to show one board per member of the group [RQ:4372]
            - Within a board users can choose what field to organize data by as columns (the x-axis) [RQ:4373]
            - Within a board users can choose what field to organize data by as rows (the y-axis) [RQ:4374]
        
        * **Planning board cards design updated with greater customization**

            - Planning board cards always show a standard set of information that is useful and meaningful [RQ:4382]
            - Planning board cards can optionally show the artifact's description, type, status, and position [RQ:4375]
            - Planning board cards can optionally show the artifact's task progress and task mini indicators [RQ:4376]
            - Planning board cards can optionally show the artifact's test coverage and test case mini indicators [RQ:4377]
        
        * **Incident cards can be shown alongside requirement cards for certain views of the Planning Board**

            - When organizing the planning board by priority, incident priority names are matched to requirement importance names [RQ:4379]
            - Incident cards can be displayed alongside requirement cards in certain views of the planning board [RQ:4380]
            - Teams/Tracks Support in Boards (SpiraPlan only) [RQ:2316]

    * ** System Administration**

        - System admins [can enable or disable](../../Spira-Administration-Guide/System/#general-settings) beta functionality across the application for their users [RQ:4317]
        - System admins can create and manage [a list of team names](../../Spira-Administration-Guide/System-Users/#view--edit-teams) (SpiraPlan only) [RQ:3689]
        - Product admins can [associate product users to specific teams](../../Spira-Administration-Guide/Product-Users/#team-membership) [RQ:3690]


??? bug "Bug fixes and enhancements"

    - Retain the user-designated ordering on the planning board in all cases (including the first time a card is moved, and moving a card to the end of a stack) [IN:6467]
    - Ensure all incident progress tooltips are shown in the user's local time zone and not in UTC [IN:6573]
    - Improve performance by caching user avatar images in the browser [IN:7287]
    - Fix the SpiraApp for WorX actions that happen when you click the buttons in the column grids [IN:7391]
    - Do not restrict task start and end dates to its release's dates, so that changes to a task whose dates fall outside those of its release are not blocked [IN:7435]
    - Fix the status filter dropdown on the requirement sorted list page not being localized [IN:7470]
    - Show the correct testing settings for SpiraTest (show "Allow users to mark every step in a test case as N/A at once" and hide "Users can create tasks...") [IN:7488]
    - Fix concurrency dates and concurrency checks to serialize using the Invariant Culture to avoid problems using certain cultural settings (for example, Thai) [IN:7499]
    
    * **Logging in and out**

        - Fix a user being logged out and redirected to a broken URL by removing the product ID portion of this broken URL [IN:7584]
        - Fix the browser from getting stuck in a loop if there is unsaved user input after client-side forced session termination [IN:7587]
        - Fix the error that can occur when starting test execution if you have lost the authorization in the current tab for any reason [IN:7607]
        - Fix some actions on the detail pages causing a logged out user to be redirected to a broken URL if their Form Manager, onRetrieve wasn't calling proper URL redirect on Auth Failure [IN:7669]

    * **On premise installer**
    
        - Fix the installer for on premise customers so that users are informed when they are using an incorrect SQL Version for an upgrade [IN:7588]
        - Fix the wrong installer version number being recorded in the web.config file [IN:7612]
        - Fix edge case null reference exception in the installer [IN:7638]
        - When on premise customers upgrade, include the version they are upgrading from on the summary screen and in the log [IN:7610]
    
    * **Documentation and logging**
        - Change the color of the message box about the best browser to use for the document spreadsheet from red to yellow [IN:7563]
        - Clarify the API documentation about what happens when the user create call is made but the user already exists [IN:7618]
        - Fix the help link used for the Rapise Floating Licenses administration page [IN:7490]
        - Correct the v6 SOAP API documentation example for the Document_AddFile method documentation [IN:7654]
        - Record a success audit log message into the event log when any datasync 'Reset Sync' button is pressed. [IN:7525]
        - Turn off logging for a specific "TaraVault active for a product" check to not confuse users with extra noise in the logs [IN:7608]


## Version 7.2 (October 2022)

!!! info "Summary"
    Manage products in a whole new way (SpiraPlan only). New system level custom properties and custom lists let program users see and manage your products with custom data and through new dedicated pages and custom report options. You can use these new features for improved Project Portfolio Management, to implement product charts, and much more.

    Along with existing support for creating and editing dynamic documents inside Spira (including diagrams and documents), the new spreadsheet editor lets you create simple spreadsheets to better organize your teams and track work. You can have multiple sheets, apply formatting to cells, use a wide number of functions, and even import from and export to Excel spreadsheets.

??? Success "New Features"

    - Allow users to create and [edit simple spreadsheets](../../Spira-User-Manual/Document-Management/#editing-spreadsheets) as an option for inline documents [RQ:4322]
    - Email all system administrators every time that the concurrent user limit is exceeded by a user trying to login but can't due to license issues [RQ:4361]
    
    * **Improved Product Management and Customization**
        
        - System admins can add, edit, and remove up to 30 [custom properties](../../Spira-Administration-Guide/System-Custom-Properties/#edit-custom-properties), shared across all products [RQ:4147]
        - System admins can add and manage [system-wide custom lists](../../Spira-Administration-Guide/System-Custom-Properties/#edit-custom-lists) and their values [RQ:4150]
        - The program level [product list page](../../Spira-User-Manual/Program-Products/#product-list) shows all products in a program and lets users see, sort, and filter by any standard or custom field (but not edit) [RQ:4145]
        - The program level [product detail page](../../Spira-User-Manual/Program-Products/#product-details) lets users see all information about a specific product (including custom fields) [RQ:4146]
        - [Custom report views](../../Reporting/Custom-Report-Tables) support [product level custom properties](../../Reporting/Custom-Report-Tables/#global-system-custom-property-definitions), including on the [products report](../../Reporting/Custom-Report-Tables/#projects-products) [RQ:4192]


??? bug "Bug fixes and enhancements"

    - Add a link on the product home page, [overview widget](../../Spira-User-Manual/Product-Homepage/#product-overview) to the new product details page, shown to program members only [IN:7501]
    - Add a new dedicated "Account Lockout Period" [security setting](../../Spira-Administration-Guide/System/#security-settings), so system admins can specify how long a user is locked out for once they enter too many wrong passwords within the relevant window [IN:5010]
    - Add a new system admin [security setting](../../Spira-Administration-Guide/System/#security-settings) to enforce stricter security only possible on HTTPS sites [IN:7359]
    - Fix a typo in the 7.1 onboarding tour about TaraVault [IN:7443]
    - Fix editing tasks or requirements on the [release details page](../../Spira-User-Manual/Release-Management/#reqs-tasks) not triggering notification events [IN:6954]
    - Fix the documentation link on the user's [Add 2-Step Authentication](../../Spira-User-Manual/User-Product-Management/#2-step-authentication) page [IN:7396]
    - Improve explanatory text in two places in administration for the flag that [disables rollup calculations](../../Spira-Administration-Guide/Product-Planning/#testing-settings), and also the 2 pop-up messages [IN:7338]
    - Improve the error pages throughout the app, with a more consistent design in more places, and showing stack trace information to system admins only [IN:6293]
    - Reduce css file sizes by removing Internet Explorer 11 specific rules and values [IN:7412]
    - Show more of the test case names on the [test case grid](../../Spira-User-Manual/Test-Set-Management/#overview---test-cases) of the test set details page (up to 150 characters) [IN:7299]
    - Show the program artifact dropdown when a user goes to a program page before ever going to a product [IN:7474]
    - Update the minimum SQL Server required version under which SpiraPlan can be installed to 2016 [IN:7424]
    - Set the minimum required version of .NET that the application will work under to 4.8 [RQ:3085]
    - When a product has [rollup calculations disabled](../../Spira-Administration-Guide/Product-Planning/#testing-settings), also disable test case parameter hierarchy refreshes [IN:7422]


## Version 7.1 (August 2022)

!!! info "Summary"
    Cloud customers can now [more easily and flexibly set up source code integration](../../Spira-Administration-Guide/System/#taravault-for-source-code) inside SpiraTeam and SpiraPlan. TaraVault is the default provider for Git or Subversion. Along with other quality of enhancements you can now, for each product, either user TaraVault or any other cloud based source code provider. This lets you pick the best provider for each product.

    Our latest [SpiraApp integrates SpiraPlan and OctoPerf](../../SpiraApps/OctoPerf) seamlessly. Kick off load testing in OctoPerf directly from SpiraPlan and the results of the test get logged against each relevant test case.

??? Success "New Features"

    - Ability to switch (at a product level) cloud Spira between [TaraVault and external Git/Subversion](../../Spira-Administration-Guide/System/#taravault-for-source-code) [RQ:4287]
    - A new [SpiraApp integrates SpiraPlan with Octoperf](../../SpiraApps/OctoPerf) to allow users to launch tests directly from Spira and see relevant results as test runs [RQ:4121]

??? bug "Bug fixes and enhancements"

    - Improve diagram export options when viewing a diagram on the document details page to save a diagram as an SVG [IN:7134]
    - Replace Internet Explorer to Edge in sample data, as Internet Explorer has finally, officially retired [IN:7311]
    - Do not let a product have more than one source code provider in active use at any one time [IN:7321]
    - Let product admins disable / enable TaraVault for a product (in addition to full deactivation (hard deletion) as now) [IN:7324]
    - Fix typos and a screenshot in the 7.0 walkthrough popup [IN:7328]
    - Fix the documentation link on the System and Product Admin > SpiraApps settings pages [IN:7330]
    - Fix Product Template custom lists letting you save a blank value name (even though it shows an error suggesting this not allowed) [IN:7384]

    
## Version 7.0 (July 2022)

!!! info "Summary"
    [SpiraApps](../../SpiraApps) bring a brand new of tailoring SpiraTest, SpiraTeam, and SpiraPlan to your needs. Dedicated SpiraApps will extend what is possible, each addressing a specific use case. This release introduces the first 7 SpiraApps and expect more to follow:

    - The FMEA SpiraApp adds full support for Failure Mode & Effects Analysis (FMEA) in the Risk Management module in SpiraPlan (only - not available in SpiraTeam or SpiraTest)
    - New SpiraApps deepen the integration with Github Actions, GitLab Pipelines, and CircleCI Pipelines. Start a new Pipeline or Action directly from SpiraPlan.
    - Two new SpiraApps let you work faster than ever. Create rich descriptions that are automatically added when you create a new artifact. And quickly create a preset list of new tasks or test cases on a requirement or a release to manage workloads better than ever.

    We have updated our data synchronization platform to improve ease of use and simplify setup for administrators, with tailored guidance and information right inside the app.


??? success "New Features"
    * **Data synchronization**

        - Improve ease of use when configuring the most common datasync plugins with better field names and additional helper text [RQ:4280]

    * **Testing**

        - Add [testing setting to mark a whole test case during execution as N/A](../../Spira-Administration-Guide/Product-Planning/#testing-settings) with one click [RQ:4273]
        - Ability to schedule test cases in a test set by Planned Date on the [test case section of the test set details page](../../Spira-User-Manual/Test-Set-Management/#overview-test-cases), and through the API when mapping a new test set to a test case, or updating an existing mapping [RQ:4277]

    * **[SpiraApps](../../SpiraApps)**

        - [CircleCI SpiraApp](../../SpiraApps/CircleCI) integration lets users launch pipelines from Spira and see their results in Spira as builds [RQ:4141]
        - [GitLab CI SpiraApp](../../SpiraApps/GitLab) integration lets users launch pipelines from Spira and see their results in Spira as builds [RQ:4142]
        - [GitHub CI SpiraApp](../../SpiraApps/GitHub) integration lets users launch actions from Spira and see their results in Spira as builds [RQ:4143]
        - Extend the built-in risk functionality by supporting FMEA with a dedicated [FMEA SpiraApp](../../SpiraApps/FMEA) that calculates the Risk Priority Number [RQ:4140]
        - Improved [WorX Manual Testing Accelerator](../../SpiraApps/WorX) functionality, as a new SpiraApp [RQ:4225]
        - Allow users to quickly create [preset tasks or tests cases](../../SpiraApps/Task-Test-Presets) for a specific requirement or release [RQ:4176]
        - Allow users to create artifacts from their details pages with [pre-populated descriptions](../../SpiraApps/Default-Descriptions) (as defined in the SpiraApp settings) [RQ:4224]

    * **SpiraApps Administration**

        - The [system SpiraApps list page](../../Spira-Administration-Guide/System/#spiraapps) lets admins see all available SpiraApps and enable or disable them [RQ:4200]
        - The [system SpiraApps settings page](../../Spira-Administration-Guide/System/#spiraapp-settings) let sys admins manage any system-level settings for the SpiraApp [RQ:4202]
        - The [product SpiraApps list page](../../Spira-Administration-Guide/Product-General-Settings/#spiraapps) lets users see all system-wide active SpiraApps and enable or disable them for the product [RQ:4201]
        - The [product SpiraApps settings page](../../Spira-Administration-Guide/Product-General-Settings/#spiraapp-settings) let users manage any product-level settings for the SpiraApp [RQ:4203]
       
    * **[SpiraApps](../../SpiraApps) Architecture**

        - SpiraApps can be added by Inflectra, storing their functionality, logic, and descriptions in the system [RQ:4211]
        - SpiraApps can be configured by users with system-wide settings [RQ:4212]
        - SpiraApps can be configured by users with product-specific settings [RQ:4213]
        - SpiraApps can run from the button menu toolbar on specific artifact detail pages [RQ:4207]
        - SpiraApps can run from the button menu toolbar on specific artifact list pages [RQ:4206]
        - SpiraApps can run from a custom column shown on artifact grids [RQ:4208]
        - SpiraApps can display as a dashboard widget on the product and reporting home pages [RQ:4209]
        - SpiraApps can run as behind-the-scenes actions, running user-driven events, on artifact details pages [RQ:4214]


??? bug "Bug fixes and enhancements"

    - Add a new API call to get all requirements covered by a specific test case [IN:5862]
    - Add a new API call to update an existing test set test case mapping (can update its owner, planned date, and isTeardown status)  [RQ:4277]
    - Enforce a minimum of two minutes for [authentication expiry settings](../../Spira-Administration-Guide/System/#security-settings) [IN:7174]
    - Fix GitHub Actions integration so that results are always recorded, even if the JSON body contains longs (previously only ints were supported) [IN:7215]
    - Fix GitHub and CircleCI build creation dates not always being the correct timezone [IN:7270]
    - Fix incorrect special character display on the incident and risk workflow transition detail pages [IN:7197]
    - Fix LIS source code commit dates in sample data so that there are no commits in the future [IN:6881]
    - Fix some accented characters not displaying correctly in certain places [IN:7103]
    - Improve the experience of adding comments to an artifact by only showing the "Add Comment" button when a user cannot otherwise edit the artifact (but can add comments) [IN:7111]
    - Let users define product level 'definitions of done' to apply to a requirement through using the new "Task and Test Case Presets" SpiraApp [IN:6052]