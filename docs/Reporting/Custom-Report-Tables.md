# Available Custom Reports Tables
!!! info "How to use this page"
    Spira has a number of database views available for creating custom reports using ESQL queries. Below, each available table is listed with all of their exact field names. 

    Many tables have a single field shown in *italic* - these are the Primary Keys for that table, which means that field can be used as the unique identifier for each row of data. 

## Artifact Associations
| R_ArtifactAssociations    |
| ------------------------- |
| ARTIFACT_LINK_TYPE_ID     |
| SOURCE_ARTIFACT_ID        |
| SOURCE_ARTIFACT_TYPE_ID   |
| DEST_ARTIFACT_ID          |
| DEST_ARTIFACT_TYPE_ID     |
| CREATOR_ID                |
| CREATION_DATE             |
| COMMENT                   |
| SOURCE_ARTIFACT_TYPE_NAME |
| DEST_ARTIFACT_TYPE_NAME   |
| CREATOR_NAME              |
| ARTIFACT_LINK_TYPE_NAME   |

## Artifact Associations - Extended
For normal use we strongly recommend using the standard artifact association view above. This extended view adds the artifact names, which can be very helpful, but will make the reports using it run much slower. 

| R_ArtifactAssociationExtended |
| ----------------------------- |
| ARTIFACT_LINK_TYPE_ID         |
| SOURCE_ARTIFACT_ID            |
| SOURCE_ARTIFACT_TYPE_ID       |
| DEST_ARTIFACT_ID              |
| DEST_ARTIFACT_TYPE_ID         |
| CREATOR_ID                    |
| CREATION_DATE                 |
| COMMENT                       |
| SOURCE_ARTIFACT_TYPE_NAME     |
| DEST_ARTIFACT_TYPE_NAME       |
| CREATOR_NAME                  |
| ARTIFACT_LINK_TYPE_NAME       |
| SOURCE_ARTIFACT_NAME          |
| DEST_ARTIFACT_NAME            |

## Artifact Attachments
| R_ArtifactAttachments |
| --------------------- |
| ARTIFACT_TYPE_ID      |
| ARTIFACT_ID           |
| ARTIFACT_TYPE_NAME    |
| ARTIFACT_NAME         |
| COMMENT               |
| CREATOR_ID            |
| CREATION_DATE         |
| CREATOR_NAME          |
| ATTACHMENT_ID         |
| PROJECT_ID            |
| ARTIFACT_STATUS_NAME  |

## Artifact Tags
| R_ArtifactTags     |
| ------------------ |
| ARTIFACT_ID        |
| ARTIFACT_TYPE_ID   |
| TAGS               |
| PROJECT_ID         |
| PROJECT_NAME       |
| ARTIFACT_TYPE_NAME |

## Artifact Types
| R_ArtifactTypes    |
| ------------------ |
| *ARTIFACT_TYPE_ID* |
| NAME               |
| PREFIX             |

## Attachments
| R_Attachments                  |
| ------------------------------ |
| *ATTACHMENT_ID*                |
| ATTACHMENT_TYPE_ID             |
| AUTHOR_ID                      |
| EDITOR_ID                      |
| FILENAME                       |
| DESCRIPTION                    |
| UPLOAD_DATE                    |
| EDITED_DATE                    |
| SIZE                           |
| CURRENT_VERSION                |
| PROJECT_ID                     |
| PROJECT_ATTACHMENT_FOLDER_ID   |
| CONCURRENCY_DATE               |
| DOCUMENT_STATUS_ID             |
| DOCUMENT_TYPE_ID               |
| DOCUMENT_STATUS_NAME           |
| DOCUMENT_TYPE_NAME             |
| TAGS                           |
| CUST_01...                     |
| CUST_99                        |
| IS_KEY_DOCUMENT                |
| DOCUMENT_STATUS_IS_OPEN_STATUS |
| PROJECT_IS_ACTIVE              |
| PROJECT_GROUP_ID               |
| PROJECT_NAME                   |
| AUTHOR_NAME                    |
| EDITOR_NAME                    |
| ATTACHMENT_TYPE_NAME           |
| PROJECT_ATTACHMENT_FOLDER_NAME |

## Attachment Folders
| R_AttachmentFolders                 |
| ----------------------------------- |
| *PROJECT_ATTACHMENT_FOLDER_ID*      |
| PROJECT_ID                          |
| PARENT_PROJECT_ATTACHMENT_FOLDER_ID |
| NAME                                |
| PROJECT_NAME                        |
| PROJECT_GROUP_ID                    |

## Attachment Versions
| R_AttachmentVersions    |
| ----------------------- |
| *ATTACHMENT_VERSION_ID* |
| ATTACHMENT_ID           |
| AUTHOR_ID               |
| FILENAME                |
| DESCRIPTION             |
| UPLOAD_DATE             |
| SIZE                    |
| VERSION_NUMBER          |
| IS_CURRENT              |
| CHANGESET_ID            |
| AUTHOR_NAME             |
| ATTACHMENT_TYPE_ID      |
| PROJECT_ID              |

## Automation Hosts
| R_AutomationHosts    |
| -------------------- |
| *AUTOMATION_HOST_ID* |
| PROJECT_ID           |
| NAME                 |
| DESCRIPTION          |
| TOKEN                |
| LAST_UPDATE_DATE     |
| IS_DELETED           |
| CUST_01...           |
| CUST_99              |
| PROJECT_NAME         |
| PROJECT_GROUP_ID     |
| IS_ACTIVE            |
| IS_ATTACHMENTS       |
| CONCURRENCY_DATE     |
| LAST_CONTACT_DATE    |

## Baselines
See [this KB](https://www.inflectra.com/Support/KnowledgeBase/KB550.aspx) for some examples of using this custom report table

| R_Baselines             |
| ----------------------- |
| *BASELINE_ID*           |
| PROJECT_ID              |
| CREATOR_USER_ID         |
| CHANGESET_ID            |
| RELEASE_ID              |
| NAME                    |
| DESCRIPTION             |
| IS_ACTIVE               |
| IS_APPROVED             |
| IS_DELETED              |
| CREATION_DATE           |
| LAST_UPDATE_DATE        |
| CONCURRENCY_DATE        |
| BASELINE_CREATOR_LOGIN  |
| CHANGESET_CREATOR_ID    |
| CHANGESET_CREATOR_LOGIN |
| ARTIFACT_TYPE_ID        |
| ARTIFACT_TYPE_NAME      |
| CHANGESET_DATE          |
| CHANGESET_TYPE_ID       |
| CHANGESET_TYPE_NAME     |

## Builds
Note that BUILD_STATUS_ID can have the following values: 1 = Failed, 2 = Succeeded, 3 = Unstable, 4 = Aborted.

| R_Builds        |
| --------------- |
| *BUILD_ID*      |
| BUILD_STATUS_ID |
| RELEASE_ID      |
| PROJECT_ID      |
| NAME            |
| DESCRIPTION     |

## Build Statuses
| R_BuildStatuses |
| --------------- |
| BUILD_STATUS_ID |
| NAME            |
| IS_ACTIVE       |

## Capabilities
| R_ProjectGroup_Capabilities |
| --------------------------- |
| *CAPABILITY_ID*             |
| PROJECT_GROUP_ID            |
| MILESTONE_ID                |
| STATUS_ID                   |
| TYPE_ID                     |
| PRIORITY_ID                 |
| NAME                        |
| DESCRIPTION                 |
| IS_DELETED                  |
| PERCENT_COMPLETE            |
| PROJECT_REQUIREMENT_COUNT   |
| INDENT_LEVEL                |
| CONCURRENCY_GUID            |
| CREATOR_ID                  |
| OWNER_ID                    |
| CREATION_DATE               |
| LAST_UPDATED_DATE           |
| IS_SUMMARY                  |
| STATUS_NAME                 |
| STATUS_IS_OPEN              |
| TYPE_NAME                   |
| PRIORITY_NAME               |
| PRIORITY_COLOR              |
| PRIORITY_SCORE              |
| MILESTONE_NAME              |
| CREATOR_NAME                |
| OWNER_NAME                  |
| PROJECT_GROUP_NAME          |
| CUST_01...                  |
| CUST_30                     |

## Capability Priorities
| R_ProjectGroup_Capability_Priorities |
| ------------------------------------ |
| *PRIORITY_ID*                        |
| NAME                                 |
| COLOR                                |
| IS_ACTIVE                            |
| IS_DELETED                           |
| SCORE                                |

## Capability Requirement Associations
| R_ProjectGroup_Capability_Project_Requirements |
| ---------------------------------------------- |
| CAPABILITY_ID                                  |
| REQUIREMENT_ID                                 |
| ARTIFACT_LINK_TYPE_ID                          |
| CAPABILITY_NAME                                |
| REQUIREMENT_NAME                               |
| ARTIFACT_LINK_TYPE_NAME                        |

## Capability Statuses
| R_ProjectGroup_Capability_Statuses |
| ---------------------------------- |
| *STATUS_ID*                        |
| NAME                               |
| POSITION                           |
| IS_ACTIVE                          |
| IS_DELETED                         |
| IS_DEFAULT                         |
| IS_OPEN                            |
| ON_BOARD                           |

## Capability Types
| R_ProjectGroup_Capability_Types |
| ------------------------------- |
| *TYPE_ID*                       |
| NAME                            |
| IS_ACTIVE                       |
| IS_DELETED                      |
| IS_DEFAULT                      |

## Comments
| R_Comments         |
| ------------------ |
| ARTIFACT_TYPE_ID   |
| ARTIFACT_ID        |
| CREATOR_ID         |
| COMMENT_TEXT       |
| CREATION_DATE      |
| CREATOR_NAME       |
| ARTIFACT_TYPE_NAME |


## Components
| R_Components     |
| ---------------- |
| *COMPONENT_ID*   |
| PROJECT_ID       |
| NAME             |
| IS_DELETED       |
| IS_ACTIVE        |
| PROJECT_NAME     |
| PROJECT_GROUP_ID |

## Custom Lists
| R_CustomLists             |
| ------------------------- |
| *CUSTOM_PROPERTY_LIST_ID* |
| PROJECT_ID                |
| NAME                      |
| IS_ACTIVE                 |
| IS_SORTED_ON_VALUE        |
| PROJECT_NAME              |
| PROJECT_IS_ACTIVE         |
| PROJECT_TEMPLATE_ID       |

## Custom List Values
| R_CustomListValues                |
| --------------------------------- |
| *CUSTOM_PROPERTY_VALUE_ID*        |
| CUSTOM_PROPERTY_LIST_ID           |
| NAME                              |
| PROJECT_ID                        |
| CUSTOM_PROPERTY_LIST_NAME         |
| CUSTOM_PROPERTY_LIST_IS_ACTIVE    |
| PROJECT_NAME                      |
| PROJECT_IS_ACTIVE                 |
| IS_ACTIVE                         |
| IS_DELETED                        |
| DEPENDENT_CUSTOM_PROPERTY_LIST_ID |
| PARENT_CUSTOM_PROPERTY_VALUE_ID   |

## Custom Property Definitions
| R_CustomPropertyDefinitions  |
| ---------------------------- |
| *CUSTOM_PROPERTY_ID*         |
| CUSTOM_PROPERTY_TYPE_ID      |
| PROJECT_ID                   |
| ARTIFACT_TYPE_ID             |
| NAME                         |
| PROPERTY_NUMBER              |
| IS_DELETED                   |
| CUSTOM_PROPERTY_LIST_ID      |
| LEGACY_NAME                  |
| PROJECT_NAME                 |
| PROJECT_IS_ACTIVE            |
| ARTIFACT_TYPE_NAME           |
| CUSTOM_PROPERTY_TYPE_NAME    |
| CUSTOM_PROPERTY_LIST_NAME    |
| DEPENDENT_CUSTOM_PROPERTY_ID |
| PROJECT_TEMPLATE_ID          |

## Document Statuses
| R_DocumentStatuses    |
| --------------------- |
| *DOCUMENT_STATUS_ID*  |
| PROJECT_TEMPLATE_ID   |
| NAME                  |
| POSITION              |
| IS_ACTIVE             |
| IS_OPEN_STATUS        |
| IS_DEFAULT            |
| PROJECT_TEMPLATE_NAME |

## Document Types
| R_DocumentTypes       |
| --------------------- |
| *DOCUMENT_TYPE_ID*    |
| PROJECT_TEMPLATE_ID   |
| DOCUMENT_WORKFLOW_ID  |
| NAME                  |
| DESCRIPTION           |
| IS_ACTIVE             |
| IS_DEFAULT            |
| PROJECT_TEMPLATE_NAME |

## Events
| R_Events                 |
| ------------------------ |
| EVENT_TYPE_ID            |
| EVENT_TIME_UTC           |
| EVENT_TIME               |
| EVENT_CATEGORY           |
| EVENT_SEQUENCE           |
| EVENT_OCCURRENCE         |
| EVENT_CODE               |
| EVENT_DETAIL_CODE        |
| MESSAGE                  |
| APPLICATION_PATH         |
| APPLICATION_VIRTUAL_PATH |
| MACHINE_NAME             |
| REQUEST_URL              |
| EXCEPTION_TYPE           |
| DETAILS                  |
| EVENT_TYPE_NAME          |

## Global / System Custom Property Definitions
| R_GlobalCustomPropertyDefinitions |
| --------------------------------- |
| *CUSTOM_PROPERTY_ID*              |
| CUSTOM_PROPERTY_TYPE_ID           |
| CUSTOM_PROPERTY_TYPE_NAME         |
| WORKSPACE_TYPE_ID                 |
| WORKSPACE_TYPE_NAME               |
| NAME                              |
| PROPERTY_NUMBER                   |
| IS_DELETED                        |
| CUSTOM_PROPERTY_LIST_ID           |
| CUSTOM_PROPERTY_LIST_NAME         |
| POSITION                          |
| DESCRIPTION                       |

## Global / System Custom Property Lists
| R_GlobalCustomLists       |
| ------------------------- |
| *CUSTOM_PROPERTY_LIST_ID* |
| NAME                      |
| IS_ACTIVE                 |
| IS_SORTED_ON_VALUE        |

## Global / System Custom Property List Values
| R_GlobalCustomListValues       |
| ------------------------------ |
| *CUSTOM_PROPERTY_VALUE_ID*     |
| NAME                           |
| IS_ACTIVE                      |
| IS_DELETED                     |
| CUSTOM_PROPERTY_LIST_ID        |
| CUSTOM_PROPERTY_LIST_NAME      |
| CUSTOM_PROPERTY_LIST_IS_ACTIVE |

## Global / System History Change-Sets
| R_Global_HistoryChangeSets |
| -------------------------- |
| *CHANGESET_ID*             |
| USER_ID                    |
| CHANGE_DATE                |
| CHANGETYPE_ID              |
| ARTIFACT_TYPE_ID           |
| ARTIFACT_ID                |
| ARTIFACT_DESC              |
| WORKSPACE_TYPE_ID          |
| WORKSPACE_ID               |
| CHANGETYPE_NAME            |
| USER_NAME                  |
| ARTIFACT_TYPE_NAME         |
| WORKSPACE_TYPE_NAME        |

## Global / System History Details
| R_Global_HistoryDetails |
| ----------------------- |
| *ARTIFACT_HISTORY_ID*   |
| FIELD_NAME              |
| OLD_VALUE               |
| NEW_VALUE               |
| CHANGESET_ID            |
| FIELD_TYPE_ID           |
| CUSTOM_PROPERTY_ID      |
| ARTIFACT_ID             |
| USER_ID                 |
| ARTIFACT_TYPE_ID        |
| CHANGE_DATE             |
| USER_NAME               |
| CHANGE_NAME             |
| CHANGETYPE_ID           |
| ARTIFACT_FIELD_TYPE_ID  |
| ARTIFACT_TYPE_NAME      |

## History Change-Sets
| R_HistoryChangeSets |
| ------------------- |
| *CHANGESET_ID*      |
| USER_ID             |
| ARTIFACT_TYPE_ID    |
| ARTIFACT_ID         |
| CHANGE_DATE         |
| CHANGETYPE_ID       |
| PROJECT_ID          |
| REVERT_ID           |
| ARTIFACT_DESC       |
| CHANGETYPE_NAME     |
| USER_NAME           |
| ARTIFACT_TYPE_NAME  |
| SIGNATURE_HASH      |
| MEANING             |

## History Details
| R_HistoryDetails   |
| ------------------ |
| FIELD_NAME         |
| OLD_VALUE          |
| FIELD_CAPTION      |
| NEW_VALUE          |
| OLD_VALUE_INT      |
| OLD_VALUE_DATE     |
| NEW_VALUE_INT      |
| NEW_VALUE_DATE     |
| CHANGESET_ID       |
| FIELD_ID           |
| CUSTOM_PROPERTY_ID |
| ARTIFACT_ID        |
| USER_ID            |
| ARTIFACT_TYPE_ID   |
| CHANGE_DATE        |
| CHANGER_NAME       |
| CHANGE_NAME        |
| CHANGETYPE_ID      |

## Incidents
| R_Incidents                     |
| ------------------------------- |
| *INCIDENT_ID*                   |
| PROJECT_ID                      |
| PRIORITY_ID                     |
| SEVERITY_ID                     |
| INCIDENT_STATUS_ID              |
| INCIDENT_TYPE_ID                |
| OPENER_ID                       |
| OWNER_ID                        |
| DESCRIPTION                     |
| CREATION_DATE                   |
| CLOSED_DATE                     |
| LAST_UPDATE_DATE                |
| DETECTED_RELEASE_ID             |
| RESOLVED_RELEASE_ID             |
| START_DATE                      |
| COMPLETION_PERCENT              |
| ESTIMATED_EFFORT                |
| ACTUAL_EFFORT                   |
| REMAINING_EFFORT                |
| PROJECTED_EFFORT                |
| IS_DELETED                      |
| VERIFIED_RELEASE_ID             |
| PRIORITY_NAME                   |
| PRIORITY_COLOR                  |
| SEVERITY_NAME                   |
| SEVERITY_COLOR                  |
| INCIDENT_STATUS_NAME            |
| INCIDENT_TYPE_NAME              |
| OPENER_NAME                     |
| OWNER_NAME                      |
| DETECTED_RELEASE_VERSION_NUMBER |
| RESOLVED_RELEASE_VERSION_NUMBER |
| VERIFIED_RELEASE_VERSION_NUMBER |
| PROJECT_GROUP_ID                |
| PROJECT_NAME                    |
| CUST_01...                      |
| CUST_99                         |
| NAME                            |
| IS_ATTACHMENTS                  |
| COMPONENT_IDS                   |
| INCIDENT_STATUS_IS_OPEN_STATUS  |
| PROJECT_IS_ACTIVE               |
| INCIDENT_TYPE_IS_ISSUE          |
| INCIDENT_TYPE_IS_RISK           |
| CONCURRENCY_DATE                |
| RANK                            |
| END_DATE                        |
| DETECTED_BUILD_ID               |
| RESOLVED_BUILD_ID               |
| DETECTED_BUILD_NAME             |
| RESOLVED_BUILD_NAME             |
| TAGS                            |

## Incident Priorities
| R_IncidentPriorities  |
| --------------------- |
| *PRIORITY_ID*         |
| PROJECT_TEMPLATE_ID   |
| NAME                  |
| COLOR                 |
| IS_ACTIVE             |
| SCORE                 |
| PROJECT_TEMPLATE_NAME |

## Incident Severities
| R_IncidentSeverities  |
| --------------------- |
| *SEVERITY_ID*         |
| PROJECT_TEMPLATE_ID   |
| NAME                  |
| COLOR                 |
| IS_ACTIVE             |
| SCORE                 |
| PROJECT_TEMPLATE_NAME |

## Incident Statuses
| R_IncidentStatuses    |
| --------------------- |
| *INCIDENT_STATUS_ID*  |
| PROJECT_TEMPLATE_ID   |
| NAME                  |
| IS_ACTIVE             |
| IS_OPEN_STATUS        |
| IS_DEFAULT            |
| PROJECT_TEMPLATE_NAME |

## Incident Types
| R_IncidentTypes       |
| --------------------- |
| *INCIDENT_TYPE_ID*    |
| PROJECT_TEMPLATE_ID   |
| WORKFLOW_ID           |
| NAME                  |
| IS_ACTIVE             |
| IS_ISSUE              |
| IS_DEFAULT            |
| PROJECT_TEMPLATE_NAME |

## Pending Test Runs
| R_PendingTestRuns      |
| ---------------------- |
| *TEST_RUNS_PENDING_ID* |
| PROJECT_ID             |
| TEST_SET_ID            |
| TESTER_ID              |
| NAME                   |
| CREATION_DATE          |
| LAST_UPDATE_DATE       |
| COUNT_PASSED           |
| COUNT_FAILED           |
| COUNT_BLOCKED          |
| COUNT_CAUTION          |
| COUNT_NOT_RUN          |
| COUNT_NOT_APPLICABLE   |
| TESTER_LOGIN           |
| TESTER_FULLNAME        |
| TEST_SET_NAME          |
| PROJECT_NAME           |

## Portfolios
| R_Portfolios      |
| ----------------- |
| *PORTFOLIO_ID*    |
| NAME              |
| DESCRIPTION       |
| IS_ACTIVE         |
| START_DATE        |
| END_DATE          |
| PERCENT_COMPLETE  |
| REQUIREMENT_COUNT |

## Program Milestones
| R_ProjectGroup_Milestones       |
| ------------------------------- |
| *PROJECT_GROUP_MILESTONE_ID*    |
| PROJECT_GROUP_ID                |
| TYPE_ID                         |
| STATUS_ID                       |
| NAME                            |
| DESCRIPTION                     |
| IS_DELETED                      |
| START_DATE                      |
| END_DATE                        |
| PERCENT_COMPLETE                |
| CHILDREN_START_DATE             |
| CHILDREN_END_DATE               |
| PROJECT_RELEASE_COUNT           |
| PROJECT_GROUP_REQUIREMENT_COUNT |
| CONCURRENCY_GUID                |
| CREATOR_ID                      |
| OWNER_ID                        |
| CREATION_DATE                   |
| LAST_UPDATED_DATE               |
| STATUS_NAME                     |
| STATUS_IS_OPEN                  |
| TYPE_NAME                       |
| CREATOR_NAME                    |
| OWNER_NAME                      |
| PROJECT_GROUP_NAME              |
| CUST_01...                      |
| CUST_30                         |

## Program Milestone Releases
| R_ProjectGroup_Milestone_Project_Releases |
| ----------------------------------------- |
| *PROJECT_GROUP_MILESTONE_ID*              |
| RELEASE_ID                                |
| ARTIFACT_LINK_TYPE_ID                     |
| PROJECT_GROUP_MILESTONE_NAME              |
| RELEASE_NAME                              |
| ARTIFACT_LINK_TYPE_NAME                   |

## Program Milestone Statuses
| R_ProjectGroup_Milestone_Statuses |
| --------------------------------- |
| *STATUS_ID*                       |
| NAME                              |
| IS_ACTIVE                         |
| IS_DELETED                        |
| IS_DEFAULT                        |
| IS_OPEN                           |

## Program Milestone Types
| R_ProjectGroup_Milestone_Types |
| ------------------------------ |
| *TYPE_ID*                      |
| NAME                           |
| IS_ACTIVE                      |
| IS_DELETED                     |
| IS_DEFAULT                     |

## Project Artifacts Sharing 
Retrieves data about cross product associations

| R_ProjectArtifactSharings |
| ------------------------- |
| SOURCE_PROJECT_ID         |
| DEST_PROJECT_ID           |
| ARTIFACT_TYPE_ID          |
| SOURCE_PROJECT_NAME       |
| DEST_PROJECT_NAME         |
| ARTIFACT_TYPE_NAME        |
| ARTIFACT_TYPE_PREFIX      |

## Projects (Products)
| R_Projects                  |
| --------------------------- |
| *PROJECT_ID*                |
| PROJECT_GROUP_ID            |
| NAME                        |
| DESCRIPTION                 |
| CREATION_DATE               |
| WEBSITE                     |
| WORKING_HOURS               |
| WORKING_DAYS                |
| NON_WORKING_HOURS           |
| TASK_DEFAULT_EFFORT         |
| PROJECT_GROUP_NAME          |
| PROJECT_GROUP_DESCRIPTION   |
| IS_ACTIVE                   |
| IS_TIME_TRACK_INCIDENTS     |
| IS_TIME_TRACK_TASKS         |
| IS_EFFORT_INCIDENTS         |
| IS_EFFORT_TASKS             |
| IS_TASKS_AUTO_CREATE        |
| REQ_DEFAULT_ESTIMATE        |
| REQ_POINT_EFFORT            |
| IS_REQ_STATUS_BY_TASKS      |
| IS_REQ_STATUS_BY_TEST_CASES |
| IS_EFFORT_TEST_CASES        |
| IS_REQ_STATUS_AUTO_PLANNED  |
| PROJECT_TEMPLATE_ID         |
| START_DATE                  |
| END_DATE                    |
| PERCENT_COMPLETE            |
| REQUIREMENT_COUNT           |
| CUST_01...                  |
| CUST_30                     |

## Project Groups (Programs)
| R_ProjectGroups     |
| ------------------- |
| *PROJECT_GROUP_ID*  |
| NAME                |
| DESCRIPTION         |
| WEBSITE             |
| PROJECT_TEMPLATE_ID |
| IS_ACTIVE           |
| IS_DEFAULT          |
| PERCENT_COMPLETE    |
| START_DATE          |
| END_DATE            |
| PORTFOLIO_ID        |
| REQUIREMENT_COUNT   |

## Project Group Membership (Program Membership)
| R_ProjectGroup_MembershipUsers |
| ------------------------------ |
| PROJECT_GROUP_ID               |
| PROJECT_GROUP_NAME             |
| PROJECT_GROUP_IS_ACTIVE        |
| PROJECT_GROUP_ROLE_ID          |
| PROJECT_GROUP_ROLE_NAME        |
| PROJECT_GROUP_ROLE_ISACTIVE    |
| USER_ID                        |
| USER_NAME                      |
| USER_FULLNAME                  |

## Project (Product) Membership
| R_ProjectMembership |
| ------------------- |
| PROJECT_ID          |
| USER_ID             |
| PROJECT_ROLE_ID     |
| PROJECT_NAME        |
| PROJECT_ROLE_NAME   |
| USER_NAME           |
| FIRST_NAME          |
| LAST_NAME           |
| DEPARTMENT          |
| IS_SYSTEM_ADMIN     |

## Project Release Resources
| R_ProjectReleaseResources |
| ------------------------- |
| PROJECT_ID                |
| USER_ID                   |
| RELEASE_ID                |
| INCIDENT_EFFORT           |
| TASK_EFFORT               |

## Project Roles
| R_ProjectRoles           |
| ------------------------ |
| *PROJECT_ROLE_ID*        |
| NAME                     |
| IS_ACTIVE                |
| DESCRIPTION              |
| IS_ADMIN                 |
| IS_DISCUSSIONS_ADD       |
| IS_SOURCE_CODE_VIEW      |
| IS_SOURCE_CODE_EDIT      |
| IS_DOCUMENT_FOLDERS_EDIT |
| IS_LIMITED_VIEW          |
| IS_TEMPLATE_ADMIN        |
| ARTIFACT_TYPE_ID         |
| ARTIFACT                 |
| PERMISSION               |

## Project (Product) Tags
| R_ProjectTags |
| ------------- |
| PROJECT_ID    |
| TAG           |
| PROJECT_NAME  |

## Project Teams Users
| R_Project_Team_Users |
| -------------------- |
| PROJECT_ID           |
| PROJECT_NAME         |
| USER_ID              |
| USER_NAME            |
| TEAM_ID              |
| TEAM_NAME            |

## Project (Product) Templates
| R_ProjectTemplates    |
| --------------------- |
| *PROJECT_TEMPLATE_ID* |
| NAME                  |
| DESCRIPTION           |
| IS_ACTIVE             |

## Releases
| R_Releases               |
| ------------------------ |
| *RELEASE_ID*             |
| PROJECT_ID               |
| CREATOR_ID               |
| NAME                     |
| VERSION_NUMBER           |
| DESCRIPTION              |
| INDENT_LEVEL             |
| CREATION_DATE            |
| LAST_UPDATE_DATE         |
| START_DATE               |
| END_DATE                 |
| RESOURCE_COUNT           |
| DAYS_NON_WORKING         |
| PLANNED_EFFORT           |
| AVAILABLE_EFFORT         |
| COUNT_BLOCKED            |
| COUNT_CAUTION            |
| COUNT_FAILED             |
| COUNT_NOT_APPLICABLE     |
| COUNT_NOT_RUN            |
| COUNT_PASSED             |
| TASK_COUNT               |
| TASK_PERCENT_ON_TIME     |
| TASK_PERCENT_LATE_FINISH |
| TASK_PERCENT_NOT_START   |
| TASK_PERCENT_LATE_START  |
| TASK_ESTIMATED_EFFORT    |
| TASK_ACTUAL_EFFORT       |
| TASK_PROJECTED_EFFORT    |
| TASK_REMAINING_EFFORT    |
| IS_DELETED               |
| CREATOR_NAME             |
| FULL_NAME                |
| PROJECT_NAME             |
| PROJECT_GROUP_ID         |
| CUST_01...               |
| CUST_99                  |
| RELEASE_TYPE_ID          |
| RELEASE_STATUS_ID        |
| OWNER_ID                 |
| IS_SUMMARY               |
| IS_ATTACHMENTS           |
| OWNER_NAME               |
| RELEASE_TYPE_NAME        |
| RELEASE_STATUS_NAME      |
| CONCURRENCY_DATE         |
| MILESTONE_ID             |
| PERCENT_COMPLETE         |
| PLANNED_POINTS           |
| REQUIREMENT_POINTS       |
| REQUIREMENT_COUNT        |
| TAGS                     |

## Release Test Case Mapping
| R_ReleaseTestCases     |
| ---------------------- |
| RELEASE_ID             |
| TEST_CASE_ID           |
| RELEASE_NAME           |
| RELEASE_VERSION_NUMBER |
| TEST_CASE_NAME         |
| PROJECT_ID             |
| PROJECT_NAME           |
| RELEASE_TYPE_ID        |
| RELEASE_TYPE_NAME      |
| EXECUTION_STATUS_ID    |
| EXECUTION_DATE         |
| ACTUAL_DURATION        |

## Requirements
| R_Requirements           |
| ------------------------ |
| *REQUIREMENT_ID*         |
| AUTHOR_ID                |
| OWNER_ID                 |
| RELEASE_ID               |
| PROJECT_ID               |
| IMPORTANCE_ID            |
| NAME                     |
| CREATION_DATE            |
| INDENT_LEVEL             |
| DESCRIPTION              |
| LAST_UPDATE_DATE         |
| COVERAGE_COUNT_TOTAL     |
| COVERAGE_COUNT_PASSED    |
| COVERAGE_COUNT_FAILED    |
| COVERAGE_COUNT_CAUTION   |
| COVERAGE_COUNT_BLOCKED   |
| TASK_COUNT               |
| TASK_ESTIMATED_EFFORT    |
| TASK_ACTUAL_EFFORT       |
| TASK_PROJECTED_EFFORT    |
| TASK_REMAINING_EFFORT    |
| TASK_PERCENT_ON_TIME     |
| TASK_PERCENT_LATE_FINISH |
| TASK_PERCENT_NOT_START   |
| TASK_PERCENT_LATE_START  |
| IS_DELETED               |
| AUTHOR_NAME              |
| OWNER_NAME               |
| IMPORTANCE_NAME          |
| RELEASE_VERSION_NUMBER   |
| PROJECT_NAME             |
| PROJECT_GROUP_ID         |
| CUST_01...               |
| CUST_99                  |
| REQUIREMENT_TYPE_ID      |
| REQUIREMENT_STATUS_ID    |
| COMPONENT_ID             |
| IS_SUMMARY               |
| IS_ATTACHMENTS           |
| CONCURRENCY_DATE         |
| REQUIREMENT_STATUS_NAME  |
| REQUIREMENT_TYPE_NAME    |
| COMPONENT_NAME           |
| ESTIMATE_POINTS          |
| ESTIMATED_EFFORT         |
| RANK                     |
| GOAL_ID                  |
| START_DATE               |
| END_DATE                 |
| PERCENT_COMPLETE         |
| TAGS                     |

## Requirement Importances
| R_Requirement_Importance |
| ------------------------ |
| *IMPORTANCE_ID*          |
| PROJECT_TEMPLATE_ID      |
| NAME                     |
| IS_ACTIVE                |
| COLOR                    |
| SCORE                    |

## Requirement Incidents
| R_RequirementIncidents |
| ---------------------- |
| REQUIREMENT_ID         |
| INCIDENT_ID            |
| DETECTED_RELEASE_ID    |
| IS_OPEN_STATUS         |

## Requirement Incidents - Extended
For normal use we strongly recommend using the standard artifact association view above. This extended view adds the artifact names, which can be very helpful, but will make the reports using it run much slower. 

| R_RequirementIncidents |
| ---------------------- |
| REQUIREMENT_ID         |
| INCIDENT_ID            |
| DETECTED_RELEASE_ID    |
| IS_OPEN_STATUS         |
| REQUIREMENT_NAME       |
| INCIDENT_NAME          |

## Requirement Steps
| R_RequirementSteps           |
| ---------------------------- |
| REQUIREMENT_ID               |
| POSITION                     |
| DESCRIPTION                  |
| IS_DELETED                   |
| CREATION_DATE                |
| LAST_UPDATE_DATE             |
| CONCURRENCY_DATE             |
| REQUIREMENT_NAME             |
| REQUIREMENT_LAST_UPDATE_DATE |
| PROJECT_IS_ACTIVE            |
| PROJECT_PROJECT_GROUP_ID     |
| PROJECT_NAME                 |

## Requirement Test Case Coverage
| R_RequirementTestCases |
| ---------------------- |
| REQUIREMENT_ID         |
| TEST_CASE_ID           |
| REQUIREMENT_NAME       |
| TEST_CASE_NAME         |
| PROJECT_ID             |
| PROJECT_NAME           |

## Requirement Test Step Coverage
| R_RequirementTestSteps |
| ---------------------- |
| TEST_STEP_ID           |
| REQUIREMENT_NAME       |
| POSITION               |
| STEP_DESCRIPTION       |
| EXPECTED_RESULT        |
| SAMPLE_DATA            |
| PROJECT_ID             |
| PROJECT_NAME           |

## Requirement Types
| R_RequirementTypes      |
| ----------------------- |
| *REQUIREMENT_TYPE_ID*   |
| REQUIREMENT_WORKFLOW_ID |
| PROJECT_TEMPLATE_ID     |
| NAME                    |
| ICON                    |
| IS_ACTIVE               |
| IS_STEPS                |
| IS_DEFAULT              |
| IS_KEY_TYPE             |
| PROJECT_TEMPLATE_NAME   |

## Risks
| R_Risks                  |
| ------------------------ |
| *RISK_ID*                |
| RISK_IMPACT_ID           |
| RISK_STATUS_ID           |
| RISK_PROBABILITY_ID      |
| RISK_TYPE_ID             |
| PROJECT_ID               |
| CREATOR_ID               |
| OWNER_ID                 |
| PROJECT_GROUP_ID         |
| RELEASE_ID               |
| COMPONENT_ID             |
| NAME                     |
| DESCRIPTION              |
| IS_DELETED               |
| CREATION_DATE            |
| LAST_UPDATE_DATE         |
| CONCURRENCY_DATE         |
| REVIEW_DATE              |
| GOAL_ID                  |
| CLOSED_DATE              |
| IS_ATTACHMENTS           |
| RISK_PROBABILITY_NAME    |
| RISK_PROBABILITY_COLOR   |
| RISK_PROBABILITY_SCORE   |
| RISK_IMPACT_NAME         |
| RISK_IMPACT_COLOR        |
| RISK_IMPACT_SCORE        |
| RISK_EXPOSURE            |
| RISK_STATUS_NAME         |
| RISK_STATUS_IS_OPEN      |
| RISK_TYPE_NAME           |
| CREATOR_NAME             |
| OWNER_NAME               |
| RELEASE_VERSION_NUMBER   |
| RELEASE_NAME             |
| COMPONENT_NAME           |
| GOAL_NAME                |
| PROJECT_IS_ACTIVE        |
| PROJECT_PROJECT_GROUP_ID |
| PROJECT_NAME             |
| CUST_01...               |
| CUST_99                  |
| TAGS                     |

## Risk Impacts
| R_RiskImpacts         |
| --------------------- |
| *RISK_IMPACT_ID*      |
| PROJECT_TEMPLATE_ID   |
| NAME                  |
| COLOR                 |
| IS_ACTIVE             |
| POSITION              |
| SCORE                 |
| PROJECT_TEMPLATE_NAME |

## Risk Mitigations
| R_RiskMitigations        |
| ------------------------ |
| RISK_ID                  |
| *RISK_MITIGATION_ID*     |
| POSITION                 |
| DESCRIPTION              |
| IS_DELETED               |
| CREATION_DATE            |
| LAST_UPDATE_DATE         |
| CONCURRENCY_DATE         |
| IS_ACTIVE                |
| REVIEW_DATE              |
| RISK_NAME                |
| RISK_REVIEW_DATE         |
| PROJECT_IS_ACTIVE        |
| PROJECT_PROJECT_GROUP_ID |
| PROJECT_NAME             |
| PROJECT_ID               |

## Risk Probabilities
| R_RiskProbabilities   |
| --------------------- |
| *RISK_PROBABILITY_ID* |
| PROJECT_TEMPLATE_ID   |
| NAME                  |
| COLOR                 |
| IS_ACTIVE             |
| POSITION              |
| SCORE                 |
| PROJECT_TEMPLATE_NAME |

## Risk Statuses
| R_RiskStatuses        |
| --------------------- |
| *RISK_STATUS_ID*      |
| NAME                  |
| IS_ACTIVE             |
| IS_DEFAULT            |
| IS_OPEN               |
| POSITION              |
| PROJECT_TEMPLATE_ID   |
| PROJECT_TEMPLATE_NAME |

## Risk Types
| R_RiskTypes           |
| --------------------- |
| *RISK_TYPE_ID*        |
| NAME                  |
| IS_ACTIVE             |
| IS_DEFAULT            |
| PROJECT_TEMPLATE_ID   |
| RISK_WORKFLOW_ID      |
| PROJECT_TEMPLATE_NAME |

## Source Code Associations
| R_SourceCodeAssociations         |
| -------------------------------- |
| ARTIFACT_SOURCE_CODE_REVISION_ID |
| ARTIFACT_TYPE_ID                 |
| ARTIFACT_ID                      |
| REVISION_KEY                     |
| COMMENT                          |
| CREATION_DATE                    |
| ARTIFACT_TYPE_NAME               |
| ARTIFACT_TYPE_PREFIX             |


## Source Code Commits
| R_SourceCodeCommits                |
| ---------------------------------- |
| VERSION_CONTROL_SYSTEM_ID          |
| PROJECT_ID                         |
| *REVISION_ID*                      |
| NAME                               |
| REVISION_KEY                       |
| AUTHOR_NAME                        |
| MESSAGE                            |
| UPDATE_DATE                        |
| CONTENT_CHANGED                    |
| PROPERTIES_CHANGED                 |
| VERSION_CONTROL_SYSTEM_NAME        |
| VERSION_CONTROL_SYSTEM_DESCRIPTION |
| VERSION_CONTROL_SYSTEM_IS_ACTIVE   |
| PROJECT_NAME                       |
| BRANCH_NAME                        |
| BRANCH_PATH                        |
| BRANCH_IS_HEAD                     |

## Tasks
| R_Tasks                |
| ---------------------- |
| *TASK_ID*              |
| TASK_STATUS_ID         |
| PROJECT_ID             |
| REQUIREMENT_ID         |
| RELEASE_ID             |
| CREATOR_ID             |
| OWNER_ID               |
| TASK_PRIORITY_ID       |
| NAME                   |
| DESCRIPTION            |
| CREATION_DATE          |
| LAST_UPDATE_DATE       |
| START_DATE             |
| END_DATE               |
| COMPLETION_PERCENT     |
| ESTIMATED_EFFORT       |
| ACTUAL_EFFORT          |
| PROJECTED_EFFORT       |
| REMAINING_EFFORT       |
| IS_DELETED             |
| TASK_STATUS_NAME       |
| OWNER_NAME             |
| CREATOR_NAME           |
| TASK_PRIORITY_NAME     |
| PROJECT_NAME           |
| PROJECT_GROUP_ID       |
| RELEASE_VERSION_NUMBER |
| CUST_01...             |
| CUST_99                |
| TASK_TYPE_ID           |
| TASK_FOLDER_ID         |
| IS_ATTACHMENTS         |
| CONCURRENCY_DATE       |
| REQUIREMENT_NAME       |
| TASK_TYPE_NAME         |
| COMPONENT_ID           |
| COMPONENT_NAME         |
| RISK_ID                |
| TAGS                   |

## Task Folders
| R_TaskFolders         |
| --------------------- |
| *TASK_FOLDER_ID*      |
| PROJECT_ID            |
| NAME                  |
| PARENT_TASK_FOLDER_ID |
| HIERARCHY_LEVEL       |
| INDENT_LEVEL          |

## Task Priorities
| R_TaskPriorities      |
| --------------------- |
| *TASK_PRIORITY_ID*    |
| PROJECT_TEMPLATE_ID   |
| NAME                  |
| IS_ACTIVE             |
| COLOR                 |
| SCORE                 |
| PROJECT_TEMPLATE_NAME |

## Task Types
| R_TaskTypes           |
| --------------------- |
| *TASK_TYPE_ID*        |
| PROJECT_TEMPLATE_ID   |
| TASK_WORKFLOW_ID      |
| NAME                  |
| POSITION              |
| IS_ACTIVE             |
| IS_DEFAULT            |
| IS_PULL_REQUEST       |
| PROJECT_TEMPLATE_NAME |

## Teams
| R_Teams     |
| ----------- |
| *TEAM_ID*   |
| NAME        |
| DESCRIPTION |
| IS_ACTIVE   |
| IS_DELETED  |

## Test Cases
| R_TestCases              |
| ------------------------ |
| *TEST_CASE_ID*           |
| EXECUTION_STATUS_ID      |
| TEST_CASE_PRIORITY_ID    |
| PROJECT_ID               |
| AUTHOR_ID                |
| NAME                     |
| OWNER_ID                 |
| DESCRIPTION              |
| EXECUTION_DATE           |
| CREATION_DATE            |
| LAST_UPDATE_DATE         |
| AUTOMATION_ENGINE_ID     |
| AUTOMATION_ATTACHMENT_ID |
| ESTIMATED_DURATION       |
| IS_DELETED               |
| EXECUTION_STATUS_NAME    |
| TEST_CASE_PRIORITY_NAME  |
| AUTHOR_NAME              |
| OWNER_NAME               |
| AUTOMATION_ENGINE_NAME   |
| PROJECT_NAME             |
| PROJECT_GROUP_ID         |
| CUST_01...               |
| CUST_99                  |
| CONCURRENCY_DATE         |
| TEST_CASE_STATUS_ID      |
| TEST_CASE_TYPE_ID        |
| TEST_CASE_FOLDER_ID      |
| IS_ATTACHMENTS           |
| IS_TEST_STEPS            |
| ACTUAL_DURATION          |
| TEST_CASE_STATUS_NAME    |
| TEST_CASE_TYPE_NAME      |
| COMPONENT_IDS            |
| IS_SUSPECT               |
| TAGS                     |

## Test Case Folders
| R_TestCaseFolders          |
| -------------------------- |
| *TEST_CASE_FOLDER_ID*      |
| PARENT_TEST_CASE_FOLDER_ID |
| PROJECT_ID                 |
| NAME                       |
| DESCRIPTION                |
| EXECUTION_DATE             |
| LAST_UPDATE_DATE           |
| ESTIMATED_DURATION         |
| ACTUAL_DURATION            |
| COUNT_PASSED               |
| COUNT_FAILED               |
| COUNT_BLOCKED              |
| COUNT_CAUTION              |
| COUNT_NOT_RUN              |
| COUNT_NOT_APPLICABLE       |
| PROJECT_NAME               |
| PROJECT_GROUP_ID           |
| HIERARCHY_LEVEL            |
| INDENT_LEVEL               |

## Test Case Incidents
| R_TestCaseIncidents |
| ------------------- |
| TEST_CASE_ID        |
| INCIDENT_ID         |
| DETECTED_RELEASE_ID |
| RESOLVED_RELEASE_ID |
| VERIFIED_RELEASE_ID |
| IS_OPEN_STATUS      |

## Test Case Priorities
| R_TestCase_Priorities |
| --------------------- |
| TEST_CASE_PRIORITY_ID |
| PROJECT_TEMPLATE_ID   |
| NAME                  |
| IS_ACTIVE             |
| COLOR                 |
| SCORE                 |

## Test Case Types
| R_TestCaseTypes       |
| --------------------- |
| *TEST_CASE_TYPE_ID*   |
| PROJECT_TEMPLATE_ID   |
| TEST_CASE_WORKFLOW_ID |
| NAME                  |
| IS_ACTIVE             |
| POSITION              |
| IS_DEFAULT            |
| IS_EXPLORATORY        |
| IS_BDD                |
| PROJECT_TEMPLATE_NAME |

## Test Configuration Entries
| R_TestConfigurationEntries       |
| -------------------------------- |
| TEST_CONFIGURATION_ID            |
| TEST_CONFIGURATION_SET_ID        |
| POSITION                         |
| TEST_CONFIGURATION_SET_NAME      |
| IS_TEST_CONFIGURATION_SET_ACTIVE |
| CUSTOM_PROPERTY_VALUE_ID         |
| TEST_CASE_PARAMETER_NAME         |
| TEST_CASE_PARAMETER_VALUE        |
| PROJECT_NAME                     |
| PROJECT_GROUP_ID                 |
| PROJECT_ID                       |

## Test Configuration Sets
| R_TestConfigurationSets     |
| --------------------------- |
| *TEST_CONFIGURATION_SET_ID* |
| PROJECT_ID                  |
| NAME                        |
| DESCRIPTION                 |
| IS_ACTIVE                   |
| IS_DELETED                  |
| CREATION_DATE               |
| LAST_UPDATED_DATE           |
| CONCURRENCY_DATE            |
| PROJECT_NAME                |
| PROJECT_GROUP_ID            |

## Test Runs
Note that the TEST_RUN_TYPE_ID can have two values: 1 = Manual, 2 = Automated

| R_TestRuns             |
| ---------------------- |
| *TEST_RUN_ID*          |
| TEST_CASE_ID           |
| NAME                   |
| DESCRIPTION            |
| ESTIMATED_DURATION     |
| ACTUAL_DURATION        |
| TEST_RUN_TYPE_ID       |
| TESTER_ID              |
| EXECUTION_STATUS_ID    |
| START_DATE             |
| END_DATE               |
| RUNNER_NAME            |
| RUNNER_TEST_NAME       |
| RUNNER_ASSERT_COUNT    |
| RUNNER_MESSAGE         |
| RUNNER_STACK_TRACE     |
| EXECUTION_STATUS_NAME  |
| TESTER_NAME            |
| TEST_RUNS_PENDING_ID   |
| RELEASE_ID             |
| TEST_SET_ID            |
| TEST_SET_TEST_CASE_ID  |
| RELEASE_NAME           |
| RELEASE_VERSION_NUMBER |
| TEST_SET_NAME          |
| TEST_RUN_TYPE_NAME     |
| AUTOMATION_HOST_ID     |
| AUTOMATION_HOST_NAME   |
| AUTOMATION_ENGINE_ID   |
| BUILD_ID               |
| BUILD_NAME             |
| TEST_RUN_FORMAT_ID     |
| PROJECT_NAME           |
| PROJECT_GROUP_ID       |
| CUST_01...             |
| CUST_99                |
| IS_ATTACHMENTS         |
| IS_DELETED             |
| CONCURRENCY_DATE       |
| PROJECT_ID             |
| CHANGESET_ID           |
| TEST_CONFIGURATION_ID  |
| TAGS                   |

## Test Run Incidents
| R_TestRunIncidents  |
| ------------------- |
| TEST_RUN_ID         |
| INCIDENT_ID         |
| DETECTED_RELEASE_ID |
| RESOLVED_RELEASE_ID |
| VERIFIED_RELEASE_ID |
| IS_OPEN_STATUS      |
| TEST_STEP_ID        |
| TEST_RUN_STEP_ID    |

## Test Run Steps
| R_TestRunSteps        |
| --------------------- |
| *TEST_RUN_STEP_ID*    |
| EXECUTION_STATUS_ID   |
| TEST_CASE_ID          |
| TEST_STEP_ID          |
| TEST_RUN_ID           |
| DESCRIPTION           |
| POSITION              |
| EXPECTED_RESULT       |
| SAMPLE_DATA           |
| ACTUAL_RESULT         |
| EXECUTION_STATUS_NAME |
| TEST_CASE_NAME        |
| PROJECT_ID            |
| PROJECT_NAME          |
| PROJECT_GROUP_ID      |
| START_DATE            |
| END_DATE              |
| ACTUAL_DURATION       |

## Test Sets
| R_TestSets                  |
| --------------------------- |
| *TEST_SET_ID*               |
| PROJECT_ID                  |
| RELEASE_ID                  |
| TEST_SET_STATUS_ID          |
| CREATOR_ID                  |
| OWNER_ID                    |
| AUTOMATION_HOST_ID          |
| TEST_RUN_TYPE_ID            |
| RECURRENCE_ID               |
| NAME                        |
| DESCRIPTION                 |
| CREATION_DATE               |
| PLANNED_DATE                |
| LAST_UPDATE_DATE            |
| IS_DELETED                  |
| CONCURRENCY_DATE            |
| RELEASE_VERSION_NUMBER      |
| PROJECT_NAME                |
| TEST_CASE_COUNT             |
| TEST_SET_STATUS_NAME        |
| CREATOR_NAME                |
| OWNER_NAME                  |
| PROJECT_ACTIVE_YN           |
| PROJECT_IS_ACTIVE           |
| AUTOMATION_HOST_NAME        |
| TEST_RUN_TYPE_NAME          |
| RECURRENCE_NAME             |
| PROJECT_GROUP_ID            |
| CUST_01...                  |
| CUST_99                     |
| TEST_SET_FOLDER_ID          |
| IS_ATTACHMENTS              |
| BUILD_EXECUTE_TIME_INTERVAL |
| ESTIMATED_DURATION          |
| ACTUAL_DURATION             |
| COUNT_PASSED                |
| COUNT_FAILED                |
| COUNT_CAUTION               |
| COUNT_BLOCKED               |
| COUNT_NOT_RUN               |
| COUNT_NOT_APPLICABLE        |
| EXECUTION_DATE              |
| IS_DYNAMIC                  |
| DYNAMIC_QUERY               |
| IS_AUTO_SCHEDULED           |
| TEST_CONFIGURATION_SET_ID   |
| TAGS                        |

## Test Set Folders
| R_TestSetFolders          |
| ------------------------- |
| *TEST_SET_FOLDER_ID*      |
| PROJECT_ID                |
| PARENT_TEST_SET_FOLDER_ID |
| NAME                      |
| DESCRIPTION               |
| CREATION_DATE             |
| LAST_UPDATE_DATE          |
| EXECUTION_DATE            |
| ESTIMATED_DURATION        |
| ACTUAL_DURATION           |
| COUNT_PASSED              |
| COUNT_FAILED              |
| COUNT_CAUTION             |
| COUNT_BLOCKED             |
| COUNT_NOT_RUN             |
| COUNT_NOT_APPLICABLE      |
| PROJECT_NAME              |
| PROJECT_GROUP_ID          |
| HIERARCHY_LEVEL           |
| INDENT_LEVEL              |

## Test Set Incidents
| R_TestSetIncidents  |
| ------------------- |
| TEST_SET_ID         |
| INCIDENT_ID         |
| DETECTED_RELEASE_ID |
| RESOLVED_RELEASE_ID |
| VERIFIED_RELEASE_ID |
| IS_OPEN_STATUS      |

## Test Set Test Cases
| R_TestSetTestCases      |
| ----------------------- |
| *TEST_SET_TEST_CASE_ID* |
| TEST_SET_ID             |
| TEST_CASE_ID            |
| OWNER_ID                |
| POSITION                |
| TEST_SET_NAME           |
| TEST_CASE_NAME          |
| OWNER_NAME              |
| PROJECT_ID              |
| PROJECT_NAME            |
| PLANNED_DATE            |
| IS_SETUP_TEARDOWN       |

## Test Steps
| R_TestSteps           |
| --------------------- |
| *TEST_STEP_ID*        |
| TEST_CASE_ID          |
| EXECUTION_STATUS_ID   |
| DESCRIPTION           |
| LINKED_TEST_CASE_ID   |
| POSITION              |
| EXPECTED_RESULT       |
| SAMPLE_DATA           |
| LAST_UPDATE_DATE      |
| IS_DELETED            |
| EXECUTION_STATUS_NAME |
| TEST_CASE_NAME        |
| PROJECT_ID            |
| PROJECT_NAME          |
| PROJECT_GROUP_ID      |
| CUST_01...            |
| CUST_99               |
| IS_ATTACHMENTS        |
| CONCURRENCY_DATE      |
| PRECONDITION          |


## Timesheets
| R_Timesheets          |
| --------------------- |
| *TIMESHEET_ID*        |
| SUBMITTER_USER_ID     |
| SUBMITTER_USER_NAME   |
| APPROVER_USER_ID      |
| APPROVER_USER_NAME    |
| TIMESHEET_STATUS_ID   |
| TIMESHEET_STATUS_NAME |
| CREATION_DATE         |
| APPROVAL_DATE         |
| LAST_UPDATE_DATE      |
| START_DATE            |
| END_DATE              |
| COMMENTS              |
| APPROVER_COMMENTS     |

## Timesheet Entries
| R_TimesheetEntries   |
| -------------------- |
| *TIMESHEET_ENTRY_ID* |
| TIMESHEET_ID         |
| USER_ID              |
| USER_NAME            |
| ARTIFACT_TYPE_ID     |
| ARTIFACT_TYPE_NAME   |
| ARTIFACT_ID          |
| ARTIFACT_NAME        |
| EFFORT_MINUTES       |
| EFFORT_DATE          |
| PROJECT_ID           |
| PROJECT_NAME         |
| PROJECT_GROUP_ID     |
| PROJECT_GROUP_NAME   |
| RESOURCE_CATEGORY_ID |

## Timesheet Statuses
| R_TimesheetStatuses   |
| --------------------- |
| *TIMESHEET_STATUS_ID* |
| TIMESHEET_STATUS_NAME |
| IS_ACTIVE             |
| IS_OPEN               |

## Timesheets with Entries
This table combines the information from the timesheets table and the timesheet entries table to give a unified view of a timesheet and all of its key information. 

| R_TimesheetWithEntries |
| ---------------------- |
| *TIMESHEET_ID*         |
| SUBMITTER_USER_ID      |
| SUBMITTER_USER_NAME    |
| APPROVER_USER_ID       |
| APPROVER_USER_NAME     |
| TIMESHEET_STATUS_ID    |
| TIMESHEET_STATUS_NAME  |
| CREATION_DATE          |
| APPROVAL_DATE          |
| LAST_UPDATE_DATE       |
| START_DATE             |
| END_DATE               |
| COMMENTS               |
| APPROVER_COMMENTS      |
| TIMESHEET_ENTRY_ID     |
| ARTIFACT_TYPE_ID       |
| ARTIFACT_TYPE_NAME     |
| ARTIFACT_ID            |
| ARTIFACT_NAME          |
| EFFORT_MINUTES         |
| EFFORT_DATE            |
| PROJECT_ID             |
| PROJECT_NAME           |
| PROJECT_GROUP_ID       |
| PROJECT_GROUP_NAME     |
| RESOURCE_CATEGORY_ID   |


## Users
| R_Users                         |
| ------------------------------- |
| *USER_ID*                       |
| USER_NAME                       |
| EMAIL_ADDRESS                   |
| IS_ACTIVE                       |
| CREATION_DATE                   |
| LDAP_DN                         |
| FIRST_NAME                      |
| LAST_NAME                       |
| MIDDLE_INITIAL                  |
| DEPARTMENT                      |
| LAST_UPDATE_DATE                |
| TIMEZONE                        |
| LAST_OPENED_PROJECT_ID          |
| IS_APPROVED                     |
| LAST_LOGIN_DATE                 |
| LAST_ACTIVITY_DATE              |
| ORGANIZATION                    |
| LAST_OPENED_PROJECT_GROUP_ID    |
| LAST_OPENED_PROJECT_TEMPLATE_ID |
| IS_ADMIN                        |
| IS_REPORT_ADMIN                 |
| IS_RESOURCE_ADMIN               |
| IS_PORTFOLIO_ADMIN              |
| LAST_PASSWORD_CHANGED_DATE      |
