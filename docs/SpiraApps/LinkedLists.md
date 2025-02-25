# Linked Lists

!!! warning "Some of this SpiraApp's functionality is not compatible with SpiraTest"

This SpiraApp helps you link artifact list fields so that if a specific field is set to a certain value, then another list field will have its dropdown options limited. For example, an Incident of Type 'Enhancement' could have it's owner field limited to the user who is the Product Owner, because they review all logged enhancements so they can be added to the product backlog. The SpiraApp is highly customizable using the product settings, so the behavior can be applied to each product separately.

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
This SpiraApp limits dropdown options on Artifact Details pages, but users can avoid these limits by using the API or editing fields on list pages. This is intended to guide your employees in best practices and simplify your workflows without adding extra permissions.

## Setup
### Product Settings
Once the SpiraApp has been activated system wide, and enabled for a product you can edit its product settings.

This is where you define the custom links between List fields on artifacts. 
Use the following format for each link in an artifact's setting textbox:  
{primary field name}={field value} | {linked field name}={comma separated list of field values}  
See the following screenshot for an example:  
![Incident Rules: IncidentTypeId = Security | PriorityId = 1 - Critical, 2 - High, 3 - Medium](img/linked-lists-incident-rules.png)


You must use the lookup name for each field name, which can be found in SpiraDocs [here](../Developers/SpiraApps-Reference.md/#available-field-names).  
As you can see from the example above, if you want to use the Type field for Incidents, you enter "IncidentTypeId" in the spot for the field name. 
For the field values, you must use the exact text string as it appears in the dropdown for that field on the details page. 
For Incident Priority, you would use "1 - Critical", "2 - High", etc. The same goes for all other fields.  

You can also use multiple primary fields to only apply a rule if all values are matched. 
Here is an example: 
![Requirement Rules: RequirementTypeId = Feature,  ComponentId = Database | OwnerId = Backend Developer](img/linked-lists-requirement-multiple-primary.png)  
This rule specifies that if a requirement has Type = Feature and ComponentId = Database, then "Backend Developer" will be the only user shown in the Owner dropdown on the requirement details page. In reality, 'Backend Developer' would be replaced by the first and last name of a user in your Spira instance.

Custom properties are supported, and must be listed like "Custom_01" for the field name. For the field values, you use the user-defined text values as they appear on the details page, just like built-in fields.

The menu button at the bottom the settings page can be used to validate your settings. It will check each settings box for valid field names and make sure none of the rules conflict. If there are any conflicts or a field name is spelled incorrectly, it will say which artifact setting has invalid rules.

If multiple rules apply to a single dropdown at once, the dropdown will be limited to 
the values shared between the limiting rules. Take this example:
![Task Rules: (first rule): TaskTypeId = Development | OwnerId = Intern, Developer1, Developer2, Product Manager. (Second rule): ComponentId = Administration | OwnerId = Product Manager, Permissions Expert](img/linked-lists-requirement-overlap-effected.png)  
In this case, if a Task has the Development type, its Owner field would be limited to the four users listed. If it also has the Administration Component,
then its owner field will be limited to just the Product Manager, because that is the only option included in both rules.

## Using the SpiraApp

This SpiraApp works automatically on the details page for Requirements, Releases, Test Cases, Test Sets, Incidents, Documents, Tasks, and Risks.

The SpiraApp applies the appropriate rules to the dropdown menus on a page in two instances: When a user first opens the details page, and whenever a dropdown that is used as a primary field is changed. This way the dropdown options will always be limited to what the rules specify whenever an artifact is being edited on the details page.

Here is an example of using this SpiraApp to limit the Priority of incidents of the type "Security".
![Incident has type of "Security" and the priority dropdown is selected, showing 3 options: "1 - Critical", "2 - High", "3 - Medium"](img/linked-lists-incident-example.png)

Notice that the options listed in the Priority dropdown are the exact options listed above in the [Incident Rules](#product-settings). 

When the type is set to something other than "Security", you still see all of the normal options, as shown below.
![Incident has type of "Incident" and the priority dropdown is selected, showing 4 options: "1 - Critical", "2 - High", "3 - Medium", "4 - Low"](img/linked-lists-incident-nonexample.png)