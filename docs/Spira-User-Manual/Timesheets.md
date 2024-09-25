# Timesheets
Spira's timesheets functionality lets users track how much time they have spent on incidents and tasks across all their products. They can record time against each artifact for a given day in the current week. This time data is used to update the effort recorded against each artifact. Users can also easily see timesheets from the past. 

!!! tip "Locking down actual efforts" 
    If you want to ensure that effort values are only updated by timesheet entries, and not by editing the individual task or incident, you can update the workflows to make the Actual Effort field read only for every status.

!!! info "Timesheets will continue to evolve"
    Currently timesheets provide valuable features that let users track their time quickly and conveniently. We will be adding more features to timesheets in future releases to make this even more powerful, including with support for reporting, approval workflows, and more. 

## My Timesheet
You can access "My Timesheet" from the User Profile dropdown on the [Global Navigation](./User-Product-Management.md/#global-navigation) menu.

When you first load the My Timesheet the page will have the following parts:

- **Navigation buttons**: these let you navigate backward or forward to see previously saved timesheets. Each button is disabled if there are no earlier/later timesheets to navigate to
- **Artifact dropdown**: this lists all the incidents and tasks you own across all active products you are a member of
- **Timesheet data range**: a heading showing the start and end date of the current timesheet
- **Timesheet grid**: a table for viewing and recording timesheet entries for each day of the timesheet. Each time you load the page it will start by showing the current week's timesheet.

The timesheet grid will be empty at first. To add information to it, select an artifact from the artifact dropdown and click the "+" button. You will then see a row added for the artifact. 

To add a time entry to an artifact, click into the cell for the relevant artifact and day. Type the time in the format hh:mm (min 00:01, max 23:59).

If there are unsaved time entries in the timesheet the save button will be enabled. Click Save to commit the changes. This will update the actual effort for each task or incident. If you add 1 hour to a task for 3 different days on the timesheet, then the actual effort for that task will be increased by 3 hours. 

Other features to note when using the timesheet grid:

- The timesheet is sorted by the artifact name in alphabetical order
- You cannot add timesheet entries to an artifact that you do not have permission to modify. In this case you will see a warning message identifying which artifacts were not updated
- A single history record is recorded for each artifact modified in each save, even if multiple days are modified for a given artifact in a single save
- You are not able to edit previously saved entries (which are shown as grayed out)
- You can see totals for how much time you have recorded against each artifact, each day, and across the whole timesheet
- When viewing the timesheet for the current week, today will be highlighted to help you more easily add data for today
- If you add an artifact to the timesheet but do not enter any time for any day then the artifact is not saved to the timesheet