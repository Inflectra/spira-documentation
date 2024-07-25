# Successfully integrating with SpiraPlan

## How to setup the Jira syncing integration {: .section-break}
We have dedicated guides explaining this in detail for: [Jira Cloud](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md) and [Jira Server](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-JIRA-5+.md). Below is a very high level summary with further links

- First you need the datasync service. If you are using Jira Cloud and are hosted with us then the easiest way is to sign up for our cloud hosted data sync service. You can do this in your customer area at https://inflectra.com
- Next, you will need to setup the [datasync service](../External-Bug-Tracking-Integration/Setting-up-Data-Synchronization.md/#spira-external-tool-cloud-hosted) 
- Then you will have to set up [everything in Spira](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md) to make sure the right products are syncing in the right way to between Jira and Spira

## How to configure the cloud data sync service {: .section-break}
For cloud-hosted Spira instances you can use Inflectra's cloud data sync to simplify how you sync with third party providers like Jira. To configure a cloud data sync:

- go to your Customer Area on the Inflectra website, inflectra.com: 'Login' > Customer Area
- From there click on "My Cloud Subscriptions" > [Spira]
- Configure the username to use for the dataSync
    
    - we strongly recommend creating a dedicated user in Spira for this to aid troubleshooting
    - make sure this user has the role of "Product Owner" for all products that you want to sync with the third party service


## How to set up a second DataSync plugin of the same external service {: .section-break}
Depending on your system's specific needs and setup, you might require a separate dataSync plugin for each distinct instance of an external service (Jira, GitHub, YouTrack, or others supported). This is necessary when your Spira instance needs to connect to multiple instances of the same external service located at different URLs.
For example, you might need to sync Spira product A with a Jira project on your company's Jira Sandbox instance, while also syncing Spira product B with a Jira project on a different Jira instance, such as your Jira Production. In order to do this, you need to:

- Create two different DataSync plugins. Their "Name" fields should be defined according to their type (e.g., "JiraDataSync"), and their "Caption" fields should be used to differentiate them (e.g., "Jira Sandbox" and "Jira Production")
- Make sure to enter the correct credentials (URL, Login, and API Key) for each plugin and complete the configuration as needed
- On the Data Synchronization page in Spira, for each plugin, select the product(s) you want to sync against and configure the mappings
- Finally, activate the Data Sync plugins

!!! danger "Never activate more than one dataSync plugin type for the same Spira product or external project"
    Having two dataSync plugins of the same type active for the same Spira product and/or external project will lead to duplicate data in one or both applications, depending on your configuration. To avoid this issue, it's recommended to use only one plugin for each combination of Spira product and external project.