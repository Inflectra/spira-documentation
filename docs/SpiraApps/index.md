# SpiraApps Overview

!!! question "What are SpiraApps?"
    SpiraApps let you tailor SpiraTest, SpiraTeam, and SpiraPlan to your needs. Dedicated SpiraApps extend what is possible, each addressing a specific use case.

    One of the key attributes of the Spira platform is that it is a complete, integrated turnkey solution for companies that need to develop, test and manage their software applications. However there are specific features that are needed by different industries and methodologies that are better served by a more extensible set of ‘add-on’ features to the core system. For example, working in healthcare you have to comply with 21 CFR Part 11, whereas in automotive you need to support ISO 26262. SpiraApps allow Inflectra and its customers and partners to easily, safely, and seamlessly provide niche features for different industries and needs.

    Currently, Inflectra Corporation creates and manages all available SpiraApps, and they are distributed through installing or upgrading SpiraPlan itself.

Inside Spira, administrators can browse the list of available SpiraApps. From here they can activate, configure, and then enable for relevant products. SpiraApps functionality is limited to each product they are enabled for - in other words, they do not work in programs, portfolios, or system wide.

!!! example "For Developers"
    Developers can make their own SpiraApps and have them published and distributed by Inflectra. See our [developer overview](../Developers/SpiraApps-Overview.md) for more information.

## Getting Started with a SpiraApp
Here is a quick overview of how to start using a SpiraApp (we recommend also reading the documentation for the SpiraApp too):

1. Activate the [SpiraApp system wide](../Spira-Administration-Guide/System.md/#spiraapps)
2. Edit any [system level settings](../Spira-Administration-Guide/System.md/#spiraapp-settings) required
3. Enable the [SpiraApp for a particular product](../Spira-Administration-Guide/Product-General-Settings.md/#spiraapps)
4. Edit any [product level settings](../Spira-Administration-Guide/Product-General-Settings.md/#spiraapp-settings)
5. Start using the SpiraApp

## Finding SpiraApps
System admins can see which SpiraApps are currently installed on the by going to the System Administration > System > [SpiraApps](../Spira-Administration-Guide/System.md/#spiraapps) page.

Meanwhile, product admins can see which SpiraApps are available to use in their product(s) by going to the Product Administration > General Settings > [SpiraApps](../Spira-Administration-Guide/Product-General-Settings.md/#spiraapps) page. Only SpiraApps that a system has activated at the system level are available for use in products.

## Setting up a SpiraApp
Some SpiraApps have [system-wide settings](../Spira-Administration-Guide/System.md/#spiraapp-settings) that need to configured for the SpiraApp to work properly. For instance, if a SpiraApp integrates with a third party service, you may need to store login credentials (securely) in the SpiraApp's system settings.

Many SpiraApps have [product-specific settings](../Spira-Administration-Guide/Product-General-Settings.md/#spiraapp-settings). For the SpiraApp to function correctly, you will need to fill in these settings. For example, if you want to use the SpiraApp to add default descriptions to all new tasks created on the task details page, you have to tell the SpiraApp what description to use.

Once system and product level settings have been configured, the SpiraApp will be ready to use. Depending on the SpiraApp, end users may need to prepare specific artifacts to work with the SpiraApp. They will do this by editing artifacts and their fields in exactly the same way as normal. For example, if a SpiraApp lets you integrate a third party CI/CD tool, you will use releases to start a build on that service: each release may link to a different build job or pipeline in that service, and you have to add that information to dedicated custom fields on the release.

## End User Experience
End users likely will not know they are using a SpiraApp at all. They will interact with the SpiraApp functionality in the same way as any other part of the system.

## What can SpiraApps do
SpiraApps can work in the following places:

- Buttons with dropdown menu items in the toolbars on artifact list and details pages. These are shown to the right of the built-in toolbar buttons
- In a dedicated column on a list of artifacts
- Widgets on the product home pages and reporting home page
- They can even work on artifact details pages behind-the-scenes (automatically based on what a user does)

SpiraApps can do a range of different types of things:

- Provide dynamic links to users
- Show users popups with information and/or choices to make
- Communicate securely with external services (like CI/CD or load testing tools) to, for instance, trigger a new build or test to run
- Respond to events while looking at an artifact, such as saving or creating a new artifact, to update pre-configured fields. This can be used to update a custom field based on a calculation every time an artifact is saved

Some SpiraApps may use only one of the features, others may use multiple. Some may be available in a single part of the application, others across multiple places and pages.

## Available SpiraApps
You can learn more about each of the currently available SpiraApps by accessing the other pages in this section of the documentation (see the menu on the left).