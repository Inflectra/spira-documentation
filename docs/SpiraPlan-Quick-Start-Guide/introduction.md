# Welcome to the SpiraPlan Quick Start Guide
In this guide we will learn about the different parts of the application, how to use them, and how they fit together. 

You don't need to know how to use the application already, and you don't need to be familiar with application management tools, or agile, or waterfall.

All you need to get started is the application itself.

## Introduction
!!! tip "You say SpiraTest, I say SpiraPlan"

    The SpiraPlan family of applications comes in 3 different editions:

    - SpiraTest
    - SpiraTeam, which is SpiraTest plus some extra features
    - SpiraPlan, which takes all the features of SpiraTeam and adds a few more

    Whatever flavor of Spira you have (we will say **"Spira"** from here on) you can use this Quick Start Guide. 

This Quick Start Guide is split into different parts. You can dip into any part you want. However, we recommend doing the parts in order. This will really let you see the power of how things connect together to help you meet your goals. However you approach it and whatever edition of Spira you have, there will be clear signposts and tips to guide you along the way.

### Guide to the Guide

``` mermaid
  flowchart LR
  id1(Overview) --> id2
  id2(Planning) --> id3 & id4
  id3(QA) --> id4
  id4(Tracking) --> id3

  style id1 fill:#fdcb26
```

## Application Overview

!!! info "What you will learn"

    - Logging in to the application
    - Your user profile
    - Workspaces (products and projects)
    - Artifacts (bugs, sprints, tests)


### Logging In to the application

You have a brand new SpiraPlan application ready to go. This is either in the cloud or on-premise. First, go to the home page of the application in your browser to get to the login page:

![](img/qsg-intro-login.png)

Login using the default admin account:

- **User Name**: administrator
- **Password**: PleaseChange

You are now logged-in and will see the "My Page". The My Page looks pretty empty right now. This is normal.

![](img/Logging_In_and_Selecting_a_Product_4.png)

The first time you log in you will see a popup that gives you a quick orientation of the application.

![](img/Logging_In_and_Selecting_a_Product_5.png)


### Your user profile

### Workspaces
For this tutorial we want to start with an empty product that has no data in it, so click the hyperlink under 'My Products' for 'Sample Empty Product 2' / 'Sample Program'. That will select the empty product. Now to see the homepage for the product you just selected, click on the hexagon in the top left:

![](img/Logging_In_and_Selecting_a_Product_6.png)

The product home page shows various widgets containing key product metrics. These are empty now, because the product has no data in it. In the rest of this guide we are going to fix that.

### Artifacts



# NOTES
## Structure
1. Planning (making stuff and linking)

- What are your major goals (req)
- Make some tasks for reqs (2 ways)
- Think about the risks
- Check your goals are being met with tests (TC - and link to RQ)
- Plan your time with sprints
- Map your work to sprints (add RQ to RL, TC to RL)

2. Doing the work (editing)

- Using the workflows on details pages - complete tasks, progress requirements (auto settings)
- Move other things around using planning boards

3. Checking your work (QA)

- QA your goals and find a bug (test execution)
- Triage your incidents

4. Big picture review

- Are you ready to launch? Using home pages
- Ideally 1 or 2 small issues outstanding - resolve
- Ready to release!

5. Advanced section:

- Test sets
- Test parameters
- Admin - planning
- Admin - make a product
- Admin - components
- Admin - custom properties

## Artifacts
Creates 16 in total, which is about half of the current QSG - seems about right

### Requirements
Prepare the spaceship rq1 [rl2]
> Pack my suitcase rq2 [rl2]
> Take the right amount of rocket fuel rq3 [rl2]
Get a cool spacesuit rq4 [rl3]

### Tasks
buy a LOT of snacks tk1 [rq2]
finalize flight path tk2 [rq3]
Book a spacesuite test fitting tk3 [rq4]
set 'out of office' before launch day tk4 [rl3]

### Risks
Fly right on past Mars rk1 [rq3]
Spaceship computer turns evil rk2 [rl3]
> Be its friend mitgitation1
> Know how to turn it off mitgitation2

### Test Cases
Verify suitcase is well packed tc1 [rq2, rl2]
Spaceship computer seems nice [rq1, rl2] 

### Releases
Build spaceship rl1 [already complete]
Prep for launch rl2 
Lift off rl3

### Incidents
There are too many snacks to fit in the suitcase in1 [tc1]
