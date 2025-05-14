# Confluence SpiraApp

This SpiraApp lets you integrate Spira Requirements and Confluence so that you can:

- Open existing links to Confluence stored against the requirement
- Automatically create a new page in Confluence about a requirement


!!! info "About this SpiraApp"
    - [x] system settings
    - [x] product template setup required
    - [x] product settings
    - [x] toolbar button on requirement details page

## Setup
### System settings
- **`confluenceBaseUrl` (Confluence Base URL):** (required) The root URL for your Confluence instance. This is used for API calls and constructing page links. For example, `https://your-company.atlassian.net`
- **`confluenceApiEmail` (Confluence API Email for Basic Auth):** (required) The email address associated with the Confluence API Token that will be used for authentication. For example, `your.email@example.com`
* **`confluenceApiToken` (Confluence API Token / Password):** (required) The API token generated from Confluence. This is used as the password component for Basic Authentication with the Confluence API. This setting is stored securely by Spira. 

### Product template setup
- Create a [Requirement Custom Field](../Spira-Administration-Guide/Template-Custom-Properties.md). This is used to store the Confluence Page Link. Make sure the type is set to "Text".

### Product setting
- **`confluenceLinkFieldName` (Link Custom Field Name):** (required) The exact system name (e.g., `Custom_01`, `Custom_10`) of the Requirement custom property that stores and displays the URL to the Confluence page.
- **`confluenceSpaceKey` (Target Confluence Space Key):** (required) The unique key of the Confluence Space where new pages should be created if no existing link is found. For example, `MYPROJKEY`
- **`confluenceParentPageId` (Target Parent Page ID - Optional):** If you want new Confluence pages to be created as children of a specific existing page in Confluence, enter that parent page's numerical ID here. If left blank, pages will be created at the root of the specified space.

## Using the SpiraApp
If you have an existing Confluence page to link to a requirement, paste its link into the Confluence Page Link custom field, and save it

To use the SpiraApp go to any requirement and click the Confluence SpiraApp button in the toolbar. The SpiraApp will do one of two actions:

* **Confluence Page Link exists**: if the Confluence Page Link field is filled in, this page will be opened in a new tab
* **No Confluence Page Link exists**: if the Confluence Page Link field is blank then the SpiraApp will:

    - Create a new Confluence page (based on the product settings)
    - Open this page in a new browser tab.
    - Add the link to that page into the Confluence Page Link field
    - Show a success message stating: "Confluence page created. Link has been populated into the '[YourCustomFieldName]' field on this form. Please click Spira's 'Save' button to persist this change."

**IMPORTANT (If a new page was created):** After the link is populated into the Spira Requirement form, you **MUST click Spira's main "Save" button** for that Requirement. *Usability Note:* You might need to first click into the custom field where the link was populated to ensure Spira's "Save" button becomes active. Then, click "Save".