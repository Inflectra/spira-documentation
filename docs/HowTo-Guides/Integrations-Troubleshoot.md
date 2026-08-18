# Successfully integrating with SpiraPlan

## How to setup the Jira syncing integration {: .section-break}
We have dedicated guides explaining this in detail for: [Jira Cloud](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md) and [Jira Server](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-JIRA-5+.md). Below is a very high level summary with further links

- First you need the datasync service. If you are using Jira Cloud and are hosted with us then the easiest way is to sign up for our cloud hosted data sync service. You can do this in your customer area at https://inflectra.com
- Next, you will need to setup the [datasync service](../External-Bug-Tracking-Integration/Setting-up-Data-Synchronization.md/#setup-spira-datasync-in-the-cloud) 
- Then you will have to set up [everything in Spira](../External-Bug-Tracking-Integration/Using-SpiraTeam-with-Jira-Cloud.md) to make sure the right products are syncing in the right way to between Jira and Spira

## How to configure the cloud data sync service {: .section-break}
For cloud-hosted Spira instances you can use Inflectra's cloud data sync to simplify how you sync with third party providers like Jira. To configure a cloud data sync:

- go to your Customer Area on the Inflectra website, inflectra.com: 'Login' > Customer Area
- From there click on "My Cloud Subscriptions" > [Spira]
- Configure the username to use for the dataSync
    
    - we strongly recommend creating a dedicated user in Spira for this to aid troubleshooting
    - make sure this user has the role of "Product Owner" for all products that you want to sync with the third party service


## How to set up a second DataSync plugin of the same external service {: .section-break}

!!! warning "Avoid Syncing Multiple External Tools to the Same Spira Product for the Same Artifact"
     
     Do not configure multiple external projects (e.g., two different Jira projects coming from the same source URL) or multiple DataSync plugins to sync the same artifact type (such as Requirements, Incidents, or Tasks) into a single Spira product.

     While Spira allows multiple DataSync plugins and project mappings to be active globally, mapping multiple external projects to the same Spira product for the same artifact creates severe risks of data overwrites, mapping ID collisions, and infinite update loops.

     - **Default Best Practice:** Keep a strict 1:1 relationship between a Spira product and an external project (e.g., 1 Jira Project ↔ 1 Spira Product).

     - **Allowed Exception:** Multiple external projects or DataSync plugins may target the same Spira product **only if** they manage completely separate, non-overlapping artifact types (e.g., Jira Project A syncs Requirements while Jira Project B syncs Incidents).

### Advanced Considerations: Syncing Multiple External Systems

While Spira supports multiple active DataSync plugins at the system level, combining multiple integrations within a single Spira product requires extreme caution.

Depending on your system's specific needs and setup, you might require a separate dataSync plugin for each distinct instance of an external service (Jira, ADO, GitHub, YouTrack, or others supported application). This is necessary when your Spira instance needs to connect to multiple instances of the same external service located at different URLs.
For example, you might need to sync Spira product A with a Jira project on your company's Sandbox instance, while also syncing Spira product B with a Jira project on a different Jira instance, such as your Jira Production. In order to do this, you need to:

- Create two different DataSync plugins. Their "Name" fields should be defined according to their type (e.g., "JiraDataSync" for integration with Jira Cloud), and their "Caption" fields should be used to differentiate them (e.g., "Jira Sandbox" and "Jira Production")
- Make sure to enter the correct credentials (URL, Login, and API Key) for each plugin and complete the configuration as needed
- On the Data Synchronization page in Spira, for each plugin, select the product(s) you want to sync against and configure the mappings
- Finally, activate the Data Sync plugins

### Why Multi-Source Syncing for the Same Artifact is Discouraged

!!! danger "Avoid more than one dataSync plugin type activation for the same Spira product or external project"
   
      Having two dataSync plugins of the same type active for the same Spira product and/or external project without careful isolation will lead to duplicate data in one or both applications, depending on your configuration. To avoid this issue, it's recommended to use only one plugin for each combination of Spira product and external project.

When two external projects (e.g., two separate Jira projects from the same source URL, or a Jira project and an Azure DevOps project) are both configured to sync the same artifact type (e.g., Incidents) with the same Spira product, several technical conflicts arise:

1. **Mapping Table Ambiguity:** Spira tracks external sync state using the project key and  DataSync internal mapping tables (linking Spira Artifact IDs to External IDs per plugin/project). When multiple external projects sync the same artifact type into one Spira product, the sync engine cannot deterministically look up which external project owns an updated Spira item, corrupting the internal mapping relationship.
2. **Data Race Conditions:** If an item is updated in Tool A, synced to Spira, and then immediately picked up by Tool B's DataSync, Tool B may overwrite fields in Spira with outdated or mismatched metadata from Tool B.
3. **Echo/Loop Syncing:** Changes pushed from System A into Spira can trigger System B to register a "new change," creating an unintended synchronization loop across both external systems.

### Best Practices for Multi-Tool Architecture

If your organization uses multiple ALM tools (e.g., engineering uses Jira while business uses ADO):

- **Separate Spira Products:** Create dedicated Spira products for each external project integration, and use Spira's native product-to-product linking or enterprise reporting to aggregate data at the program level.

- **Isolate Artifact Types:** If you *must* target the same Spira product with multiple external project mappings, ensure that each project mapping handles mutually exclusive artifact types (e.g., Project A syncs Requirements only, Project B syncs Incidents only).

- **Disable Unneeded Sync Directions:** If one project or system is purely used for reading data, set that DataSync configuration to Import Only or Export Only to prevent bidirectional sync conflicts.


