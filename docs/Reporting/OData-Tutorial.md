# OData Tutorial
## Introduction
[OData](https://en.wikipedia.org/wiki/Open_Data_Protocol) is an open protocol that lets you easily query data, over the web. Exclusive to SpiraPlan (6.9+), with OData you can directly query the raw data in your database in a secure and safe way. Whenever you use OData in SpiraPlan you are communicating through a secure intermediary (the application itself) to get data from read-only [reporting views](../Custom-Reporting-Tables). Tools like Excel, PowerBI, Tableau support OData and can therefore communicate with SpiraPlan to access this data with just a few clicks.

With OData you don't need to be a SQL expert to generate rich and dynamic insights into your data. If you can fiddle with a spreadsheet, you can stich tables of data from SpiraPlan ("joins" in database language) to get just the data you need. What sort of insights can you get with OData and SpiraPlan reporting views? Here are some examples:

- a pie chart of how many users are members of each of SpiraPlan's products
- a list of how long ago each open task was assigned to the current owner
- get the most recent test run for each test case against each requirement assigned to a sprint
- the top 5 most closed then reopened bugs in a product (or program)

In this tutorial series we will be using Excel and its built-in Power Query to communicate with SpiraPlan. Over this series we will build up to creating the final example listed above: a list of the most reopened bugs. This is not meant as a tutorial of Power Query itself, there are lots of those online. But if you don't know how to use Power Query don't worry, you will still be able to follow along

## Connecting Excel and SpiraPlan using OData
In the first tutorial you will learn how to: 

- connect Excel to SpiraPlan
- pick a table to explore (incidents in this case)
- filter incidents to those from just one product
- get rid of columns you don't need to make our data more readable
- get the data into Excel itself
- update the data directly from SpiraPlan without leaving Excel

### Who can use OData?
Not all SpiraPlan users can connect to OData to see live data. Access to OData lets you see all data across all products in your entire system - it is not restricted by product membership or product role permissions. Therefore you need to think carefully about who can and should have this read-only access.

Two types of users can use OData:

- system administrators
- report administrators

Each user can be one, both, or neither of these. Admins can turn these settings on or off in the admin user profile screens.

Before carrying on with this tutorial make sure you are either a system or report admin, are using SpiraPlan, and are on at least version 6.9.0.0.

### Connect Excel and SpiraPlan
Open Excel and find the Get Data > From OData Feed button. This should be in the Data ribbon, under Get Data > From Other Sources.

![Excel's From OData Feed menu location](img/odata-1.png)

Once you click this button you will see a popup. Stick with "Basic" and enter the special OData url for your SpiraPlan. This is the "base url" for your application with "api/odata" added at the end. If your site is at https://mycompany.spiraservice.net/ then your OData url will be https://mycompany.spiraservice.net/api/odata. Click OK.

![Entering your special OData Feed's url](img/odata-2.png)

Once Excel connects to SpiraPln you see a popup "Navigator" where you can see all the different data views you can access ("query"). There is a lot here and a lot to explore. You can access pretty much all the information in your application, across all its products and templates, from these views. But if you click on now to take a look you will not be able to see anything. That's because you have not authenticated yet with Spira. You have to authenticate to view this data for obvious security reasons.

To authenticate you need to pieces of information:

- username
- API-key (also called the RSS token)

You can find both of these on your Profile page in the application.

In Excel, the easiest way to add your authentication information is to click on one of the view names. It will fail, then show you a dialog box like this:

![Failed authentication popup](img/odata-3.png)

Click on "Basic" on the left, then fill it in as below and click Connect.

- User name: put your "username" here
- Password: put your "API-key here

![Completed authentication popup](img/odata-4.png)

### Viewing data
You should now see a preview of the table you clicked on. Here we are looking at incidents. You can see a few rows of data, not everything.

![Successful connection and data preview](img/odata-5.png)

To see all the data you have two options:

- **Load**: this loads the whole view, with all records, into a new Excel sheet in the current workbook
- **Transform Data**: this puts the data into Excel's Power Query so that you can manipulate the data that Spira sends to Excel

We will finish this first tutorial by clicking "Load". Your new sheet with Incident data in should look something like this...

![Incident data from Spira in Excel](img/odata-6.png)

You can now: connect Excel and Spira together using OData and view data from Spira live in Excel. In the next tutorial we will build a simple query to filter the data to just those parts we are interested in

## Writing your first query
In this tutorial you will learn how to use Excel's Power Query to filter down all the Incidents in your SpiraPlan application. You will end up with a list of incidents in a single product, sorted by priority. You do not need any coding or SQL skills - everything you do will feel very similar to how you normal use Excel itself.

To get started:

- connect SpiraPlan and Excel using the OData feed (explained in the previous tutorial)
- click on the Incidents view in the Excel Navigator (just as we did in the last tutorial)
- click Transform Data at the bottom of the Excel Navigator popup to load the Power Query interface
- NOTE: if you followed along with the last tutorial and "loaded" your data into an Excel sheet, look to the "Queries and Connections" sidebar on the right. Double click where it says **Incidents**, *xx rows loaded*.

The Power Query interface looks very similar to Excel

![Power Query Editor window](img/odata-7.png)

The Power Query Editor window is made up of:

- ribbons and buttons at the top
- a query (data) navigator on the left (this is collapsed in the above screenshot)
- the data for your current query. This is always a flat 2 dimensional list - each column is a certain field, and each row a record (in this example each row is an incident)
- query settings sidebar on the right. This is very useful and lets you see all the steps you took to change your query. You can also go back to see what the query looked like at an earlier stage

### Choose columns
To make the data easier to look at and filter, the first thing to do is get rid of columns we don't need. Ther are well over 100 columns (because of all the custom fields we include) and that is way too many.

Click on the "Choose Columns" button from the Home ribbon. Only select the following columns (make sure the rest are unchecked), and then click OK

- INCIDENT_ID
- PROJECT_NAME
- PRIORITY_NAME
- NAME

You should now see a table of data like the one below. We are showing all the records still, but only 4 columns. The query settings sidebar has an extra line at the end that says "Removed Other Columns." This is what we just did. You can undo the action by deleting it from the sidebar, or change which columns to show by double clicking on it.

![Choosing columns](img/odata-8.png)

### Filtering data
Just like when filtering data on a sheet, the column names have dropdown arrows to open the filtering popup. 

- Click on the arrow in the PROJECT_NAME column header. Select just one product. In the screenshot below we are going to only show incidents for "Library Information System"
- Click OK

You have filtered your data! That's all there is to it. It is really easy. What is cool, is that we are not hiding rows of our table like we do in Excel normally. We are actually changing the query we are sending to SpiraPlan so that SpiraPlan is only sending us the information we have asked for.

![Filtering the PROJECT_NAME column](img/odata-9.png)

Let's filter again. This time filter on the PRIORITY_NAME column. Below we are filtering to only get data for "1 - Critical". We have gone from getting 60 rows to only now getting 14 rows. You can see below we have a new entry in the list of Applied Steps in the right hand sidebar - for our Filtering Rows work.

![Filtering the PRIORITY_NAME column](img/odata-10.png)

### Sorting data
Sorting data is just as easy as filtering data. Click on the dropdown arrow for the column you want to sort by and click "Sort Ascending" or "Sort Descending". That's all there is to it. You can, if you want, sort by multiple columns at once. In the example below, we are sorting ascending by the NAME column. Again, there is a new entry in the list of Applied Steps in the right hand sidebar - for our Sorting Rows.

![Sorting the NAME column](img/odata-11.png)

Hopefully, this feels very straightforward, because it is. In the background Excel is creating the right OData query to send to SpiraPlan, which is then writing a secure query to the database to get just the data you need. But you don't need to think about any of that.

In the next tutorial we are going to try another query with incidents and make things more complicated by combining data across two tables at once.

## Combining two lots of data
take the above and combine it with statuses to pick just those that are open (can use the open flag for this but this is another way)

## Building complex queries
Incidents combined with history and a join on open incidents. Filter on history so that old value is only a closed status. Group by and show id, name, owner, count. 
Sort by count and limit to the top X

## Making your queries more dynamic
repeat the above but use a query on statuses to work out which ones are open