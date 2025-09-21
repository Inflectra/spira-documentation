# Auto-Sprints
!!! abstract "Compatible with SpiraTest, SpiraTeam, SpiraPlan"

!!! warning "This SpiraApp works with Spira v8.3+" 

This SpiraApp automates sprint creation based on your product's settings. It creates a set of sprints for a selected major or minor release, from the Release List page.

!!! info "About this SpiraApp"
    - product settings 
    - toolbar button on the release list page

## Setup
### Product Settings
Once the SpiraApp has been activated system-wide and enabled for a specific product, you can configure its product-level settings. All settings, except for "Sprint Gap" (which defaults to 0), are **required**. These settings allow you to control:

- [length](#length): days in each sprint and the gap between the sprints (for example, to skip weekends)
- [how many sprints](#parallel-and-sequential): options for how many sprints to create in parallel and/or in series
- [names](#naming-templates): customization options for the sprint name and version number

**Important:** The SpiraApp cannot generate sprints without these settings properly configured. Attempting to do so will result in an error message to end users.

Hover over the label for any setting to get a tooltip with guidance about how to use it.

#### Length
These settings define the length of each sprints and an optional gaps between them.

![product settings page](img/auto-sprints-product-length.png)

- **Sprint Days:** Enter an integer between 2 and 60 for the length, in days, of each generated sprint.
- **Sprint Gap:** Enter an optional integer between 0 and 30 (defaults to 0) for the number of days between the end of one sprint and the start of the next. Examples:
    - Sprint gap of 0: one sprint ends on a Friday, the next sprint will start on Saturday
    - Sprint gap of 2: one sprint ends on a Friday, the next sprint will start on Monday

#### Parallel and Sequential
These settings control the different number of parallel and sequential sprints users can create. Parallel sprints also require custom names to differentiate them.

![product settings page](img/auto-sprints-product-parallel&sequential.png)

- **Parallel Options:** Provide up to 3 comma-separated integer values, each between 1 and 5. These values determine how many parallel sprints will run concurrently. Examples:
    - `1` creates a single sprint (not really parallel)
    - `2,3,4` lets users create either 2 sprints in parallel, 3 sprints in parallel, or 4 sprints in parallel

- **Parallel Increment List:** Provide up to 5 comma-separated names. These names are used to uniquely identify parallel sprints that start at the same time. If "Parallel Options" is set to `1`, this field can be left empty. Otherwise, you must provide enough names to match the maximum number of parallel sprints specified. Examples:
    - `1,2,3` creates parallel sprints differentiated as 1, 2, and 3
    - `Blue, Red, Yellow` creates parallel sprints differentiated as Blue, Red, and Yellow

- **Sequential Options:** Provide up to 5 comma-separated integer values, each between 1 and 10. These values determine the total number of sequential sprints to be generated.
    - `1` creates a single sprint (not really series)
    - `2,5,10` lets users create either 2 sprints in series (one after the other), 5 sprints in series, or 10 sprints in series

You can combine parallel and sequential options to create X sprints at once (parallel), Y times after each other (sequentially or in series). This means the maximum total number of sprints users can create is 50 (5 parallel sprints for each of 10 sequential periods).

#### Naming Templates
These settings let you customize the naming and version numbering conventions for all generated sprints using a combination of predefined tokens. This allows users to very quickly create sprints with names that work exactly how the admin determines.

![product settings page](img/auto-sprints-product-namingTemplates.png)
 
**Sprint Naming Template:** Define how your sprints will be named. You can use the following allowed tokens:

- `{release}`: Replaced by the name of the selected parent release.
- `{product}`: Replaced by the name of the current product.
- **Date Tokens:**:
    - `{yyyy}`: Full year (e.g., 2025)
    - `{yy}`: Two-digit year (e.g., 25)
    - `{mm}`: Two-digit month (e.g., 01 for January)
    - `{mmm}`: Three-letter month abbreviation (e.g., Jan)
    - `{dd}`: Two-digit day (e.g., 05)
    - `{d}`: Day of the week (1 for Monday, 7 for Sunday)
    - `{ww}`: Two-digit week number (e.g., 01 for the first week of the year)
- `{s-increment}`: Represents the sequential depth of the sprint as an integer (e.g., 1, 2, 3...)
- `{p-increment}`: Differentiates between parallel sprints using the values from "Parallel Increment List"


**Sprint Version Template:** Define the versioning template for your sprints. You can use the following allowed tokens:

- `{version}`: Takes the full version number of the parent release (e.g., 1.0.0).
- `{version,stop=X}`: Takes the part of the parent release version up to the first occurrence of character `X` (e.g., if version is `1.2.3` and `X` is `.`, this token would result in `1`).
- **Date Tokens:** These are the same as for the Sprint Naming Template (`{yyyy}`, `{yy}`, `{mm}`, `{mmm}`, `{dd}`, `{d}`, `{ww}`)
- `{s-increment}`: Represents the sequential depth of the sprint as an integer (e.g., 1, 2, 3...).
- `{p-increment}`: Differentiates between parallel sprints (uses values from "Parallel Increment List").

#### Product Actions Button
These buttons let you to validate your settings and preview the generated sprint details.

![product settings page](img/auto-sprints-product-actions-button.png)

- **Validate Sprint Details:** It is very important to use this button to **verify your configurations are valid** before saving. If any validation fails, the app will clearly indicate what needs to be corrected, preventing sprint generation failures for end users on the Release List page.
- **Preview Details:** Use this button to **see a sample of your sprint names and versions** based on your current template configurations. Notes:
    - The preview will display a maximum of the first four example names and versions.
    - If your settings are invalid, a pop-up error will inform you which fields need to be fixed, and no preview will be available.

#### Example of Product Admin Configuration
Here is a detailed worked example demonstrating how to configure the SpiraApp for automated sprint generation.

**Scenario:** You want to generate sprints for a release in this way:

- 10 day sprints
- With a gap of 2 days between sprints
- Users must always create 2 sprints in parallel
- Users must always create 3 sequential sprints
- Sprint names should include the product name, release name, the sequential increment, and a parallel identifier
- Sprint versions should be based on the release version, with a sequential increment and parallel identifier

**Product Settings Configuration:** Based on the scenario, here's how you would configure each section:

- **Length:**
    - **Sprint Days:** `10`
    - **Sprint Gap:** `2`
- **Parallel and Sequential:**
    - **Parallel Options:** `2`
    - **Parallel Increment List:** `A,B`
    - **Sequential Options:** `3`
- **Naming Templates:**
    - **Sprint Naming Template:** `{product} - {release} - S{s-increment} - {p-increment} {yy}/{mm}/{dd}`
    - **Sprint Version Template:** `{version}.{s-increment}.{p-increment}`

**Preview:**

Assuming the product is called "Web App", the chosen release is called "Release 1", the chosen release has a version number of "1.0", and a starting date of June 20, 2025, here's what the generated sprints *would look like* in the preview:

| Sprint Names                          | Sprint Version Numbers |
| :------------------------------------ | :--------------------- |
| Web App - Release 1 - S1 - A 25/06/20 | 1.0.1.A                |
| Web App - Release 1 - S1 - B 25/06/20 | 1.0.1.B                |
| Web App - Release 1 - S2 - A 25/07/02 | 1.0.2.A                |
| Web App - Release 1 - S2 - B 25/07/02 | 1.0.2.B                |


## Using the Spira App
The SpiraApp is accessed from the Release List page, allowing users to generate sprints for any major or minor releases. To use the SpiraApp, navigate to the Releases list page and follow the steps below.

- **Select a Release:** Select a **single major or minor release** by checking its checkbox.

![Release list page](img/auto-sprints-release-list-page.png)

- **Access Auto-Sprints:** Click the **"Auto-Sprints"** toolbar button, and then click **"Create Sprints"** from the dropdown

![Auto-Sprints button](img/auto-sprints-button.png)

- **Choose Sprint Configuration:** From the pop-up window select the sprint configuration you want from the dropdown list of available configurations. These options are generated based on your "Parallel Options" and "Sequential Options" defined in the product settings.

![Create Sprints](img/auto-sprints-create-sprints-dropdown.png)

- **Generate Sprints:** Select your desired configuration from the dropdown. Once selected, click "Confirm" and the Auto-Sprints app will automatically generate the specified number of sprints as children of your selected major or minor release, adhering to all your configured product settings.

!!! info "Tips and tricks"
    - The start date of the first sprint created will match the start date of the selected release
    - The end date of the selected release will be updated if the end date of the final sprint created is later than the release's original end date
    - Once the sprints are created you can freely edit them, including their dates, names, and version numbers
    - Version numbers have to be unique across a product
    - If the sprint configuration by the product admin has errors in it, when you click the Auto-Sprints dropdown you will see an error message.
    - You are only able to select 1 release at a time for Auto-Sprints. If you do not select 1 or if it is the wrong type, you will see an error message.