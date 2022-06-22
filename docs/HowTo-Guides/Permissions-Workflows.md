# Permissions and Workflows

## How do Spira's permissions and workflows work {: .section-break}
You give users specific roles to give them specific permissions. These permissions are mostly about what that role can do with each artifact in general. Users with a role that lets them view incidents can view every single incident in the product.

A workflow controls what a specific artifact will look like and how it can be edited. For example Bug1 may have lots of fields hidden, while Bug2 has every field visible. Bug1 and Bug2 look different because their display is controlled by different parts of a workflow system. One workflow step applies to Bug1 and a different workflow step applies to Bug2.

So roles let admins control who can see what in general. Workflow let admins control, if you can see something (say a bug), exactly how that bug (for example) should behave based the bug's state at the time. When you change an item's state (by changing this bug's status, for instance) you can change how it will look or behave.

How do you change an item's state? The most common way is changing the item's status. This is called a *transition*. Transitions are special because they let users make this big changes to something - for instance hiding or showing information. Because transitions can be so powerful, they can also be protected. An admin can control who can carry out each and every transition (including based on product roles).

Taken together, this system of roles and workflows, with their combination of permissions, statuses, and transitions, give admins a lot of power to customize how things should work. They are powerful, but also they can be fiddly. It can be confusing to a user or an admin why things work one way for one user, but differently for another. 

The tips and tricks below should help work through the most common problems and stumbling blocks.


## What does a workflow do and control {: .section-break}
Workflows are a way to control a number of things about your artifacts. A workflow is based on a series of steps (statuses) that you move the artifact through. 

At each step you can control:

- what fields are hidden
- what fields are visible
- what fields are disable (cannot be edited)
- what fields cannot be empty (you will not be able to save the artifact until these fields are filled in)
- which steps you can move to next - this is called a transtion

Transition are how you move from one step (status) to another. At each workflow step you can make as many transitions as you want. Each transition will move the workflow to a new step. For each transition you can control:

- which product roles can carry out the transition
- if the author of the artifact can carry out the transition
- if the current owner of the artifact can carry out the transition
- if a digital signature is required to carry out the transition


## What does a product role do and control {: .section-break}
When you add a user to a product, you have to set the specific product role they should have. This grants them specific permissions to view certain data, edit other data, maybe the ability to delete some data too. 

Each user has to be actively given a particular role for each product. In other words, you cannot make a user a member of a product without giving them a specific role. Likewise, you cannot make a user a "Tester" for any products they are or will be a member of.

### Permissions
The application ships with some built-in product roles but you can edit these roles or add new ones too. Each role defines if users with that role:

- are admins of that product
- can only see artifacts assigned directly to them (ano nothing else)
- can (set on an artifact by artifact basis) view, create, delete, edit, or bulk edit an artifact

For example:

- If one user cannot see test cases but another user can see test cases in a product, that is because they each have different roles on that product
- If a user can see incidents in one product but only requirements in another, that is because they have different roles in each of those products
- If a user can see risks but the button to add a new risk is disabled or hidden, that means their role does not give them the permission to create risks only to view them

### Other uses for product roles
Your product role is used to control if you:

- can carry out a specific workflow transition
- will receive a notification after a specific event (for example, when a new bug is logged)

## How to stop users being able to delete artifacts {: .section-break}
Product Role permissions control if users with that product role can or cannot delete a specific artifact. To stop users being able to delete artifacts, edit the product role. Make sure that the "Delete" checkboxes are NOT checked for all relevant artifacts.

## Why is a field disabled or hidden or required {: .section-break}
Each field can be controlled by the relevant workflow to show, hide, disable, or be required. If you thought a field should be visible, but in reality it is hidden, this is the workflow at work.

The workflow controlling that specific artifact has a step that matches the current status of the specific artifact. That step sets whether each field is visible, disabled, hidden, or required. You need to work through [how this is happening](#how-to-make-a-field-required-or-hidden-or-disabled).

## How to make a field required or hidden or disabled {: .section-break}
There are two ways that a field can be required. The best way to control this is through the workflow. This controls what fields are required, not required, disabled/read only, or hidden.

### Workflow
The below works for any artifact that has a workflow. Below we are changing the Incident workflow

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
2. As a template administrator go to Template Administration, find the artifact section you need, and click its "Custom Properties" link
4. Find the custom property you want to change
5. Click `Edit Defintion`
6. Go to the `Options` tab in the popup
7. Set the "Allow Empty" dropdown to Yes or No as desired
8. Hit `Save`

## Why can't I change the status of an artifact {: .section-break}
If you are looking at an artifact and the status has no button next to it, then you cannot change its status. The button (if there) shows which transitions you can do to move the artifact to a new status.

Why is this button missing? Either because:

1. you do not have the correct permissions to see any of the available transitions
2. There are no transitions at all from the current status

Read more about these issues [below](#why-does-a-user-not-see-the-right-transitions)

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


## What workflow controls a specific artifact {: .section-break}

**Note**: the following does NOT apply to releases.

When you are looking at a specific artifact on its full details page, the fields you see or not and which transitions are available are determined by the workflow. However, you can have more than one actie workflow for each artifact. How can this be? 

Because you can match a workflow to a specific type. This means that one type (say incidents of type bug) will use one workflow, but a different type (say incidents of type enhancement) will use a second workflow.

If you do not know why you are seeing what you are seeing for a workflow, it could be because a different workflow is actually controlling the artifact. You can check this by:

1. Go to the specific details page and make a note of the type and status assigned to that specific item
2. Go to the artifact's Type page from the Product Template administration menu (you must be a template admin to do this)
3. Check to see which workflow is linked to the type assigned to the specific item (in #1 above)
4. Go to the artifact's Workflows page from the Product Template administration menu
5. Click on the workflow noted in #3 above
6. Click on the step (status) that matches the status assigned to the specific item (in #1 above)


## Can I change which workflow step is the default {: .section-break}
You can change the default workflow step for artifacts that let you edit their statuses.

On the relevant product template administration status page for an artifact (if present) one of the options is to pick a single default status. Changing the status will change the default status for every workflow of that artifact for that product template.

Artifacts that support editing of statuses, and picking a default workflow step are:

- Documents
- Incidents
- Risks

Other artifacts do **not** support editing of their statuses (Test Cases, Test Sets, Requirements, Releases, and Tasks)