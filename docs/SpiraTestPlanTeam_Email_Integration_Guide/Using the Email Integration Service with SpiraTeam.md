# Using the Email Integration Service with SpiraTeam

Once you have the email integration service configured, we recommend
that you initially clear the Windows Application Log on the machine.
This will allow you to quickly see any errors that occur due to
misconfiguration. The event viewer can be found in Control Panel \>
Administrative Tools \> Event Viewer.

Once you have the email integration enabled and running, any users that
email in a support ticket to one of the "watched" email addresses will
experience the following process:

1.  The user emails <incident.logger@mycompany.com> with an incident to
create.

2.  The contents (including attachments) of the email will be parsed by
the email integration service.

-   The application will look for tokens to decide if it should be
inserted in the default project or another user-specified
project.

-   The sender's email address will be queried to make sure that the
user has access to create incident in the selected project. (If
not, the system will then check the user's permissions for the
default project.)

-   If the user has permission, the new incident is created.

3.  The user will receive an automated email from the system letting
them know that the incident was created:

> SpiraTeam
> Incident "Need New Security Settings updated in
> Documentation" in project \"Project1\" has been changed.
>
> Please log into SpiraTeam to view this Incident\'s details.

<https://localhost/spirateam/6/Incident/2196.aspx>

4.  The user will not be subscribed to the ticket unless the user falls
under normal Workflow Notification or Event Notification settings.

5.  Any time the user gets a notification email from the server, they
can reply to the email -- leaving the token in the subject line
unaltered -- and their reply will be put into the ticket as a new
comment. It's important that -- if enabled in the SpiraTeam
application -- the separator line is not altered, and the reply is
kept above the line. Any test under that line will not be imported.
(If the separator line is altered, or the option is disabled in the
SpiraTeam administration, then the entire email, including quotes
and reply text, will be inserted.)

