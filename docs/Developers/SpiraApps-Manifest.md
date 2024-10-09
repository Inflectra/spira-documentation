# SpiraApp Manifest
## Introduction
The manifest is a yaml file that stores all information about the SpiraApp, including its name, references to code files, settings, and where the SpiraApp is used in the application. It is an essential part of every SpiraApp, determining where and how the SpiraApp should run. 

## Overview
The manifest can have up to 8 different sections, but all of them are optional, except for the metadata section. Only use the sections that are relevant to your SpiraApp.

1. General [metadata](#spiraapp-metadata) and information about the SpiraApp (we recommend putting this at the top of the yaml file)
2. System level [settings](#settings) for admins to fill in
3. [Product level settings](#product-admin-settings) for product admins to fill in
4. [Setting groups](#settings-groups) to help visually organize system and product settings
5. Insert [code content](#page-contents) onto specific pages
6. [Menu](#menus) buttons with dropdown entries on toolbars on specific pages
7. [Columns](#page-columns) on grids with custom HTML
8. [Dashboard](#dashboards) widgets with embedded js code

There are some potential gotchas or restrictions to keep in mind. You can only have one:

- menu item on each unique page
- pageContent item (so one js and css file) on each unique page
- column on a grid for each relevant page
- dashboard widget on each dashboard type
- setting, product setting, and setting group with a specific name (unique in each category - you can reuse a name between settings and product settings, for example)


Below, we describe each manifest section along with example yaml.

## SpiraApp metadata
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
    - **icon**: Optionally provide the relative path to a single SVG file in the form of `data:image/svg+xml;base64,file://filename.svg` (note the special syntax before the filename that is used to properly embed the SVG)
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
    icon: data:image/svg+xml;base64,file://myIcon.svg
    license: MIT License
    copyright: Copyright My Company
    version: 0.2
    ```

## Settings
SpiraApps can have [system wide](#settings) and [product specific](#product-admin-settings) settings. Settings can optionally be organized into [groups](#settings-groups) to make it easier for admins to configure them.

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
    - **settingGroup**: Optional name of the settingGroup to use for this setting

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
        settingGroup: groupAlpha
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
    - **settingGroup**: Optional name of the settingGroup to use for this setting

=== "Example"

    ```yaml
    productSettings:
      - settingTypeId: 3 
        name: customProperty1
        caption: Select a release custom property
        artifactTypeId: 1
        position: 1
        tooltip: Please select a requirement custom property from the dropdown list
        settingGroup: groupAlpha
    ```

## Pages
SpiraApps will often run on specific [artifact pages](./SpiraApps-Reference.md/#pages). This can be as a code running in the background, functionality triggered by a user, or actions a user can take on rows on a grid. 

### Page Contents
A SpiraApp can run on a [wide number of product pages](./SpiraApps-Reference.md/#pages). The functionality comes from code (JS, HTML, and CSS) from the SpiraApp. This code is loaded onto the page based on the configuration provided in the manifest. You can load different javascript code on each page, or the same code. Different SpiraApp features use different code types (for example, only page columns uses HTML).

The pageContents setting is an array of objects, one for each page that content should appear on. 

=== "Explanation"
    - **pageId**: an integer for the [page](./SpiraApps-Reference.md/#pages) the code should be embedded on
    - **name**: codeFriendlyName to describe the content (not currently used)
    - **code**: relative path to a single JS file to include on the page in the form of `file://{filename.js}`
    - **css**: relative path to a single CSS file to include on the page in the form of `file://{filename.css}`. **NOTE** do not embed encoded images in CSS, if you need to include SVG images, then reference them in the form `"data:image/svg+xml;base64,file://icon.svg"`.

=== "Example"

    ```yaml
    pageContents:
      - pageId: 9
        name: mySpiraAppCode
        code: file://app.js
        css: file://styles.css
    ```

### Menus
Users can proactively interact with a SpiraApp via menu buttons on [product pages](./SpiraApps-Reference.md/#pages). Each menu button has a number of entries. These entries provide the actual links to the SpiraApp code. For example, if users have 5 different actions they can take with a SpiraApp, then there will be 5 entries in the menu button - 5 menu entries in the button's dropdown.

The menu setting is an array of objects, one for each page the menu should be on. Each menu object will have an entries key that contains an array of "entry" objects.

=== "Explanation"
    **Menu object**:

    - **pageId**: an integer for the [page](./SpiraApps-Reference.md/#pages) the menu should display on
    - **caption**: the button text
    - **icon**: CSS classes to use for displaying an icon button. These can either be Font Awesome classes, or custom css classes from the SpiraApp
    - **isActive**: boolean whether the menu should be visible or not. If set to false or omitted the menu will not show
    - **entries**: list of menu entry objects

    **Entry object**:

    - **name**: codeFriendlyUniqueName
    - **caption**: User facing name
    - **tooltip**: On hover tooltip
    - **icon**: CSS classes to use for displaying an icon button. These can either be Font Awesome classes, or custom css classes from the SpiraApp
    - **isActive**: boolean whether the menu should be visible or not. If set to false or omitted the menu will not show
    - **actionTypeId**: an integer for the [type of action](./SpiraApps-Reference.md/#action-types) to run when the user clicks on the entry
    - **action**: the details of the action to run on user interaction (used for providing the URL to open if that is the action type)

=== "Example"

    ```yaml
    menus:
    - pageId: 9
      caption: Analyze Requirement
      icon: fa-light fa-flask
      isActive: true
      entries:
      - name: readingLevelScore
        caption: Reading Level Grade
        tooltip: Get the reading level grade score for the requirement description
        icon: fa-light fa-graduation-cap
        isActive: true
        actionTypeId: 2
        action: scoreDescriptionGrade
    ```

### Page Columns
Artifact list pages can have a special type of SpiraApp where SpiraApp functionality is provided as a column. 

The pageColumns setting is an array of objects, with only one object per unique page id.


=== "Explanation"
    - **pageId**: an integer for the [page](./SpiraApps-Reference.md/#pages) the menu should display on
    - **name** codeFriendlyName describing the column (not currently used)
    - **caption**: user friendly name
    - **template**: relative path to a single HTML template file in the form of `file://{filename.html}`
    
=== "Example"

    ```yaml
    pageColumns: 
      - pageId: 8
        name: myAppColumn
        caption: My App
        template: file://myColumn.html
    ```

## Dashboards
SpiraApps can run as custom widgets on [specific dashboard pages](./SpiraApps-Reference.md/#dashboard-types) in Spira. These widgets can show rich dynamic and interactive content to users.

The dashboards setting is an array of objects, with only one object per unique dashboard id.

=== "Explanation"
    - **dashboardTypeId**: an integer for the [dashboard page](./SpiraApps-Reference.md/#dashboard-types) the SpiraApp widget is on
    - **name**: User facing widget title
    - **isActive**: boolean set to true for the widget to be available to users
    - **description**: User friendly description
    - **code**: relative path to a single JS file to include in the widget in the form of `file://{filename.js}`

=== "Example"

    ```yaml
    dashboards:
      - dashboardTypeId: 1
        name: My Widget
        isActive: true
        description: A hello world example widget
        code: file://widget.js
    ```
