# Template: Notifications

Each template has a separate notification system. This lets admins control what events trigger a notification being sent (via email), with what subject line, and who it should go to. You can create as many event triggers as you want, to give you fine grained control over when notifications are created. Each template has a single notification template (email body with tokens) per artifact. You can have, for example, 20 different requirement event triggers for a product template, each with their own rules and subjects; but they will all send the same email body, because they will all use the same requirement notification template.

To configure emails across the entire system see [Email Configuration](../System/#email-configuration).

## Notification Templates

Notification templates are used by notification events, and are defined for each supported artifact type[^supported-artifacts] in the template.

![](img/Template_Notifications_183.png)

To edit a template, click the Edit button. To send a test email notification to yourself using the current template, click the Test button.

Clicking the Edit button will take you to a page similar to the following. Depending on the artifact type you selected, the list of available fields will vary.

![](img/Template_Notifications_184.png)

On this screen you are presented with the same rich text editor available elsewhere in the application. Displayed in it is the current template (with template tags showing) for the artifact. Template tags start with a $ (dollar sign) and then a string name enclosed in {}
parentheses. When email notifications are sent, tokens will be replaced with specific information from the artifact that the notification is being sent for. Invalid tokens will be stripped from the template text. Clicking the link "(Display Email Template Field Tokens" to see a list of available tokens to insert into the textbox for easy selecting and editing.

![](img/Template_Notifications_185.png)

If HTML notifications are disabled, the template will be converted to plain text before sending.

When finished, click the update button to save your new template. The new template will take effect immediately.


## Notification Events

The Notification Events section is where template administrators can set up when and to whom notifications are sent out to users of the system. Clicking on the Notification Events link will present you with a list of all events defined for the current template:

![](img/Template_Notifications_186.png)

**Note:** These events can handle all changes to any of the artifacts except changes handled by Status changes to Incidents. Incident status changes are handled through the Workflow configuration.

When clicking on the Edit or Add buttons, you will be presented with the event details screen:

![](img/Template_Notifications_187.png)

The top section defines general configuration items for the event:

-   **Event Name:** used to name the event, only used for administrative purposes.
-   **Artifact Type:** The artifact type this event is attached to. Once an event is created, the artifact type cannot be changed.
-   **On Creation?** If set to yes, this event will fire when an artifact is created, as well as when any configured fields are changed.
-   **Active?** If set to yes, this event is active and will send notifications when configured fields are modified.
-   **Subject Line:** The subject line of the notification email.

The Artifact Fields will let you configure which fields will cause this notification to send an email notification:

![](img/Template_Notifications_188.png)

Selected fields are treated in an OR-based query, so that if you have two or more fields checked for an event, the event will send a notification if **either** of the two fields are changed. Depending on the artifact type configured above, the available fields will vary.

The last section is the configuration of whom to send the notifications to:

![](img/Template_Notifications_189.png)

If a user belongs to more than one group or they have manually signed up to receive notifications to any changes in the artifact, they will only receive one notification for the artifact change.

[^supported-artifacts]: Document, Incident, Release, Requirement, Risk, Task, Test Case, Test Set