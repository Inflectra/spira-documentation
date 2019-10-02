# Product: Changing the Template a Product Uses

## Introduction
Each product in Spira has a template that controls the bulk of how that product is configured and will work for end users. Each product is controlled by one template, though each template can control many products at once. A template affects a product’s fields, custom properties, workflows, and more.

If you change a product’s template, you are not changing the core data inside the product. But you are changing how that product will work. This is not something to do lightly. There is a deep connection between a product and its template. When you change templates, you are changing the workflows, and also all the links in the product from the old template to the new template. 

It’s like trying to change out the engine in a car by replacing it with parts from another engine. If that new engine has different pistons and gears then the car will look the same, with the same seats, the same windows, and the same doors. It will just run a little differently. Below, we explain in gory detail:

* what happens when you try to change the engine (the template) of your car (product)
* how to work out if your system is set up to make the process run as successfully as possible
* where things are different between the two relevant templates, what will happen to your product.


## Key Facts
- By changing a product's template to a new one, you can make many pre-existing products be controlled by a single template. This can make it really easy to, for instance, change the workflow across lots of products at once
- Changing a product’s template is irreversible.
- The change updates all links in the product that point to the old template so that they point to the new template
- The templates are 100% **not** changed in any way. No templates are merged together, and none of their data changes
- No other products are changed in any way, whether or not they are using the old or the new templates
- All data in the product that is **not** controlled by a template 100% does **not** change in any way (this includes product membership, components, names, description fields, comments, most custom fields)
- The application will show you how much data loss there could be, but if you are at all worried about losing data take a pause.
- The only custom fields that change are those of type lists or type multilist. No other custom field is altered (though it may not display as you expect)
- The only standard fields that change are those controlled by templates (see the full list below)
- After changing templates any data syncs the product uses are turned off and their fields reset
- You can see a success audit entry in the event log that records when a product's template was changed and what it was changed from and to


## Health Warnings
- Because references inside the product to the template it uses get updated/changed there is a chance of some data loss.
- Because this may change many records in your product, we recommend that you make the change at a time when users are not actively using the system - certainly not that particularly product.
- If you work in a heavily regulated environment we recommend not making use of this feature


## How to Change the Product's Template
1. You need to be a product administrator or system administrator to perform this action
2. Make sure the starting and ending templates for the product are as closely aligned as possible/required - based on the standard and custom fields specified above
3. Go to the “[View/Edit Products](System-Workspaces.md#viewedit-products)” page in system administration
4. Click “Edit” next to the product you want to change templates for
5. If you are not a system administrator, go to the Admin home page for the product and click “View Details” in the overview widget in the top left of the page
6. On the edit product page you will see a “Product Template” field. Click the “Change” button to its right
7. A popup will show. Read the warning message, and if you wish to continue select the active template you are changing the product to from the alphabetical list (this also shows the template ID)
8. Click “Next”
9. If you see a little table at the top of the next page of the popup then some standard field data will be lost by changing template. The number of artifacts affected for each field will be listed
10. Read the warning message. If you wish to proceed, type the name of the product into the text box and click “Change”
11. A progress meter will show. When it disappears, the product’s template has been successfully changed.


## What happens to standard fields
As mentioned above, only those standard fields controlled by templates can change when changing templates for a product. Let’s call these fields “dynamic fields” No other standard fields (i.e. non custom fields) in the product will change in any way. The dynamic fields in SpiraPlan are below (not all of these are available in SpiraTeam or SpiraTest):

  - Requirement Importance
  - Requirement Type
  - Document Status
  - Document Type
  - Test Case Priority
  - Test Case Type
  - Incident Priority
  - Incident Severity
  - Incident Status
  - Incident Type
  - Task Priority
  - Task Type
  - Risk Impact
  - Risk Probability
  - Risk Status
  - Risk Type

For each of the dynamic fields above the system will:

1. Try and find a matching name for each entry in the old template in the new template
2. If there is an exact match, all references in the product to that name get updated to the matching reference in the new template
3. If there is no match and the field is not required then all references in the product to that name are deleted
4. If there is no match and the field is required then all references in the product to that name are replaced with the default value in the new template


### Example of a non required field - eg incident priority

| # | Old template values | New template values | Value after changing template |
|---|---------------------|---------------------|-------------------------------|
| A | high   | high   | high   |
| B | middle | medium | [null] |
| C | low    | low    | low    |
| D | v low  | -      | [null] |


### Example of a required field - eg incident type

| # | Old template values | New template values | Default in new template | Value after changing template |
|---|---------------------|---------------------|-------------------------|------------------|
| E | bug         | bug         | Y | bug         |
| F | incident    | issue       |   | bug         |
| G | enhancement | enhancement |   | enhancement |
| H | limitation  | limit       |   | bug         |


## What happens to custom fields
As mentioned above, only custom fields of type list or multilist are affected by changing templates. No other custom field changes in any way and custom lists are also completely unchanged. 

Matching custom fields between templates is more complicated than for standard fields. Before the system can match values of custom list/multilist fields, it checks that the custom field in the old template has a matching field in the new template. 

A custom list/multilist field has a match between the templates if: 

1. There is a custom field at the exact same position in both templates
2. These two fields are the exact same type (eg multilist)
3. These two fields have the same name
4. The custom lists that the two fields use have the same name

If all the above conditions are met, the system will:

1. Try and find a matching name in the relevant custom lists that the old template uses for that field and the new template uses for that field
2. If there’s an exact match between these names, all references in the product to that name get changed from the old template to the new template
3. If there is no match then the old data is not changed at all (though it may appear like it was blanked out when you look at it in the application)


## How does the history get updated?
When you look at the history for artifacts after the template has been changed, you won’t see any difference. Behind the scenes, references to dynamic fields and custom list/multilist fields, are updated to the new template. 

This so that, where possible, when you try and revert a history change, the reverted data updates the artifact to the new template - not the old one. If there was no match found when changing templates, then reverting history will not revert that particular field.


## What about test configurations?
Test configurations use the template’s custom lists. So when you change templates to a new template with different custom lists, what will happen? The system will:

1. Look for a custom list in the new template that has the exact same name as that in the old template
2. If there is a match for the list, it looks for matches by name of each value between the templates
3. If there is a match on a name in the list, then any configuration using that name gets updated to use the matching value in the new template
4. If there is no match then any rows in the test configuration using that value are removed


## How to prepare for the change
As you will see above, the process of changing templates is not without risks. We flag many of these risks to you during the process itself to guide you. Below are five steps to help you prepare for changing to a product's template.

1. **Check your standard "dynamic" fields**: go through all of the dynamic fields (listed above) and check that every name in the old template has an exact match in the new template. These names do not need to be in the same position necessarily, and it does not matter if they are active or inactive. All that matters is that every name in use has a matching name in the new template 
2. **Check all custom lists in use**: for all custom lists that are used by custom fields or test configurations, make sure that the names of the lists match between the templates, and that all the values within the lists match as well 
3. **Check custom fields/properties of type list/multilist**: make sure that each field is in the same position (1 to 30) and has the same name and type in both templates
4. **Understand the risks and benefits of changing**
5. **Get buy in for the change**