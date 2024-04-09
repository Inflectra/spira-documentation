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


## Coding the SpiraApp


## Available Resources
- React v16
- FontAwesome 6
- Mustache
- Inflectra unity utility library of classes
- Spira theming variables for light and dark mode
- SpiraApp helper functions
- Make internal API calls to Spira
- Make external API calls