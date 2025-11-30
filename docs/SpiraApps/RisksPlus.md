# Risks+ SpiraApp
!!! abstract "Compatible with SpiraTeam and SpiraPlan"

!!! warning "Some of this SpiraApp's functionality requires Spira v8.3+"

This SpiraApp extends the built-in risk functionality by:

- adding a "Move to Incident" button on the Risk details page 
- adding optional validation for the Risk Review Date field

!!! info "About this SpiraApp"
    - product settings 
    - runs automatically on the risk details page
    - adds a menu button to the risk details page

## Setup
### Product Settings
!!! warning "Checkbox settings require Spira 8.3"

Once the Risks+ SpiraApp has been activated system wide, and enabled for a product, there are two settings:

![Shows two settings. Moved to Incident Status: with a dropdown select, and Validate Risk Review Date?: with a blank text box](img/risksplus-settings.png)

- When moving a risk to an incident, the risk should be moved to a specific status. Pick the status the risk should get using the "Moved to Incident Status" dropdown. If left blank the risk status will not be changed.
- To restrict Risk Review dates so they must be before the Risk Closed date, check the "Validate Risk Review Date" setting (defaults to unchecked).

## Using the SpiraApp
### Risk Details Page
On the Risk Details page, you can press the Risks+ menu button and then **Move to Incident** to create an Incident based on this Risk. This will:

- Create a new incident based off the risk
- Copy the risk's name, description, owner, release, tags, component to this incident
- Set this incident to use the default status and the default type
- Update the risk's status based off the product setting[^1]
- Update the risk's probability to the highest one available (by score) 
- Create a "related-to" association between the new incident and the existing risk
- Create a comment on both the Risk and the new Incident, which includes the Artifact IDs and the date the incident was created 

When the "**Validate Risk Review Date**" product setting is enabled, any Risk that is saved must have a Review Date that comes before its Closed Date. If you save a Risk with a Review Date *after* its Closed Date, the Review Date will be automatically set to that of the Closed Date and a message will appear saying the previous value was invalid. Note that the overwritten Review Date will be shown in the Risk's History tab as the latest change, if you need to refer to it.

[^1]: If the product setting is empty, the SpiraApp will leave the status of the risk unchanged.