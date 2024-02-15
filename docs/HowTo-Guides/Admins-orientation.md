# Getting to Know Spira Administration
## How to know what, if anything, you are an admin of {: .section-break}
1. If you are an administrator then you will see three yellow cogs in the far right of the global navigation bar of the application (at the very top of the page)
2. You will always see these cogs if you are a system administrator because you can always access system administration
3. If you are a workspace admin (eg product or program) you will only see the cogs when you are on a workspace that you are an admin of
4. If you do not see the three cogs but think you may be an administrator, then it may be you do not have the correct workspace (product, program, etc)
5. You can quickly tell if you are an administrator of any workspace by opening the workspace selector from the global navigation bar. Look down the list of workspaces. You are an admin for anything in the list that shows a little cog at the end of the workspace name

## How to access the administration menu {: .section-break}
1. Clicking on the three cogs in the far right of the global navigation bar will bring up the administration menu. What it shows will vary based on where you are in the application
2. Once you click on one of the administration links you will open up the relevant administration page
3. When in administration you will still see those three cogs at the top right. You will also see a dark thin bar on the left hand side. Clicking this will open up an identical administration menu to clicking on the three cogs
4. Where relevant, one part of the administration menu may be highlighted. This shows you either the part you are currently on, or the part that most closely matches where you are in the application

## What are the different sections of administration {: .section-break}
You can read about the different types of administration [here](../Spira-Administration-Guide/System-Administration.md).

## Admin home pages {: .section-break}
1. Each administration section has a dedicated homepage. For workspaces or templates, these homepages change based on the current workspace
2. The administration home page gives you quick access to important information about that administration section through a series of homepage widgets
3. You can click on links in each of these widgets to dive into the detail as needed

## What happens when artifacts are deleted {: .section-break}
Users can only delete artifacts if their product role has the delete permission enable for that specific artifact. The exception to this is folders: users who have "Bulk Edit" permissions for the relevant artifact can also add, edit, and delete those artifacts folders.

- **Folder deletion**: Documents, Tasks, Test Cases, and Test Sets have folders. Deleting folders is permanent and cannot be undone

    - Document folders can only be deleted when they are empty
    - When deleting other folders (tasks, test cases, or test sets) any subfolders are also deleted. All contents of the folder and its subfolders are moved to the 'Root' folder.
    
- **Artifact deletion**: 

    - Deleting documents and test runs is permanent and cannot be undone
    - If any other artifact is deleted a log is kept and the deletion can be reverted.
    - To see all deleted artifact go to Product Administration > Product History Changes (only accessible to product admins). You can filter this list by the action type (i.e. deletes), and the artifact type.
    - You can see who deleted an artifact by clicking on it from the above page. This will show you more information about the delete
    - You can revert any delete by clicking the "Revert" button. 
    - Read more about product history [here](../../Spira-Administration-Guide/Product-General-Settings/#product-history-changes)

## How to add a new product {: .section-break}
Only system administrators can create new products in Spira.

1. Login as a system administrator and open the [system administration menu](#how-to-access-the-administration-menu)
2. Look for the "Workspaces" section and click the "View/Edit Products" link
3. This will open the "Product list" page
4. From here click the "Add" button at the bottom of the page and follow [these instructions](../../Spira-Administration-Guide/System-Workspaces/#add-a-new-product)

## How to add a new user {: .section-break}
There are two ways to add new users to Spira: a system administrator creates the user; or the user registers for a new account, which a system admin then approves. 

To create a new user directly:

1. Login as a system administrator and open the [system administration menu](#how-to-access-the-administration-menu)
2. Look for the "Users" section and click the "View/Edit Users" link
3. This will open the "User list" page
4. From here click the "Add" button at the bottom of the page and follow [these instructions](../../Spira-Administration-Guide/System-Users/#add-a-new-user)

For users to register for an account themselves:

1. Your security settings must [allow user registration](../../Spira-Administration-Guide/System/#security-settings) 
2. The prospective user should [register for a new account](../../Spira-User-Manual/User-Product-Management/#register-for-an-account)
3. Login as a system administrator and open the [system administration menu](#how-to-access-the-administration-menu)
4. Look for the "Users" section and click the "Pending Requests" link
5. Review any pending requests and approve them or not, as described [here](../../Spira-Administration-Guide/System-Users/#pending-requests)

## How to add a user to a product {: .section-break}
Only product or system administrators can add or remove a user from a product. When you add a user to a product you must give them a specific product role. This role gives them specific permissions. To add a user to a product:

1. Login as a system administrator or product administrator and open the [product administration menu](#how-to-access-the-administration-menu)
2. Look for the "Users" section and click the "Product Membership" link
3. This will open the "Product Membership" page.
4. From here follow these [instructions](../../Spira-Administration-Guide/Product-Users/#add-a-user-to-a-product) to add an existing user to that product by given them the correct role