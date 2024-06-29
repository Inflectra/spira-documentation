# SpiraApps Overview for Developers
## Introduction
This page provides an overview of how SpiraApps work, what they can do, and how the development process works. This is in addition to [technical reference material](./SpiraApps-Reference.md), the [manifest explanation](./SpiraApps-Manifest.md), and details about [available APIs](./SpiraApps-Manager.md) to help you get started. 

SpiraApps will often use Spira's REST API. We have extensive reference documentation for the API as part of each Spira install. Get started by following this [API overview](./API-Overview.md).

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

- a [manifest.yaml](./SpiraApps-Manifest.md) file that describes the SpiraApp, where it should appear and what it does
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

## Creating the manifest
The [manifest](./SpiraApps-Manifest.md) is an essential part of a SpiraApp. It lets admins configure the SpiraApp, and tells Spira where and how inside the application to deploy your SpiraApp. Without a proper and well crafted manifest you will not be able to test or deploy your SpiraApp.

A SpiraApp can exist in multiple places in Spira and it can have different types of settings. While a very large SpiraApp may be deployed in many ways and places and offer differ functionality on each, most SpiraApps will be targeted on a single page or very focused subset of pages.

For example, Inflectra's [FMEA](../SpiraApps/FMEA.md) has:

- a number of admin settings
- runs code in the background on the risk details page (no user interaction)
- has a product dashboard / product home page widget

!!! tip "Determining scope"
    We recommend starting your SpiraApp by understanding what it will do, where, and how. This will help narrow your focus. 

    Start small and built up from there. That will help validate your concept, 



## Coding the SpiraApp
### Overview
Code (JS and / or CSS) to add into specific pages: pageContents
HTML (currently) data to add as columns on specific grids: pageColumns
Code (JS) to add onto specified dashboard pages in widgets: dashboards

### Page Contents
A SpiraApp can include the contents of a single CSS file and a single JS file on each / any of the [relevant pages](./SpiraApps-Reference.md/#pages). You specify what files to load on what pages in the [manifest](./SpiraApps-Manifest.md/#page-contents). The file contents are then loaded automatically onto the page(s). 

**CSS files** are used for storing logos as SVGs, or helping to style widgets. You should primarily use class based selectors in your CSS. When loaded onto the page, the CSS contents is [nested](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_nesting) inside a class based off of the guid of the SpiraApp. Any UI elements created on the page will have a wrapper with this same class defined on it. In this way you can be flexible in how you use CSS as you are not able to pollute any other CSS.  

**JavaScript files** are the core part of most SpiraApps and should be written in dedicated JS files. When dynamically inserted onto the page, the SpiraApp code is wrapped in an IIFE block and set to use strict. This means that code can be written relatively flexibly, and can declare "global" variables as they will be confined to the IIFE on load.

### File references in CSS and JS
You may wish to include file references in your css or js files. This is required if the CSS has embedded images. For js files it can be useful if you have code you wish to share across several files (such as for localization), or to help you organize your code. 

To add a file reference in a CSS or JS file, you do so in the same way you do in the manifest. Add a reference like this: `file://nameOfFile.extension`. When the SpiraApp is packaged any file reference in any CSS or JS file will be automatically embedded into the final contents. Note that the file reference is replaced by the full contents of the file. 

### Menus
Menus and their entries allow users to interact with SpiraApps on [relevant pages](./SpiraApps-Reference.md/#pages). You specify what menus to create on what pages in the [manifest](./SpiraApps-Manifest.md/#menus). SpiraApp menu entries can either call a URL or a JavaScript function. 

For the user interaction to work you must:

- Set the correct action type on the menu entry
- Give the menu entry a name unique to your app on that page
- If the action is JavaScript, write code to run when the entry is clicked
- Connect your code function to the menu entry click event by calling the `registerEvent_menuEntryClick` API on the spiraAppManager

If the **action type is URL**, you can use `{project_id}` or `{artifact_id}` in the url and these will be automatically converted to the current product ID or artifact ID respectively.

If the **action type is a function**, make sure to also provide valid Page Contents information in the manifest.

### Widgets
A SpiraApp can be used to generate a widget on one of the [relevant dashboard pages](./SpiraApps-Reference.md/#dashboard-types). The widget requires JavaScript code to run. Just like with Page Contents, the SpiraApp code is wrapped in an IIFE block and set to use strict. This means that code can be written relatively flexibly, and can declare "global" variables as they will be confined to the IIFE on load.

The code is responsible for rendering the widget. You can render the contents of the widget using one or all of:

- JavaScript string literals
- mustache templating
- React

Note that the widget will not display by default on the dashboard. The end user will need to manually add the widget to show.

### Columns
SpiraApps can show buttons in columns on [list pages](./SpiraApps-Reference.md/#pages). This uses HTML only, provided in the [manifest](./SpiraApps-Manifest.md/#page-columns). You can use `{project_id}` or `{artifact_id}` in this HTML (typically used for URLs) and these will be automatically converted to the current product ID or artifact ID respectively. 

CSS styling can be done with classes provided to SpiraApps. To provide additionally styling add a CSS file to the relevant page as [page contents](#page-contents).

### Accessing settings
SpiraApp settings stored by admins when they set up the SpiraApp [can be accessed by the SpiraApp](./SpiraApps-Reference.md/#spiraappsettings). This provides a way to tailor and customize the experience for users based on these settings.

## Development Tips and Tricks
### Localization
SpiraApps do not currently provide native localization support. We encourage developers to implement localization where possible. SpiraApps have access to the user's preferred culture / language using the [currentCulture](./SpiraApps-Manager.md/#properties) helper function.

### Design patterns to follow
- [x] Use [officially provided](./SpiraApps-Reference.md/#available-resources) libraries or resources
- [x] Use external URLs or APIs (make sure to provide details in submission)
- [x] Focus on code that is performant
- [x] Match browser compatibility to Spira’s standards
- [x] Write code that can be reviewed by a web developer

## Design patterns to avoid
- [ ] Access the global namespace of the browser
- [ ] Using internal Spira functions or properties
- [ ] Links to or importing external libraries  (including any CDN)
- [ ] Editing or deleting any const or helper class provided by Spira for the SpiraApp, such as the spiraAppManager
- [ ] External links to images
- [ ] Base64 encoded and embedded resources
- [ ] Implement or change a CSP
- [ ] Import any JS library or module
- [ ] Provide code pre minified
- [ ] Use JQuery
- [ ] Write out encoded HTML strings using javascript
- [ ] Write out `<style>` tags using javascript
- [ ] Hardcode the GUID in CSS (CSS is pre-nested)
- [ ] Hardcode the GUID in JS (use provided const)
- [ ] Directly use local storage
- [ ] Directly use localDB
- [ ] Hard code secrets in code
- [ ] Access browser APIs like Camera, Bluetooth, Location, Notifications, NFC, fonts installed, 
- [ ] Use of any data tracking techniques
- [ ] Share data with any third party without explicit disclosure and opt-in consent
- [ ] Create, save, read, or update browser cookies
- [ ] Use WebAssembly
- [ ] Use WebSockets
- [ ] Frequent background polling or high frequency API usage
- [ ] Use of any deprecated browser APIs
- [ ] Use Iframes
- [ ] Save script files pre-minified

## Submission Process
!!! tip "Give us feedback"
    The submission process will evolve over time based on developer feedback. Please share your views with us at spiraapps@inflectra.com.

Once you have a working SpiraApp that you are happy with and are looking to release to other users, you need to submit the SpiraApp to Inflectra. Inflectra carefully reviews all SpiraApps to make sure that they:

- adhere to the guidance in this documentation
- are secure and performant
- does not duplicate existing functionality (of Spira itself or other SpiraApps)
- add value to end users
- works as expected with easy to follow documentation

Below the submissions process steps are outlined

### Prepare your code
Host the SpiraApp in a repo on GitHub.

Create a branch for the current work. Make sure to commit to a feature branch and not the main branch to make PRs easier to manage.

### Prepare your documentation
Each SpiraApp should have useful and easy to follow documentation about how to setup and use the SpiraApp. 

This documentation should clearly list any third party URLs contacted by the SpiraApp with a brief explanation of why each is needed.

!!! tip "Documentation Examples"
    Inflectra's SpiraApps all have detailed documentation [available](../SpiraApps/index.md). We recommend this format and level of content as a good practice example to use for your own documentation for SpiraApps.

### Create a PR for Inflectra
Invite the user spiraapps@inflectra.com to the repo. Then create a PR using the template below and assign it to spiraapps@inflectra.com for review.

```md title="GitHub Pull Request Template"
# {Public name of SpiraApp} for version {latest version number}

- **goal of SpiraApp**: {summarize the purpose of the SpiraApp and how it helps users}
- **documentation**: {link to help and setup documentation - this must be public on release, but may be a readme during the submission process}
- **support contact**: {email contact for users to get support or ask questions - make sure this is also in the documentation}
- **third party URL domains**: {list any third party (non Spira) domains used by the SpiraApp with a brief note about why this access is needed}
- **test setup**: {if any special test setup is required for Inflectra to get the SpiraApp working please provide simple steps or other information}

{any other information you wish to share}

```

The Inflectra team will review the PR and the SpiraApp. Their process follows these steps:

- static code analysis on GitHub of the SpiraApp
- verifying the manifest and code match the details provided in the PR template
- reviewing the help documentation
- downloading the source code and checking that it creates a valid SpiraApp package
- installing the SpiraApp package on a VM and performing a happy path test that the SpiraApp can be configured and works as expected

If Inflectra finds any issues or has any questions they will raise them on the PR. Discussion between you and the Inflectra team can happen on that PR to keep everything in one place. 

Once Inflectra completes all validation and review, it will approve the PR.

### Publishing a SpiraApp
Once a PR completes successfully, Inflectra will take the latest code from the GitHub repo and prepare it for publication:

- create a SpiraApp bundle for distribution
- validate that the URL in the manifest has the correct documentation and clearly lists the support contact
- publish the bundle on the Inflectra SpiraApp page with the following attributes

    - name: the name from the manifest
    - author: the author from the manifest
    - summary: the summary from the manifest
    - version number: the version number from the manifest
    - support link: url from the manifest
    - support email: the email address provided in the PR (and that matches the support contact in the documentation)

The Inflectra team will communicate over email via the support email address you provide regarding any logistics regarding publication. Note that you should expect the SpiraApp to go live normally within 2 business days of the PR being approved.