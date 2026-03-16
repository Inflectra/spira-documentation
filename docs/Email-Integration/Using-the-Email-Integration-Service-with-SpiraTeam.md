# Using the Email Integration Service
!!! abstract "Compatible with SpiraTest, SpiraTeam, SpiraPlan"

This section explains how to use the Spira Email Integration Service (also known as the Email Importer) to process incoming and outgoing  emails.


!!! Info "Clearing the Event Log"
Once you have the email integration service initially configured, we recommend clearing the Windows Application Log on the host machine. This will allow you to quickly spot any errors that occur due to misconfiguration. The event viewer can be found in Control Panel > Administrative Tools > Event Viewer.

## Understanding Inbound vs. Outbound Email

In Spira, email functionality is split into two distinct systems that work together:

**Outbound Email (Spira Application)**: Handled directly within the Spira web application. This system sends out notifications when items are created, assigned, or updated. You configure this in Spira under System Administration > System > Email Configuration - [here are the details about this](../Spira-Administration-Guide/System.md/#email-configuration).
**Inbound Email (Email Integration Service)**: A separate background service that monitors a specific email inbox. It reads incoming emails and translates them into actions within Spira.

*Important*: For the inbound Email Integration Service to function correctly when users reply to notifications, specific settings must be configured in Spira's [Outbound Email Configuration](../Spira-Administration-Guide/System.md/#email-configuration) first.

## Prerequisites: Spira Email Configuration

Before users can successfully reply to system notifications (e.g. have their comments logged), you must ensure your  Spira settings for outbound settings are configured to route replies back to the Email Integration Service.

For that to configure the outbound email setting:
- Log in to Spira as a System Administrator 
- Navigate to System Administration > System > Email Configuration
- Ensure the following settings are applied:
    - **Reply-To E-mail Address**: This must be set to the exact email address that the Email Integration Service is monitoring (e.g., incident.logger@mycompany.com). If this is left blank or set to a "no-reply" address, user replies will never reach the inbound service.
    - **Send Email Importer Separator?**: This setting is off by default and must be enabled. 
    Why this matters: 
        - This option makes possible to replying to emails;
        - When enabled, Spira adds a specific separator line to the bottom of each email. The Email Importer uses this line to cut off the previous email chain, ensuring that only the new reply text is added as a comment.

## Feature 1: Adding Comments & Attachments via Email Reply

When a user receives a Spira email notification, they can reply directly to that email to add a comment to the item.
Supported Artifacts: Unlike creating new items, commenting via email is supported across multiple artifacts. This works for:
    - Requirements (RQ)
    - Test Cases (TC)
    - Incidents (IN)
    - Releases (RL)
    - Tasks (TK)
    - Test Sets (TX)
(Note: Any other artifact tokens will be ignored, and the service will attempt to create a new Incident instead).

**How it works**:

*Token Matching*: The service identifies the artifact using the token in the Subject Line of the email. It supports various formats, such as [TK:12], TK:12, [TK-12], TK-12, [TK 12], or TK 12.
*Important Constraint*: The artifact token must be in the Subject Line. Tokens placed only in the body of the email are ignored by the service.
*Attachments*: The contents of the email will be parsed, and any files attached to the user's email reply will be automatically uploaded to Spira and attached to the corresponding artifact.
Formatting: Users must type their reply above the email separator line so that only their new text is added as the comment.

## Feature 2: Creating New Incidents via Email

If a user emails the dedicated email account with a fresh email (one that is not a reply to an existing Spira-generated email, and lacks an artifact token in the subject line), the service will automatically create a new item in Spira.

Supported Artifacts:
Email creation is strictly limited to Incidents. You cannot create new Requirements, Tasks, Test Cases, or other artifacts via a fresh email.

**How it works**:
*Incident Details*: The email's Subject becomes the Incident Name, and the email Body becomes the Incident Description. Any attachments on the email will be added to the new Incident.
*Project Routing*: The new Incident will be created in the default Project specified in your Email Importer configuration settings for that email account. 
Note: Currently, any project tokens or project names included in the subject line or body of an email are being ignored.
*Permissions Check*: The sender's email address will be queried to make sure the user has access to create Incidents in the default project. If the user does not have appropriate permissions, the email will not be imported. It will remain in the inbox and get processed as soon as the user is granted permission for that Product.
*Notification*: If the user has permission and the Incident is created, they will receive an automated email from the system letting them know, which may look like this:

> SpiraTeam
    > Incident "Need New Security Settings updated in
    > Documentation" in project "Project1" has been changed.
    >
    > Please log into SpiraTeam to view this Incident's details.
    > 
    > <https://localhost/spirateam/6/Incident/2196.aspx>

**Note**: The user will not be automatically subscribed to the Incident moving forward unless they fall under normal Workflow Notification or Event Notification settings.

!!! attention "Important Notes":
- ***IMPORTANT:*** If upgrading from v1 or v2 to v3 - the latest - you will need to edit the configuration for any Spira applications and change the password to the account's API key. Until this is done, email will not be imported.
- An email will be imported into a comment if the Subject line contains an artifact token (`[XX:####]`), only for artifact types Requirements, Test Cases, Incidents, Releases, Tasks, and Test Sets. All other artifact tokens will be ignored, and the email will be imported as a new incident.
- If a user does not have access to create an incident in the specified or default Product, then the email will not be imported. As long as the email remains in the inbox, it will get processed as soon as the user has permission for the given Product.









Once you have the email integration enabled and running, any users that email in a support ticket to one of the "watched" email addresses will experience the following process:

- The user emails `incident.logger@mycompany.com` with an incident to create.
- The contents (including attachments) of the email will be parsed by the email integration service.

    * The application will look for tokens to decide if it should be inserted in the default project or added as a comment to an existing artifact.
    * The sender's email address will be queried to make sure that the user has access to create incident in the selected project. (If not, the system will then check the user's permissions for the default project.)
    * If the user has permission, the new incident is created.

- The user will receive an automated email from the system letting them know that the incident was created that may look like that below:

    > SpiraTeam
    > Incident "Need New Security Settings updated in
    > Documentation" in project "Project1" has been changed.
    >
    > Please log into SpiraTeam to view this Incident's details.
    > 
    > <https://localhost/spirateam/6/Incident/2196.aspx>

- The user will not be subscribed to the ticket unless the user falls under normal Workflow Notification or Event Notification settings
- Any time the user gets a notification email from the server, they can reply to the email -- leaving the token in the subject line unaltered -- and their reply will be put into the ticket as a new comment. It's important that -- if enabled in the SpiraTeam application -- the separator line is not altered, and the reply is kept above the line. Any text under that line will not be included in the new comment. (If the separator line is altered, or the option is disabled in the SpiraTeam administration, then the entire email including quotes and reply text will be inserted into the comment.)



