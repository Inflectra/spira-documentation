# Release Notes for Inflectra.ai

## October 31 2025
!!! success "New Features"
    - **[Release analysis](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#release-analysis)**
        - As an Inflectra.ai and release user, I can analyze the broader status of my release, to gain a better understanding of its content and progress [RQ:5450]

!!! bug "Bug fixes and enhancements"
    - Enhance Inflectra.ai to provide results in the same language as the input (for example French) [IN:11698]


## October 17 2025
!!! success "New Features"
    - **[Release analysis](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#release-analysis)**
        - As an Inflecta.ai and release user, I can open the Inflectra.ai side panel on the release details page [RQ:5429]
        - As an Inflectra.ai and release user, I can summarize the requirements in a release, to gain a better understanding of its content and progress [RQ:5428]
        - As an Inflectra.ai and release user, I can log the analysis of my release's requirements, to gain a better understanding of its content and progress [RQ:5451]

## October 3 2025
!!! bug "Bug fixes and enhancements"
    - Make previous chat interactions appear grayed out compared to the current one [RQ:5412]
    - Remove 'Create Task' follow-up button for EARS Analysis when it cannot be used [IN:11581]
        {: .edition-spiratest }

## September 19 2025
!!! bug "Bug fixes and enhancements"
    - Prepare Inflectra.ai for upcoming integration with Rapise 8.6
    - Show hand icon when hovering cursor over button group titles, so users know they can interact with the title [IN:11561]

## September 5 2025
!!! success "New Features"
    - Sidebar design and user experience
        - As an Inflectra.ai user, when I open the sidebar, actions I can take are grouped together clearly, so I can easily see and understand what I can do [RQ:5404] 
        - As an Inflectra.ai user, when I open the sidebar, I can collapse action groups so I can focus on the actions I need [RQ:5405] 
        - As an Inflectra.ai user, when I open the sidebar, I can expand a collapsed action group so I can focus on the actions I need [RQ:5408] 
        - As an Inflectra.ai user, when I open the sidebar, it remembers for my machine and browser the state of action group (whether they are expanded or collapsed) [RQ:5409] 
        - As an Inflectra.ai user, I can invoke any action inside a sidebar group, so I can use the functionality I need [RQ:5410] 

## August 22 2025
!!! success "New Features"
    - **[Requirement analysis against EARS](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#ears-analysis)**
        - As a requirement user, when I use Inflectra.ai to analyze a requirement, I can save the analysis as an attachment to the requirement [RQ:5400]
        - As a requirement user, when I use Inflectra.ai to analyze a requirement, I can create a task against the requirement of how to improve the requirement [RQ:5401]
            {: .edition-spiraplan .edition-spirateam}
    
!!! bug "Bug fixes and enhancements"
    - Fix Inflectra.ai action buttons text not being lined wrapped with long phrases or on small screens [IN:11430]
    - Fix the tag ai-augmented being added multiple times to a requirement if you click to Improve its description more than once in a row [IN:11457]
    - Stop text wrapping on list page grids when Inflectra.ai is enabled [IN:11468]
    - Update Inflectra.ai deterministic messages to handle single and plural phrases consistently [IN:11051]

## August 7 2025
!!! success "New Features"
    - **[Requirement analysis against EARS](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#ears-analysis)**
        - As a requirement user, after I have analyzed a requirement using Inflectra.ai, I can ask Inflectra.ai to improve how the requirement is written [RQ:5360]
        - As a requirement user, when I use Inflectra.ai to improve how the requirement is written, screenshots are preserved [RQ:5361]
        - As a requirement user, when I click the "Improve?" button, I can improve the requirement for EARS using Inflectra.ai [RQ:5362]
    
!!! bug "Bug fixes and enhancements"
    - Ensure localizations fall back to English for individual strings not currently translated [IN:11403]
    - Improve how Inflectra.ai updates in Spira after a new release by improving its cache expiration mechanisms [IN:11398] and [IN:11402]
    - Improve the consistency of creating artifacts using Inflectra.ai by using an agentic flow to ensure data is correctly formatted more reliably [IN:11252]
    

## July 25 2025
!!! success "New Features"
    - **[Requirement analysis against EARS](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#ears-analysis)**
        - As a requirement user, I see a button to analyze the current requirement against "EARS" on the Inflectra.ai sidebar of the details page [RQ:5353]
        - As a requirement user, when I use Inflectra.ai to analyze a requirement, I can analyze it using EARS, to give me a score out of 5 about the requirement [RQ:5355]
        - As a requirement user, when I use Inflectra.ai to analyze a requirement, I can analyze it using EARS, to give me guidance about how I can improve the requirement [RQ:5359]
    

!!! bug "Bug fixes and enhancements"
    - Improve the sidebar close button to look more consistent with other close buttons in Spira [IN:11312]


## July 11 2025
!!! success "New Features"
    - As an Inflectra.ai and requirement user, from the [requirement hierarchy list page](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirements-list-pages) I can create child requirements for a requirement using Inflectra.ai [RQ:5357]
    - Improve the performance of Inflectra.ai in Australia by upgrading it to be able to use Amazon Nova models [IN:11290]

!!! bug "Bug fixes and enhancements"
    - Improve how the inflectra.ai sidebar chat provides feedback to the end user with a progress bar for artifacts being created in Spira [IN:10960]
    - Update Inflectra.ai to better handle single and plural phrases AND Match the case of the Button [IN:11051]
    

## June 27 2025
!!! success "New Features"
    - **[Requirement list page](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirements-list-pages)**

        - As an Inflectra.ai and requirement user, I can see the Inflectra.ai button on the requirement list pages [RQ:5317]
        - As an Inflectra.ai and requirement user, I can open the Inflectra.ai side panel on the requirement list pages [RQ:5318]
        - As an Inflectra.ai and requirement user, from the requirement list page I can select 1 to 10 requirements to perform Inflectra.ai actions on [RQ:5319]
        - As an Inflectra.ai and requirement user, from the requirement list page I can create test cases for 1 to 10 requirements using Inflectra.ai [RQ:5320]
        - As an Inflectra.ai and requirement user, from the requirement list page I can create tasks for 1 to 10 requirements using Inflectra.ai [RQ:5321]
            {: .edition-spiraplan .edition-spirateam}
        - As an Inflectra.ai and requirement user, from the requirement list page I can create scenarios for 1 to 10 requirements using Inflectra.ai [RQ:5341]
        - As an Inflectra.ai and requirement user, from the requirement list page I can create risks for 1 to 10 requirements using Inflectra.ai [RQ:5322]
            {: .edition-spiraplan .edition-spirateam}

!!! bug "Bug fixes and enhancements"
    - Fix Inflectra.ai Sidebar sometimes not appearing due to race condition between loading scripts and setting the necessary data on the page [IN:11172]
    - When Inflectra.ai is used to generate a test case with test steps for a requirement, include the number of test steps created for each test case in the list of test case links [IN:11016]

## June 13 2025
!!! bug "Bug fixes and enhancements"
    - Improve the reliability of Inflectra.ai producing consistent outputs for artifacts created from requirements, test cases, and risks [IN:11125]

## May 30 2025
!!! bug "Bug fixes and enhancements"
    - Add syntax highlighting to BDD scenarios created for a [requirement](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page) [IN:10978]
    - Fix Inflectra.ai showing chat history from multiple demos in the same region when accessed from the same browser [IN:11041]
    - Improve the performance of Inflectra.ai in Singapore by upgrading the model used to Amazon Nova [IN:11101]
    - Improve the quality of generated BDD scenarios, including to ensure they always exclude the requirement name [IN:11079]

## May 16 2025
!!! success "New Features"
    - As a [requirement user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page), when I use Inflectra.ai to create content the requirement hierarchy is given as extra context [RQ:5266]
    - As a [requirement user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page), when I use Inflectra.ai to create content the component is given as artifact data [RQ:5272]
    - As a [requirement user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page), when I use Inflectra.ai to create content the product name is given as extra context [RQ:5275]
    - As a [requirement user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page), when I use Inflectra.ai to create content the requirement type is given as part of the artifact info [RQ:5265]
    - As a [requirement user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page), when I use Inflectra.ai, the quality of the content is more useful and of higher quality, to save me time improving the outputs manually [RQ:5267]
    - As a [risk user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#risks-details-page), when I use Inflectra.ai to create content the product name is given as extra context [RQ:5276]
        {: .edition-spiraplan .edition-spirateam}
    - As a [risk user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#risks-details-page), when I use Inflectra.ai to create content the risk type, probability and impact is given as artifact data [RQ:5271]
        {: .edition-spiraplan .edition-spirateam}
    - As a [risk user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#risks-details-page), when I use Inflectra.ai, the quality of the content is more useful and of higher quality, to save me time improving the outputs manually [RQ:5269]
        {: .edition-spiraplan .edition-spirateam}
    - As a [test case user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#test-case-details-page), when I use Inflectra.ai to create content the components are given as artifact data [RQ:5273]
    - As a [test case user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#test-case-details-page), when I use Inflectra.ai to create content the product name is given as extra context [RQ:5274]
    - As a [test case user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#test-case-details-page), when I use Inflectra.ai to create content the test case type is given as artifact data [RQ:5270]
    - As a [test case user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#test-case-details-page), when I use Inflectra.ai, the quality of the content is more useful and of higher quality, to save me time improving the outputs manually [RQ:5268]

!!! bug "Bug fixes and enhancements"
    - Fix Inflectra.ai showing options on the [requirement details page](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page) for creating tasks and risks, when using SpiraTest [IN:11040]
        {: .edition-spiratest }
    - Hide Inflectra.ai buttons when the user does not have permissions to perform the particular API actions associated with the button [IN:10976]
    - Include the currently displayed risk mitigations in the information to AI when generating new mitigations [IN:10999]
        {: .edition-spiraplan .edition-spirateam}
    - Include the currently displayed test steps in the information to AI when generating content based on a test case [IN:10997]
    - Provide users with a clearer error message when a response can not be provided as it contravenes our responsible AI policy, to help users better understand what is going on [IN:11009]
    - Reduce the chance of Inflectra.ai not giving responses, by decreasing false positives from requests it thinks contravene Inflectra's responsible AI policies [IN:10996]

## April 2025
!!! success "New Features"  
    - **[Requirement details page](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page)**:

        - As an Inflectra.ai user, I can see the Inflectra.ai icon on requirement details page, so I can access the AI features for a requirement [RQ:5196]
        - As an Inflectra.ai user, I can open the Inflectra.ai side panel on the requirement details page, so I can access the AI features for a requirement [RQ:5200]
        - As an Inflectra.ai and requirement user, I can use the Inflectra.ai side panel to generate test cases from a requirement [RQ:5202]
        - As an Inflectra.ai and requirement user, I can use the Inflectra.ai side panel to generate BDD scenarios for a requirement [RQ:5218]
        - As an Inflectra.ai and requirement user, I can use the Inflectra.ai side panel to generate risks for a requirement [RQ:5217]
            {: .edition-spiraplan .edition-spirateam}
        - As an Inflectra.ai and requirement user, I can use the Inflectra.ai side panel to generate tasks from a requirement [RQ:5216]
            {: .edition-spiraplan .edition-spirateam}
    
    - **[Test case details page](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#test-case-details-page)**
    
        - As an Inflectra.ai user, I can see the Inflectra.ai icon on test case details page, so I can access the AI features for a test case [RQ:5197]
        - As an Inflectra.ai and test case user, I can use the Inflectra.ai side panel to generate requirements from a test case [RQ:5220]
        - As an Inflectra.ai and test case user, I can use the Inflectra.ai side panel to generate test steps for a test case [RQ:5219]
    
    - **[Task details page](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#task-details-page)**
        {: .edition-spiraplan .edition-spirateam}
    
        - As an Inflectra.ai user, I can see the Inflectra.ai icon on task details page, so I can access the AI features for a task [RQ:5198]
        - As an Inflectra.ai and task user, I can use the Inflectra.ai side panel to generate sample code with tests for a task in a variety of languages [RQ:5222]
        - As an Inflectra.ai and task user, I can use the Inflectra.ai side panel to generate sample code for a task in a variety of languages [RQ:5221]

    - **[Risk details page](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#risks-details-page)**
        {: .edition-spiraplan .edition-spirateam}

        - As an Inflectra.ai user, I can see the Inflectra.ai icon on risk details page, so I can access the AI features for a risk [RQ:5199]
        - As an Inflectra.ai and risk user, I can use the Inflectra.ai side panel to generate risk mitigations for a risk [RQ:5223]
    
    - As an Inflectra.ai user, when I access the Inflectra.ai sidebar all text is localized for me, so I can interact with the sidebar in my preferred supported language [RQ:5232]