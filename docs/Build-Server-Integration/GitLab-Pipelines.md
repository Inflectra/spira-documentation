# GitLab Pipelines

## Introduction
SpiraTest, SpiraTeam, and SpiraPlan (from here on called SpiraPlan) integrated seamlessly with GitLab in a number of ways. In this section we discuss SpiraPlan's GitLab Pipelines reporting integration.

You can easily configure your GitLab Pipelines to report against a release and create a new build in SpiraPlan each time they run. This let's you see the health of your CI/CD process within SpiraPlan. 

!!! check "GitLab SpiraApp"
    You can also let end users start GitLab Pipelines from within SpiraPlan itself. To do so you will need to [enable and configure the GitLab SpiraApp](../SpiraApps/GitLab.md)

The integration has two parts, which are discussed below:

1. Setting things up in SpiraPlan (in the product and in its template)
2. Configuring GitLab (by adding a custom webhook to your repo)

!!! tip "Summary"

    1. Create a release custom property (plain text) called "gitlab-branch-name" in SpiraPlan
    2. Link a release to your CI/CD code branch by entering the branch name into the custom property on the release page in SpiraPlan
    3. Add the product token (e.g. "[PR:123]") into the project description of the GitLab repo
    4. In GitLab, create a webhook with a url in the form: `{{base url}}/Services/Webhooks/BuildService.svc/GitLab?username={{username}}&api-key={{api key}}`
    5. Make sure the user in the webhook has access to the product and can create releases in that product


## Setting up the integration in Spiraplan

The integration with GitLab Pipelines works by having a dedicated custom field for GitLab. This lets you link a release or sprint to a specific branch in a GitLab repo. In SpiraPlan we need to specify the branch name only. Then from GitLab we configure our specific repo to talk to the correct SpiraPlan product.

The first step in SpiraPlan is to **create a release custom property**:

- As a product template administrator open the template admin menu for the relevant product(s). These are products that you want to integrate with GitLab
- Go to the Releases Custom Properties page
- Add a new custom property called "gitlab-branch-name" that is of type Text (not rich text)

![Custom property definition popup](img/gitlab-pipelines-custom-property-definition.png)

Next, in your SpiraPlan product:

- Find the release you want to connect to GitLab
- Set the "gitlab-branch-name" to the exact name of the branch in the relevant GitLab repo (for instance "develop")
- Save the release

![Release list page with custom property filled in](img/gitlab-pipelines-release-page.png)


## Setting up the integration in GitLab

In GitLab we now need to setup our repo to talk to the correct SpiraPlan product. Your GitLab repo/project will need to use Pipelines for the integration to work. You can add or edit Actions at any time - this will not impact the integration.

First, we have to add information to link up the GitLab repo and SpiraPlan, by adding the SpiraPlan product reference into the repo. To do this:

- Go to your GitLab repo
- Go to the Settings > General page
- In the "Project description" box enter the SpiraPlan product token in the form of `[PR:{{product id}}]`. For example, "[PR:1]". You can have other text in the description, as long as the token is in there somewhere.
- Click "Save Changes"

![Project description with the product token](img/gitlab-pipelines-repo-description.png)

Second, you need to add a dedicated webhook. This means that when the GitLab Pipeline(s) completes, GitLab will send the results, along with the project description (and that SpiraPlan product token) to SpiraPlan via that webhook. SpiraPlan processes that data and adds it as a build.

- Go to the Settings > Webhooks page of the GitLab repo

![Project settings](img/gitlab-pipelines-repo-settings.png)

- Enter the URL (see below)
- The secret token is not used by SpiraPlan can be left blank
- For triggers, you must enable "Pipelines events"
- For SSL verification, make sure "Enable SSL verification" is checked (default)
- Click "Add webhook"

![Add webhook page](img/gitlab-pipelines-repo-webhook.png)

!!! example "The webhook URL"
    The webhook URL is made of different parts.

    - First get the base url of your instance - for instance `https://mysite.spiraservice.net`. This is the start of every URL you use when using SpiraPlan
    - Add the following to the end of that URL `/Services/Webhooks/BuildService.svc/GitLab`
    - Add your SpiraPlan user authentication to the end of this url. This needs a username and an [api-key](../HowTo-Guides/Users-profile-management.md/#how-to-get-or-make-your-rss-token-or-api-key). The user must be a member of the relevant product and be able to create releases. This part of the URL looks like `?username={{username}}&api-key={{api key}}`

    The final URL will look like this: `https://mysite.spiraservice.net/Services/Webhooks/BuildService.svc/GitLab?username=gitlab-pipelines&api-key={11111111-1111-1111-1111-111111111111}`


## Run the Action

When an Action on the GitLab project next runs (either from GitLab, or with the GitLab SpiraApp)it will report its results to SpiraPlan. SpiraPlan reads the product token to know what product the Action is for. SpiraPlan then looks the first release in that product that has the repo branch in the correct custom property that the GitLab Pipeline was run against.

SpiraPlan creates a build against that release, with the key information, including the build status.

![Build list on the release details page](img/gitlab-pipelines-build-list.png)

You can click on the build name/link to open its build details page. The build will also appear on any relevant widgets in SpiraPlan.