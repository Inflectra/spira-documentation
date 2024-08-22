# Quick Tasks SpiraApp

!!! warning "This SpiraApp's functionality is not compatible with SpiraTest"

This SpiraApp lets users create, complete, and view tasks from a convenient Product Home Page widget. 

## Setup
To effectively implement Quick Tasks in your product, you have to set up the Task Type that will be used and make it use a specific workflow. 

### Product Template Setup
In the product template for each product that uses Quick Tasks, you need to:

1. Go to Tasks > Workflow and add a new Workflow called "Quick Task Workflow". Do not change anything else about this workflow.

2. Go to Tasks > Type and add a new Type called "Quick Task" (or other name of your choice) and select the Workflow you just created

3. Record the ID number of that Type to use for the product setting

![A row in the Task Type table containing the following: Type ID number, Type name, selected workflow, "No" (for pull request switcher), an empty radio button (for default type), "Yes" (for Active switcher). There is a red outlined box around the Type ID number and the selected workflow](img/quicktasks-task-type-setting.png)

!!! info "Reusing a Task Type"
    If your team already uses a special Task Type for miscellaneous to-do items, you can use that instead of creating a new one.

### Product Settings
For each product that uses Quick Tasks, you must fill in the Quick Tasks SpiraApp product setting: "Quick Task Type ID Number". Enter the ID number for the Task Type that you created in the Product Template. 

![SpiraApp product settings page with the Quick Task Type ID Number outlined by a red box](img/quicktasks-product-settings.png)

## Using the SpiraApp

!!! warning "Users must have Modify All Tasks permission in order to complete their owned tasks using this widget"
!!! warning "Users must have View permissions for Releases in order to use this widget"

### Using the Quick Tasks Widget

This widget serves as a group to-do list for all your users that can create tasks in your product. The widget shows the Name, End Date, and Owner of the most recent Quick Tasks, along with the Release if the task has one. You can also use the top row of the table to create a new Quick Task. This is automatically assigned to you, given the "In Progress" Status, and given the Type chosen in the product setting. 

If a release is selected using the Product Home Page release dropdown, only Quick Tasks for that release will be shown, and any newly created Quick Tasks will be added to that release.

Below the New Task row, the widget displays up to fifty incomplete Quick Tasks, sorted first by latest Creation Date and then alphabetically by Owner. The widget considers any Quick Tasks with a Status of "Not Started", "In Progress", "Blocked", or "Needs Review" as incomplete, and includes only those tasks in this section. You can click the empty checkbox to the left of an incomplete Quick Task to mark it as Completed.

Below the incomplete Quick Tasks, the widget also shows up to five Completed Quick Tasks, sorted by latest updated. You can click the filled checkbox to the left of a completed Quick Task to mark it as In Progress, which moves it back to the upper section.

![Product home page widget with four incomplete tasks and one completed task. Two different names across the five tasks are shown in the Owner column, and two of the incomplete tasks have a release in small text underneath the task name](img/quicktasks-widget.png)

Note that when a release is selected on the product home page, the end date for the task will always match the end date for the release, and cannot be changed by the user. When entering a date, make sure to use YYYY-MM-DD format or the date will be rejected. The exact datetime used for the end date for tasks is 11:59:59 PM in your timezone on the date that you enter. So if you enter "2025-01-01", the computed datetime will be "2025-01-01T11:59:59". The widget also rejects dates in the past, since the purpose of this widget is to help you plan out your next few tasks for the current day or week, not to keep track of work you have already done.
