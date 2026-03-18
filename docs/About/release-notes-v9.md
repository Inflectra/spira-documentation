# Release Notes for Spira v9

## Version 9.0 (April 2026)
!!! info "Summary"
    With version 9 of Spira, we have upgraded much of the behind-the-scenes plumbing to improve stability and performance across the application. It also provides a solid foundation for future innovation.

    System administrators can now opt to enforce that all users logging in with a username and password (including with LDAP) also log in using a 2-Step Authentication token.

??? success "New Features"
    - Upgrade core data access infrastructure to improve performance, stability, and maintainability [RQ:5594] [RQ:5595] [RQ:5596]
    - As a system admin, I can force users to only be able to login to the application if they have MFA setup, to meet our organization's security and compliance needs [RQ:5608]

??? bug "Bug fixes and enhancements"
    - Fix a bug with custom properties in graphs [IN:12318]
    - Documentation improvements [IN:7186] [IN:11730] [IN:12192] [IN:12252] [IN:12291] [IN:12327] [IN:12343] [IN:12371] [IN:12697] [IN:12398]
    - Fix a bug related to the Anti XSRF token error in Chrome under specific conditions [IN:11832]
    - Fix being unable to change the graph type view in some scenarios [IN:12300]
    - Fix being unable to filter requirements by "text field" in certain cases [IN:12359]
    - Fix endpoints being excluded from the OpenAPI documentation in edge cases [IN:12220]
    - Fix how history is recorded for test cases so that changes to the read-only "Test Steps" flag are recorded in history [IN:12004]
    - Fix left side artifact panel expansion not possible in some situations [IN:12249]
    - Fix login failure after email update for non-admin users [IN:12250]
    - Fix New Milestone page having no page title [IN:12314]
    - Fix non-admin users receiving an authorization error when attempting to delete an incident on the details page, even when they have the appropriate permissions [IN:12311]
    - Fix not being able to register an existing account to an external provider when 2-Step Authentication is enabled [IN:12386]
    - Fix the position of the follower card on artifact details pages [IN:12302]
    - Fix selection of invalid programs in planning boards [IN:12400]
    - Fix Test Execution window not fitting on the screen when there is a long description [IN:12247]
    - Fix Test Set Planned Date Calendar popup being obscured [IN:12405]
    - Fix the instant messenger occasionally showing messages in the wrong order [IN:12305]
    - Fix a bug in the My Subscribed Artifacts widget related to user permissions [IN:12006]
    - Rename Azure AD to Microsoft Entra ID throughout the application and documentation  [IN:12260] [IN:12259]