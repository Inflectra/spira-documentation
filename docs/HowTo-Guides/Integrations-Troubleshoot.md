# Successfully integrating with SpiraPlan

## How to setup the Jira syncing integration {: .section-break}
We have dedicated guides explaining this in detail for: [Jira Cloud](../../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud/) and [Jira Server](../../External-Bug-Tracking-Integration/Using-SpiraTeam-with-JIRA-5+/). Below is a very high level summary with further links

- First you need the datasync service. If you are using Jira Cloud and are hosted with us then the easiest way is to sign up for our cloud hosted data sync service. You can do this in your customer area at https://inflectra.com
- Next, you will need to setup the [datasync service](../../External-Bug-Tracking-Integration/Setting-up-Data-Synchronization/#spira-external-tool-cloud-hosted) 
- Then you will have to set up [everything in Spira](../../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud/) to make sure the right products are syncing in the right way to between Jira and Spira

## How to configure the cloud data sync service {: .section-break}
For cloud-hosted Spira instances you can use Inflectra's cloud data sync to simplify how you sync with third party providers like Jira. To configure a cloud data sync:

- go to your Customer Area on the Inflectra website, inflectra.com: 'Login' > Customer Area
- From there click on "My Cloud Subscriptions" > [Spira]
- Configure the username to use for the dataSync
    
    - we strongly recommend creating a dedicated user in Spira for this to aid troubleshooting
    - make sure this user has the role of "Product Owner" for all products that you want to sync with the third party service
