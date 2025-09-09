# Versioning
!!! abstract "Compatible with SpiraTest, SpiraTeam, SpiraPlan"

!!! warning "This SpiraApp works with Spira v8.13+" 

This SpiraApp helps you create incremental versions for requirements and test cases. This allows you to easily mark a requirement or test case as a new version. Versioning can be restricted by workflow as well.

!!! info "About this SpiraApp"
    - [ ] system settings
    - [x] product template setup required
    - [x] product settings 
    - [x] toolbar button on the requirement details page
    - [x] toolbar button on the test case details page

## Setup
### Product Template Setup
- [x] Add a plain text custom property for Requirements in the product's template.
- [x] Add a plain text custom property for Test Cases in the product's template.

THese custom properties store the version number created by the SpiraApp. You may want to call them `Version` but you can call them whatever you want.

### Product Settings
Once the SpiraApp has been activated system-wide and enabled for a specific product, you can configure its product-level settings. These settings allow you to control:

- For each artifact separately:

    - the custom property (set above) to use to store the version
    - the version template pattern to use - make sure this includes `{version}` in it somewhere, which will become 1, 2, 3 etc as you create new versions. You can for example have a template like this: "version {version}" or "{version}.0".

- General settings that apply to all artifacts in the same way:

    - whether or not to append the version number to the artifact name (off by default)
    - whether or not to restrict creating new versions by workflow (off by default). When on you can only create a new version when the current workflow allows the Name field to be edited. In other words, when this setting is checked you can not create a new Version if the Name field is disabled.

## Using the Spira App
The SpiraApp is accessed from the Requirement or Test Case Details page, allowing users to create a new version as needed. To use the SpiraApp:

- click the Versioning button in the toolbar to show the dropdown
- click the Versioning option in the dropdown

If the SpiraApp has been properly configured and you are allowed to create a version then:

- the version custom property field will be incremented by 1
- if the Name field is set to update, the new version will be added / updated to the artifact name


!!! info "Tips and tricks"
    - If the product admin has not properly configured the SpiraApp you will get an error explaining this
    - If the version custom property has text in it already that does not match the template set by the product admin, then the version will not be created
    - Workflow controls only apply to detecting if the Name field is editable or not