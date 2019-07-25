# Product: Planning

## Edit Components

SpiraPlan lets you define a list of Components for each product. These
components represent the main functional areas of the system and
artifacts can be associated with each of the defined components.

![](img/Product_Planning_109.png)




This page lets you display the list of components based on three
predefined filters:

-   **All Active** -- This displays only the components that are listed
as Active = Yes. Only active components will be displayed inside the
main application.

-   **All But Deleted** -- This displays all the components (active and
inactive) except those that have been deleted.

-   **All** -- This displays all the components (active, inactive, and
deleted).

From this page you can click on the 'Add Component' option to add a new
component in the list:

![](img/Product_Planning_110.png)




After entering the name of the new component and choosing its Active
status, click on 'Save' to commit the new item. To edit an existing
component, edit its name and Active status and click 'Save'. To delete a
component, click the 'Delete' option next to its name. Once deleted, an
item can be undeleted by changing the display to 'All' and then clicking
'Undelete'.

## Planning Options

The Planning Options page lets you configure the schedule and calendar
options for the various product estimation and planning modules. The
settings are specific to each product:

![](img/Product_Planning_111.png)




This page allows you to make changes to the following settings:

**General**

**Work Hours Per Day** -- this setting allow you to specify how many
work hours should be used when converting an effort calculation from
hours to calendar days. For example a 12 hour task will occupy two days
if you set the working hours per day to 6 hours, whereas the same task
will occupy 1 ½ days only if you set the working hours per day to 8
hours.

**Work Days Per Week** -- this setting allows you to specify how many
days in the week are *typically* worked on the product. By default the
system assumes a 5-day (Mon-Fri) working week, but if your organization
works Saturdays (for example), you may want to switch to a 6-day working
week. If you want to use partial days, then just round up to the nearest
day and add non-working hours (see below) to compensate.

**Non-Working Hours Per Month** -- this setting allows to specify how
many non-working hours *typically* need to be accounted for. This is
useful if you want to have a working week that contains a fractional
number of days or if you have recurring activities that need to be
removed from each month. *Note that if you have specific holidays,
vacation days that need to be accounted for, it is better to use the
Release/Iteration non-working time feature instead.*

**Effort Calculations** -- When calculating how much effort has been
scheduled in a release or iteration, the system will aggregate the
individual effort values (both estimated and actual) for all the task,
incident and test cases artifacts associated with the release/iteration.
This setting allows you to specify if you want only task, incident, or
test case effort values to be included in the release/iteration total.
This is useful if your product management methodology requires that
incident or test case effort values be excluded from the total.

**Requirements**

**Default Estimate** -- Normally when you create a new Requirement in
the system it will be given an empty initial estimate (in points).
However if many requirements are typically a standard size, then as a
time-saver, the system will let you specify a default estimate value
that will be used when a new requirement is created.

**Point Effort** -- When requirements are added to the Planning Board or
Iteration planning screen, they will have an initial effort (in hours)
that is used until tasks are added (see Auto-Create Tasks option). This
field contains the standard conversion factor used to convert points
into hours based on the current team velocity (how much time it takes on
average to accomplish one story point). As the product progresses, the
team velocity will change, so you can click on the \[Suggest\] button to
have the system calculate how many hours each existing story point has
taken to implement in the product and provide that as a recommendation:

![](img/Product_Planning_112.png)




**Auto-Create Tasks** -- When you change the status of a Requirement in
the system to "In-Progress" the system will automatically add a default
Task to that requirement if no tasks already exist. This is a useful
shortcut that makes planning with requirements easier in the case when
the requirements are of a size where they don't need to be formally
decomposed into multiple developer tasks. However if you don't want the
system to automatically create tasks in, you can deselect the option for
the current product and it will turn off the feature.

**Auto-Planned** -- When this option is enabled, if you assign a
release/iteration to a requirement, and the requirement is not already
in the 'Planned' status, the system will automatically switch the status
of the requirement to 'Planned'.

**Use Task Status** -- When this option is enabled, if you add any tasks
to a requirement, the status of the requirement will be automatically
governed by the aggregate status of the associated tasks.

**Use Test Status** - When this option is enabled, if you associate any
test cases to a requirement, the status of the requirement will be
automatically switched from 'Developed' to 'Tested' when all the
associated test cases are passed.

**Task & Incidents**

**Default Effort** -- Normally when you create a new Task in the system
it will be given an empty initial estimated effort. However if many
tasks are typically a standard size, then as a time-saver, the system
will let you specify a default estimated effort that will be used when a
new task is created.

**Time Tracking** -- SpiraPlan® has an integrated time tracking system
that allows the easy entry of the hours spent on all assigned incidents
and tasks in one place (see the *SpiraPlan User Manual* for more details
on this feature). This setting allows administrators to specify if they
want the integrated time tracking features enabled for both incidents or
tasks (or neither).

