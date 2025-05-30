# Azure OpenAI SpiraApp

!!! warning "Some of this SpiraApp's functionality is not compatible with SpiraTest"

!!! info "Upgrade to Inflectra.ai"
	Inflectra.ai is available for all cloud Spira customers. It is easy to set up and manage, and is deeply integrated into Spira. Inflectra.ai provides more powerful features than is possible with this SpiraApp.

	[Explore all of its features](../Spira-User-Manual/Inflectra-Ai-In-Spira.md) and [contact us to find out how to upgrade](mailto:sales@inflectra.com).

This SpiraApp lets you generate downstream artifacts from Spira requirements, test cases and risks using the Azure OpenAI engine developed by OpenAI and provided by Microsoft.
The current functionality uses the power of generative AI to suggest probable test cases with steps from requirements, generate the likely
development tasks for the requirement, generate the BDD scenarios for the requirement, and identify common business and technical risks.
It also will let you generate the test steps for an existing test case, and suggest mitigations for an existing risk.

It can provide an easy and effective way for users to create a foundational set of items that they can refine and tailor easily and effectively. Note that Tasks and Risks are not available in SpiraTest.

By using this SpiraApp users will, by necessity, share information with Azure OpenAI. For that reason, system admins must configure this SpiraApp to an existing Azure OpenAI subscription for your organization.

!!! info "About this SpiraApp"
    - [x] system settings
    - [x] product settings 
    - [ ] product template setup required
    - [x] toolbar button on requirement details page
    - [x] toolbar button on test case details page
    - [x] toolbar button on risk details page
    - [x] toolbar button on task details page

## Setup
### System Settings
- [x] Provide the full base URL to your Azure OpenAI host
- [x] Enter the the API Key users will access Azure OpenAI with
- [x] Enter the Azure OpenAI Version (this is in the form of a date in the format YYYY-MM-DD)

![system settings page](img/azureopenai-system-settings.png)

### Product Settings
Once the SpiraApp has been activated system wide, and enabled for a product you can edit its product settings. **All of these settings are optional**. You can use the SpiraApp without editing any of the product settings. The settings are here to help you customize the results from the SpiraApp, including if using languages other than English.

#### Code Generation

This is where you can customize the list of programming languages available:

![product settings page](img/azureopenai-product-settings.png)

- **Coding Languages**: In this text box, provide a comma-separated list of programming languages that the user can pick from. If you don't provide a value, the default list of languages will be provided.
- **Unit Test Frameworks**: In this text box, provide a comma-separated list of programming languages and unit test frameworks that the user can pick from. The programming language and unit test framework should be separated by a pipe (|) symbol If you don't provide a value, the default list of languages and unit test frameworks will be provided.


#### Prompt Customization

This is where you can customize the prompts sent to the LLM:

![product prompt settings](img/azureopenai-product-settings-2.png)

| Setting name            | Default Value                                                                                                                         | Explanation                                                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Global Prompt        | You are a business analyst that only speaks in JSON. Do not generate output that isn't in properly formatted JSON. | This prompt is used to control the output format of all the repsonses to be JSON.                                                                                        |
| Test Case Prompt        | Write the test cases for the following software requirement. For each test case include the description, input and expected output in the following format { \"Description\": [Description of test case], \"Input\": [Sample input in plain text], \"ExpectedOutput\": [Expected output in plain text] } | This prompt is used to generate the test cases from the requirement                                                                                              |
| Task Prompt             | Write the development tasks for the following software requirement. For each task include the name and description in the following format { \"Name\": [name in plain text], \"Description\": [description in plain text] }                                                                 | This prompt is used to generate the tasks from the requirement                                                                                                   |
| Risk Prompt             | Identify the possible business and technical risks for the following software requirement. For each risk include the name and description in the following format { \"Name\": [name in plain text], \"Description\": [description in plain text] }                                          | This prompt is used to generate the risks from the requirement.                                                                                                  |
| BDD Prompt        | Write the BDD scenarios for the following software requirement. Write the BDD scenarios for the following software requirement. For each scenario use the following Gherkin format { \"Name\": [The name of the scenario], \"Given\": [single setup in plain text], \"When\": [single action in plain text], \"Then\": [single assertion in plain text] }                                                                     | This prompt is used to generate the BDD steps for the requirement.                                                                                               |
| Test Step Prompt        | Write the test steps for the following test case. For each test step include the description, expected result, and sample data in the following format { \"Description\": [Description of test step], \"ExpectedResult\": [The expected result], \"SampleData\": [Sample data in plain text] }                                                                     | This prompt is used to generate the test steps steps for the test case.                                                                                               |
| Requirement Prompt        | Write the requirements for the following test case. For each requirement include the name and description in the following format { \"Name\": [name in plain text], \"Description\": [description in plain text] }                                                                     | This prompt is used to generate the requirements for the test case.                                                                                               |
| Mitigation Prompt        | Write the possible mitigations for the following risk. For each mitigation include the description in the following format { \"Description\": [description in plain text] }                                                                     | This prompt is used to generate the mitigations for the risk.                                                                                               |

#### General Settings

This is where you can specify the other SpiraApp settings:

![product prompt settings](img/azureopenai-product-settings-3.png)

| Setting name            | Default Value                                                                                                                         | Explanation                                                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Temperature             | 0.2                                                                                                                                   | A number between 0 and 2, used to control the output's randomness. A higher temperature gives a more random output, a lower one give a more deterministic output |
| Deployment Name                   | gpt-4o-mini                                                                                                                         | The name of the OpenAI model Deployment we want to use (not the model name, but the Deployment name you entered inside the Microsoft Azure control panel)                                                                                                                     |
| Detailed Test Steps     | false                                                                                                                         | Should we create detailed test steps for test cases, or just a single step?                                                                                                                     |
| Use Artifact Descriptions     | false                                                                                                                         | Should we use the artifact descriptions as well as the names in the prompts?                                                                         

## Using the SpiraApp

The user can navigate to different pages to use the SpiraApp, each one will have a toolbar with various generation options.

### Requirement Details Page

When a user goes to the requirement details page, they will see an extra button in the toolbar. To generate relevant data they should follow these steps:

- Click the "Azure OpenAI" button
- Select the artifact to generate (e.g. Tasks)

![toolbar button](img/azureopenai-toolbar-button.png)

- This will send the requirement name (and optionally the description) to Azure OpenAI
- The information coming back is parsed and analyzed by the SpiraApp and then created in Spira

A message will show at the top of the page informing the user when information is sent or if there was a problem.


### Test Case Details Page

When a user goes to the testc ase details page, they will see an extra button in the toolbar. To generate relevant data they should follow these steps:

- Click the "Azure OpenAI" button
- Select the artifact to generate (e.g. Test Steps)

![toolbar button](img/azureopenai-toolbar-button-2.png)

- This will send the test case name (and optionally the description) to Azure OpenAI
- The information coming back is parsed and analyzed by the SpiraApp and then created in Spira

A message will show at the top of the page informing the user when information is sent or if there was a problem.

### Task Details Page

When a user goes to the task details page, they will see an extra button in the toolbar. To generate relevant data they should follow these steps:

- Click the "Azure OpenAI" button
- Select the type of code to generate (e.g. Source Code)

![toolbar button](img/azureopenai-toolbar-button-4.png)

Once you choose the appropriate code generation option, a dialog box will be displayed where you can choose which programming langauage (and optionally unit test framework) to use:

![code generation dialog box](img/azureopenai-code-dialog-box.png)

- This will send the task name (and optionally the description) to Azure OpenAI
- The information coming back is parsed and analyzed by the SpiraApp and then created in Spira

A message will show at the top of the page informing the user when information is sent or if there was a problem.

### Risk Details Page

When a user goes to the risk details page, they will see an extra button in the toolbar. To generate relevant data they should follow these steps:

- Click the "Azure OpenAI" button
- Select the artifact to generate (e.g. Mitigations)

![toolbar button](img/azureopenai-toolbar-button-3.png)

- This will send the risk name (and optionally the description) to Azure OpenAI
- The information coming back is parsed and analyzed by the SpiraApp and then created in Spira

A message will show at the top of the page informing the user when information is sent or if there was a problem.

### Extra details to be aware of

- The generated artifacts only have their names and descriptions populated, with the exception of test cases that will have detailed test steps.
- To generate artifacts the user must have create permission for that artifact.
- BDD steps can only be generated on requirements of types that support steps.

## Appendix - Default prompts

If you are interested in customizing the prompts used in the plugin, please use the following starting points:

### Global Prompt

`You are a business analyst that only speaks in JSON. Do not generate output that isn't in properly formatted JSON.`

### Requirement Prompts

#### 1. Generate Test Cases

`Write the test cases for the following software requirement. For each test case include the description, input and expected output in the following format { \"Description\": [Description of test case], \"Input\": [Sample input in plain text], \"ExpectedOutput\": [Expected output in plain text] }`

#### 2. Generate Tasks

`Write the development tasks for the following software requirement. For each task include the name and description in the following format { \"Name\": [name in plain text], \"Description\": [description in plain text] }`

#### 3. Generate Scenarios

`Write the BDD scenarios for the following software requirement. Write the BDD scenarios for the following software requirement. For each scenario use the following Gherkin format { \"Name\": [The name of the scenario], \"Given\": [single setup in plain text], \"When\": [single action in plain text], \"Then\": [single assertion in plain text] }`

#### 3. Generate Risks

`Identify the possible business and technical risks for the following software requirement. For each risk include the name and description in the following format { \"Name\": [name in plain text], \"Description\": [description in plain text] }`

## Risk Prompts

#### 1. Generate Mitigations

`Write the possible mitigations for the following risk. For each mitigation include the description in the following format { \"Description\": [description in plain text] }`

## Test Case Prompts

#### 1. Generate Steps

`Write the test steps for the following test case. For each test step include the description, expected result, and sample data in the following format { \"Description\": [Description of test step], \"ExpectedResult\": [The expected result], \"SampleData\": [Sample data in plain text] }`

#### 2. Generate Requirements

`Write the requirements for the following test case. For each requirement include the name and description in the following format { \"Name\": [name in plain text], \"Description\": [description in plain text] }`

## Task Prompts

#### 1. Generate Source Code

`You are a programmer working in the [CODE_LANGUAGE] programming language. Write sample code that implements the following feature in the following format { \"Filename\": [filename for source code], \"Code\": [source code in plain text] }`

#### 2. Generate Source Code with Unit Tests

`You are a programmer working in the [CODE_LANGUAGE] programming language. Could you write a sample unit test for the following feature using [CODE_LANGUAGE] and the [TEST_FRAMEWORK] framework in the following format { \"Filename\": [filename for source code], \"Code\": [source code in plain text] }`