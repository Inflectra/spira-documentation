# Requirements

## How to create a requirement {: .section-break}
1. Select requirements from the "Artifact" dropdown on the global navigation bar
2. This will open the requirements list view
3. Click the "Insert" button from the toolbar. 
    
    - If you have no requirement selected then the new requirement is added at the bottom of the list (this will be on the last page if you have multiple pages of requirements)
    - If you have one requirement selected, the new requirement is added immediately above that requirement, as its sibling

4. Note that the dropdown for this button has two options and the second lets you insert a new requirement as a child of an existing requirement, if one is selected

## How to fix the requirement hierarchy {: .section-break}
Sometimes the requirement list will not look as you expect (on the main list view or in the sidebar when looking at a single requirement). Some nodes may be hidden that should be visible, or vice versa. This can happen due to the combination of expanding/collapsing different nodes / parent requirements, and filtering requirements by different fields. You can get this back to normal by doing the following:

1. Go to the requirements list view
2. Make sure you are looking at the hierarchy/tree view
3. At the top is a dropdown that says: "--- show level ---"
4. Select "All Levels" from the dropdown and wait for the page to reload (this resets any collapsing of requirements you may have done)
5. If applicable, clear any existing filter (hit the `Clear Filter` button above the table of requirements)


## Why does my requirement status change by itself {: .section-break}
Sometimes you may change the status of a requirement, then when you look at it again the status was the *old* status, not the new one you tried to change it to. What causes this?

1. As a product admin go to Product Admin > Planning > [Planning Options](../Spira-Administration-Guide/Product-Planning.md/#requirements)
2. Look at the [Requirements](../Spira-Administration-Guide/Product-Planning.md/#requirements) section
3. There are two options that can keep a requirement status stuck: "Use Task Status" and "Use Test Status".
4. If "Use Task Status" is enabled, a requirement will move to "developed" when all its tasks are complete (and cannot be moved to developed before that)
5. If "Use Test Status" is enabled, a developed requirement will move to "tested" when all its test cases have passed (and cannot be moved to tested before that)