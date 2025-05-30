# Release Notes for Inflectra.ai

## May 30 2025
    - Add syntax highlighting to BDD scenarios created for a [requirement](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page) [IN:10978]
    - Fix Inflectra.ai showing chat history from multiple demos in the same region when accessed from the same browser [IN:11041]
    - Improve the performance of Inflectra.ai in Singapore by upgrading the model used to Amazon Nova [IN:11101]
    - Improve the quality of generated BDD scenarios, including to ensure they always exclude the requirement name [IN:11079]

## May 16 2025
!!! success "New Features"
    - As a [requirement user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page), when I use Inflecta.ai to create content the requirement hierarchy is given as extra context [RQ:5266]
    - As a [requirement user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page), when I use Inflecta.ai to create content the component is given as artifact data [RQ:5272]
    - As a [requirement user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page), when I use Inflecta.ai to create content the product name is given as extra context [RQ:5275]
    - As a [requirement user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page), when I use Inflecta.ai to create content the requirement type is given as part of the artifact info [RQ:5265]
    - As a [requirement user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page), when I use Inflecta.ai, the quality of the content is more useful and of higher quality, to save me time improving the outputs manually [RQ:5267]
    - As a [risk user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#risk-details-page), when I use Inflecta.ai to create content the product name is given as extra context [RQ:5276]
    - As a [risk user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#risk-details-page), when I use Inflecta.ai to create content the risk type, probability and impact is given as artifact data [RQ:5271]
    - As a [risk user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#risk-details-page), when I use Inflecta.ai, the quality of the content is more useful and of higher quality, to save me time improving the outputs manually [RQ:5269]
    - As a [test case user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#test-case-details-page), when I use Inflecta.ai to create content the components are given as artifact data [RQ:5273]
    - As a [test case user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#test-case-details-page), when I use Inflecta.ai to create content the product name is given as extra context [RQ:5274]
    - As a [test case user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#test-case-details-page), when I use Inflecta.ai to create content the test case type is given as artifact data [RQ:5270]
    - As a [test case user](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#test-case-details-page), when I use Inflecta.ai, the quality of the content is more useful and of higher quality, to save me time improving the outputs manually [RQ:5268]

!!! bug "Bug fixes and enhancements"
    - Fix Inflectra.ai showing options on the [requirement details page](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#requirement-details-page) for creating tasks and risks, when using SpiraTest [IN:11040]
    - Hide Inflectra.ai buttons when the user does not have permissions to perform the particular API actions associated with the button [IN:10976]
    - Include the currently displayed risk mitigations in the information to AI when generating new mitigations [IN:10999]
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
        - As an Inflectra.ai and requirement user, I can use the Inflectra.ai side panel to generate tasks from a requirement [RQ:5216]
    
    - **[Test case details page](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#test-case-details-page)**
    
        - As an Inflectra.ai user, I can see the Inflectra.ai icon on test case details page, so I can access the AI features for a test case [RQ:5197]
        - As an Inflectra.ai and test case user, I can use the Inflectra.ai side panel to generate requirements from a test case [RQ:5220]
        - As an Inflectra.ai and test case user, I can use the Inflectra.ai side panel to generate test steps for a test case [RQ:5219]
    
    - **[Task details page](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#task-details-page)**
    
        - As an Inflectra.ai user, I can see the Inflectra.ai icon on task details page, so I can access the AI features for a task [RQ:5198]
        - As an Inflectra.ai and task user, I can use the Inflectra.ai side panel to generate sample code with tests for a task in a variety of languages [RQ:5222]
        - As an Inflectra.ai and task user, I can use the Inflectra.ai side panel to generate sample code for a task in a variety of languages [RQ:5221]

    - **[Risk details page](../Spira-User-Manual/Inflectra-Ai-In-Spira.md/#risk-details-page)**
    
        - As an Inflectra.ai user, I can see the Inflectra.ai icon on risk details page, so I can access the AI features for a risk [RQ:5199]
        - As an Inflectra.ai and risk user, I can use the Inflectra.ai side panel to generate risk mitigations for a risk [RQ:5223]
    
    - As an Inflectra.ai user, when I access the Inflectra.ai sidebar all text is localized for me, so I can interact with the sidebar in my preferred supported language [RQ:5232]