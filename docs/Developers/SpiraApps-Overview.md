# SpiraApps Overview for Developers
## Introduction
This page provides an overview of how SpiraApps work, what they can do, and how the development process works. This is in addition to [technical reference material](./SpiraApps-Reference.md) useful for developers and a more [guided tutorial](./SpiraApps-Tutorial.md). 

SpiraApps will often use Spira's REST API. We have extensive reference documentation for the API as part of each Spira install. Get started by following this [API tutorial](./API-Tutorial.md).

!!! info "What is a SpiraApp?"
    - [x] a small piece of client-side code 
    - [x] runs on a variety of pages in Spira (including most list and details pages, the My Page, product home page, and the product reporting page)
    - [x] can be configured at the system or product level by admins
    - [x] are portable and secure files that can be shared and installed into any new Spira application
    - [x] are stored in the Spira database to provide a secure and fast experience for users
    - [x] uses dedicated classes and helpers to listen to and interact with Spira securely and easily

SpiraApps let users make use of additional functionality seamlessly in Spira to do a [wide variety of useful actions](../SpiraApps/index.md).

## Technical overview
SpiraApps consist of two essential pieces:

- a manifest.yaml file that describes the SpiraApp, where it should appear and what it does
- code files, referenced in the manifest file, that provide the user experience required

The code files can be a mix of html, javascript, or CSS files, depending on what sort of SpiraApp you are building.

In order to test your code you need to install it into Spira. To do this you need to:

1. create a `.spiraapp` package from the manifest file and code, using our [helper node project](https://github.com/Inflectra/spiraapp-package-generator).
- turn on developer mode in Spira
- go to the SpiraApp page in system admin in Spira
- upload the `.spiraapp` package file

Here is a schematic of a SpiraApp and its process from development to release to customers

``` mermaid
flowchart LR
    subgraph Developer
    jscss(JS and CSS files) --> m(manifest.yaml)
    html(HTML files) --> m
    m --> p[[Package Generator]]
    p --> sp(SpiraApp package)
    end
    subgraph Inflectra
    im(manifest + other files)
    im --> ib(SpiraApp Bundles)
    end
    subgraph Customers
    end
    Developer --> Inflectra
    Inflectra --> Customers

```

## Creating a Manifest
The manifest is a yaml file that stores all information about the SpiraApp, including its name, references to code files, settings, and where the SpiraApp is used in the application.

The manifest can have up to 8 different sections. For each section, example yaml is provided below, with an explanation about each property provided as the values

### SpiraApp metadata
The metadata below provides essential information to identify and explain the SpiraApp. This section is the only mandatory section for the manifest. Note that all properties are at the root level.

=== "Explanation"
    - **guid**: Provide a new guid in the form of aaaaaaaa-bbbb-cccc-ddd-eeeeeeeeeeeee
    - **name**: CodeFriendlyAppName (no spaces or hyphens)
    - **caption**: User facing SpiraApp name
    - **summary**: Shown on the system admin SpiraApp list page
    - **description**: Shown on the system admin SpiraApp details page
    - **productSummary**: Shown on the product admin SpiraApp list page
    - **productDescription**: Shown on the product admin SpiraApp details page
    - **author**: Organization who owns the SpiraApp
    - **url**: Where should users go to get help, documentation, and support for this SpiraApp?
    - **icon**: Optionally provide a base 64 encoded SVG (be mindful of file size and keep it as small as possible)
    - **license**: The type of license the SpiraApp is under
    - **copyright**: Any copyright information
    - **version**: Version number in the form a decimal

=== "Example"

    ```yaml
    guid: 9cbb6a57-ffc1-4ff8-aef7-a740d6bd22b1
    name: myFirstSpiraApp
    caption: My first SpiraApp
    summary: A hello world example SpiraApp
    description: The aim of this SpiraApp is to show a basic hello world style proof of concept
    productSummary: A hello world example SpiraApp
    productDescription: The aim of this SpiraApp is to show a basic hello world style proof of concept
    author: My Company
    url: https://mycompany.com/help/spirapps/hello-world
    icon: data:image/svg+xml;base64,PD...
    license: MIT License
    copyright: Copyright My Company
    version: 0.2
    ```

### Settings groups
Setting groups help you visually organize any system level of product level administration settings. They are not required, but can be useful to improve the admin user experience. The settingGroups is an array of objects, each object must have a name and a caption.

=== "Explanation"
    - **name**: codeFriendlyUniqueName (no spaces or hyphens)
    - **caption**: User friendly name

=== "Example"

    ```yaml
    settingGroups:
      - name: groupAlpha
        caption: First Group
      - name: groupBravo
        caption: Second Group
    ```

### System admin settings
A SpiraApp can require system level settings to be configured and stored. These settings are useful for:

- storing credentials securely for making API calls to a third party service. The credentials are never exposed to the browser, but can be used by their name when making requests to the server
- storing settings used for My Page widgets client side, as these widgets apply system wide. For example, how many rows of data should be displayed to the user. Only non-secure settings are available to My Page widgets


=== "Explanation"
    The settings is an array of objects, each object contains the following properties (some are optional)

    - **settingTypeId**: an integer for the type of [setting](./SpiraApps-Reference.md/#setting-types)
    - **name**: codeFriendlyUniqueName
    - **caption**: User friendly Name
    - **isSecure**: boolean (true or false - defaults to false)
    - **placeholder**: Placeholder for the setting to help users
    - **position**: Optional int for the order to show the settings in
    - **tooltip**: On hover tooltip for users
    - **settingGroupName**: Optional name of the settingGroup to use for this setting

=== "Example"

    ```yaml
    settings:
      - settingTypeId: 1 
        name: rowsToDisplay
        caption: How many rows should we display on the My Page widget?
        isSecure: false
        placeholder: 5
        position: 1
        tooltip: By default 5 rows are displayed
        settingGroupName: groupAlpha
    ```

### Product admin settings
A SpiraApp can also have product level settings. These settings are unique per product and are useful for:

- storing settings used by Product Home Page or Reporting SpiraApp widgets
- storing settings used on any product artifact page by the SpiraApp
- storing any secure securely (not currently used)

Only non-secure settings are available to SpiraApps client side.

The settings is an array of objects, each object must be in the form as below. See our reference for [settingTypeIds](./SpiraApps-Reference.md/#setting-types)

=== "Explanation"
    - **settingTypeId**: an integer for the type of [setting](./SpiraApps-Reference.md/#setting-types) 
    - **name**: codeFriendlyUniqueName
    - **caption**: User friendly Name
    - **artifactTypeId**: Optional [artifact type](./SpiraApps-Reference.md/#artifact-types) you wish to specify (useful for status or custom property setting types)
    - **isSecure**: boolean (true or false - defaults to false)
    - **placeholder**: Placeholder for the setting to help users
    - **position**: Optional int for the order to show the settings in
    - **tooltip**: On hover tooltip for users
    - **settingGroupName**: Optional name of the settingGroup to use for this setting

=== "Example"

    ```yaml
    productSettings:
      - settingTypeId: 3 
        name: customProperty1
        caption: Select a release custom property
        artifactTypeId: 1
        position: 1
        tooltip: Please select a requirement custom property from the dropdown list
        settingGroupName: groupAlpha
    ```

### Menu entries
A SpiraApp can add a menu button to a [wide number of product pages](./SpiraApps-Reference.md/#pages) 

=== "Explanation"

=== "Example"

    ```yaml
    menus:
    - pageId: 1 [see possible values below]
      caption: User facing name
      icon: fas fa-play [FontAwesome or custom css classes]
      isActive: true
      entries:
      - name: CodeFriendlyName
        caption: User facing name
        tooltip: On hover tooltip
        icon_class: fas fa-circle [FontAwesome or custom css classes]
        isActive: true
        actionTypeId: 1 [see possible values below]
        action: [URL or a codeFriendlyName to create an element ID]
    ```

Menu buttons on toolbars on specific pages: menus
Dropdown entries inside those menu buttons: entries inside a menu
Code (JS and / or CSS) to add into specific pages: pageContents
HTML (currently) data to add as columns on specific grids: pageColumns
Code (JS) to add onto specified dashboard pages in widgets: dashboards


## Coding the SpiraApp


## Available Resources
- React v16
- **FontAwesome 6**: 
- Mustache
- Inflectra CSS utility library
- Spira theming variables for light and dark mode
- SpiraApp helper functions
- Make internal API calls to Spira
- Make external API calls

## Submission Process