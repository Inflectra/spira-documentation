# GitLab SpiraApp

This SpiraApp lets you integrate SpiraPlan and GitLab so users can launch pipelines from Spira and see their results in Spira as builds.

!!! info "About this SpiraApp"
    - [x] system settings
    - [x] product settings 
    - [x] product template setup required
    - [x] toolbar button on release details page
    - [x] additional integration required to record results in Spira
    - [x] configuration in GitLab (for recording results in Spira)

## Setup
This SpiraApp has two independent parts (you do not need one for the other to work):

- a button on the release details page so users can manually kick off a new GitLab Pipeline 
- backend integration (using webhooks) so the results of all relevant Pipelines are recorded in Spira as new builds

To record builds in SpiraPlan, you must [setup the webhook integration with GitLab](../../Build-Server-Integration/GitLab-Pipelines/). 

To configure this SpiraApp that lets users manually kick off a new Pipeline, you must additionally do the following:

### System settings
- [x] Enter the [GitLab username](https://docs.gitlab.com/ee/user/profile/#change-your-username)
- [x] Enter the [Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-tokens) - make sure the PAT has read and write API permissions

![system settings page](img/gitlab-system-settings.png)

### Product Settings
- [x] Enter the name of the GitLab project

![product settings page](img/gitlab-product-settings.png)

### Product Template Setup
- [x] Add a plain text custom property called "gitlab-branch-name" for Releases in the product's template. Note: you may already have a custom property for this already if you setup the webhook integration - if you have, do not create a second one.

## Using the SpiraApp
To use the SpiraApp to start a new GitLab Pipeline go to a release in that product. 

You must make sure the custom property "gitlab-branch-name" has the exact name of the branch in the relevant repo (for instance "develop") that you are building the release/sprint against. Note: this field is used by both the GitLab SpiraApp and the GitLab webhook integration.

Once the release has the branch name filled in, at any time you can click on the GitLab button in the top toolbar. This opens the dropdown. Click "Run Pipeline" to start the pipeline on GitLab. You will see an info message telling you the Pipeline has started. 

![release details page](img/gitlab-release-details.png)

Because a pipeline can take a while to run, do not expect to automatically see the build as soon as the info popup goes away. It may take a few minutes or more for the build to be recorded (if this part of the integration has been configured).