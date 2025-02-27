# Linked Lists

!!! warning "Some of this SpiraApp's functionality is not compatible with SpiraTest"

This SpiraApp helps admins create dynamic and powerful customizations for end users when they work with artifacts on details pages. It lets you create pairs of list fields (dropdowns) that are linked together, so changing one list dynamically updates the options in the other list. For example, an Incident of Type 'Enhancement' could have it's owner field limited to a certain group of users, but an incident of type "Bug" could have the owner field limited to a different group of users. The SpiraApp is highly customizable using the product settings to meet a variety of different use cases.

!!! info "About this SpiraApp"
    - [ ] system settings
    - [x] product settings 
    - [ ] product template setup required
    - [x] toolbar button on product settings page
    - [x] runs automatically on the requirement details page
    - [x] runs automatically on the release details page
    - [x] runs automatically on the test case details page
    - [x] runs automatically on the test set details page
    - [x] runs automatically on the incident details page
    - [x] runs automatically on the document details page
    - [x] runs automatically on the task details page (not available in SpiraTest)
    - [x] runs automatically on the risk details page (not available in SpiraTest)

!!! warning "Limitations"
    This SpiraApp is intended to guide your employees in best practices and simplify your workflows without adding extra permissions. It works specifically by limiting dropdown options on artifact details pages only for both single select and multi-select list fields.
    
    This SpiraApp does not: 
    
        - work on artifact list pages
        - work with any fields that are not lists
        - change the actual value of any field (only the items shown in its dropdown)
        - restrict any changes made on list pages or via the API 
        - modify or impact the workflow (including control the available transitions based on a list field)

## Setup
### Product Settings
Once the SpiraApp has been activated system wide and enabled for a product you can edit its product settings.

This is where you define the custom links between List fields on artifacts. Use the following format for each link in an artifact's setting textbox:  

`{primary field name}={field value} | {linked field name}={comma separated list of field values}`  

See the following screenshot for an example:  

![Incident Rules: IncidentTypeId = Security | PriorityId = 1 - Critical, 2 - High, 3 - Medium](img/linked-lists-incident-rules.png)

!!! info "Example admin configuration"
    Here is a more detailed worked example for the incident artifact window:

    - select the **primary field** using the [field names](../Developers/SpiraApps-Reference.md/#available-field-names). This is the field that, when changed, will control the linked field. This field must be a list (dropdown) field. For example, if you want the primary field to be the incident type, enter `IncidentTypeId`. The setting should now look like this: `IncidentTypeId`
    - for the primary field's **field value** enter the exact text as it appears in the dropdown for the field on the details page. This is the value that, when selected, will change the values visible in the linked list chosen. For example, if you want to control what happens when the incident type is a "Security", enter `Security`. This setting should now look like this: `IncidentTypeId=Security`
    - next, you need to specify the list that you want to link with. This is the field that will be controlled by the primary field (the type field) and may be a list (dropdown) field. For example, if you want the linked field to be the incident priority field, enter `PriorityId`. The setting should now look like this: `IncidentTypeId=Security |  PriorityId`
    - finally, you need to provide the list of values that the priority field should show when the incident type is Security (with all other values being hidden). For example, because security incidents are so important, let's assume we want to hide the lowest priorities, and instead want to show only the critical, high, and medium priorities. To do this copy and paste these values are displayed in the application, separated by commas. The setting should now look like this: `IncidentTypeId=Security | PriorityId = 1 - Critical, 2 - High, 3 - Medium`
    - to add extra settings, place them on a new line

You can also use **multiple primary fields** so that the linked list is only changed if each specific primary field's value is set as specified. In the example below we have a setting for requirements:

![Requirement Rules: RequirementTypeId = Feature,  ComponentId = Database | OwnerId = Backend Developer](img/linked-lists-requirement-multiple-primary.png)  

This rule specifies that if a requirement has both a Type of Feature *and* a Component of Database, then owner dropdown list will be limited to only "Backend Developer". In reality, 'Backend Developer' would be replaced by the first and last name of a user in your Spira instance.

**Custom properties** are supported. These must be listed like "Custom_01" for the field name. For the field values, you use the user-defined text values as they appear on the details page, just like built-in fields.

You can also set multiple rules to apply to the same list field. In this case, if both rules apply at the same time then the linked list's dropdown will be limited to the values shared between the limiting rules. For example:

![Task Rules: (first rule): TaskTypeId = Development | OwnerId = Intern, Developer1, Developer2, Product Manager. (Second rule): ComponentId = Administration | OwnerId = Product Manager, Permissions Expert](img/linked-lists-requirement-overlap-effected.png)  

In this case, there are 2 task rules that both apply to the owner field - one with a primary field of type, and the other of component.

- When a task has the Development type, its owner field would be limited to the four users listed. 
- When a task has the Administration component, its owner field would be limited to the three users list
- When a task has both a type of Development and a component of Administration, then its owner field will be limited to the overlap between the four users and the three users in each rule, whicch will be just the Product Manager in this example, because that is the only option included in both rules.

The menu button at the bottom the settings page can be used to **validate your settings**. It will check each settings box for valid field names and make sure none of the rules conflict with any other for a specific artifact. If there are any conflicts or a field name is spelled incorrectly, it will say which artifact setting has invalid rules.

## Using the SpiraApp
This SpiraApp works automatically on the details page for the following artifacts:

- Requirements
- Releases
- Test Cases
- Test Sets
- Incidents
- Documents
- Tasks
- Risks

The SpiraApp applies the appropriate rules to the dropdown menus on a page in three cases: 

- When a user first opens the details page
- When a user changes the artifact on the details page (for example, by selecting one from the sidebar)
- When a list field that is set as a primary field in any setting is changed. 

This will mean that list field dropdown options will always be limited based on the rules specified when working with artifacts on the details page.

Here is an example of using this SpiraApp to limit the Priority of incidents of the type "Security".

![Incident has type of "Security" and the priority dropdown is selected, showing 3 options: "1 - Critical", "2 - High", "3 - Medium"](img/linked-lists-incident-example.png)

Notice that the options listed in the Priority dropdown are the exact options listed above in the [Incident Rules](#product-settings). 

When the type is set to something other than "Security", you still see all of the normal options, as shown below.

![Incident has type of "Incident" and the priority dropdown is selected, showing 4 options: "1 - Critical", "2 - High", "3 - Medium", "4 - Low"](img/linked-lists-incident-nonexample.png)