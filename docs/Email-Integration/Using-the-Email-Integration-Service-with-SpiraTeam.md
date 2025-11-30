# Using the Email Integration Service
!!! abstract "Compatible with SpiraTest, SpiraTeam, SpiraPlan"

Once you have the email integration service configured, we recommend that you initially clear the Windows Application Log on the machine. This will allow you to quickly see any errors that occur due to misconfiguration. The event viewer can be found in Control Panel > Administrative Tools > Event Viewer.

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


## Important Notes:
- ***IMPORTANT:*** If upgrading from v1 or v2 to v3 - the latest - you will need to edit the configuration for any Spira applications and change the password to the account's API key. Until this is done, email will not be imported.
- An email will be imported into a comment if the Subject line contains an artifact token (`[XX:####]`), only for artifact types Requirements, Test Cases, Incidents, Releases, Tasks, and Test Sets. All other artifact tokens will be ignored, and the email will be imported as a new incident.
- If a user does not have access to create an incident in the specified or default Product, then the email will not be imported. As long as the email remains in the inbox, it will get processed as soon as the user has permission for the given Product.
