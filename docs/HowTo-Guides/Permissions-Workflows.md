# Permissions and Workflows

## How to make a field required or hidden or disabled {: .section-break}
There are two ways that a field can be required. The best way to control this is through the workflow. This controls what fields are required, not required, disabled/read only, or hidden.

### Workflow
The below works for any artifact that has a workflow. Below we changing the Incident workflow

1. Find the template that your product is using
2. As a template administrator go to Template Administration > Incidents > Workflows
3. If you have more than workflow decide which one to change (different incident types can be set to use different workflows)
4. Click `Steps` next to the workflow
5. The left most column shows the steps/statuses. Decide which steps/statuses you want to change
6. For each relevant step/status click on the name of the status
7. Edit the field(s) by selected the appropriate option - eg if you want the "Detected Release" to be required, make sure "Required" is selected.
8. Hit `Save`

### Custom properties
Custom properties have a special option that says whether a blank value is allowed or not. If a blank value is allowed, then the field will onyl be required if the workflow step/status says so. If a blank value is *not* allowed then anytime you try to save an artifact with that field and the value is blank it will prompt you for a value.

To change if a blank value is allowed or not for a custom property:
1. Find the template that your product is using
2. As a template administrator go to Template Administration > Custom Properties > Edit Custom Properties
3. There is a dropdown at the top of the page - make sure you open this and pick the artifact you want to edit
4. Find the custom property you want to change
5. Click `Edit Defintion`
6. Go to the `Options` tab in the popup
7. Set the "Allow Empty" dropdown to Yes or No as desired
8. Hit `Save`


## Why does a user not see the right transitions {: .section-break}
When a user goes to look at the detail of an artifact they may be able to change the status by transitioning from one status to another. This is called a transition. What transitions show up when for what users is controlled by a number of things.

To troubleshoot the issue you need to be a template administrator. The summary steps to review are below. Please refer to the [admin guide](../../Spira-Administration-Guide) for more information.

1. Is the right workflow in use? 
    - You can have lots of workflows for an artifact
    - One workflow will be the default
    - Other workflows can be made inactive
    - Different workflows can be assigned to different types of that artifact
    - **So...** if you have an incident of type bug, check what workflow is assigned to bugs - that is the one to explore
2. Is there a transition in the right place?
    - Now that you know you are looking at the right workflow you can see if the transition exists
    - Look at the starting step/status and see if there is a transition going from it to the correct new step/status
3. Are the right people able to see and execute that transition?
    - You should now have the right workflow and the right transition
    - The next place to look is at the transition itself
    - Click on the transition button on the workflow page
    - Can the right users see/execute the transition? 
    - Make sure to enable the necessary product roles and hit `Save` to commit any changes