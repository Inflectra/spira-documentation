# Release Notes for Spira v7


## Version 7.1 (August 2022)

!!! info "Summary"
Cloud customers can now [more easily and flexibly set up source code integration](../../Spira-Administration-Guide/System/#taravault-for-source-code) inside SpiraTeam and SpiraPlan. TaraVault is the default provider for Git or Subversion. Along with other quality of enhancements you can now, for each product, either user TaraVault or any other cloud based source code provider. This lets you pick the best provider for each product.

Our latest [SpiraApp integrates SpiraPlan and OctoPerf](../../SpiraApps/OctoPerf) seamlessly. Kick off load testing in OctoPerf directly from SpiraPlan and the results of the test get logged against each relevant test case.

??? Success "New Features"

    - Ability to switch (at a product level) cloud Spira between [TaraVault and external Git/Subversion](../../Spira-Administration-Guide/System/#taravault-for-source-code) [RQ:4287]
    - A new [SpiraApp integrates SpiraPlan with Octoperf](../../SpiraApps/OctoPer) to allow users to launch tests directly from Spira and see relevant results as test runs [RQ:4121]

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