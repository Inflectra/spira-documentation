# Timesheets
Spira's timesheets functionality lets users track how much time they have spent on incidents and tasks across all their products. They can record time against each artifact for a given day in the current week. This time data is used to update the effort recorded against each artifact. Users can also easily see timesheets from the past. <span class="pill">SpiraTeam</span> <span class="pill">SpiraPlan</span>

!!! tip "Locking down actual efforts" 
    If you want to ensure that effort values are only updated by timesheet entries, and not by editing the individual task or incident, you can update the workflows to make the Actual Effort field read only for every status.

!!! info "Timesheets will continue to evolve"
    Currently timesheets provide valuable features that let users track their time quickly and conveniently. We will be adding more features to timesheets in future releases to make this even more powerful, including with support for reporting, approval workflows, and more. 

## My Timesheet
You can access "My Timesheet" from the User Profile dropdown on the [Global Navigation](./User-Product-Management.md/#global-navigation) menu.

![My Timesheet in global navigation menu](img/my-timesheet-global-navigation.png)

When you first load the My Timesheet the page will have the following parts:

- **Navigation buttons**: these let you navigate backward or forward to see previously saved timesheets. Each button is disabled if there are no earlier/later timesheets to navigate to
- **Artifact dropdown**: this lists all the incidents and tasks you own across all active products you are a member of
- **Timesheet data range**: a heading showing the start and end date of the current timesheet. Click on it to bring up a datepicker. Selecting a date will navigate you to the timesheet for that relevant period. If there is no timesheet for that date then a new timesheet is automatically created.
- **Timesheet grid**: a table for viewing and recording timesheet entries for each day of the timesheet. Each time you load the page it will start by showing the current week's timesheet.

![My Timesheet page example](img/my-timesheet-page.png)

### Viewing
When viewing the timesheet for the current week, today will be highlighted to help you more easily add data for today.

### Adding
The timesheet grid will be empty at first. To add information to it, select an artifact from the artifact dropdown and click the "+" button. You will then see a row added for the artifact. 

To add a time entry to an artifact, click into the cell for the relevant artifact and day. Type the time in the format hh:mm (min 00:01, max 23:59).

You cannot add timesheet entries to an artifact that you do not have permission to modify. In this case you will see a warning message identifying which artifacts were not updated. The same is true if the artifact has been deleted.

If you add an artifact to the timesheet but do not enter any time for any day then the artifact is not saved to the timesheet.

### Editing 
To edit a newly entered or existing entry to an artifact on a timesheet, click into the relevant cell and adjust the time as needed. Setting the time to 0:00 will effectively delete the time in that cell (doing so for all cells for an artifact will delete the artifact from that timesheet). 

If there are unsaved time entries in the timesheet the save button will be enabled. Click Save to commit the changes. This will update the actual effort for each task or incident. If you add 1 hour to a task for 3 different days on the timesheet, then the actual effort for that task will be increased by 3 hours. 

### Deleting
To delete any row of a relevant timesheet, access the context menu (right click) on that row and choose delete. Deleting a row will remove the effort against that artifact and record a new history entry for that change. You can not delete a row for an artifact that has been deleted, or if you no longer have permissions to change the artifact's effort.

To delete an entire timesheet, click the trash can icon below the timesheet on the far right. Deleting a whole timesheet is equivalent to deleting each of its rows in turn (meaning that effort changes are made and history entries are created for each artifact row removed. The delete button will be disabled if there is any row on the timesheet that is disabled.

You can not delete a timesheet that has been submitted for approval (or that later has been approved).

### Downloading
To download a timesheet in CSV format, access the context menu (right click) on any row and choose to download the timesheet as a CSV file.

### My timesheet approvals
If [timesheet approvals](../Spira-Administration-Guide/System.md/#general-settings) is enabled for your organization, then any timesheet with at least one entry in it will show the timesheet's status above it. 

There are four available timesheet statuses:

- Draft: the default for any new timesheet
- Submitted: the timesheet has been submitted for approval by a timesheet manager. Timesheets in this status cannot be edited or deleted.
- Approved: the timesheet has been approved by a timesheet manager. Timesheets in this status cannot be edited or deleted.
- Rejected: the timesheet has been rejected by a timesheet manager. Timesheets in this status can be edited and even deleted, to allow you to make the changes required by the manager before you resubmit it.

![draft status button](./img/my-timesheet-draft-status.png)

Once you have fully completed a draft timesheet, you can submit it for approval. To do so click on the `Draft` button to the right of the artifact dropdown. You will see a confirmation message: "Do you wish to submit this timesheet for approval?" Click Yes to change the status to "Submitted".

![draft status button](./img/my-timesheet-submitted-status.png)

### Other features to note
- The timesheet is sorted by the artifact name in alphabetical order
- A single history record is recorded for each artifact modified in each save, even if multiple days are modified for a given artifact in a single save
- You can see totals for how much time you have recorded against each artifact, each day, and across the whole timesheet