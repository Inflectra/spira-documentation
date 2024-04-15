# SpiraApps Overview for Developers
## Introduction
This page provides an overview of how SpiraApps work, what they can do, and how the development process works. This is in addition to [technical reference material](./SpiraApps-Reference.md) and the [manifest explanation](./SpiraApps-Manifest.md) useful for developers and a more [guided tutorial](./SpiraApps-Tutorial.md) to help you get started. 

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
Code (JS and / or CSS) to add into specific pages: pageContents
HTML (currently) data to add as columns on specific grids: pageColumns
Code (JS) to add onto specified dashboard pages in widgets: dashboards





## Submission Process


## Tips and Tricks
| Design pattern | Allowed |
| -- | -- |
| Using internal Spira functions or properties | N |
| Links to or importing external libraries  | N (including any CDN) |
| External links to images | N |
| Base64 encoded images | Y but we need to verify (either check it against the mimetype or have the bundler do this for the images) |
| Implement or change a CSP | N |
| Import any JS library | N |
| Provide code pre minified | N |
| Use mustache from Spira | Y |
| Use React from Spira (we may want to have a version for them and a different one for us) | Y |
| Use JQuery from Spira | N |
| Write out encoded HTML strings to render inside the allocated dom ID | N |
| Write out <style> tags inside the allocated dom ID | N |
| Hardcode the GUID in CSS | Y (because no other way - Simon to research)
| Hardcode the GUID in JS | N |
| Use local storage | Y  (but must be namspaced with GUID) |
| Use local DB | N |
| Hard code secrets in code | N |
| Have external URLs for interaction with 3rd party APIs | Y (but declare them and why needed in manifest - new section, and to customers) |
| Provided user facing documentation consistent with our guidance | Y |
| Access any browser APIs like Camera, Bluetooth, Location, Notifications, NFC, fonts installed, etc | N |
| Use any data tracking | N |
| Share any data with third parties without explicit disclosure and opt-in consent | N |
| Creating, saving, reading, updating browser cookies | N |
| WebAssembly use | N |
| WebSockets | N |
Background polling or high frequency API usage | Discouraged to improve performance |
| Focus on code that is performant | Y |
| Use of any deprecated browser APIs | N |
| Match browser compatibility to Spira’s standards | Y |
| Can be code reviewed by a human being with general web development skills | Y |
| Iframes | N |
| Save script files pre-minified | N |

