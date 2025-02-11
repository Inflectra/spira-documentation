# Linked Lists
This SpiraApp helps you link artifact list fields so that if a specific field is set to a certain value, then another list field will have its dropdown options limited. For example, an Incident of Type 'Enhancement' could have it's owner field limited to the user who is the Product Owner, because they review all logged enhancements so they can be added to the product backlog. The SpiraApp is highly customizable using the product settings, so the behavior can be applied to each product separately.

!!! info "About this SpiraApp"
    - [ ] system settings
    - [x] product settings 
    - [ ] product template setup required
    - [x] toolbar button on product settings page
    - [x] runs automatically on the requirement details page
    - [x] runs automatically on the test case details page
    - [x] runs automatically on the incident details page
    - [x] runs automatically on the document details page
    - [x] runs automatically on the task details page
    - [x] runs automatically on the risk details page

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
As you can see from the example above, if you want to use the Type field for Incidents, you enter "IncidentTypeId" in the spot for the field name. For the field values, you must use the exact text string as it appears in the dropdown for thar field on the details page. For Incident Priority, you would use "1 - Critical", "2 - High", etc. The same goes for all other fields.  
You can also use multiple primary fields to only apply a rule if each primary condition is satisfied. Here is an example: 
![Requirement Rules: RequirementTypeId = Feature,  ComponentId = Database | OwnerId = Backend Developer](img/linked-lists-requirement-multiple-primary.png)  
This rule specifies that if a requirement has Type = Feature and ComponentId = Database, then "Backend Developer" will be the only user shown in the Owner dropdown on the requirement details page. In reality, 'Backend Developer' would be replaced by the first and last name of a user in that Spira product.

Custom properties are supported, and must be listed like "Custom_01" for the field name. For the field values, you use the user-defined text values as they appear on the details page, just like built-in fields.
