# System


## General Settings

The general settings page allows you to configure SpiraPlan® to better match your environment and setup. In the current version, you can specify the default language, or configure the folder used to store document attachments:

![](img/System_57.png)

The available settings include:

- **Default Culture**: SpiraPlan can display information in a variety of different languages (assuming that the appropriate language packs have been installed) and number formats. By default, SpiraPlan will use the regional settings (language and number formats) of the operating system it has been installed on. However, you can override this default by choosing the appropriate culture from the list of options displayed in the drop-down list. *Note: The list of culture options does not reflect the available language packs, so in some cases, the setting will only change the number formats.*
- **Default Timezone**: SpiraPlan stores all dates and times internally in Universal Coordinated Time (UTC) and can therefore display dates/times adjusted for different timezones. By default, SpiraPlan will display dates in the timezone specified in the operating system it has been installed on. However, you can override this default by choosing the appropriate display timezone from the list of options displayed in the drop-down list.
- **Web Server URL**: This is the URL that your users use to access the system. Do not put the /Login.aspx or any other page here, as this URL is used to generate links to pages in the application.
- **Attachments Folder**: By default when SpiraPlan® is installed, the document attachments uploaded in the system get stored inside
    the `C:\Program Files\SpiraPlan\Attachments` folder located inside the main SpiraPlan® installation root. However you may want to have the documents stored on a remotely mounted drive or on a different hard disk partition. In which case you can simply change the folder pointed to in the text-box illustrated above and then click \[Update\] to commit the change.
- **Cache Folder**: By default when SpiraPlan needs to store temporary data (generated reports, the version control cache, etc.) it will store them in the C:\\ProgramData\\Inflectra\\Spira folder. Sometimes this folder is not appropriate (e.g. you want them on a different drive that has more space). You can enter in a different folder for temporary storage and SpiraPlan will use that instead.
- **Cache Refresh**: you can adjust the default number of minutes after which the source code cache should be refreshed.
- **Login Notice**: this can be used system wide to set a message to permanently display at the bottom of the login screen for all users (for example, a company disclaimer).
- **Administration Message**: this can be used by the administrator to display a temporary notice displayed on the login screen for all users. For example it could be used to remind all users that the server will be down for upgrading over the weekend. The administrator should delete the message once it is no longer needed.
- **Instant Messenger**: SpiraPlan and SpiraTeam come with a built-in instant messenger that allows users to communicate with each other in real-time. This can result in higher levels of network traffic and some system administrators may wish to disable this feature. This option lets you disable the integrated instant messenger. In addition, you can specify how long (in days) instant messages are retained in the system.
- **Event Log Retention**: As described in  [Event Log](#event-log), SpiraPlan comes with a built-in diagnostic event log. By default the system will only retain the last 30-days of events to avoid wasting storage space. You can adjust the retention period in this section to match your organization's policies.
- **Enable Free Text Indexes**: This tells SpiraPlan to use SQL Server Free Text Indexing to speed up keyword searches in the Global Search box. You should only have this set to "Yes" if you have the Free Text Indexing featured enabled in SQL Server, otherwise you will cause SpiraPlan to display error messages when users try and use the global search.
- **Disable Rollup Calculations**: (default = no) Setting this to Yes will prevent the system from calculating 'rollup' metrics when data is entered for any product in the system. This should not be done unless you have been told by the Inflectra Support team to do so. To disable rollup calculations for a specific product instead use the product admin level [equivalent setting](Product-Planning.md/#testing-settings). 
- **Enable Beta Features**: (default = yes) Enabling this will allow all users to preview any currently live beta features in the product. If you wish to try out the latest features please enable this setting. Any administration changes that are part of the current betas will be marked as such on the administration menu.
- **Enable Developer Mode**: (default = no) Enabling this will allow system administrators to update locally developed SpiraApps from the SpiraApps admin page. This should only be turned on for internal development purposes.
- **Enable Timesheet Approvals**: (default = no) Enabling this will allow users to submit timesheets for Timesheet Managers who can approve or reject them. <span class="pill">SpiraPlan</span>
- **Inflectra.ai**: (default = no) Enabling this will allow users to access Inflectra.ai to supercharge their productivity with purpose-built AI tooling (access to the service may require additional settings to be enabled - for example at the product level). This is only available for cloud instances. <span class="pill" title="Inflectra.ai settings are only available in the cloud, after purchasing the add-on">Inflectra.ai</span>


## File Type Icons

The "File Types List" administration page allows you to view all the different filetypes that are recognized by SpiraPlan and add or edit the associated icon, name, description and MIME type:

![](img/System_59.png)

If you click on the "Edit" button next to a filetype, or click on the "Add" button at the bottom of the screen, the system will display the page that lets you add or edit a filetype entry:

![](img/System_60.png)

On this page you can enter/edit the file extension that's used to recognize the type of file uploaded, the description of the file type (displayed in popup tooltips), the MIME type (used to determine how the browser handles the file type) and the path to the icon image. Once you are satisfied with the values, you can click on the "Save" button to confirm the changes.


## License Details
!!! info 
    This page is accessible under the System subsection of the sytem admin menu. It is only visible if you have Spira installed on premise.

    ![license details admin menu](img/System_LicenseDetailsMenu.png)

The license details page displays the information about the installed license for the particular instance of SpiraPlan® being used. This will display less information for hosted customers. The information displayed for self-hosted customers includes: the product name (e.g. SpiraPlan), the license version (e.g. v6.0.0.0), type of license in effect (x-user fixed, x-user concurrent, demonstration, enterprise, etc.), the expiration date (if any) of the license, the organization that the license belongs to, and the number of users concurrently logged-in right now. This last piece of information is useful as it helps administrators track down how many licenses are currently in use.

A sample page is illustrated below:

![](img/System_61.png)

To change the license key used by the system (for example, if to upgrade from Trial edition to Standard edition), you do **not**
need to reinstall SpiraPlan®. All you need to do is change the
**organization** and **license key** text-boxes to match the license key and organization name found in the customer area of our website (<http://www.inflectra.com/CustomerArea>) and click the "Save" button.

If there is an issue with the license key (e.g. a trial version that is passed its expiration date, or where the license key doesn't match the organization name) an error will be displayed describing the specific issue with the information you entered. If you are unable to get the system to work with the license key information, please contact Inflectra<sup>®</sup> customer support at: <support@inflectra.com>.


## LDAP Configuration

As described previously, you can configure SpiraPlan® to use an external LDAP server for importing new user profiles into the system, and for authenticating users -- instead of having to store separate passwords inside SpiraPlan®. However, you need to first configure the LDAP server settings. To do this, click on the "LDAP Configuration" link the Administration navigation:

![](img/System_62.png)

You need to fill out the various configuration settings for your LDAP server, each of which is explained in more detail below:

- **LDAP Host**: This should contain the name of the LDAP server that you want SpiraPlan to connect to together with the port number if it's not the default of 389.
- **Use Secure Sockets Layer (SSL)**: You should select this check-box if your LDAP server requires use of the LDAPS secure protocol. Leave unchecked for unencrypted LDAP communication.
- **Base DN**: This should be the distinguished name of the object inside your LDAP server that contains the list of user accounts. This varies by the type of LDAP server, please consult your LDAP server documentation for more details.
- **Bind DN**: This should be the distinguished name of the user inside your LDAP server that will be used to authenticate against when importing users. If not provided, SpiraPlan® will try and authenticate with the LDAP server anonymously.
- **Bind Password**: The is the password of the user specified in the Bind DN field above.
- **Login Attribute**: When SpiraPlan® imports users from the LDAP server it needs to know the user attribute inside the LDAP server that it should use to generate the SpiraPlan® user-name. For most LDAP servers the appropriate attribute would be "uid". However for Windows ActiveDirectory, the attribute "sAMAccountName" should be used instead.
- **First Name Attribute**: Providing this optional attribute will allow SpiraPlan® to automatically populate the first name field of the imported user instead of simply using the username as a placeholder.
- **Last Name Attribute**: Providing this optional attribute will allow SpiraPlan® to automatically populate the last name field of the imported user instead of simply using the username as a placeholder.
- **Middle Initial Attribute**: Providing this optional attribute will allow SpiraPlan® to automatically populate the middle initial field of the imported user instead of simply leaving it blank.
- **Email Address Attribute**: Providing this optional attribute will allow SpiraPlan® to automatically populate the email address field of the imported user instead of simply using the username@spiratest.com as a placeholder.
- **Sample User**: You can optionally enter a sample user and password to test that the user is correctly authenticated against the server. You can update the LDAP configuration without setting this, but if you do provide a sample user/password, it will not save the configuration unless the authentication succeeds. If you choose to enter it, the user's name should be the fully-distinguished name of the user (e.g. CN=Sample User, CN=Users, OU=Headquarters, DC=MyCompany, DC=Com).


## Security Settings

The "Security Settings" administration page lets you specify the various security settings within SpiraPlan to match your organization's policies and processes:

![](img/System_63.png)

![](img/System_64.png)

The following settings can be changed within the system, once you are satisfied, click the "Save" button to commit the changes:

- **Allow User Registration**: Set this to "Yes" if you want to allow users to self-register for SpiraPlan accounts (that you can subsequently approve). If you set this to "No", a system administrator will need to create all user accounts. Also set this to "No" if you plan on using LDAP-based authentication.
- **HTTPS Only**: Set this to Yes if the application will only be running on HTTPS. This enables tighter security that is only available on HTTPS.
- **Minimum Required Password Length**: Set this to the minimum length of passwords in the system. Choosing a longer password will make it harder for an unauthorized user to crack a password and gain entry into the system.
- **Minimum Required Special Characters** - Set this to the minimum number of non-alphanumeric characters that will be required for passwords in the system. Choosing more required special characters will make it harder for an unauthorized user to crack a password and gain entry into the system.
- **Maximum # Invalid Password Attempts**: Set this to the number of times a user can enter an incorrect password (during the time window specified in the setting below) before their account is temporarily locked out. This is important in preventing 'brute force' password hacking attempts.
- **Max Login Attempts Window**: Set this to the number of minutes over which invalid login attempts are evaluated before locking the user's account.
- **Account Lockout Period**: Set this to the duration (in minutes) to keep an account locked after too many invalid login attempts.
- **Password Change Interval**: If set to a value, it will require all password to be changed after the specified number of days.
- **Require Password Change on First Login**: Enabling this requires all new users to change their password on first login.
- **Disallow Names in Passwords**: If enabled, passwords cannot contain the user's real name and/or username.
- **Enable [2-Step](#enable-2-step-authentication) Authentication**: If enabled (the default), users can add a one-time password to their profile in addition to their primary password for added security. This feature is available to users who authenticate using the application's username and password system, or with LDAP. Users who authenticate with an external provider can not use SpiraPlan's 2-step authentication. Users can manage their one-time passwords on their [User Profile](../Spira-User-Manual/User-Product-Management.md/#2-step-authentication). Administrators can remove a one-time password for a user from [Edit User](System-Users.md/#edit-an-existing-user) page. 
{: #enable-2-step-authentication}

!!! hint "2-Step Authentication tips"   
    - Once enabled, users with a one-time password must enter it on each login to access the system.
    - If the global security setting is ever disabled, user with a one-time password will immediately not need to provide that password to login.
    - If installing on-premise, the web server must have the correct time. Any minor deviation from the correct time will mean users' one-time passwords will not be in sync with the server and they will not be able to login. 

- **[Enforce](#enforce-provider-login) Provider Login**: If enabled (default is disabled), users cannot connect an existing user to a Provider account, and cannot unlink an account for a Provider. Users must register new accounts using a Provider account 
{: #enforce-provider-login}

!!! hint "How does enforcing Provider login work?"
    This setting is useful for organizations who have at least one [login provider](System-Users.md/#login-providers) configured (where users can login with an SSO provider like Google or Microsoft). It limits the way that users can manage their account and that new users can register. We recommend it for organization looking to make sure all their users only login using a provider.
    
    With this setting enabled the following changes are made to the system:

    - the option to register a new account is removed from the login page
    - To create a Spira account, users must click the button for the relevant provider on the login page to add that provider account as a new SSO user in Spira
    - users who login with a provider can no longer go to their [My Profile](../Spira-User-Manual/User-Product-Management.md/#my-profile) and disconnect from that provider
    
    The following functionality is not affected by this change:

    - Users who already login with a username and password can continue to login as normal (note that the username and password fields remain visible on the login page but are de-emphasized)
    - LDAP users can continue to login as normal
    - System administrators can create new users with standard username and password credentials
    - System administrators can unlink an existing user from a provider

    Before enabling this setting, consider the following points:

    - Make sure you have at least one login provider configured, active, and working correctly
    - If you have existing users, check if any of them are logging in with LDAP or a standard username and password. If you want them to login with a provider, migrate them before enabling this setting (as they will not be able to do with the setting enabled)

- **Authentication Expiration**: This specifies the amount of time (in minutes - minimum of 2) after which a user will be logged out due to inactivity when they login without choosing the 'Keep Me Logged-In' option.
- **Keep Me Logged-In Expiration**: This specifies the amount of time (in minutes - minimum of 2) after which a user will be logged out due to inactivity if they have chosen to login with the 'Keep Me Logged-In' option. This should normally be longer than the previous setting.
- **Allowed Domains**: This should contain the list of other web domains that are allowed to make CORS (cross-origin) REST API calls to this instance. You can specify a comma separated list of base URLs (e.g. https://www.domain1.com, http://www.domain2.com) or an asterisk (\*) to denote all domains are allowed (not recommended).


## Event Log

The "System Event Log" administration page lets you view all of the errors, warning and other diagnostic messages that have been logged in the system:

![](img/System_70.png)

Each event entry is displayed along with the date-time it occurred, the type of event (error, warning, information, success audit, failure audit), category (application, source code provider, data-synchronization) and the short name. To view the full message, click on the "View Item" hyperlink:

![](img/System_71.png)

The popup dialog box will display the full error message log and stack trace in a moveable dialog box. This information should be provided to Inflectra customer support if you log a help desk ticket.


## Email Configuration

The Email Configuration page is split into two sections. The first section covers email notification details, and the second section configures how email from the application is sent.

![](img/System_73.png)

- **Email Notifications Active?**: Defaults to Yes. If changed to No, the system will not send out any emails, regardless of other settings. Note that this means that new user requests will not get sent either.
- **From Email Address:** This is the email address specified in the 'From:' field of email notifications sent from the application.
- **Reply-To Email Address:** This is the address specified in the 'ReplyTo:' field for notification emails sent from the application.
- **Send HTML Emails?**: Defaults to Yes. This option specifies whether HTML or Plain-Text emails are sent from the system.
- **Allow Users Control of Receiving Emails?**: Defaults to Yes. This specifies whether or not a user can modify their profile to not receive any emails from the system. If set to no, users' preference will be enabled and locked out.
- **Hide passwords in new user emails?**: Default to No. If enabled, the automated email sent to new users when an account is created by a system admin will not include the user's password.

![](img/System_74.png)

To use the internal IIS's default virtual SMTP server, leave all fields blank. The virtual server must then be configured to use proper SMTP server and network configuration. If you want the application to contact an SMTP server directly, use the following fields:

- **Host Name**: This is the SMTP server to connect to.
- **Port Number**: This is the port number to use, blank uses the default port 25.
- **SSL Connection**: Whether or not to use an SSL connection with the server. Be sure that the SMTP server's SSL certificate is trusted on the application server.
- **User Name**: When using an authentication method, this is the username to log in as.
- **Password**: When using an authentication method, this is the password to use.

Example settings for connecting to Gmail/Google Mail for sending notifications:

-   **Host Name:** smtp.gmail.com
-   **Port Number:** 587
-   **SSL Connection:** Yes
-   **User Name:** "account"@gmail.com
-   **Password:** "account password"

## SpiraApps
The SpiraApps page shows system administrators every SpiraApp currently installed, sorted alphabetically[^app-compatibility].

[^app-compatibility]: SpiraApps are shown even if they will not fully function in your application. For instance, the FMEA SpiraApp is not compatible with SpiraTest but will still show in the list if you are using SpiraTest. 

![SpiraApp list page view](img/System_SpiraApps_List.png)

For each SpiraApp in the list you see:

- Its icon and name
- The author organization (e.g. Inflectra Corporation)
- A short summary description of what the SpiraApp does
- The version number
- If the SpiraApp is active or not
- Available operations

    - Use the "power" icon to toggle if the SpiraApp is active or not
    - Use the "cog" icon to open the [settings page](#spiraapp-settings) for that SpiraApp
    - Use the "trash" icon (developer mode only) to fully delete the SpiraApp from the system

### Installing SpiraApps
Beneath the table of available SpiraApps, there is an upload area for installing new SpiraApps. To install a SpiraApp, take your `*.spab` bundle file and either drag it over the upload area, or click the upload area to locate the file. Then click "Install SpiraApp".

If developer mode is turned on, there will be an additional section at the bottom of the page. This allows you to upload any developer generated `.spirapp` package file. 

![SpiraApp dev mode section](img/System_SpiraApps_DevMode.png)

!!! info "Staying Safe With SpiraApps"
    During [development of a SpiraApp](../Developers/SpiraApps-Overview.md), developers write their code and then package it up into an `.spirapp` package file. These files can **only** by uploaded into Spira when developer mode is turned on. Anything you install in this way is at your own risk.

    Once a SpiraApp is ready to be released to customers, it goes through a detailed [submission process](../Developers/SpiraApps-Overview.md/#submission-process). Once Inflectra approves a SpiraApp, Inflectra packages and securely bundles the SpiraApp into a special "spab" filetype (it stands for **Sp**ir**a**App **B**undle). These files can be safely distributed over the internet, much like apps can be. 

    When you upload a SpiraApp (as an spab bundle), Spira performs a number of checks and validations against the file before it adds it to your system, to ensure it's origin. Spira does not need to have internet access to carry out these checks.

## SpiraApp Settings
The SpiraApp Settings page shows any system wide settings available for the particular SpiraApp. 

For more detailed information about each Inflectra created SpiraApp them refer to the [dedicated SpiraApp documentation](../SpiraApps/index.md). For third party SpiraApps, you will see a URL to get more information about that SpiraApp at the top of this settings page.

If the SpiraApp has no settings you can still access the page but there will be no settings to edit.

![SpiraApp list page view](img/System_SpiraApps_Settings_None.png)

If the SpiraApp has system level settings you will see:

- Some instructions about how edit the settings on the page (at the top of the page)
- One or more grouping of settings
- Within each group a list of available settings:

    - the setting name
    - a tooltip about how to fill in the setting by hovering over the setting name
    - the field to edit (when empty this may show some placeholder text).

![SpiraApp list page view](img/System_SpiraApps_Settings.png)

Click the "Save" button to commit any edits.


## System History Changes
This page displays a list of relevant changes made to system level artifacts or other relevant information.
 
![system history list page](img/system-history-list.png)

!!! info "What changes are tracked in system history?"
    - Capabilities
    - Product template custom properties
    - Product membership
    - Program Milestones
    - Product Roles
    - SpiraApps
    - User profiles
    - System admin General Settings

The system history list page shows system administrators all the currently recorded changes made at the system level. By default, items are shown in chronological order with the most recent at the top. The list can be filtered. Each history entry shows:

- **Change ID**: unique identifier. Clicking this will open the history details page for that change (see below)
- **Change date**: when the change was made
- **Change by**: who is recorded as having made the change (the user's name and ID)
- **Artifact Type**: the system level artifact (e.g. product)
- **Artifact ID**: the unique identifier of the artifact
- **Artifact Name**: the name field of the artifact
- **Change Type**: what sort of change was made:

    -   **Modified**: when one or more fields in the system artifact were changed.
    -   **Added**: when a new system artifact is created.
    -   **Deleted**: when the system artifact is deleted from the system.

- **Workspace**: the workspace type of that artifact (product, program, portfolio, or system)
- **Workspace ID**: the unique identifier of the workspace 


The system history details screen will show basic information as well as fields that were changed in this change set. 

![system history details page](img/system-history-details.png)

The top part of the page shows relevant **properties**: change date, changed by, change type, workspace, artifact type, artifact (name).

Below this, the **change actions** are shown. This shows one row for each field that was changed in this change set. It shows:

- **Field Category**: the type of field changed (for example, standard field or custom property)
- **Field Name**: the name of the field that was changed 
- **Old Value**: the value of the field before the change
- **New Value**:  the value the field was changed to
