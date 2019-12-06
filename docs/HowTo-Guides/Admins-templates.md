# Template Administration
## What is a template? {: .section-break}
Read about the template workspace [here](../Spira-Administration-Guide/System-Administration.md).

## How to create a new template {: .section-break}
You cannot create a template by itself. You can only create a new template when creating a new product.

1. Log in as a system administrator
2. Go to `Administration` > `System` > `Workspace` > `View/Edit Products`
3. Click `Add` to add a new product
4. On the add product page you will see a `Template` field. From here you can select an existing template or `Create New Template`.
5. To create a brand new template select this `Create New Template` option
6. Click `Insert`

## How to clone a template {: .section-break}
To clone a template, you need to clone a product that uses the template you wish to clone

1. Log in as a system administrator
2. Go to `Administration` > `System` > `Workspace` > `View/Edit Products`
3. Find a product that is using the template you wish to clone
4. Click the `Clone` button on that product's row
5. In the popup that appears, make sure to select the option `Clone product and its template`
6. Click `Clone`
7. This will create a create a copy of the product and a full clone of the template

## How to move a product to a new template {: .section-break}
For more information about changing a product's template see [here](../Spira-Administration-Guide/Product-Changing-Template.md).

1. Log in as a system administrator
2. Go to `Administration` > `System` > `Workspace` > `View/Edit Products`
3. Find a product that is using the template you wish to move from one template to another
4. Click `Edit`
5. Click `Change Template`
6. Read the information in the dialog that pops up, then choose the template you wish to move to
7. Click `Next`
8. Read carefully the warnings shown on the next screen
9. If you are sure you want to change template follow the instructions


## How to split off a product from its template  {: .section-break}
If you have 2+ products using the same template, but decide 1 products needs slightly different template settings, you need to branch its template off into a brand new template. This is possible, but requires a few different steps to make it work smoothly.

1. Clone the existing template - following the steps [above](#how-to-clone-a-template)
2. Remember what product you cloned in this step (you will be deleting it later)
3. Move the product you wish to have different template settings to this new template - following the steps [here](how-to-move-a-product-to-a-new-template)
4. Go back and delete the product from step 2 above (you don't need it anymore and it will just create clutter)
5. You now have your product using a new template that is exactly the same as its original template
6. Start making the changes to this new template as needed