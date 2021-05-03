# Release Notes for Spira v6

## Version 6.9 (May 2021)

!!! info "Summary"
    - **Improved [requirement document view](../../Spira-User-Manual/Requirements-Management/#requirements-document-view)** (SpiraTeam and SpiraPlan): Users can now customize which fields to display; edit requirement names, descriptions, and other rich text fields; and display the requirement hierarchy position as an outline code (e.g. 1.2.11). Navigation and pagination have also been improved.
    
    - **Baselining enhancements** (SpiraTeam and SpiraPlan): There are now [new views](../../Spira-Administration-Guide/Product-General-Settings/#baseline-artifact-details) and existing views improved to make it easier to see what changed in a baseline.

    - **Access custom report data from external tools** (SpiraPlan): First, we've added [lots more reporting views](../../Reporting/Custom-Report-Tables) to help build out even more queries (available in all editions of Spira). Next, SpiraPlan customers can use 3rd party tools like spreadsheets and database reporting packages to query and report against all custom report tables in the application via the ODATA standard (read our [in-depth tutorial](../../Reporting/OData-Tutorial)). This takes custom reports to a whole new level of integration and ease of use.

    - **Customize custom fields**: Custom properties have been turned up to 100 (minus 1). You can now have 99 custom properties for each artifact in a template. Order your custom properties how you like, and add a useful tooltip description for users to read on details pages. 

    **NOTE**: Internet Explorer is no longer supported by SpiraTest, SpiraTeam, or SpiraPlan. You should use a modern and secure browser instead.

??? success "New Features"

    * **[Requirements document view](../../Spira-User-Manual/Requirements-Management/#requirements-document-view)**

        - Users with bulk edit permission can [edit the name and rich text fields inline](../../Spira-User-Manual/Requirements-Management/#editing-the-requirements-documents) on the requirements documents list view [RQ:2953]
        - Users can [show or hide key standard fields](../../Spira-User-Manual/Requirements-Management/#requirements-document-options) on the requirements documents view [RQ:2954]
        - Users can [show or hide rich text custom properties](../../Spira-User-Manual/Requirements-Management/#requirements-document-options) on the requirements documents view [RQ:3047]
        - The requirements document view can optionally show the requirement's position in the hierarchy as an [outline number code](../../Spira-User-Manual/Requirements-Management/#requirements-document-options) (in a form like 1.1.2.4) [RQ:2958]
        - The requirements document view has improved [navigation](../../Spira-User-Manual/Requirements-Management/#requirements-document-navigation) where click an epic in the sidebar loads only that epic and its children, and the system remembers your selection [RQ:3065]
        - Users can quickly print the current requirement documents list with the addition of a dedicated on-page print button [RQ:3066]

    * **Custom Properties**

        - You can optionally set a position for custom properties to change the order custom properties are displayed in each section on details pages [RQ:3053]
        - You can optionally add a description to custom properties to explain to users how to use the field (they show as tooltips on details pages) [RQ:3055]
        - Each artifact that has custom properties already now supports an additional 69 custom properties in each template, bringing the total to 99 [RQ:3052]

    * **History and Baselining**

        - Clicking on Artifact Name on the [baseline details page](../../Spira-Administration-Guide/Product-General-Settings/#baseline-details) opens the [baseline artifact details page](../../Spira-Administration-Guide/Product-General-Settings/#baseline-artifact-details) to view all changes made in that baseline to that artifact [RQ:2989]
        - Show enhanced history tracking on the [product admin history](../../Spira-Administration-Guide/Product-General-Settings/#product-history-changes) pages and [baseline details](../../Spira-Administration-Guide/Product-General-Settings/#baseline-details) page (including test coverage and step position changes) [RQ:3040]
        - Enhance history to track document versioning (history records are created for adding, deleting, and setting a version active) [RQ:3064]

    * ** Report Customization**

        - Allow access to custom report views via API using the ODATA standard (SpiraPlan only) - read our [in-depth tutorial](../../Reporting/OData-Tutorial) [RQ:3037]
        - Users can have a dedicated [Report Admin role]()../../Spira-Administration-Guide/System-Users/#add-a-new-user), which lets them view, edit, and manage custom reports (in the app, via ODATA, and via the API) [RQ:2984]

    * **Other**

        - Release artifacts have event and subscription notifications [RQ:2979]
        - Let template admins prevent status changes by users with bulk edit permissions on artifact list and board pages via a new product template setting [RQ:3049]
        - Show warnings on login page to all users a week before a license expires and clearer messages after a license has expired [RQ:2649]
        - Carry out a security review of SpiraPlan and address vulnerabilities found [RQ:2673]
        - Improve product cloning by giving users two options: a full product clone or a product copy to use as a clean slate [RQ:3083]

??? bug "Bug fixes and enhancements"

    * **Administration**

        - Stop product cloning exiting midway with a failure message if an attachment file is missing from the directory [IN:5611]
        - Improve the performance of cloning a product by improving how attachments are copied into the new product [IN:6172]
        - Add product and system admin settings option to disable various calculations and updates to temporarily improve performance [IN:6207]
        - Add direct links to 'Custom Properties' in the Admin Menu under each Artifact Type to make navigation easier [IN:6239]
    
    * **Bug fixes**

        - Add jira.inflectra.com as an automatically trusted CORS domain to allow easier connection to Inflectra's Jira marketplace addon [IN:5520]
        - Ensure full database metadata parity between a clean install and an upgraded cloud installation [IN:6181]
        - Ensure full database metadata parity between a clean install and an upgraded on-premise installation [IN:6182]
        - Enable spell checking on the actual results field during test execution [IN:6192]
        - Fix opening a details page to a specified tab not working for some pages and tabs [IN:6202]
        - Fix creating tasks during test execution not triggering notifications [IN:6204]
        - Fix inline document editing version number not increasing automatically for all cultures (eg if a comma is used for denoting decimals) [IN:6253]
        - Do not allow users to create multiple custom properties for an artifact with the same property number as this can cause detail pages not to load [IN:6264]
        - Limit requirement tooltip to only show the start of, not the whole, description and comment fields, if the field is long (hierarchical views only) [IN:6302]

    * **Enhancements**

        - Make it clear when using the application with Internet Explorer that the browser is no longer supported [IN:6246]
        - Add an attachments tab for documents, to enable, for example, pasting of images into inline rich text documents [IN:6243]
        - Allow document names to be edited on list and details pages (note that the filename will be overwritten when you upload a new version) [IN:6292]
        - Add an option on the requirement detail page to insert a child requirement to the current requirement [IN:4913]
        - Convert the Saved Reports Widget's hyperlinks to make them shareable [IN:6106]
        - Improve the performance of associations tabs by adding a database index to speed up the most common retrieval [IN:6173]
        - Navigating tabs on details pages updates the URL with the tab name to make it easier to share your current view with others [IN:6194]
        - Add [additional views for custom reporting](../../Reporting/Custom-Report-Tables) to give more flexibility in what data can be queried [IN:6307]

    * **Findings from security review**

        - Version control tables should fully encrypt sensitive information in the database [IN:6242]
        - Fix "Vulnerable JS Library" issues by upgrading relevant external JS libraries [IN:6073]
        - Fix XSS vulnerabilities in the components Sidebar [IN:6289]
        - Fix HTML injection vulnerability on saved reports [IN:6303]
        - Fix HTML and IFrame injection vulnerabilities [IN:6300]
        - Fix XSS vulnerabilities in saved filters and reports [IN:6297]
        - Fix reflected XSS vulnerability [IN:6294]
        - Fix XSS vulnerabilities caused by using pre ASP .NET 4.6 databinding encoding syntax [IN:6295]


## Version 6.8 (March 2021)

!!! info "Summary"
    **BDD and Gherkin Support**: Create and write BDD style requirements and test cases 100% in Spira using Gherkin syntax with automatic syntax highlighting. Managed through the [documents repository](../../Spira-User-Manual/Document-Management), which includes workflow, checkout, and versioning support.

    **[Inline content editing](../../Spira-User-Manual/Document-Management/#add-new-inline-documents)**: Write plain text, rich text, and markdown inside Spira and have all of the versioning and workflow capabilities at your disposal. Of course, you can link this content to your requirements, test cases, and other Spira artifacts.

??? success "New Features"
    - **Document Management**: [Inline editing](../../Spira-User-Manual/Document-Management/#edit) of Text/Markdown/HTML in the Documents Management module [RQ:1697]
    - **Administration**: Add support for future implementation of program, template and portfolio settings [RQ:3051]
    - Add APIs for Risk management (including risk mitigations and reading risk template fields) [RQ:2544]

??? bug "Bug fixes and enhancements"
    * **Testing and test coverage**

        - [My Assigned Test Cases](../../Spira-User-Manual/User-Product-Management/#my-assigned-test-cases) widget adds options to show or hide the last executed date and the workflow status [IN:3935]
        - Fix package not changing status to "Tested" once all its child features are marked "Tested" [IN:4008]
        - Requirement test coverage for test cases in a different product should always reflect those tests' execution results [IN:4856]
        - Limited View role: do not show error message when the user creates an incident during test execution by clicking the Add button [IN:5984]
        - Generic test case/set list URL should always open the test case list to the last folder (this was not the case if the folder has an ID of 1) [IN:5989]
        - Improve performance of [test case parameter](../../Spira-User-Manual/Test-Case-Management/#parameters) hierarchy refresh [IN:6094]
        - Fix not being able to reassign pending test runs from product home page or My Page (introduced in 6.7.1) [IN:6161]
        - Fix system error that occurred when baselining was on for a product and you attempted an operation that added or edit test steps [IN:6179]
        - Test Case > [Automation Section](../../Spira-User-Manual/Test-Case-Management/#overview-automation): add file icon and link to document details page for filename [IN:6196]
        - Do not associate a test case with a release if the test case is a different product to the release [IN:4863]
    
    * **Home pages and reporting**

        - The image saved from a graph should look the same as the original (without oddly shaped black shaded areas) [IN:4960]
        - Program Home page [Test Execution Status](../../Spira-User-Manual/Program-Homepage/#test-execution-status) widget: when specified in the options, the number of test runs should be limited to active releases only [IN:5844]
        - [Incident Summary Report](../../Spira-User-Manual/Reports-Center/#incident-summary-report) has a field called "Resolved Release" but it should read "Planned Release" [IN:5943]
        - Improve Performance by switching My Page widget pagination to be fully handled by the database [IN:6102]
        - Fix My Page, [Recent Artifacts](../../Spira-User-Manual/User-Product-Management/#recent-artifacts): Test Run and Document links had 0 for the product ID, so the links did not work [IN:6092]
        - Tooltips on the My Page [My Assigned Test Cases](../../Spira-User-Manual/User-Product-Management/#my-assigned-test-cases) and [My Assigned Test Sets](../../Spira-User-Manual/User-Product-Management/#my-assigned-test-sets) widgets should always display [IN:6167]

    * **API**

        - Add API methods to open and delete document versions [IN:2237]
        - Add API methods to delete an existing association [IN:3623]
        - Add API methods to manage Document Types for a template [IN:6217]
        - Add API method to retrieve release builds without description information [IN:5031]
        - Add API function to v6.0 API to retrieve event logs [IN:5128]

    * **Other**
    
        - Add a [product setting](../../Spira-Administration-Guide/System-Workspaces/#edit-a-product) to filter list page name field by name only (not name and description as now) - this can speed up search for very large lists of artifacts [IN:5969]
        - [Build details](../../Spira-User-Manual/Release-Management/#build-details) page: improve the display of logs and, for long logs, cut out the middle of the log not the end [IN:6145]
        - Ignore extra spaces around a product or between words when attempting to [change templates](../../Spira-Administration-Guide/Product-Changing-Template) or [delete a product](../../Spira-Administration-Guide/System-Workspaces/#view-edit-products) [IN:5949]
        - Fix [Data Tools](../../Spira-Administration-Guide/Product-General-Settings/#product-data-tools) operation to fix releases missing the required field of Percent Complete [IN:6109]
        - Pull Request tasks should show the correct icon on the [task tab](../../Spira-User-Manual/Requirements-Management/#tasks) of the requirement details page (currently shows no icon) [IN:6156]
        - Document detail page, [versions tab](../../Spira-User-Manual/Document-Management/#document-versions): buttons should be hidden if the user does not have permission to edit the current document [IN:6214]
        - When another users has changed the same artifact as you, you see the wrong message if that other user changed status, and there is no transition from the new status back to the old status [IN:4822]
        - Clicking "Save And New" on a requirement/release should always add the subsequent artifact as a sibling, not add it at the bottom of the list [IN:4878]
        - Fix opening a details page directly to a specific tab via a dedicated url like requirements/1/Tasks.aspx [IN:5730]
        - Fix when creating one artifact from another (via associations tabs), new artifact notifications were not firing as they would for a normally new item [IN:5990]
        - Code in comments and plain text boxes should render as a monospace font [IN:6149]
        - Improve performance of saving recent products and artifacts a user visits by adding dedicated database tables for this functionality [IN:6070]
        - Improve performance of common operations by adding datbase asc and desc indexes to key tables [IN:6100]
        - Add security improvement to always prevent the application being loaded inside frames/iframes [IN:6051]
        - Add security improvement to fix "Format String Error" found during ZAP analysis [IN:6072]
        - Add security improvement to fix "X-Content-Type-Options Header Missing" found during ZAP analysis [IN:6076]
        - Updating risks should correctly check for concurrency (if another user has updated the risk since you opened it) [IN:6165]
        - Fix not being able to save a risk after transitioning to a status that requires a comment [IN:6203]


## Version 6.7.1 (February 2021)

!!! info "Summary"
    **[Pull Requests](../../Spira-User-Manual/Pull-Requests)** (SpiraTeam and SpiraPlan): The Developing menu in the global navigation now includes Pull Requests, where you can create and manage pull requests. For each [pull request](../../Spira-User-Manual/Pull-Requests/#pull-request-details) you can see all of the relevant commits, their code changes, and discuss any code changes.

    **The [build details](../../Spira-User-Manual/Release-Management/#build-details) page** has been overhauled to improve usability and bring the most important information to your fingertips. Key information is more clearly displayed at the top of the page and source code commits and artifact associations are more prominent.


    **[Source code diff](../../Spira-User-Manual/Commits/#commit-file-details) view** (SpiraTeam and SpiraPlan): by default, source code files now collapse unchanged sections, making it easier to quickly review the changes in larger files. You can quickly toggle the page to view the entire file, if you need to.

    **Recording Product setting changes** (SpiraTeam and SpiraPlan only): The application now automatically tracks when certain settings on a product change (turning baselining on and off, changing testing settings, or changing some planning options) and who made the change. This is our first step to better tracing admin level changes. Changes are shown on the [product history page](../../Spira-Administration-Guide/Product-General-Settings/#product-history-changes).

??? success "New Features"
    * **Source Code** (SpiraTeam and SpiraPlan only)

        - Add [Pull Request list page](../../Spira-User-Manual/Pull-Requests#pull-request-list) to display and create pull requests (tasks with a type that enables pull requests) [RQ:3005]
        - Can create a new pull request on the [Pull Request list page](../../Spira-User-Manual/Pull-Requests#pull-request-list), specifying the source branch and the destination branch [RQ:3006]
        - Task pages shows pull request with different icon [RQ:3045]
        - [Pull Request task details page](../../Spira-User-Manual/Pull-Requests#pull-request-details) shows source code commits [RQ:3046]

    * **Enhanced history tracking** (SpiraTeam and SpiraPlan only)

        - Enhance history to track position changes of test steps, use case steps, and risk mitigations [RQ:2659]
        - Enhance History to record Product Setting Changes (this includes toggling baseling, testing settings, and some planning options) [RQ:3044]
        - Ability to [save a report directly into documents](../../Spira-User-Manual/Reports-Center/#saving-and-sharing) on generating the report, and specify a document name and folder for the report [RQ:2295]

??? bug "Bug fixes and enhancements"
    * **Source Code / Development** (SpiraTeam and SpiraPlan only)

        - Omit the "Source Code Commits" widget on Development Home page in SpiraTest [IN:4090]
        - Source code file details and commit details association tabs: should require source code edit permissions to be able to manage associations [IN:5987]
        - [Source code clone popup](../../TaraVault-User-Manual/Provisioning-Projects-&-Users/#connecting-to-the-source-code-repository) for TaraVault users should only display on products the user has TaraVault access to [IN:5996]
        - Improve the design of the [build details](../../Spira-User-Manual/Release-Management/#build-details) page to make it easier to use [IN:5665]
        - [Build details](../../Spira-User-Manual/Release-Management/#build-details) page truncates very large console logs to improve performance page load time [IN:6056]
        - Add ability to copy to clipboard the full canonical commit ids for git and subversion (not the shorthand version) on the commit details page [IN:6026]
        - [File diff view for source code](../../Spira-User-Manual/Commits/#commit-file-details) auto collapses to only show changed lines (with option to expand) [IN:6006]
        - Association Panel (source code): build associations are added by the system (like commits) so users should not be able to remove or edit [IN:6010]
        - Add preview and syntax highlighting for .ignore and .gitignore files for documents and source code [IN:5999]
        - Add preview and syntax highlighting for a range of common development file formats (including csv, sql, scss, log, swift) and image formats (ico and webp) [IN:6037]
        - Add preview and syntax highlighting for all powershell file types [IN:6067]
        - Fix not being able to activate TaraVault if host site name is too long or contains the word "demo" [IN:6063]
        - Fix [activating TaraVault](../../TaraVault-User-Manual/Provisioning-Projects-&-Users/#provisioning-products) for a product causing errors in other products that use the TestProvider for source code [IN:6066]
        - With new cloud instance, [activating and deactivating TaraVault](../../TaraVault-User-Manual/Provisioning-Projects-&-Users/#provisioning-products) on a product should not cause any errors [IN:6069]
        - Display list of products using source code on TaraVault's main administration page [IN:6013]
        - [Source code product admin](../../Spira-Administration-Guide/Product-General-Settings/#source-code) page: do not display "source code up to date" if it has never been initialized successfully [IN:6034]
        - [Source code product admin](../../Spira-Administration-Guide/Product-General-Settings/#source-code) page: the test button should correctly check and verify the connection to git repositories [IN:6035]
        - [Source code file list](../../Spira-User-Manual/Source-Code/#source-code-file-list) page: when a fatal error has occurred during cache refresh, give a message to that effect [IN:6036]
        - Different commit grids should each have a separately saved filter and sort [IN:6016]
        - Fix some source code commits sometimes not being shown if the commits are from a deleted branch [IN:6054]
        - Fix SubversionProvider problem where it may not work on hosted systems due to event log permission issues
    
    * **Other**

        - Cloning releases or test cases should record in the history the user who performed the clone, not the artifact's author [IN:5208]
        - [Test set details page](../../Spira-User-Manual/Test-Set-Management/#test-set-details): the dropdowns for setting parameters should never contain duplicates, even if multiple test cases in the set have same parameter names [IN:5855]
        - Remove the loophole where under very particular circumstances a user could log back in to the application after their password had expired [IN:5893]
        - When adding test cases to a requirement, automatically map them to the same release as the requirement [IN:5899]
        - Improve the contrast of widget config icons whe in dark mode on home pages or the reporting page [IN:5965]
        - Improve performance of loading any application URL by reformatting the regular expressions used to parse and rewrite all application URLs (including API calls) [IN:5997]
        - Administration: sort all template dropdowns alphabetically, not by ID, and include the ID after the name [IN:5998]
        - Allow users to delete tasks from the [requirements](../../Spira-User-Manual/Requirements-Management/#tasks) and [risks detail](../../Spira-User-Manual/Risks-Management/#tasks) pages (not just remove the link to the task(s)) [IN:6020]
        - Association history records should not be visible on the Product Admin Product History Widget [IN:6027]
        - [Product Home Page](../../Spira-User-Manual/Product-Homepage) (Development) should not show error if no source code providers are active [IN:6050]
        - Admin [product history](../../Spira-Administration-Guide/Product-General-Settings/#product-history-changes) changes: allow users to revert more than one change at a time (as in earlier versions) [IN:6081]
        - Installer: display an error message on upgrading to v6+ if the database had not been DB properly upgraded to v5.4.0.4 first [IN:6086]

    * **API**

        - Create an API call that retrieves source code connection information [IN:5866]
        - Create a generic API call that can be called by an external service to trigger internal functions [IN:6045]

## Version 6.7 (December 2020)

!!! info "Summary"
    This release focused on **improving the experience and functionality for developers and development teams** using SpiraTeam and SpiraPlan. On top of integrating with the top [IDEs](../../IDE-Integration/Visual-Studio), your [CI/CD](../../Build-Server-Integration/Jenkins--Hudson) processes, and unit test, this release brings massive improvements to our [source code](../../Spira-User-Manual/Source-Code) features.
    
    **We have revamped the [source code management module](../../Spira-User-Manual/Source-Code)** (SpiraTeam and SpiraPlan only), and for the first time, there is now a native [code difference viewing](../../Spira-User-Manual/Commits/#commit-file-details) capability in Spira. We have also improved views of branches, commits, files and given the source code system a huge performance boost. *Note, source code is not included in SpiraTest*.
    
    **View rendered markdown files** directly in Spira with rich previews for documents and source code files. John Gruber's markdown format is an incredibly popular and easy way to write human readable plain text that renders as html with images, headings, lists, and more.

??? success "New Features"
    - Improve functionality and performance of Git source code control (for [GitProvider](../../Version-Control-Integration/Integrating-with-Git) and [TaraVault-Git](../../TaraVault-User-Manual/Using-Git)) [RQ:3033]
    - Improve functionality and performance of Subversion source code control (for [SubversionProvider](../../Version-Control-Integration/Integrating-with-Subversion) and [TaraVault-Subversion](../../TaraVault-User-Manual/Using-Subversion)) [RQ:3034]
    - Improve the performance and data integrity of source code by moving commits from a file cache to the database [RQ:3026]
    - Enhance and improve the Source Code [File list](../../Spira-User-Manual/Source-Code/#source-code-file-list) page [RQ:3016]
    - Enhance and improve the Source Code [File details](../../Spira-User-Manual/Source-Code/#source-code-file-details) page [RQ:3018]
    - Enhance and improve the Source Code [Commit list](../../Spira-User-Manual/Commits/#commit-list) page [RQ:3010]
    - Enhance and improve the Source Code [Commit details](../../Spira-User-Manual/Commits/#commit-details) page [RQ:3014]
    - Add a new Source Code [Commit File details](../../Spira-User-Manual/Commits/#commit-file-details) page to show diffs between current and previous commits [RQ:3013]
    - Global navigation bar's artifact dropdown has a new "Developing" section for Source Code and Commits [RQ:3003]
    - Change the source code branch selector from showing a fake 'master' to "(None)" when there are no branches to avoid confusion [RQ:3004]
    - Change the source code branch selector to a hierarchical dropdown using slash separator to represent folders [RQ:3007]
    - Improve usability with a more accessible source code cache retention settings that is now measured and set in minutes not hours [RQ:3032]
    - Enhance and improve the sample source code repository to showcase difference branches and file types [RQ:3023]
    - Ensure users can review a build and easily explore what code was committed in that build [RQ:3029]
    - Ensure users can readily find what a specific file looks like at each commit and across different branches [RQ:3028]
    - Ensure users can easily see how a file changed in a particular commit [RQ:3027]

??? bug "Bug fixes and enhancements"
    * **Source Code** (SpiraTeam and SpiraPlan only)
    
        - Fix source code files missing their author and date information [IN:4526]
        - Adding a source code file via the Add Existing Document dialog should succeed when not on the main branch / trunk [IN:4827]
        - [Build details page](../../Spira-User-Manual/Release-Management/#build-details): fix the commits tab to always show complete information [IN:5701]
        - [Build details page](../../Spira-User-Manual/Release-Management/#build-details) > Associations Tab: do not show duplicates items if the commit message has the same token more than once [IN:5703]
        - Improve the performance of source code on artifact details pages (specifically on the association and attachment panels) [IN:5710]
        - Add preview support in documents and source code for additional filetypes (bat, feature, markdown, json, yaml, typescript, svg files) [IN:5859]
        - [Source Code File Details](../../Spira-User-Manual/Source-Code/#source-code-file-details) > Associations tab: should not show duplicate rows if the file exists in more than one branch [IN:5860]
        - Fix the GitProvider to not require event log entries that can block usage of third party git providers on cloud installs [IN:5867]
        - Add preview support for Markdown in Source Code Files [IN:5912]
        - Update the use of the word "Revision" to "Commit" throughout the application [IN:5920]
        - Product Home page > [Source Code Commits widget](../../Spira-User-Manual/Product-Homepage/#source-code-commits): improve the widget to make the branch selectable and show the most recent 5 commits [IN:6003]
        - Source code file preview for binary files (like png or jpeg) should work correctly for TaraVault Git [IN:6005]
        - Rename sample source code "master" branch to "main" [IN:5945]

    * **Other**

        - Product Admin > [Planning Options](../../Spira-Administration-Guide/Product-Planning/#requirements): improve the description of "Use Task Status" [IN:2612]
        - Ensure all requirement statuses roll up correctly to parent requirements [IN:5664]
        - Allow full artifact tag search (eg [IN:123]) in association panels, global search, and filtering on grids (outside of admin) [IN:5706]
        - Clicking Insert or Add while editing rows on a list page should save all current edits before adding the new row/artifact [IN:5786]
        - System Admin > Product Create page: make the template dropdown list existing templates alphabetically and show their IDs [IN:5811]
        - [Document details](../../Spira-User-Manual/Document-Management/#document-details) page: add new overview tab to match the design of other detail pages [IN:5869]
        - [Document details](../../Spira-User-Manual/Document-Management/#document-details) page > Associations tab: add the ability to create an association to a risk [IN:5952]
        - Add preview support for Markdown in Documents [IN:5913]
        - Release detail page > test case tab: ensure pagination and rows shown is respected (instead of always showing all test cases) [IN:5878]
        - Upgrade Josefin Sans font to v2 so that it supports more accented characters [IN:5887]
        - Password Expired page explainer note about password requirements includes information about special characters [IN:5892]
        - Fix e-signatures for some artifacts not correctly checking passwords or RSS Tokens [IN:5962]
        - Global navigation: ensure the dropdowns do not get cut off behind browser horizontal scroll bar if the dropdown extends beyond the bottom of the page [IN:5904]
        - Cloud Installer: remove duplicate entry in the web.config file for FIPS [IN:5905]
        - Product Admin > [Data Tools](../../Spira-Administration-Guide/Product-General-Settings/#product-data-tools): upgrade it to not run check on requirements or releases on page load to improve performance [IN:5940]
        - [Task list](../../Spira-User-Manual/Task-Tracking/#task-list) page: ensure in-progress tasks with no end date do not cause the page to load correctly [IN:5950]
        - System Admin > Template Edit page: make the active selector disabled if the template has any products associated with it [IN:5956]
        - [Test Run details](../../Spira-User-Manual/Test-Run-Management/#test-run-details) page: strip html and body tags from all rich text fields that can render due to importing data from applications that do not correctly generate HTML [IN:5960]
        - Add test runs (as an option) to the [requirements detailed report](../../Spira-User-Manual/Reports-Center/#requirements-detailed-report) [IN:5947]
        - Reports default to not automatically generating history or attachment sections [IN:5947]
        - Ensure moving or adding requirement to a release add history records for any test cases that are automatically add to the release [IN:5973]
    
    * **API**

        - Fix the API that [creates a user](http://api.inflectra.com/Spira/Services/v6_0/RestServiceOperation.aspx?uri=users%3fpassword%3d%7bpassword%7d%26password_question%3d%7bpassword_question%7d%26password_answer%3d%7bpassword_answer%7d%26project_id%3d%7bproject_id%7d%26project_role_id%3d%7bproject_role_id%7d&method=POST) can so that it will not create a user without a user profile if the API body is incomplete [IN:5432]
        - API to [update custom lists](http://api.inflectra.com/Spira/Services/v6_0/RestServiceOperation.aspx?uri=project-templates%2f%7bproject_template_id%7d%2fcustom-lists%2f%7bcustom_list_id%7d&method=PUT) should update list items that are currently inactive (as well as those that are active) [IN:5958]
        - POST call to [search for automated test runs](http://api.inflectra.com/Spira/Services/v6_0/RestServiceOperation.aspx?uri=projects%2f%7bproject_id%7d%2ftest-runs%2fsearch%2fautomated%3fstarting_row%3d%7bstarting_row%7d%26number_of_rows%3d%7bnumber_of_rows%7d%26sort_field%3d%7bsort_field%7d%26sort_direction%3d%7bsort_direction%7d&method=POST) has incorrect URL formulation with ?? instead of ? at start of query [IN:6032]

## Version 6.6.1 (October 2020)

!!! info "Summary"

    **Baselining Enhancements** (SpiraTeam and SpiraPlan only): with baselining enabled, you can now still revert recent changes in a product. Additionally, with baselining enabled, test coverage changes to requirements and releases are tracked and recorded. This release also includes a number of further bug fixes and enhancements.

??? success "New features"
    - Store source code branches and commit information directly in the database to improve reliability and performance (SpiraTeam and SpiraPlan only) [RQ:2975]
    - Show a warning about future deprecation (after March 31, 2021) on the login page if user is using Internet Explorer 11 [RQ:2987]
    
    * Baselining (SpiraTeam and SpiraPlan only)
        - Product admins can purge or revert recent history changes (those not covered by any baselines) [RQ:2988]
        - Enhanced history to track release test coverage (if baselining is enabled for a product) [RQ:3015]
        - Enhanced history to track requirement test coverage (if baselining is enabled for a product) [RQ:2991]

??? bug "Bug fixes and enhancements"
    - On Administration -> Projects -> Data Tools page, update the text to explain the new index refresh button [IN:3655]
    - On Administration -> Projects -> Data Tools add a new option to fix Folder hierarchies [IN:5839]
    - On Administration -> Projects -> Data Tools add a new option to fix Test Case Parameters cache [IN:5840]
    - On Administration -> Projects -> Data Tools combine the two Refresh Cache buttons into a single button [IN:5807]
    - On the Test Case details page, "Linked" script type option in the "Automation" section should not be greyed out when it's actually available [IN:4668]
    - On the Test Case details page, inserting a link to child that has no direct parameters should refresh the test case parameters cache [IN:5851]
    - On the Test Case details page, the releases tab should show the correct artifact prefix (RL), and not TC [IN:5877]
    - On the Test Run details page, the console output should better force the wrapping of long lines [IN:5780]
    - On the Requirements List page, a new requirement inserted at the end of the requirements list should have the correct indent level [IN:5864]
    - Improve performance of the RELEASE_REFRESH_PROGRESS_AND_EFFORT stored procedure [IN:5801]
    - Fix the documentation links on the Enterprise and Portfolio home pages (SpiraPlan only) [IN:5814]


## Version 6.6 (August 2020)

!!! info "Summary"

    **Planning Improvements** (SpiraTeam and SpiraPlan only): Planning and kanban boards have some great new features like new display options and improved design. Set a product to estimate releases and requirements only with points (not hours). Use dynamic WIP limits on the planning board to help manage your kanban flow of requirements.

    **Baselines** (SpiraTeam and SpiraPlan only): View all baselines created across all releases in a product, and drill down into a baseline to review every artifact that changed during that baselines period of activity.

    **Performance Improvements**: The most frequent power-hungry operations by users have been reworked from the ground up to maximize performance. Operations like updating test coverage is up to 300% faster.

??? success "New features"
    * Administering baselining within a product (SpiraTeam and SpiraPlan only)
        - With baselining turned on, product admins can access the product admin [baseline list page](../../Spira-Administration-Guide/Product-General-Settings/#baselines) [RQ:2939]
        - Label on the Product Admin home page widget tells you if baselining is enabled [RQ:2978]
        - Product admin [baseline list page](../../Spira-Administration-Guide/Product-General-Settings/#baselines) shows all baselines in a products across all releases [RQ:2977]
        - Product admin [baseline detail page](../../Spira-Administration-Guide/Product-General-Settings/#baseline-details) shows all baseline details, including all artifacts changed in that baseline [RQ:2670]
        - The [baseline tab](../../Spira-User-Manual/Release-Management/#baselines) of the release details page lets a product admin access the details page for that baseline [RQ:2665]
    
    * Product Planning (SpiraTeam and SpiraPlan only)
        - [Product planning options](../../Spira-Administration-Guide/Product-Planning/#requirements) allows users to show points not hours on the planning board and requirement and release pages [RQ:2944]
        - [Product planning options](../../Spira-Administration-Guide/Product-Planning/#kanban-work-in-progress-limits) page lets you set dynamic WIP Limits for each status on the [Planning Board](../../Spira-User-Manual/Planning-Board/#work-in-progress-limits) [RQ:2970]
        - Improve Expand/Collapse behavior on planning boards [RQ:2969]
        - Planning board and requirements board lets you group by component or epic for releases [RQ:2945]
        - Planning board and requirements board shows the requirement completion progress bar for each release [RQ:2865]

??? bug "Bug fixes and enhancements"
    * **Agile and Planning** (SpiraTeam and SpiraPlan only)
        - If the Planned Release field is blank, changing it should always enable the save button (including if the new planned release has builds associated with it) [IN:2086]
        - If planned by points is enabled for a product, hide the hours label next to the requirement point estimate [IN:5250]
        - Task Board JavaScript can error out and cause the page to not load properly [IN:5627]
        - Refine what statuses show on the Requirement and Task boards - include the default status and any statuses with both a transition to and from [IN:5766]

    * **Performance**
        - Improve the performance of retrieving parameters for test cases [IN:5600]
        - Improve the performance of updating requirement test and task coverage [IN:5601]
        - Improve the performance of retrieving the list of folders for test cases [IN:5751]
        - Improve the performance of retrieving the list of folders for test sets [IN:5752]
        - Improve the performance of retrieving the list of folders for tasks [IN:5753]
        - Improve the performance of retrieving the list of folders for documents [IN:5754]

    * **Testing**
        - Show an asterisk during test execution if there is an existing incident and incidents are required in the product's testing settings [IN:3665]
        - Inserting a new test step should save any existing data being edited for step(s) on the test case details page [IN:3773]
        - Test execution pages should show custom styling for test steps [IN:4716]
        - Test run details page should show custom styling for test steps [IN:4770]
        - A test step parameter in a linked test step, once set in a linked test step, cannot be reset to its default in a subsequent linked test step [IN:4922]
        - Exploratory test execution should ensure the menu to clone/delete a step is always visible, even with long test step descriptions [IN:5702]
        - Test Execution using Internet Explorer 11 was not not possible if the test had more than one step (since 6.5.2 only) [IN:5747]
        - Test execution task description (if tasks are enabled) can sometimes be populated with the current steps actual result [IN:5759]
        - Test step rows on test case details page should show inline editors at full width (within the cell) when editing [IN:5773]
        - Test execution with tasks enabled should let you add a task while working in table mode [IN:5774]

    * **Other**
        - The Filter dialogs and 'Export to Product' dialogs are hidden if the page is scrolled down because the dialogs are fixed to the page not the window [IN:4605]
        - Cross-site scripting vulnerability [IN:4613]
        - Documents which have at least one recorded electronic signature should be able to deleted [IN:5615]
        - OAuth Login Providers 'Return URL' has been updated to use the Web Server URL to improve ease of setup for on-premise customers [IN:5719]
        - Correct the on-boarding tour for 6.5.2 link to testing settings [IN:5742]
        - Releases and requirements with long names can be aligned too far to the left (since 6.5.2) [IN:5746]
        - Incident and task notifications don't send if the token comment:first or comment:last is used, but the artifact has no comments [IN:5749]
        - The table of baselines on the release details page should align the icons in a single row when in edit mode [IN:5772]
        - Update styling of product admin pages to more closely match the look and feel of artifact details pages [IN:5787]


## Version 6.5.2 (July 2020)

!!! info "Summary"
    **Baselining (SpiraTeam and SpiraPlan only)**: Enable baselining by product to add baselines to releases or sprints. Use baselines to create snapshots of the entire product at a specific point in time, for instance what it looked like at the start and then at the end of a sprint. 
    
    *Learn: read our blog about this feature [here](http://www.inflectra.com/Ideas/Entry/spira-652-requirements-test-case-baselining-1051.aspx), or read our [documentation overview](../../Spira-User-Manual/Release-Management/#baselining)*

    **[Testing Settings](../../Spira-Administration-Guide/Product-Planning/#testing-settings)**: testing settings are now managed at the product, not system, level. Not only that but there are now lots more ways to tailor how testing behaves.

    **DevOps (SpiraTeam and SpiraPlan only)**: streamlined and improved traceability between source code commits, CI builds, DevOps pipelines, and SpiraPlan artifacts.

??? success "New features"
    - [Testing Settings](../../Spira-Administration-Guide/Product-Planning/#testing-settings) are scoped to a product instead of at the system Level [RQ:2961] (see specific enhancements below)
    - Users can [create an Incident directly from a Task](../../Spira-User-Manual/Task-Tracking/#creating-an-incident-from-a-task) [RQ:2971]

    * Custom Reports
        - Enable custom reports to use ${ReleaseId} and ${ReleaseAndChildIds} [tokens](../../Reporting/Custom-Reporting-Tokens) in their ESQL as is already possible for custom graphs [RQ:2976]

    * [Baselining](../../Spira-User-Manual/Release-Management/#baselining) (SpiraTeam and SpiraPlan only)
        - Baselining toggle is visible and usable in SpiraTeam and SpiraPlan on the [Admin Product page](../../Spira-Administration-Guide/System-Workspaces/#add-a-new-product) [RQ:2672] (released but disabled in 6.5.1)
        - Turning on baselining for a product disables the ability to purge or revert [product history](../../Spira-Administration-Guide/Product-General-Settings/#history-details-screen) [RQ:2938] (released but disabled in 6.5.1)
        - Turning on baselining for a product shows the [baseline tab](../../Spira-User-Manual/Release-Management/#baselines) on the release details page [RQ:2940]
        - Baseline tab on the release details page lets you view existing baselines [RQ:2664]
        - Users with equivalent release permissions can add/edite/delete a new baseline from the baseline tab on a release details page [RQ:2662]
        - A new [custom reportable entity](../../Reporting/Custom-Report-Tables/#baselines) lets users create custom reports for baselines [RQ:2873]
    
    * Security Enhancements
        - Implement CSRF Anti-Forgery Tokens on Postback Pages [RQ:2959]
        - Implement CSRF Anti-Forgery Tokens on WCF Ajax Services [RQ:2960]
    
    * Improve included [sample templates](../../Spira-Administration-Guide/System-Workspaces/#included-templates)
        - Update and refresh notification event subject lines and [notification templates](../../Spira-Administration-Guide/Template-Notifications/#notification-templates) [RQ:2843]
        - A new "Regulated Industries" Template provides out-the-box best practice for workflows across all artifacts [RQ:2825]
        - A new "Lightweight" template lets users work in a very streamlined way with effectively no workflow constraints [RQ:2823]

    * Source Code Management (SpiraTeam and SpiraPlan only)
        - [Artifact associations](../../Spira-User-Manual/Application-Wide/#associations) show commits from all branches, not just the branch being filtered on in the source code view [RQ:2973]
        - There is a background feature flag to disable Source Code Commits in Documents/Associations (available to IT on-premise only) [RQ:2974]


??? bug "Bug fixes and enhancements"
    * **Testing**
        - Product admins can require a test step has at least one incident if it is executed and marked as anything other than passed [IN:1185]
        - Product admins can require that an actual result is entered for every test step during test execution (including pass) [IN:3496]
        - Product admins can block users from marking a test step as any of Caution, Blocked, N/A, or from passing all steps at once (for normal and exploratory testing) [IN:5685]
        - Product admins can limit users to only execute tests from test sets, not from test cases [IN:5686]
        - Product admins can allow [tasks](../../Spira-User-Manual/Test-Execution/#tasks) to be added during test execution (affecting both normal and exploratory testing) defaults to off [IN:5479]
        - Include an Add button on the incident tab of the test execution page to make it clearer to users how to create an incident during testing [IN:5474]
        - In exploratory testing adding/deleting steps did not correctly reset the ability to "finish" the test [IN:5581]
        - Like we have done for exploratory testing since we introduced it, auto save actual results during normal test execution [IN:5626]

    * **Home pages**
        - Improve the styling of the My Page [News Reader widget](../../Spira-User-Manual/User-Product-Management/#my-news-feeds) [IN:5718]
        - The default Product Home page should not show an authorization error if requirement view permission is lacking [IN:5661]
        - The Product Home page should not show an authorization error if attempting to view the commits widget but you do not have the permission to view source code [IN:5714]
        - Program, portfolio, enterprise schedule widgets should not show releases with an inactive parent detached from a workspace [IN:5687]
        - Program, portfolio, enterprise schedule widgets should not show releases from inactive products detached from a workspace [IN:5689]
        - All schedule widgets should work better on smaller screen sizes [IN:5605]
        - Product home page widgets should all only show active releases when displaying for a particular release [IN:5691]
        - The Relative Size widget should hide the legend when there are over 10 items to show to make it more useable [IN:5692]

    * **Other**
        - Enable custom reports to use ${ReleaseIds} token in their ESQL like custom graphs [IN:460] (see [RQ:2976] above - so nice to close out an old enhancement :tada:)
        - Do not show an error if you add a folder of test cases to the same release twice (error occurs when the folder contains deleted test cases) [IN:4880]
        - Correct references to old term "Resolved Release" to "Planned Release" in incident notifications, incident detailed report, and incident workflows [IN:5485]
        - Remove references to 'Project' when exporting an artifact from one product to another [IN:5540]
        - On the incident list page, the column labelled "Progress" is incorrectly called "Task Progress" in the column selector dropdown and filter message box [IN:5575]
        - Commits tab on build detail page should show commits more consistently and not a message about the cache [IN:5548]
        - Improve the CI/CD functionality of the association panel on artifact details pages to show commits more consistently and also to link builds to artifacts [IN:5666]
        - Task list: issues if the user's current folder has been deleted [IN:5027]
        - Test Case list: issues if the user's current folder has been deleted [IN:5658]
        - Test Set list: issues if the user's current folder has been deleted [IN:5659]
        - Document list: issues if the user's current folder has been deleted [IN:5662]
        - Performance fixes for projects with large numbers of releases by introducing a [product setting](../../Spira-Administration-Guide/Product-Planning/#general) to optionally use active releases only for detected release dropdown [IN:5671]
        - Relax the incident closed/start date validation as it can break data-syncs [IN:5693]
        - Make filtering by release more consistent between the hierarchical and sorted requirement list pages to always include any child releases/sprints [IN:5709]




## Version 6.5.1 (June 2020)

!!! info "Summary"
    **Improved dashboard widgets**: enhanced and new Recent Build widgets, let you get an easier handle on your CI/CD processes from [program](../../Spira-User-Manual/Program-Homepage/#recent-builds), [portfolio](../../Spira-User-Manual/Portfolio-Homepage/#recent-builds), and [enterprise](../../Spira-User-Manual/Enterprise-Homepage/#recent-builds) home pages; a number of widgets on the program home page by default display data for active releases only to make their data more meaningful; a brand new [product test summary table](../../Spira-User-Manual/Program-Homepage/#product-test-summary) on the program home page provides important information at a glance.

??? success "New features"
    * Baselining
        - On generating a test run the system automatically links it to the most recent history changeset to improve auditing [RQ:2655]
    
    * Enterprise Dashboard (SpiraPlan only)
        - Add an Enterprise [Recent Builds](../../Spira-User-Manual/Enterprise-Homepage/#recent-builds) widget [RQ:2937]
    
    * Porfolio Dashboard (SpiraPlan only)
        - Add a Portfolio [Recent Builds](../../Spira-User-Manual/Portfolio-Homepage/#recent-builds) widget [RQ:2934]
    
    * Program Dashboard
        - Change the [Requirements Coverage](../../Spira-User-Manual/Program-Homepage/#requirements-coverage) widget to, by default, show data for active releases only [RQ:2761]
        - Change the [Test Execution Status](../../Spira-User-Manual/Program-Homepage/#test-execution-status) widget to, by default, show data for active releases only [RQ:2762]
        - Change the [Task Progress](../../Spira-User-Manual/Program-Homepage/#task-progress) widget to, by default, show data for active releases only [RQ:2763]
        - Improve the [Program Recent Builds](../../Spira-User-Manual/Program-Homepage/#recent-builds) Widget [RQ:2936]
        - Add new [Product Test Summary](../../Spira-User-Manual/Program-Homepage/#product-test-summary) Widget [RQ:2858]
    
    * Sample Data installed with new installations
        - Improve data consistency in sample product Library Information System [RQ:2948]
        - Rename the "Agile" template to "Library Information System (sample)" [RQ:2822]
        - Create a "Default" template that matches the template you create on making a product with a new template [RQ:2947]


??? bug "Bug fixes and enhancements"
    - Global search and Association panel: improved search on different letter/number combinations [IN:4695]
    - Logging in with an OAuth provider takes you any specified return url, to improve getting you to the right place faster [IN:5413]
    - Deafault product role text descriptions have been improved for clarity [IN:5560]
    - User settings collection service does not accept or return unsafe strings [IN:5580]
    - Program home page (general) info tooltips no longer get cut off for widgets at the top of the page [IN:5593]
    - Program release list page: start and end dates are colored to improve quickly seeing the state of a release [IN:5594]
    - The My Profile page highlights to the user that they need to save after generating a new RSS token [IN:5599]
    - Program, portfolio, and enterprise schedule widgets now show sprints without an active parent inside the correct product [IN:5603]
    - Reduce the error logging from the Recent Artifacts Service [IN:5607]
    - Fixes bug in the HistoryManager when retrieving history sets by product [IN:5619]
    - My Recent Artifacts widget now displays a clickable "(none)" when the artifact does not have a name [IN:5623]
    - Fixes ability to add new documents/attachments to three sample products [IN:5655]
    - In Internet Explorer 11 some home page bar charts have an overly dark background color for bars [IN:5673]


## Version 6.5.0.2 (May 2020)

!!! bug "Bug fix"
    - On-premise upgrades to 6.5 remove baked-in custom reporting database views [IN:5512]


## Version 6.5.0.1 (May 2020)

!!! bug "Bug fix"
    - Requirement completion count calculation fails when there are over 1000 active requirements in a product [IN:5512]


## Version 6.5 (May 2020)

!!! info "Summary"
    **Portfolio management (SpiraPlan only)**: Allow users to collect programs together into portfolios, which can then be collected into a single enterprise view. Key data (like percent complete) will flow from a product, all the way up to the enterprise view. 
    
    *Learn: [editing portfolios](../../Spira-Administration-Guide/System-Workspaces/#viewedit-portfolios); [letting users see portfolio and enterprise pages](../../Spira-Administration-Guide/System-Administration/#how-user-permissions-are-set).*

    **New dashboard views to assess overall progress**: Key data about percent complete for sprints, releases, products, programs, and portfolios will be displayed in a new widget on relevant dashboards. This will be based on the requirements that are part of each active sprint and release.

    *Learn: [the portfolio dashboard](../../Spira-User-Manual/Portfolio-Homepage/); [the enterprise dashboard](../../Spira-User-Manual/Enterprise-Homepage/).*

    **New release and task views to better manage workloads (SpiraTeam and SpiraPlan only)**: View all your relevant releases and tasks in new Gantt views. These let you see at a glance what is due when, and get an overview of the schedule of work and sprints.

    *Learn: [release Gantt chart](../../Spira-User-Manual/Release-Management/#release-gantt-chart); [release mind map](../../Spira-User-Manual/Release-Management/#release-mind-map); [task Gantt chart](../../Spira-User-Manual/Release-Management/#release-gantt-chart).*

??? success "New features"

    - Generic Project Settings Provider [RQ:2852]
    - Installer can upgrade successfully with required database additions [RQ:2850]


    * [Enterprise Dashboard](../../Spira-User-Manual/Enterprise-Homepage/) (SpiraPlan only)
        - [Requirement Completion Gauge Chart](../../Spira-User-Manual/Enterprise-Homepage/#requirement-completion) [RQ:2743]
        - [Portfolios: Completion](../../Spira-User-Manual/Enterprise-Homepage/#portfolios-completion) [RQ:2744]
        - [Portfolios: Relative Size](../../Spira-User-Manual/Enterprise-Homepage/#portfolios-relative-size) [RQ:2745]
        - [Top Open Risks](../../Spira-User-Manual/Enterprise-Homepage/#top-open-risks) [RQ:2746]
        - [Enterprise Schedule Gantt Chart](../../Spira-User-Manual/Enterprise-Homepage/#schedule) [RQ:2747]

    * Porfolio Dashboard (SpiraPlan only)
        - [Requirement Completion Gauge Chart](../../Spira-User-Manual/Portfolio-Homepage/#requirement-completion) [RQ:2749]
        - [Programs: Completion](../../Spira-User-Manual/Portfolio-Homepage/#programs-completion) [RQ:2750]
        - [Programs: Relative Size](../../Spira-User-Manual/Portfolio-Homepage/#programs-relative-size) [RQ:2751]
        - [Top Open Risks](../../Spira-User-Manual/Portfolio-Homepage/#top-open-risks) [RQ:2752]
        - [Portfolio Schedule Gantt Chart](../../Spira-User-Manual/Portfolio-Homepage/#schedule) [RQ:2753]

    * Program Dashboard
        - Add General, Development, and Test Views [RQ:2755]
        - [Requirement Completion Gauge Chart](../../Spira-User-Manual/Program-Homepage/#requirement-completion) [RQ:2756]
        - [Products: Completion](../../Spira-User-Manual/Program-Homepage/#products-completion) [RQ:2757]
        - [Products: Relative Size](../../Spira-User-Manual/Program-Homepage/#products-relative-size) [RQ:2758]
        - [Program Schedule Gantt Chart](../../Spira-User-Manual/Program-Homepage/#schedule) [RQ:2759]
        - Program Overview widget shows the portfolio, where relevant [RQ:2854]

    * Product Dashboard
        - [Requirement Completion Gauge Chart](../../Spira-User-Manual/Product-Homepage/#requirement-completion) [RQ:2765]
        - [Releases: Completion](../../Spira-User-Manual/Product-Homepage/#releasessprints-completion) [RQ:2766]
        - [Releases: Relative Size](../../Spira-User-Manual/Product-Homepage/#releasessprints-relatize-size) [RQ:2767]
        - [Product Schedule Gantt Chart](../../Spira-User-Manual/Product-Homepage/#schedule) [RQ:2768]

    * My Page
        - Add [Recent Products widget](../../Spira-User-Manual/User-Product-Management/#recent-products) [RQ:2770]
        - Add [Recent Artifacts widget](../../Spira-User-Manual/User-Product-Management/#recent-artifacts) [RQ:2771]

    * Release List Page Changes
        - Add column for total # points [RQ:2774]
        - Add column for total # requirements [RQ:2775]
        - Add progress bar for requirements [RQ:2776]
        - [Release Hierarchical Diagram View](../../Spira-User-Manual/Release-Management/#releases-mind-map) - read only (SpiraTeam and SpiraPlan only) [RQ:2777]
        - [Release Gantt Chart View](../../Spira-User-Manual/Release-Management/#release-gantt-chart) - read only (SpiraTeam and SpiraPlan only) [RQ:2778]

    * Program Release List Page (SpiraPlan only)
        - Add column for total # points for all requirements in the release [RQ:2836]
        - Add column for total # requirements [RQ:2837]
        - Add [progress bar for requirements](../../Spira-User-Manual/Release-Management/#requirements-completion) [RQ:2838]

    * Product Task List Page Changes
        - Add a [Task GANTT Chart View](../../Spira-User-Manual/Task-Tracking/#task-gantt-chart) [RQ:2780]

    * Sample Data installed with new installations
        - Remove data and rename Sample Barebones Product to Sample Empty Product 1 [RQ:2782]
        - Rename Sample Empty Product to Sample Empty Product 2 [RQ:2783]
        - Rename Sample Program [RQ:2784]

    * Calculation Changes/Updates
        - Requirement completion/counts refreshed correctly product-wide following relevant triggers [RQ:2827]
        - Requirement updates in the system trigger changes in all relevant releases and workspaces [RQ:2828]
        - Release updates in the system trigger changes in all relevant releases and workspaces [RQ:2829]
        - Product changes trigger updates in all parent workspaces [RQ:2830]
        - Program changes trigger updates in all parent workspaces [RQ:2831]
        - Porfolio changes trigger updates to the enterprise level [RQ:2832]
        - Requirements calculations for counts and completion work as expected [RQ:2855]
        - [Task Effort calculations for requirements](../../Spira-User-Manual/Requirements-Management/#task-effort) work as expected (for fields shown on the requirements list page) [RQ:2863]
        - [Task effort calculations for releases](../../Spira-User-Manual/Release-Management/#task-effort) work as expected (for fields shown on the release list page) [RQ:2856]

    * Permissions to control access to portfolios and enterprise views (SpiraPlan only)
        - New Portfolio Viewer attribute on the user profile to allow access to all portfolios (and enterprise view) [RQ:2834]
        - Access to portfolios admin pages and visibility in UI restricted by permissions and Spira version [RQ:2851]
        - Access to portfolios features pages and visibility in UI restricted by permissions and Spira version [RQ:2846]

    * Administration changes
        - [Ability to create, edit, delete portfolios](../../Spira-Administration-Guide/System-Workspaces/#viewedit-portfolios) [RQ:2840]
        - [Ability to assign programs to a portfolio](../../Spira-Administration-Guide/System-Workspaces/#edit-a-program) [RQ:2841]
        - Handle the default portfolio for new programs [RQ:2844]
        - [Ability to delete sample data](../../Spira-Administration-Guide/System-Home/#delete-sample-data) (all sample products, programs, and portfolios) and where possible sample users [RQ:2845]


??? bug "Bug fixes and enhancements"
    - Add a try/catch around IIS check, as when IIS isn't installed, the Admin DLL isn't available and will crash. [IN:5219]
    - Add ability to see product role description as a tooltip when hovering over your product role in the global navigation subheader [IN:5541]
    - Add an event in the event log after the event log is cleared by a user [IN:4818]
    - Add color highlighting to start and end-dates that are today or earlier [IN:5448]
    - Can review and resume recent pending test runs when attempting to execute a single test case [IN:4364]
    - Change 'New Test Case from' text to "Verify: " when creating tests from requirements [IN:5557]
    - Disable SSL yes/no toggle in email settings for cloud customers [IN:5302]
    - Ensure long single words for field labels wrap properly on artifact details pages [IN:5539]
    - Fix a role with release delete not being able to successfully delete a release on the release detail page [IN:5118]
    - Fix error when trying to add Risk Summary widget to Development or Testing Product Dashboards [IN:5440]
    - Fix Foreign Key Error trying to Delete a Template due to importance ID not being migrated for some requirements of type Epic [IN:5399]
    - Fix Installer (on prem): Upgrading to the current version does not always show warning [IN:5517]
    - Fix Installer uninstalls always being saved in SQL default location and not being properly named [IN:5176]
    - Fix My Page widget "Assigned Requirements" sorting by Importance ID instead of Importance Score [IN:5362]
    - Fix program release list: filtering on some columns causes problems [IN:5336]
    - Fix release "plan effort" calculation counting Saturdays but not Mondays [IN:3979]
    - Fix releases, Export to Project & Project Clone will hide releases until you click "show all levels" [IN:4812]
    - Fix Rest API documentation not explaining URL parameters for GET transitions for requirements, tasks, or test cases [IN:5361]
    - Fix saved filters not saving filters for integer or decimal fields [IN:5332]
    - Fix some test cases not opening in exploratory testing mode [IN:5412]
    - Fix the rows per page control not working for MembershipAdd.aspx page [IN:5415]
    - Fix the v6 API not returning project Template id in some calls [IN:5076]
    - Fix widget info popups on dashboards getting the top chopped off when the widget is at the top of the widget list [IN:5511]
    - Improve performance by removing the last usage of a Dictionary<> used in multi-threading [IN:5450]
    - Installer: Add key in web.config for anonymous UniqueID. [IN:5546]
    - Installer: refactor tst_addl_objects.sql generatin to reduce chances of corruption and upgrade problems [IN:5473]
    - Installer: Refine master Upgrade code for minDB & maxDB Version [IN:5119]
    - Make sure that requirement export to product function includes any use case steps [IN:5370]
    - Order links to pages in the administration menu logically not alphabetically [IN:5566]
    - Remove event log entries for non configured Oauth providers after the app pool restarts [IN:5521]
    - Remove the context menu options for opening or deleting a requirement or task on the Requirement and Tasks tab of the Releases detail page [IN:5433]
    - Template Admin: on custom property page artifact dropdown, omit irrelevant artifacts [IN:5103]
    - Tools -> Print or Export: provide an actionable message when the number of items is too large for the report to generate via url [IN:5403]

## Version 6.4.0.1 (March 2020)

!!! bug "Bug fix"
    - Oauth does not work correctly in certain environments [IN:5512]


## Version 6.4 (March 2020)

!!! info "Summary"
    **Single Sign On (SSO) Support**: Built in integration with a number of OAuth 2.0 providers to provide more seamless and secure sign-on to the application. Initial providers will include Azure AD, GitHub, GitLab, Google, Microsoft ADFS, and Okta.

    **Improved reporting**: With a single release picker you can now update every graph (including custom graphs) on the main reporting page. Report formatting for Word has also been improved


??? success "New features"
    * Integration with OAuth2 Protocol
        - User can select an OAuth provider to log in with on the Login Screen [RQ:2465]
        - Users will be able to log into the application using an OAuth provider [RQ:2457]
        - Users will be able to log off of the application without signing out of their provider. [RQ:2459]
        - Automatic Timout Logoff works as normal [RQ:2481]
        - OAuth managed users can use electronic signatures by signing using their RSS Token [RQ:2604]
        - OAuth managed users have API Soap access by allowing them to authenticate using their RSS token [RQ:2461]
        - Users connected using a provider can not use the Forgot Password feature [RQ:2691]
    
    * Users will be able to register an account after signing into their OAuth account
        - Users can link their Oauth account to their existing Spira user [RQ:2466]
        - Users can register for a new Spira user with their Oauth account [RQ:2467]
 
    * All OAuth providers will have their own library
        - Standalone Library for each Provider [RQ:2468]
        - Master Library to Interface with Provider Libraries [RQ:2469]
        - Autonomous Operation [RQ:2470]

    * System Administrators can managed Oauth providers and users connected using a provider
        - Admins can see and manage all available providers [RQ:2473]
        - Unloaded Providers are handled gracefully [RQ:2474]
        - Admins can see which users are using which provider, and unlink a user from their provider [RQ:2612]

    * Error States are managed
        - Logging in with incorrect credentials [RQ:2475]
        - Logging in with deactivated provider. [RQ:2476]
        - Logging in and not able to Link to existing user [RQ:2477]

    * Business Code
        - Database Handling [RQ:2479]
        - Library Handling [RQ:2480]
        - Users can unlink their account from the OAuth Provider [RQ:2552]

    * OAuth connectors are available for specific providers
        - Google [RQ:2619]
        - Github [RQ:2617]
        - Okta [RQ:2618]
        - Azure AD / Microsoft Identity Provider [RQ:2849]
        - Microsoft ADFS [RQ:2637]
        - Gitlab [RQ:2616]

    * Other features
        - LDAP - Switch from LDAP to Native for existing user [RQ:2558]
        - LDAP - Switch from native to LDAP for existing user [RQ:2559]
        - Centrally control all reports dashboard charts with a single release dropdown [RQ:2681]

??? bug "Bug fixes and enhancements"
    - Add release filter to incident/test run snapshot and time phased graphs [IN:1696]
    - Two enhancements to the Test Run and Test Case graphs [IN:1776]
    - Test Case Summary graph data displays for all releases (inconsistent with Project Home dashboard) [IN:2407]
    - Enhancement Request: Test Run Summary Graph [IN:2812]
    - Test Case Summary widget always includes all releases: add ability to specify a release [IN:3036]
    - Association panel: search for test step by ID, step description not shown. [IN:4132]
    - Test coverage wrongly gets reset to not run sometimes when an iteration is inserted or moved [IN:4801]
    - Can not set test set configuration when POSTing test set using REST api [IN:5199]
    - API: cannot sort test set retrieve by a sort field [IN:5215]
    - Build Risk Custom Report Reportable Entity [IN:5226]
    - Add a test case type filter to test case date range graphs [IN:5307]
    - Add Release Id as option for custom graphs [IN:5313]
    - Test case details page: make it clearer with more explicit labels what the two "Delete" buttons do - for the test case and for its steps [IN:5367]
    - Test case detail page, test steps section, right-click menu: change 'Copy Items' to 'Clone' [IN:5369]
    - Improve performance when retrieving a folder's parents (for test cases, test sets, tasks, and documents) [IN:5373]
    - Sidebar panel for hierarchical artifacts can have its contents spill outside if artifacts are added to deeply collapsed parents by other users [IN:5374]
    - Detail pages: dropdowns on tabs partially obscured by the side bar [IN:5385]
    - API call to REST Release_AddTestMapping in v5 and v6 does not provide information in the documentation [IN:5390]
    - Going to task board page after clicking on a task folder in list view fails - the url is not properly structured [IN:5411]
    - Association panel: can select artifacts to add even if you cannot access these artifacts in the application [IN:5418]
    - Possibility (pre-existing) of iteration threading issue with instant messenger [IN:5434]
    - Change the incident field label "Resolved Release" to "Planned Release" to better articulate its meaning [IN:5441]
    - Ensure that Word always display embedded images, and Excel reports strip out images [IN:5445]
    - Project Documents don't upload until you select a folder [IN:5449]
    - Need to remove the UFT8 BOM from the v6.0 REST API [IN:5458]
    - Need to extend the data sync password field to more than 52 characters due to TFS breaking change [IN:5486]

## Version 6.3.0.1 (February 2020)

!!! bug "Bug fixes and performance improvements"
    - Input boxes in grids should be full when in edit mode on grids with resizable columns [IN:5376]
    - Artifacts with folders can create new items in wrong folder when loading the list page via the url [IN:5388]
    - Planning boards do not always show all items for a parent release when viewing a sprint [IN:5392]
    - Data Sync encryption does not support FIPS mode [IN:5396]

## Version 6.3 (January 2020)

!!! info "Summary"
    **TaraVault unlimited for all SpiraTeam and SpiraPlan cloud users**: To celebrate the start of a new decade, our cloud source code management solution, TaraVault, is now included at no extra charge, for all the users and repositories and branches you want.
    
    **Improvements to filters**: Update your filters and shared filters easily. Create filters that also include information about which columns you have visible, their sort, order, and width. This is a great way for saving specific “views” you and your teams need.
    
    **Improved navigation between folders and hierarchies**: Each folder now has its own unique url, so you can share links to specific folders with your team. For requirements, releases, and all artifacts with folders new clickable breadcrumbs making it easy to go straight to an artifact’s parent.

??? success "New features"

    - Replace file upload with newer control on artifact detail pages and document list page [RQ:2359]
    - TaraVault licensing has no restrictions [RQ:2530] 
    - Improvements to Convert Incident to Requirement feature [RQ:2600]
    - Breadcrumbs on artifact details page are clickable so you can navigate up hierarchy for an artifact [RQ:2651]
    - Allow for urls that link to folders on a list page [RQ:2640]
    - Can save a filter & column arrangement combination as a "view" [RQ:2642]
    - The ability to update a saved filter [RQ:2652]
    - Spira 6.3 Installer Tasks [RQ:2671]

??? bug "Bug fixes and enhancements"

    - Add tooltip to shared filter that shows the username of the filter creator [IN:4904]
    - The ability to update a saved filter [IN:5048]
    - Admin: User Edit page could potentially show TaraVault DataGrid on Self-Hosted  [IN:5133]
    - Test set and test run custom fields using lists do not sync up correctly if multiple fields use the same list [IN:5156]
    - TaraVault product config page "Edit Users" button broken [IN:5195]
    - Program Incidents & Releases sometimes displays object reference issue [IN:5264]
    - Null Reference thrown if Security Settings nulled out in Admin Page [IN:5268]
    - Improve performance of requirement test and task coverage calculations [IN:5294]
    - Product admins can delete shared filters from the product homepage Shared Searches widget [IN:5303]
    - Automation host filters cannot be retrieved [IN:5320]
    - On association tabs permission checks are not carried out to hide buttons to create new artifact X from artifact Y [IN:5344]
    - Expanders and collapsers on Reports Config page broken [IN:5355]


## Version 6.2.2 (December 2019)

!!! info "Summary"
    **SpiraTeam and SpiraPlan cloud users can use any source code provider**: In addition to our source code provider, TaraVault, cloud customers can choose to use any Git or Subversion provider they wish.

    **Bug fixes and UI improvements**: The improvements include better access to the sidebars on all main pages, and improved search in dropdowns.

??? bug "Bug fixes and enhancements"

    - Build detail page: need ability to collapse description section, or confine it within a scrollable box [IN:4300]
    - Detect and notify the user when they attempt to run a test set with a blank configuration [IN:4655]
    - Html and body tags from rich text fields are not stripped out when rendered outside of CK editors [IN:4666]
    - Cloning workflows does not copy digital signature settings correctly [IN:4674]
    - Administration > Project > Project Associations: cross project artifact dropdown does not show selected artifacts [IN:4881]
    - Accented characters in some grids do not display correctly [IN:4965]
    - Notifications for risks: many fields are blank in the email; warning about exposure [IN:4967]
    - "Source Code" link under Project Admin Menu bounces back to Project Admin Home [IN:5073]
    - Cannot delete Document with Comment [IN:5082]
    - Folder Name on Test Case List not decoding HTML  [IN:5123]
    - Test Case Details: Can Link a Test Case to itself [IN:5131]
    - For rich text custom properties, long custom property name overlaps the field itself [IN:5148]
    - Product delete fails sometimes with a TaraVault foreign key error [IN:5181]
    - Sortable grids add new item erroneously after just adding a new item and clicking buttons like refresh [IN:5192]
    - My Assigned Requirements widget shows numbers for the 6 new statuses [IN:5213]
    - Fix sidebars on list and details pages to the top of the page so they are always visible [IN:5214]
    - Test Execution Page Leave Button no functionality when on a test case not owned [IN:5218]
    - Custom Props of type list: default values are saved but not shown in the admin UI [IN:5224]
    - Export buttons on Requirements list page are set for release permissions, not requirement permissions [IN:5240]
    - User profile page: clicking username copies rss token not username [IN:5243]
    - Search in dropdowns for anywhere in the values, not just at the start [IN:5244]
    - Task board: error occurs when creating a new task with certain settings [IN:5258]
    - Error not shown in association panel when the server throws an error message [IN:5276]
    - Limit the rows displayed on the product dashboard grids [IN:5277]
    - Improve the UI for the Modal Dialog Boxes when creating Custom Reports  [IN:5293]
    - Security fix for user first or last name containing code [IN:5295]


## Version 6.2.1 (October 2019)

!!! info "Summary"
    **Enhanced product template management**: Users can migrate a product from one template to another. This will help you consolidate your templates and streamline your administration more easily.

??? success "New features"

    - Project Template Migration Wizard implemented [RQ:2489]
    - Installer tasks for cloud and download [RQ:2598]


??? bug "Bug fixes and enhancements"

    - Admin manual: Add info about Product Admin Home and Template Admin Home pages [IN:5020]
    - Requirement - Tasks grid can display timezone based exception when certain dates are null [IN:5061]
    - RSS Token on user profile and admin user/edit should be blurred like for TaraVault [IN:5072]
    - Standalone database did not upgrade from 5.4 to 6.x [IN:5127]
    - When a custom ESQL custom graph has no data, it will display a bad error message [IN:5129]
    - Test set detail page: test case section reflects execution status on list page  [IN:5132]
    - Need to reduce some of the erroneous events that get logged [IN:5169]
    - Name in global nav shows HTML encoded characters for non latin characters [IN:5173]
    - Data Sync Project Mappings Confusion since 6.0 [IN:5187]
    - The Assigned Tasks/Requirements/Pending Runs widget shows too many items [IN:5196]
    - Markierungen is not correct German translation for tags [IN:5197]
    - Folder edit buttons are misaligned in version 6.2.0.1 (regression due to fix for Chrome 76) [IN:5198]
    - Installer: v620 installer forgot one needed DELETE clause [IN:5201]
    - Add Test Set API to allow parallel distributed execution [IN:5203]
    - Performance issue when you have lots of test cases with links/parameters [IN:5204]
    - Documentation link is bad for admin > User Details Edit [IN:5207]
    - Installer can timeout when running a specific part of an upgrade [IN:5209]

## Version 6.2.0.1 (September 2019)

!!! bug "Bug fixes"
    Temporary fix to manage a bug introduced in the latest Chrome browser version


## Version 6.2 (August 2019)

!!! info "Summary"
    **Additional Requirement List Views (SpiraTeam and SpiraPlan only)**: In addition to the current hierarchical list view of requirements, additional views will make it easier for users to work with requirements in ways that work for them at the time.

    **Improved Risk Associations (SpiraPlan only)**: Now you can add links between risks to and from other risks, as well as incidents, test cases, and requirements.

??? success "New features"

    - MindMapping requirements functionality  [RQ:1708]
    - Additional Task Board View (tasks by Requirement) [RQ:2357]
    - Documentation links take you to new online documentation system [RQ:2587]
    - Requirements list view: document view [RQ:2537]
    - Requirements list view: sortable grid [RQ:2538]
    - Task Board - add by requirement view [RQ:2550]
    - Release Details - show requirement points [RQ:2551]
    - Rename Package to Epic [RQ:2555]
    - Risks has an association panel and can link to risks, tests, requirements, and incidents [RQ:2556]
    - Upgrade jQuery to 2.2.4 [RQ:2568]
    - Requirements 'mind map' view [RQ:2571]
    - Requirements use case diagram [RQ:2572]


??? bug "Bug fixes and enhancements"

    - Admin Product Membership: error when click save, if All Active is selected and there are inactive members [IN:5109]
    - Project Membership table can have bad entries [IN:5165]
    - License Key does not allow FIPS 140-2 compliance.. [IN:3305]
    - Details pages are missing grey background on type/status area [IN:5088]
    - Certain new v6 API calls are not CORS enabled [IN:5094]
    - Getting system error on Admin -> Edit User page [IN:5160]
    - SpiraTest: some tabs are visible to admins but should not be [IN:5163]
    - Installer: Upgrade from v6.0 to v6.1 leaves no Foreign Keys  [IN:5167]
    - On Product Membership page, system error occurs when deleting a member [IN:5180]
    - Allow tasks to be associated to test cases directly [IN:2990]
    - Online help: section 8.1 about the task list progress column is incomplete [IN:4460]
    - Html and body tags from rich text fields are not stripped out when rendered outside of CK editors [IN:4666]
    - New/Clone product: test type 'is exploratory' flag is not copied over from original template [IN:5080]
    - CKeditors on dark mode on live instances do not switch font color correctly [IN:5093]
    - Viewing source code of a rich text editor in dark mode does not work [IN:5102]
    - Installer - v600 upgrade code forgetting to put NOT NULL on a few columns. [IN:5104]
    - Installer: Backup Block Size could throw error. [IN:5108]
    - Some status colors are incorrect for dark and light themes [IN:5111]
    - Installer: Two Columns upgraded to not match Clean Install [IN:5114]
    - Installer: Race condition in Upgrading certain versions [IN:5115]
    - Add ranking labels to planning board detailed view [IN:5121]
    - Force admin to enter product name before product is deleted [IN:5147]
    - Documentation: formatting problem in two topics: Incident Board and Task Board  [IN:5157]
    - Project Data Tool: Correct Requirements inserts wrong Requirement Type [IN:5159]
    - Unable to expand section 11 of the Online User Guide [IN:4626]
    - Product Home, Req Incident Count widget: problem with requirement icons (either missing or huge, depending on browser) [IN:5063]


## Version 6.1.0.1 (July 2019)

!!! bug "Bug fixes"
    - Navigation bar does not properly restrict access to artifacts by Spira version [IN:5092]
    - Improves dark mode and fixes details pages missing grey background on type/status area in the header [IN:5088]


## Version 6.1 (July 2019)

!!! info "Summary"
    **Dark Mode**: The application follows the color scheme you use in your operating system, or you can set it manually. Dark mode makes every part of the application easier on the eyes and look more gorgeous than ever.

    **Improvements to Administration**: With easier filtering and more intuitive controls for key pages like tables and managing workflow permissions, administration is now more user friendly than ever.

    **Version 6 of our SOAP and REST APIs**: Our existing APIs are as compatible as they can be with version 6 of SpiraPlan. The new API version will allow access to new features, such as those from templates.

??? success "New features"

    - Enable beta dark color mode for modern browsers [RQ:2557]
    - Add new 6.0 API for existing calls [RQ:2308]
    - All workflow status field permissions are set with radio buttons not checkboxes [RQ:2408]
    - Change the artifacts that create an initial item to use a blank name v.s. "New Artifact" [RQ:2498]
    - Admin type, priority, and status pages can be filtered in the same way as components [RQ:2502]
    - Add new API functions for template management [RQ:2542]
    - Can filter admin users and product membership lists by all or active only [RQ:2548]
    - Planning Boards: Hide Statuses that have no transition to them or from them for RQs and TKs [RQ:2549]


??? bug "Bug fixes and enhancements"

    - Issues with inactive products and templates  [IN:5045]
    - Activating old project changes its assigned template [IN:5046]
    - Project role artifact view permissions are being applied, when current user has sys admin permission [IN:4140]
    - Test Set Status Widget includes deleted Test Sets [IN:4363]
    - Permission error: Attachment of a Test run can be deleted with only create permission [IN:4784]
    - API to POST artifacts causes problems on servers east of GMT [IN:4785]
    - Document_RetrieveFolders call dies [IN:4868]
    - Add friendlier error when deleting a test case parameter that is in use [IN:4915]
    - Add ability to clone a product/project in different ways [IN:4945]
    - Workspace dropdown includes inactive templates [IN:4983]
    - Test execution initial screen: cannot proceed after getting a prompt to fill in a required custom field [IN:4999]
    - Test execution: pause button does nothing [IN:5012]
    - Error on Product Admin Dashboard [IN:5021]
    - Installer: Null Reference check missing in PreReq check [IN:5081]
    - Support change/remove user membership for a project using 6.0 API [IN:4107]
    - Add ability to specify/change project group with API [IN:4108]
    - User defined start page not properly remembered on refresh/login [IN:4966]
    - On commit detail page, the link "Back to Commit List" is incorrect [IN:4974]
    - SpiraPlan: risk default values and sample data contain a misspelling [IN:4976]
    - Test configuration detail page: entries do not appear unless you refresh the page [IN:4978]
    - For TaraVault users, admin menu for product settings has incorrect label [IN:4995]
    - Project Home: All Pending Test Runs, change permissions for reassign and delete buttons [IN:4998]
    - Test execution: in table view, Pass All button does not work at first [IN:5016]
    - Tree view wraps and obscures long names - eg on adding an existing attachment [IN:5036]
    - Screen images not correctly sized on test run details page [IN:5037]
    - Installer: Upgrade overwrites existing 'DataSync' config file. [IN:5040]
    - Blank space is shown where the main nav bar should be, under certain circumstances involving an inactive template [IN:5062]
    - Test configuration detail page: remove button does not work [IN:4979]
    - Test execution: table view, image button has no label [IN:5015]
    - Admin Project History list has Revert and Purge All too close together [IN:5039]
    - Risk Details: 'Empty' name watermark doesn't match other Details Screens [IN:5068]
    - Installer: Not properly entering DataSyncConfig config tokens. [IN:5075]


## Version 6.0.0.3 (May 2019)

!!! bug "Bug fixes"
    - Displaying reports shows error (SpiraTest only) [IN:5000]
    - Null error when saving a test from Rapise into Spira 6.0.0.2 [IN:5004]
    - On premise installer fixes


## Version 6.0 (April 2019)

!!! info "Summary"
    **Enterprise Risk Management [SpiraPlan only]**: Risks have their own types, statuses, workflows, and mitigations. New reports for risks, as well as charts and a risk cube have been added. 

    **Changes to certain names in the system**: Projects are now called Products; Project Groups are now Programs; and Iterations are now Sprints.

    **Better manage your products (projects) with templates**: Templates now control many aspects of a product (such as notifications, workflows, custom fields), and can control many products at once. Each existing product from 5.4 will have its own template. Every new product can have its own template or be managed by an existing template.

    **New customizations at the template level**: Requirement, Test Case, Document, and Task types are customizable. Documents can now be managed using workflows to allow you to control versioning and check-ins. Notifications now apply to products in a template and no longer the same system wide.

    **Improve navigation and new administration user interface**: New login screens and a completely reworked navigation menu in the application make using SpiraPlan easier than ever. Navigation is more mobile friendly and intuitive. Administration menus are now only ever one click away.

??? success "New features"

    - Risk Administration (Project Template)
        - Edit Risk Statuses [RQ:2417]
        - Edit Risk Types [RQ:2418]
        - Edit Risk Impacts [RQ:2419]
        - Edit Risk Probabilities [RQ:2420]
        - Notifications for risks are customizable and get sent out properly [RQ:2488]
        - Edit Risk Workflows [RQ:2421]

    - Risks
        - Top open risks [RQ:2430]
        - Risk List Page sidebar donut chart [RQ:2492]
        - Risk List Page [RQ:2411]
        - Risk Details page displays standard risk fields inc. exposure [RQ:2422]
        - Display risk custom properties [RQ:2423]
        - Risk Mitigations [RQ:2424]
        - Risk Details page Tasks tab [RQ:2425]
        - Risk Details page Discussions / comments [RQ:2427]
        - My Assigned Risks [RQ:2428]
        - Assigned Risks RSS feed [RQ:2429]
        - Project Home Risk Widget / risk cube [RQ:2431]
        - Risk summary report [RQ:2434]
        - Risk detailed report [RQ:2435]

    - Project Templates [RQ:1703]
    - Workflows for documents, plus check-in/out/review [RQ:1930]
    - Switch licensing to annual vs. perpetual [RQ:2306]
    - Database Refactoring/Changes for future functionality [RQ:2174]
    - UI: redesign login pages [RQ:2307]
    - Cross app navigation is intuitive, quick, and clear [RQ:2351]
    - UI: replace gif/png icons with svgs [RQ:2352]
    - Customizable fields for non-incidents [RQ:2309]
    - Refactoring URL structure for existing Admin pages [RQ:2360]
    - New System Administration Home Page [RQ:2362]
    - New Project Admin Home Page [RQ:2365]
    - Add Active flag to Data Sync Plugins [RQ:2366]
    - Updates to program naming [RQ:2368]
    - Make additional fields customizable [RQ:2369]
    - Add database design for BDD support [RQ:2381]
    - Administrators and owners navigation is streamlined and consistent throughout the app [RQ:2390]
    - Users can see My Assigned Documents on the My Page [RQ:2398]
    - Can add and view comments on the document details page, consistent with the workflow [RQ:2399]
    - New installer for 6.0 [RQ:2400]
    - Onboarding framework gives quick info to new and to upgrading users [RQ:2401]
    - Project Template Migration Wizard - disable ability to change template on a product [RQ:2402]
    - Remove Change Projects Button in Admin [RQ:2403]
    - Additional standard statuses for requirements, tasks and test cases [RQ:2409]
    - Change "project" to "product" in the UI to better align with users' real business need [RQ:2455]
    - Switch history tracker to use new MEANING field [RQ:2484]
    - API backwards compatibility to make v3/4/5 work with templates [RQ:2490]
    - Template Admin Home Page  [RQ:2491]
    - Database support for multiple approvers [RQ:2503]


??? bug "Bug fixes and enhancements"

    - System Administration - Add/Edit Users: German translation for "Locked Out" misleading [IN:2230]
    - security issue when having 2 projects open in browser tabs [IN:2651]
    - Limited view role can access source code pages when should not be able to [IN:4754]
    - When a test case is created from a requirement, it lacks the default test step. [IN:3499]
    - Default task notification template does not include the task name [IN:3584]
    - System Error when trying to display the detail page for some Project History Changes [IN:4691]
    - The 'Loading / Activity' notification is nice, but off-screen. [IN:4876]
    - A general system admin should be added as an owner when they create a new template/program/product [IN:4911]
    - Administration > Projects > Project Associations: limit the list of artifact types for selection [IN:4553]
    - Can click on artifact id field on details page to copy to clipboard [IN:4793]
    - Can't easily blank out a previously populated Actual Result in normal test execution [IN:4802]