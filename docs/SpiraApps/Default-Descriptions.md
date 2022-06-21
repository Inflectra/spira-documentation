# Default Descriptions SpiraApp

!!! warning "Some of this SpiraApp's functionality is not compatible with SpiraTest or SpiraTeam"

This SpiraApp lets users to create artifacts from their details pages with pre-populated default descriptions. These descriptions are added automatically when creating new artifacts from the relevant details page. The following artifacts are supported: requirements, releases, test cases, incidents, tasks, and risks.

!!! info "About this SpiraApp"
    - [ ] system settings
    - [x] product settings 
    - [ ] product template setup required
    - [x] runs automatically on the requirement details page
    - [x] runs automatically on the release details page
    - [x] runs automatically on the test case details page
    - [x] runs automatically on the incident details page
    - [x] runs automatically on the task details page (not available in SpiraTest)
    - [x] runs automatically on the risk details page (not available in SpiraTest or SpiraTeam)

## Setup
### Product Settings
Once the SpiraApp has been activated system wide, and enabled for a product you can edit its product settings to add/update the default descriptions for the relevant artifacts.

![product settings page](img/defaultDescriptions-product-settings.png)

Enter the default description desired in each of the rich text boxes. If a rich text box is left blank, no default description will be added when making that artifact. You can use all available formatting options, except for pasting images. 

## Using the SpiraApp
When any user creates an artifact on the details page for that artifact, any default description set is automatically set as the description. The user can then continue to edit the newly created artifact as normal, including editing the description. Once an artifact has been created there is no way to reset or reinsert the default description for that artifact.

**Note** when creating artifacts (like requirements) on the list page, the default description is not added. You must create the artifact from the standard details page.