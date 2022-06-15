# Release Notes for Spira v7

## Version 7.0 (July 2022)

!!! info "Summary"

??? success "New Features"
    - The global navigation helps users understand what key features are available in the tool but not currently accessible to them [RQ:4154]
    * ** Webhooks (inbound)**

        - Integrate with [GitHub Actions](../../Build-Server-Integration/GitHub-Actions/) so they can be saved against a release as a new build [RQ:4198]
        - Integrate with [GitLab Pipelines](../../Build-Server-Integration/GitLab-Pipelines/) so they can be saved against a release as a new build [RQ:4197]
        - Integrate with [CircleCI Pipelines](../../Build-Server-Integration/CircleCI-Pipelines/) so they can be saved against a release as a new build [RQ:4196]

??? bug "Bug fixes and enhancements"

    * **Navigation**

        - Improve the [global search](../../Spira-User-Manual/User-Product-Management/#global-search) by including not just recent searches, but also a list of recently viewed artifacts [IN:6922]
        - Let users filter the [global navigation](../../Spira-User-Manual/User-Product-Management/#global-navigation) workspace dropdown to make it easier to find the workspace a user [IN:6921]
        - Show artifact icons in the headings of the template administration menu subsections to make them more visually clear [IN:7046]

    * **Reporting**

        - Fix not being able to generate the [Release Summary report](../../Spira-User-Manual/Reports-Center/#release-summary-report) in PDF format [IN:5278]
        - Let users add specific [custom graphs](../../Spira-User-Manual/Reports-Center/#custom-graphs) to their reporting page and show the name of that custom graph in the widget header [IN:4787]
        - Make the "associated task" tables in the the [Requirement Detailed Report](../../Spira-User-Manual/Reports-Center/#requirements-detailed-report) more legible by removing non essential columns [IN:7132]
        - Show the custom graph description when you hover on the help icon of a custom graph on the reporting page [IN:4700]

    * **Other**

        - Fix the "Set Sample Data" popup from continuously popping up if you open the application for the first time only after it has been installed and then upgraded [IN:7123]
        - Fix the app pool and database not being deleted on uninstall after an upgrade operation (app directory is deleted) [IN:7031]
        - Fix the association type "prerequisite-for" not showing correctly for artifacts associated to an artifact that "depends-on" it (introduced in 6.15.1) [IN:7159]
        - Fix the product home page failing with a system error with certain configurations of widgets and permissions [IN:7107]
        - Fix updating a release via the API not recording history for the changes [IN:7131]
        - Fix users and system admins not being able to turn off RSS Feeds (on user profile or system admin pages respectively) [IN:7098]
        - Fix users not being able to see or set the "displaying" release dropdown on the product home page, if the Product Overview widget is not shown (introduced in 6.15.1) [IN:7138]
        - Hide the attachment tab on artifact details pages if the user does not have document view permissions [IN:4779]
        - Make code blocks inside the rich text editor more legible when in dark mode [IN:7140]

