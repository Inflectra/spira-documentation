# Requirements

## How to fix the requirement hierarchy {: .section-break}
Sometimes the requirement list will not look as you expect (on the main list view or in the sidebar when looking at a single requirement). Some nodes may be hidden that should be visible, or vice versa. This can happen due to the combination of expanding/collapsing different nodes / epics, and filtering requirements by different fields. You can get this back to normal by doing the following:

1. Go to the requirements list view
2. Make sure you are looking at the hierarchy/tree view
3. At the top is a dropdown that says: "--- show level ---"
4. Select "All Levels" from the dropdown and wait for the page to reload (this resets any collapsing of requirements you may have done)
5. If applicable, clear any existing filter (hit the `Clear Filter` button above the table of requirements)

## Why a requirement gets marked as an Epic {: .section-break}
You may wonder why a requirement has its type marked as "Epic" even though noone ever specifically changed its type to "Epic". You may also wonder why you can't change its type to anything other than "Epic" - its type is set to read only. Here is what is going on:

- The type "Epic" is a calculated type by the system. Any requirement that has any children automatically becomes an "Epic"
- If an "Epic" later loses all children, its type reverts back to what it was before it became an "Epic" 
- A requirement type helps control which workflow is applied to a requirement. However, for an "Epic" this is a mute point: you cannot manually change an "Epic" status, this is automatically set by the system based off of the combined statuses of the "Epic"'s children


## Why does my requirement status change by itself {: .section-break}
Sometimes you may change the status of a requirement, then when you look at it again the status was the *old* status, not the new one you tried to change it to. What causes this?

1. As a product admin go to Product Admin > Planning > [Planning Options](../../Spira-Administration-Guide/Product-Planning/#requirements)
2. Look at the [Requirements](../../Spira-Administration-Guide/Product-Planning/#requirements) section
3. There are two options that can keep a requirement status stuck: "Use Task Status" and "Use Test Status".
4. If "Use Task Status" is enabled, a requirement will move to "developed" when all its tasks are complete (and cannot be moved to developed before that)
5. If "Use Test Status" is enabled, a developed requirement will move to "tested" when all its test cases have passed (and cannot be moved to tested before that)