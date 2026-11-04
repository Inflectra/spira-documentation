# Available Custom Reports Tables
!!! abstract "Available in SpiraTest, SpiraTeam, SpiraPlan"

!!! info "How to use this page"
    Spira has a number of database views available for creating custom reports using ESQL queries. Below, each available table is listed with all of their exact field names. 

    Many tables have a single field shown in *italic* - these are the Primary Keys for that table, which means that field can be used as the unique identifier for each row of data. 

    The Type column gives the data type the view returns. This matters for custom graphs: the first column you select is the category label and can be any type, but the second and later columns are plotted as series and must be numeric.

    Custom property fields are listed as a range, for example `CUST_01 ... CUST_99`, meaning every field in that range exists. They are all String, whatever the property's display type, so a numeric custom property has to be cast before it can be plotted.

## Artifact Associations
| R_ArtifactAssociations    | Type     |
| ------------------------- | -------- |
| ARTIFACT_LINK_TYPE_ID     | Int32    |
| SOURCE_ARTIFACT_ID        | Int32    |
| SOURCE_ARTIFACT_TYPE_ID   | Int32    |
| DEST_ARTIFACT_ID          | Int32    |
| DEST_ARTIFACT_TYPE_ID     | Int32    |
| CREATOR_ID                | Int32    |
| CREATION_DATE             | DateTime |
| COMMENT                   | String   |
| SOURCE_ARTIFACT_TYPE_NAME | String   |
| DEST_ARTIFACT_TYPE_NAME   | String   |
| CREATOR_NAME              | String   |
| ARTIFACT_LINK_TYPE_NAME   | String   |
| ARTIFACT_LINK_ID          | Int32    |

## Artifact Associations - Extended
For normal use we strongly recommend using the standard artifact association view above. This extended view adds the artifact names, which can be very helpful, but will make the reports using it run much slower. 

| R_ArtifactAssociationExtended | Type     |
| ----------------------------- | -------- |
| ARTIFACT_LINK_TYPE_ID         | Int32    |
| SOURCE_ARTIFACT_ID            | Int32    |
| SOURCE_ARTIFACT_TYPE_ID       | Int32    |
| DEST_ARTIFACT_ID              | Int32    |
| DEST_ARTIFACT_TYPE_ID         | Int32    |
| CREATOR_ID                    | Int32    |
| CREATION_DATE                 | DateTime |
| COMMENT                       | String   |
| SOURCE_ARTIFACT_TYPE_NAME     | String   |
| DEST_ARTIFACT_TYPE_NAME       | String   |
| CREATOR_NAME                  | String   |
| ARTIFACT_LINK_TYPE_NAME       | String   |
| SOURCE_ARTIFACT_NAME          | String   |
| DEST_ARTIFACT_NAME            | String   |
| ARTIFACT_LINK_ID              | Int32    |

## Artifact Attachments
| R_ArtifactAttachments | Type     |
| --------------------- | -------- |
| ARTIFACT_TYPE_ID      | Int32    |
| ARTIFACT_ID           | Int32    |
| ARTIFACT_TYPE_NAME    | String   |
| ARTIFACT_NAME         | String   |
| COMMENT               | String   |
| CREATOR_ID            | Int32    |
| CREATION_DATE         | DateTime |
| CREATOR_NAME          | String   |
| ATTACHMENT_ID         | Int32    |
| PROJECT_ID            | Int32    |
| ARTIFACT_STATUS_NAME  | String   |
| ARTIFACT_LINK_ID      | Int32    |

## Artifact Tags
| R_ArtifactTags     | Type   |
| ------------------ | ------ |
| ARTIFACT_ID        | Int32  |
| ARTIFACT_TYPE_ID   | Int32  |
| TAGS               | String |
| PROJECT_ID         | Int32  |
| PROJECT_NAME       | String |
| ARTIFACT_TYPE_NAME | String |

## Artifact Types
| R_ArtifactTypes    | Type   |
| ------------------ | ------ |
| *ARTIFACT_TYPE_ID* | Int32  |
| NAME               | String |
| PREFIX             | String |

## Attachments
| R_Attachments                  | Type     |
| ------------------------------ | -------- |
| *ATTACHMENT_ID*                | Int32    |
| ATTACHMENT_TYPE_ID             | Int32    |
| AUTHOR_ID                      | Int32    |
| EDITOR_ID                      | Int32    |
| FILENAME                       | String   |
| DESCRIPTION                    | String   |
| UPLOAD_DATE                    | DateTime |
| EDITED_DATE                    | DateTime |
| SIZE                           | Int32    |
| CURRENT_VERSION                | String   |
| PROJECT_ID                     | Int32    |
| PROJECT_ATTACHMENT_FOLDER_ID   | Int32    |
| CONCURRENCY                    | Int64    |
| DOCUMENT_STATUS_ID             | Int32    |
| DOCUMENT_TYPE_ID               | Int32    |
| DOCUMENT_STATUS_NAME           | String   |
| DOCUMENT_TYPE_NAME             | String   |
| TAGS                           | String   |
| CUST_01 ... CUST_99            | String   |
| IS_KEY_DOCUMENT                | Boolean  |
| DOCUMENT_STATUS_IS_OPEN_STATUS | Boolean  |
| PROJECT_IS_ACTIVE              | Boolean  |
| PROJECT_GROUP_ID               | Int32    |
| PROJECT_NAME                   | String   |
| AUTHOR_NAME                    | String   |
| EDITOR_NAME                    | String   |
| ATTACHMENT_TYPE_NAME           | String   |
| PROJECT_ATTACHMENT_FOLDER_NAME | String   |

## Attachment Folders
| R_AttachmentFolders                 | Type   |
| ----------------------------------- | ------ |
| *PROJECT_ATTACHMENT_FOLDER_ID*      | Int32  |
| PROJECT_ID                          | Int32  |
| PARENT_PROJECT_ATTACHMENT_FOLDER_ID | Int32  |
| NAME                                | String |
| PROJECT_NAME                        | String |
| PROJECT_GROUP_ID                    | Int32  |

## Attachment Versions
| R_AttachmentVersions    | Type     |
| ----------------------- | -------- |
| *ATTACHMENT_VERSION_ID* | Int32    |
| ATTACHMENT_ID           | Int32    |
| AUTHOR_ID               | Int32    |
| FILENAME                | String   |
| DESCRIPTION             | String   |
| UPLOAD_DATE             | DateTime |
| SIZE                    | Int32    |
| VERSION_NUMBER          | String   |
| IS_CURRENT              | Boolean  |
| CHANGESET_ID            | Int64    |
| AUTHOR_NAME             | String   |
| ATTACHMENT_TYPE_ID      | Int32    |
| PROJECT_ID              | Int32    |

## Automation Hosts
| R_AutomationHosts    | Type     |
| -------------------- | -------- |
| *AUTOMATION_HOST_ID* | Int32    |
| PROJECT_ID           | Int32    |
| NAME                 | String   |
| DESCRIPTION          | String   |
| TOKEN                | String   |
| LAST_UPDATE_DATE     | DateTime |
| IS_DELETED           | Boolean  |
| CUST_01 ... CUST_99  | String   |
| PROJECT_NAME         | String   |
| PROJECT_GROUP_ID     | Int32    |
| IS_ACTIVE            | Boolean  |
| IS_ATTACHMENTS       | Boolean  |
| CONCURRENCY          | Int64    |
| LAST_CONTACT_DATE    | DateTime |

## Baselines
!!! abstract "Available in SpiraTeam and SpiraPlan only"

See [this KB](https://www.inflectra.com/Support/KnowledgeBase/KB550.aspx) for some examples of using this custom report table

| R_Baselines             | Type     |
| ----------------------- | -------- |
| *BASELINE_ID*           | Int32    |
| PROJECT_ID              | Int32    |
| CREATOR_USER_ID         | Int32    |
| CHANGESET_ID            | Int64    |
| RELEASE_ID              | Int32    |
| NAME                    | String   |
| DESCRIPTION             | String   |
| IS_ACTIVE               | Boolean  |
| IS_APPROVED             | Boolean  |
| IS_DELETED              | Boolean  |
| CREATION_DATE           | DateTime |
| LAST_UPDATE_DATE        | DateTime |
| CONCURRENCY             | Int64    |
| BASELINE_CREATOR_LOGIN  | String   |
| CHANGESET_CREATOR_ID    | Int32    |
| CHANGESET_CREATOR_LOGIN | String   |
| ARTIFACT_TYPE_ID        | Int32    |
| ARTIFACT_TYPE_NAME      | String   |
| CHANGESET_DATE          | DateTime |
| CHANGESET_TYPE_ID       | Int32    |
| CHANGESET_TYPE_NAME     | String   |

## Builds
Note that BUILD_STATUS_ID can have the following values: 1 = Failed, 2 = Succeeded, 3 = Unstable, 4 = Aborted.

| R_Builds               | Type     |
| ---------------------- | -------- |
| *BUILD_ID*             | Int32    |
| BUILD_STATUS_ID        | Int32    |
| RELEASE_ID             | Int32    |
| PROJECT_ID             | Int32    |
| NAME                   | String   |
| DESCRIPTION            | String   |
| IS_DELETED             | Boolean  |
| CREATION_DATE          | DateTime |
| LAST_UPDATE_DATE       | DateTime |
| RELEASE_NAME           | String   |
| RELEASE_VERSION_NUMBER | String   |
| PROJECT_NAME           | String   |
| PROJECT_GROUP_ID       | Int32    |

## Build Statuses
| R_BuildStatuses | Type    |
| --------------- | ------- |
| BUILD_STATUS_ID | Int32   |
| NAME            | String  |
| IS_ACTIVE       | Boolean |

## Capabilities
!!! abstract "Available in SpiraPlan only"

| R_ProjectGroup_Capabilities | Type     |
| --------------------------- | -------- |
| *CAPABILITY_ID*             | Int32    |
| PROJECT_GROUP_ID            | Int32    |
| MILESTONE_ID                | Int32    |
| STATUS_ID                   | Int32    |
| TYPE_ID                     | Int32    |
| PRIORITY_ID                 | Int32    |
| NAME                        | String   |
| DESCRIPTION                 | String   |
| IS_DELETED                  | Boolean  |
| PERCENT_COMPLETE            | Int32    |
| PROJECT_REQUIREMENT_COUNT   | Int32    |
| INDENT_LEVEL                | String   |
| CONCURRENCY                 | Int64    |
| CREATOR_ID                  | Int32    |
| OWNER_ID                    | Int32    |
| CREATION_DATE               | DateTime |
| LAST_UPDATED_DATE           | DateTime |
| IS_SUMMARY                  | Boolean  |
| STATUS_NAME                 | String   |
| STATUS_IS_OPEN              | Boolean  |
| TYPE_NAME                   | String   |
| PRIORITY_NAME               | String   |
| PRIORITY_COLOR              | String   |
| PRIORITY_SCORE              | Int32    |
| MILESTONE_NAME              | String   |
| CREATOR_NAME                | String   |
| OWNER_NAME                  | String   |
| PROJECT_GROUP_NAME          | String   |
| CUST_01 ... CUST_30         | String   |
| CREATOR_LOGIN               | String   |
| OWNER_LOGIN                 | String   |

## Capability Priorities
!!! abstract "Available in SpiraPlan only"

| R_ProjectGroup_Capability_Priorities | Type    |
| ------------------------------------ | ------- |
| *PRIORITY_ID*                        | Int32   |
| NAME                                 | String  |
| COLOR                                | String  |
| IS_ACTIVE                            | Boolean |
| IS_DELETED                           | Boolean |
| SCORE                                | Int32   |

## Capability Requirement Associations
!!! abstract "Available in SpiraPlan only"

| R_ProjectGroup_Capability_Project_Requirements | Type   |
| ---------------------------------------------- | ------ |
| CAPABILITY_ID                                  | Int32  |
| REQUIREMENT_ID                                 | Int32  |
| ARTIFACT_LINK_TYPE_ID                          | Int32  |
| CAPABILITY_NAME                                | String |
| REQUIREMENT_NAME                               | String |
| ARTIFACT_LINK_TYPE_NAME                        | String |

## Capability Statuses
!!! abstract "Available in SpiraPlan only"

| R_ProjectGroup_Capability_Statuses | Type    |
| ---------------------------------- | ------- |
| *STATUS_ID*                        | Int32   |
| NAME                               | String  |
| POSITION                           | Int32   |
| IS_ACTIVE                          | Boolean |
| IS_DELETED                         | Boolean |
| IS_DEFAULT                         | Boolean |
| IS_OPEN                            | Boolean |
| ON_BOARD                           | Boolean |

## Capability Types
!!! abstract "Available in SpiraPlan only"

| R_ProjectGroup_Capability_Types | Type    |
| ------------------------------- | ------- |
| *TYPE_ID*                       | Int32   |
| NAME                            | String  |
| IS_ACTIVE                       | Boolean |
| IS_DELETED                      | Boolean |
| IS_DEFAULT                      | Boolean |

## Comments
| R_Comments         | Type     |
| ------------------ | -------- |
| ARTIFACT_TYPE_ID   | Int32    |
| ARTIFACT_ID        | Int32    |
| CREATOR_ID         | Int32    |
| COMMENT_TEXT       | String   |
| CREATION_DATE      | DateTime |
| CREATOR_NAME       | String   |
| ARTIFACT_TYPE_NAME | String   |


## Components
| R_Components     | Type    |
| ---------------- | ------- |
| *COMPONENT_ID*   | Int32   |
| PROJECT_ID       | Int32   |
| NAME             | String  |
| IS_DELETED       | Boolean |
| IS_ACTIVE        | Boolean |
| PROJECT_NAME     | String  |
| PROJECT_GROUP_ID | Int32   |

## Custom Lists
| R_CustomLists             | Type    |
| ------------------------- | ------- |
| *CUSTOM_PROPERTY_LIST_ID* | Int32   |
| PROJECT_ID                | Int32   |
| NAME                      | String  |
| IS_ACTIVE                 | Boolean |
| IS_SORTED_ON_VALUE        | Boolean |
| PROJECT_NAME              | String  |
| PROJECT_IS_ACTIVE         | Boolean |
| PROJECT_TEMPLATE_ID       | Int32   |

## Custom List Values
| R_CustomListValues                | Type    |
| --------------------------------- | ------- |
| *CUSTOM_PROPERTY_VALUE_ID*        | Int32   |
| CUSTOM_PROPERTY_LIST_ID           | Int32   |
| NAME                              | String  |
| PROJECT_ID                        | Int32   |
| CUSTOM_PROPERTY_LIST_NAME         | String  |
| CUSTOM_PROPERTY_LIST_IS_ACTIVE    | Boolean |
| PROJECT_NAME                      | String  |
| PROJECT_IS_ACTIVE                 | Boolean |
| IS_ACTIVE                         | Boolean |
| IS_DELETED                        | Boolean |
| DEPENDENT_CUSTOM_PROPERTY_LIST_ID | Int32   |
| PARENT_CUSTOM_PROPERTY_VALUE_ID   | Int32   |

## Custom Property Definitions
| R_CustomPropertyDefinitions  | Type    |
| ---------------------------- | ------- |
| *CUSTOM_PROPERTY_ID*         | Int32   |
| CUSTOM_PROPERTY_TYPE_ID      | Int32   |
| PROJECT_ID                   | Int32   |
| ARTIFACT_TYPE_ID             | Int32   |
| NAME                         | String  |
| PROPERTY_NUMBER              | Int32   |
| IS_DELETED                   | Boolean |
| CUSTOM_PROPERTY_LIST_ID      | Int32   |
| LEGACY_NAME                  | String  |
| PROJECT_NAME                 | String  |
| PROJECT_IS_ACTIVE            | Boolean |
| ARTIFACT_TYPE_NAME           | String  |
| CUSTOM_PROPERTY_TYPE_NAME    | String  |
| CUSTOM_PROPERTY_LIST_NAME    | String  |
| DEPENDENT_CUSTOM_PROPERTY_ID | Int32   |
| PROJECT_TEMPLATE_ID          | Int32   |
| POSITION                     | Int32   |
| DESCRIPTION                  | String  |

## Document Statuses
| R_DocumentStatuses    | Type    |
| --------------------- | ------- |
| *DOCUMENT_STATUS_ID*  | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| NAME                  | String  |
| POSITION              | Int32   |
| IS_ACTIVE             | Boolean |
| IS_OPEN_STATUS        | Boolean |
| IS_DEFAULT            | Boolean |
| PROJECT_TEMPLATE_NAME | String  |

## Document Types
| R_DocumentTypes       | Type    |
| --------------------- | ------- |
| *DOCUMENT_TYPE_ID*    | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| DOCUMENT_WORKFLOW_ID  | Int32   |
| NAME                  | String  |
| DESCRIPTION           | String  |
| IS_ACTIVE             | Boolean |
| IS_DEFAULT            | Boolean |
| PROJECT_TEMPLATE_NAME | String  |

## Events
| R_Events                 | Type     |
| ------------------------ | -------- |
| EVENT_TYPE_ID            | Int32    |
| EVENT_TIME_UTC           | DateTime |
| EVENT_TIME               | DateTime |
| EVENT_CATEGORY           | String   |
| EVENT_SEQUENCE           | Decimal  |
| EVENT_OCCURRENCE         | Decimal  |
| EVENT_CODE               | Int32    |
| EVENT_DETAIL_CODE        | Int32    |
| MESSAGE                  | String   |
| APPLICATION_PATH         | String   |
| APPLICATION_VIRTUAL_PATH | String   |
| MACHINE_NAME             | String   |
| REQUEST_URL              | String   |
| EXCEPTION_TYPE           | String   |
| DETAILS                  | String   |
| EVENT_TYPE_NAME          | String   |
| EVENT_ID                 | String   |

## Global / System Custom Property Definitions
| R_GlobalCustomPropertyDefinitions | Type    |
| --------------------------------- | ------- |
| *CUSTOM_PROPERTY_ID*              | Int32   |
| CUSTOM_PROPERTY_TYPE_ID           | Int32   |
| CUSTOM_PROPERTY_TYPE_NAME         | String  |
| WORKSPACE_TYPE_ID                 | Int32   |
| WORKSPACE_TYPE_NAME               | String  |
| NAME                              | String  |
| PROPERTY_NUMBER                   | Int32   |
| IS_DELETED                        | Boolean |
| CUSTOM_PROPERTY_LIST_ID           | Int32   |
| CUSTOM_PROPERTY_LIST_NAME         | String  |
| POSITION                          | Int32   |
| DESCRIPTION                       | String  |

## Global / System Custom Property Lists
| R_GlobalCustomLists       | Type    |
| ------------------------- | ------- |
| *CUSTOM_PROPERTY_LIST_ID* | Int32   |
| NAME                      | String  |
| IS_ACTIVE                 | Boolean |
| IS_SORTED_ON_VALUE        | Boolean |

## Global / System Custom Property List Values
| R_GlobalCustomListValues       | Type    |
| ------------------------------ | ------- |
| *CUSTOM_PROPERTY_VALUE_ID*     | Int32   |
| NAME                           | String  |
| IS_ACTIVE                      | Boolean |
| IS_DELETED                     | Boolean |
| CUSTOM_PROPERTY_LIST_ID        | Int32   |
| CUSTOM_PROPERTY_LIST_NAME      | String  |
| CUSTOM_PROPERTY_LIST_IS_ACTIVE | Boolean |

## Global / System History Change-Sets
| R_Global_HistoryChangeSets | Type     |
| -------------------------- | -------- |
| *CHANGESET_ID*             | Int64    |
| USER_ID                    | Int32    |
| CHANGE_DATE                | DateTime |
| CHANGETYPE_ID              | Int32    |
| ARTIFACT_TYPE_ID           | Int32    |
| ARTIFACT_ID                | Int32    |
| ARTIFACT_DESC              | String   |
| WORKSPACE_TYPE_ID          | Int32    |
| WORKSPACE_ID               | Int32    |
| CHANGETYPE_NAME            | String   |
| USER_NAME                  | String   |
| ARTIFACT_TYPE_NAME         | String   |
| WORKSPACE_TYPE_NAME        | String   |

## Global / System History Details
| R_Global_HistoryDetails | Type     |
| ----------------------- | -------- |
| *ARTIFACT_HISTORY_ID*   | Int64    |
| FIELD_NAME              | String   |
| OLD_VALUE               | String   |
| NEW_VALUE               | String   |
| CHANGESET_ID            | Int64    |
| FIELD_TYPE_ID           | Int32    |
| CUSTOM_PROPERTY_ID      | Int32    |
| ARTIFACT_ID             | Int32    |
| USER_ID                 | Int32    |
| ARTIFACT_TYPE_ID        | Int32    |
| CHANGE_DATE             | DateTime |
| USER_NAME               | String   |
| CHANGE_NAME             | String   |
| CHANGETYPE_ID           | Int32    |
| ARTIFACT_FIELD_TYPE_ID  | Int32    |
| ARTIFACT_TYPE_NAME      | String   |

## History Change-Sets
| R_HistoryChangeSets | Type     |
| ------------------- | -------- |
| *CHANGESET_ID*      | Int32    |
| USER_ID             | Int32    |
| ARTIFACT_TYPE_ID    | Int32    |
| ARTIFACT_ID         | Int32    |
| CHANGE_DATE         | DateTime |
| CHANGETYPE_ID       | Int32    |
| PROJECT_ID          | Int32    |
| REVERT_ID           | Int32    |
| ARTIFACT_DESC       | String   |
| CHANGETYPE_NAME     | String   |
| USER_NAME           | String   |
| ARTIFACT_TYPE_NAME  | String   |
| SIGNATURE_HASH      | String   |
| MEANING             | String   |
| CHANGEAREA_ID       | Int32    |

## History Details
| R_HistoryDetails       | Type     |
| ---------------------- | -------- |
| FIELD_NAME             | String   |
| OLD_VALUE              | String   |
| FIELD_CAPTION          | String   |
| NEW_VALUE              | String   |
| OLD_VALUE_INT          | Int32    |
| OLD_VALUE_DATE         | DateTime |
| NEW_VALUE_INT          | Int32    |
| NEW_VALUE_DATE         | DateTime |
| CHANGESET_ID           | Int32    |
| FIELD_ID               | Int32    |
| CUSTOM_PROPERTY_ID     | Int32    |
| ARTIFACT_ID            | Int32    |
| USER_ID                | Int32    |
| ARTIFACT_TYPE_ID       | Int32    |
| CHANGE_DATE            | DateTime |
| CHANGER_NAME           | String   |
| CHANGE_NAME            | String   |
| CHANGETYPE_ID          | Int32    |
| ARTIFACT_HISTORY_ID    | Int32    |
| ARTIFACT_FIELD_TYPE_ID | Int32    |

## Incidents
| R_Incidents                     | Type     |
| ------------------------------- | -------- |
| *INCIDENT_ID*                   | Int32    |
| PROJECT_ID                      | Int32    |
| PRIORITY_ID                     | Int32    |
| SEVERITY_ID                     | Int32    |
| INCIDENT_STATUS_ID              | Int32    |
| INCIDENT_TYPE_ID                | Int32    |
| OPENER_ID                       | Int32    |
| OWNER_ID                        | Int32    |
| DESCRIPTION                     | String   |
| CREATION_DATE                   | DateTime |
| CLOSED_DATE                     | DateTime |
| LAST_UPDATE_DATE                | DateTime |
| DETECTED_RELEASE_ID             | Int32    |
| RESOLVED_RELEASE_ID             | Int32    |
| START_DATE                      | DateTime |
| COMPLETION_PERCENT              | Int32    |
| ESTIMATED_EFFORT                | Int32    |
| ACTUAL_EFFORT                   | Int32    |
| REMAINING_EFFORT                | Int32    |
| PROJECTED_EFFORT                | Int32    |
| IS_DELETED                      | Boolean  |
| VERIFIED_RELEASE_ID             | Int32    |
| PRIORITY_NAME                   | String   |
| PRIORITY_COLOR                  | String   |
| SEVERITY_NAME                   | String   |
| SEVERITY_COLOR                  | String   |
| INCIDENT_STATUS_NAME            | String   |
| INCIDENT_TYPE_NAME              | String   |
| OPENER_NAME                     | String   |
| OWNER_NAME                      | String   |
| DETECTED_RELEASE_VERSION_NUMBER | String   |
| RESOLVED_RELEASE_VERSION_NUMBER | String   |
| VERIFIED_RELEASE_VERSION_NUMBER | String   |
| PROJECT_GROUP_ID                | Int32    |
| PROJECT_NAME                    | String   |
| CUST_01 ... CUST_99             | String   |
| NAME                            | String   |
| IS_ATTACHMENTS                  | Boolean  |
| COMPONENT_IDS                   | String   |
| INCIDENT_STATUS_IS_OPEN_STATUS  | Boolean  |
| PROJECT_IS_ACTIVE               | Boolean  |
| INCIDENT_TYPE_IS_ISSUE          | Boolean  |
| INCIDENT_TYPE_IS_RISK           | Boolean  |
| CONCURRENCY                     | Int64    |
| RANK                            | Int32    |
| END_DATE                        | DateTime |
| DETECTED_BUILD_ID               | Int32    |
| RESOLVED_BUILD_ID               | Int32    |
| DETECTED_BUILD_NAME             | String   |
| RESOLVED_BUILD_NAME             | String   |
| TAGS                            | String   |

## Incident Priorities
| R_IncidentPriorities  | Type    |
| --------------------- | ------- |
| *PRIORITY_ID*         | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| NAME                  | String  |
| COLOR                 | String  |
| IS_ACTIVE             | Boolean |
| SCORE                 | Int32   |
| PROJECT_TEMPLATE_NAME | String  |

## Incident Severities
| R_IncidentSeverities  | Type    |
| --------------------- | ------- |
| *SEVERITY_ID*         | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| NAME                  | String  |
| COLOR                 | String  |
| IS_ACTIVE             | Boolean |
| SCORE                 | Int32   |
| PROJECT_TEMPLATE_NAME | String  |

## Incident Statuses
| R_IncidentStatuses    | Type    |
| --------------------- | ------- |
| *INCIDENT_STATUS_ID*  | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| NAME                  | String  |
| IS_ACTIVE             | Boolean |
| IS_OPEN_STATUS        | Boolean |
| IS_DEFAULT            | Boolean |
| PROJECT_TEMPLATE_NAME | String  |
| POSITION              | Int32   |
| ON_BOARD              | Boolean |

## Incident Types
| R_IncidentTypes       | Type    |
| --------------------- | ------- |
| *INCIDENT_TYPE_ID*    | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| WORKFLOW_ID           | Int32   |
| NAME                  | String  |
| IS_ACTIVE             | Boolean |
| IS_ISSUE              | Boolean |
| IS_DEFAULT            | Boolean |
| PROJECT_TEMPLATE_NAME | String  |

## Pending Test Runs
| R_PendingTestRuns      | Type     |
| ---------------------- | -------- |
| *TEST_RUNS_PENDING_ID* | Int32    |
| PROJECT_ID             | Int32    |
| TEST_SET_ID            | Int32    |
| TESTER_ID              | Int32    |
| NAME                   | String   |
| CREATION_DATE          | DateTime |
| LAST_UPDATE_DATE       | DateTime |
| COUNT_PASSED           | Int32    |
| COUNT_FAILED           | Int32    |
| COUNT_BLOCKED          | Int32    |
| COUNT_CAUTION          | Int32    |
| COUNT_NOT_RUN          | Int32    |
| COUNT_NOT_APPLICABLE   | Int32    |
| TESTER_LOGIN           | String   |
| TESTER_FULLNAME        | String   |
| TEST_SET_NAME          | String   |
| PROJECT_NAME           | String   |

## Portfolios
!!! abstract "Available in SpiraPlan only"

| R_Portfolios      | Type     |
| ----------------- | -------- |
| *PORTFOLIO_ID*    | Int32    |
| NAME              | String   |
| DESCRIPTION       | String   |
| IS_ACTIVE         | Boolean  |
| START_DATE        | DateTime |
| END_DATE          | DateTime |
| PERCENT_COMPLETE  | Int32    |
| REQUIREMENT_COUNT | Int32    |

## Program Milestones
!!! abstract "Available in SpiraPlan only"

| R_ProjectGroup_Milestones       | Type     |
| ------------------------------- | -------- |
| *PROJECT_GROUP_MILESTONE_ID*    | Int32    |
| PROJECT_GROUP_ID                | Int32    |
| TYPE_ID                         | Int32    |
| STATUS_ID                       | Int32    |
| NAME                            | String   |
| DESCRIPTION                     | String   |
| IS_DELETED                      | Boolean  |
| START_DATE                      | DateTime |
| END_DATE                        | DateTime |
| PERCENT_COMPLETE                | Int32    |
| CHILDREN_START_DATE             | DateTime |
| CHILDREN_END_DATE               | DateTime |
| PROJECT_RELEASE_COUNT           | Int32    |
| PROJECT_GROUP_REQUIREMENT_COUNT | Int32    |
| CONCURRENCY                     | Int64    |
| CREATOR_ID                      | Int32    |
| OWNER_ID                        | Int32    |
| CREATION_DATE                   | DateTime |
| LAST_UPDATED_DATE               | DateTime |
| STATUS_NAME                     | String   |
| STATUS_IS_OPEN                  | Boolean  |
| TYPE_NAME                       | String   |
| CREATOR_NAME                    | String   |
| OWNER_NAME                      | String   |
| PROJECT_GROUP_NAME              | String   |
| CUST_01 ... CUST_30             | String   |

## Program Milestone Releases
!!! abstract "Available in SpiraPlan only"

| R_ProjectGroup_Milestone_Project_Releases | Type   |
| ----------------------------------------- | ------ |
| *PROJECT_GROUP_MILESTONE_ID*              | Int32  |
| RELEASE_ID                                | Int32  |
| ARTIFACT_LINK_TYPE_ID                     | Int32  |
| PROJECT_GROUP_MILESTONE_NAME              | String |
| RELEASE_NAME                              | String |
| ARTIFACT_LINK_TYPE_NAME                   | String |

## Program Milestone Statuses
!!! abstract "Available in SpiraPlan only"

| R_ProjectGroup_Milestone_Statuses | Type    |
| --------------------------------- | ------- |
| *STATUS_ID*                       | Int32   |
| NAME                              | String  |
| IS_ACTIVE                         | Boolean |
| IS_DELETED                        | Boolean |
| IS_DEFAULT                        | Boolean |
| IS_OPEN                           | Boolean |

## Program Milestone Types
!!! abstract "Available in SpiraPlan only"

| R_ProjectGroup_Milestone_Types | Type    |
| ------------------------------ | ------- |
| *TYPE_ID*                      | Int32   |
| NAME                           | String  |
| IS_ACTIVE                      | Boolean |
| IS_DELETED                     | Boolean |
| IS_DEFAULT                     | Boolean |

## Project Artifacts Sharing 
Retrieves data about cross product associations

| R_ProjectArtifactSharings | Type   |
| ------------------------- | ------ |
| SOURCE_PROJECT_ID         | Int32  |
| DEST_PROJECT_ID           | Int32  |
| ARTIFACT_TYPE_ID          | Int32  |
| SOURCE_PROJECT_NAME       | String |
| DEST_PROJECT_NAME         | String |
| ARTIFACT_TYPE_NAME        | String |
| ARTIFACT_TYPE_PREFIX      | String |

## Projects (Products)
| R_Projects                  | Type     |
| --------------------------- | -------- |
| *PROJECT_ID*                | Int32    |
| PROJECT_GROUP_ID            | Int32    |
| NAME                        | String   |
| DESCRIPTION                 | String   |
| CREATION_DATE               | DateTime |
| WEBSITE                     | String   |
| WORKING_HOURS               | Int32    |
| WORKING_DAYS                | Int32    |
| NON_WORKING_HOURS           | Int32    |
| TASK_DEFAULT_EFFORT         | Int32    |
| PROJECT_GROUP_NAME          | String   |
| PROJECT_GROUP_DESCRIPTION   | String   |
| IS_ACTIVE                   | Boolean  |
| IS_TIME_TRACK_INCIDENTS     | Boolean  |
| IS_TIME_TRACK_TASKS         | Boolean  |
| IS_EFFORT_INCIDENTS         | Boolean  |
| IS_EFFORT_TASKS             | Boolean  |
| IS_TASKS_AUTO_CREATE        | Boolean  |
| REQ_DEFAULT_ESTIMATE        | Decimal  |
| REQ_POINT_EFFORT            | Int32    |
| IS_REQ_STATUS_BY_TASKS      | Boolean  |
| IS_REQ_STATUS_BY_TEST_CASES | Boolean  |
| IS_EFFORT_TEST_CASES        | Boolean  |
| IS_REQ_STATUS_AUTO_PLANNED  | Boolean  |
| PROJECT_TEMPLATE_ID         | Int32    |
| START_DATE                  | DateTime |
| END_DATE                    | DateTime |
| PERCENT_COMPLETE            | Int32    |
| REQUIREMENT_COUNT           | Int32    |
| INFLECTRA_AI_ENABLED        | String   |
| CUST_01 ... CUST_30         | String   |
| CONCURRENCY                 | Int64    |

## Project Groups (Programs)
| R_ProjectGroups     | Type     |
| ------------------- | -------- |
| *PROJECT_GROUP_ID*  | Int32    |
| NAME                | String   |
| DESCRIPTION         | String   |
| WEBSITE             | String   |
| PROJECT_TEMPLATE_ID | Int32    |
| IS_ACTIVE           | Boolean  |
| IS_DEFAULT          | Boolean  |
| PERCENT_COMPLETE    | Int32    |
| START_DATE          | DateTime |
| END_DATE            | DateTime |
| PORTFOLIO_ID        | Int32    |
| REQUIREMENT_COUNT   | Int32    |

## Project Group Membership (Program Membership)
| R_ProjectGroup_MembershipUsers | Type    |
| ------------------------------ | ------- |
| PROJECT_GROUP_ID               | Int32   |
| PROJECT_GROUP_NAME             | String  |
| PROJECT_GROUP_IS_ACTIVE        | Boolean |
| PROJECT_GROUP_ROLE_ID          | Int32   |
| PROJECT_GROUP_ROLE_NAME        | String  |
| PROJECT_GROUP_ROLE_ISACTIVE    | Boolean |
| USER_ID                        | Int32   |
| USER_NAME                      | String  |
| USER_FULLNAME                  | String  |

## Project (Product) Membership
| R_ProjectMembership | Type    |
| ------------------- | ------- |
| PROJECT_ID          | Int32   |
| USER_ID             | Int32   |
| PROJECT_ROLE_ID     | Int32   |
| PROJECT_NAME        | String  |
| PROJECT_ROLE_NAME   | String  |
| USER_NAME           | String  |
| FIRST_NAME          | String  |
| LAST_NAME           | String  |
| DEPARTMENT          | String  |
| IS_SYSTEM_ADMIN     | Boolean |

## Project Release Resources
| R_ProjectReleaseResources | Type  |
| ------------------------- | ----- |
| PROJECT_ID                | Int32 |
| USER_ID                   | Int32 |
| RELEASE_ID                | Int32 |
| INCIDENT_EFFORT           | Int32 |
| TASK_EFFORT               | Int32 |

## Project Roles
| R_ProjectRoles           | Type    |
| ------------------------ | ------- |
| *PROJECT_ROLE_ID*        | Int32   |
| NAME                     | String  |
| IS_ACTIVE                | Boolean |
| DESCRIPTION              | String  |
| IS_ADMIN                 | Boolean |
| IS_DISCUSSIONS_ADD       | Boolean |
| IS_SOURCE_CODE_VIEW      | Boolean |
| IS_SOURCE_CODE_EDIT      | Boolean |
| IS_DOCUMENT_FOLDERS_EDIT | Boolean |
| IS_LIMITED_VIEW          | Boolean |
| IS_TEMPLATE_ADMIN        | Boolean |
| ARTIFACT_TYPE_ID         | Int32   |
| ARTIFACT                 | String  |
| PERMISSION               | String  |

## Project (Product) Tags
| R_ProjectTags | Type   |
| ------------- | ------ |
| PROJECT_ID    | Int32  |
| TAG           | String |
| PROJECT_NAME  | String |

## Project Teams Users
!!! abstract "Available in SpiraPlan only"

| R_ProjectTeamUsers | Type   |
| ------------------ | ------ |
| PROJECT_ID         | Int32  |
| PROJECT_NAME       | String |
| USER_ID            | Int32  |
| USER_NAME          | String |
| TEAM_ID            | Int32  |
| TEAM_NAME          | String |

## Project (Product) Templates
| R_ProjectTemplates    | Type    |
| --------------------- | ------- |
| *PROJECT_TEMPLATE_ID* | Int32   |
| NAME                  | String  |
| DESCRIPTION           | String  |
| IS_ACTIVE             | Boolean |

## Releases
| R_Releases               | Type     |
| ------------------------ | -------- |
| *RELEASE_ID*             | Int32    |
| PROJECT_ID               | Int32    |
| CREATOR_ID               | Int32    |
| NAME                     | String   |
| VERSION_NUMBER           | String   |
| DESCRIPTION              | String   |
| INDENT_LEVEL             | String   |
| CREATION_DATE            | DateTime |
| LAST_UPDATE_DATE         | DateTime |
| START_DATE               | DateTime |
| END_DATE                 | DateTime |
| RESOURCE_COUNT           | Decimal  |
| DAYS_NON_WORKING         | Decimal  |
| PLANNED_EFFORT           | Int32    |
| AVAILABLE_EFFORT         | Int32    |
| COUNT_BLOCKED            | Int32    |
| COUNT_CAUTION            | Int32    |
| COUNT_FAILED             | Int32    |
| COUNT_NOT_APPLICABLE     | Int32    |
| COUNT_NOT_RUN            | Int32    |
| COUNT_PASSED             | Int32    |
| TASK_COUNT               | Int32    |
| TASK_PERCENT_ON_TIME     | Int32    |
| TASK_PERCENT_LATE_FINISH | Int32    |
| TASK_PERCENT_NOT_START   | Int32    |
| TASK_PERCENT_LATE_START  | Int32    |
| TASK_ESTIMATED_EFFORT    | Int32    |
| TASK_ACTUAL_EFFORT       | Int32    |
| TASK_PROJECTED_EFFORT    | Int32    |
| TASK_REMAINING_EFFORT    | Int32    |
| IS_DELETED               | Boolean  |
| CREATOR_NAME             | String   |
| FULL_NAME                | String   |
| PROJECT_NAME             | String   |
| PROJECT_GROUP_ID         | Int32    |
| CUST_01 ... CUST_99      | String   |
| RELEASE_TYPE_ID          | Int32    |
| RELEASE_STATUS_ID        | Int32    |
| OWNER_ID                 | Int32    |
| IS_SUMMARY               | Boolean  |
| IS_ATTACHMENTS           | Boolean  |
| OWNER_NAME               | String   |
| RELEASE_TYPE_NAME        | String   |
| RELEASE_STATUS_NAME      | String   |
| CONCURRENCY              | Int64    |
| PERCENT_COMPLETE         | Int32    |
| PLANNED_POINTS           | Decimal  |
| REQUIREMENT_POINTS       | Decimal  |
| REQUIREMENT_COUNT        | Int32    |
| TAGS                     | String   |
| BRANCH_ID                | Int32    |

## Release Test Case Mapping
| R_ReleaseTestCases     | Type     |
| ---------------------- | -------- |
| RELEASE_ID             | Int32    |
| TEST_CASE_ID           | Int32    |
| RELEASE_NAME           | String   |
| RELEASE_VERSION_NUMBER | String   |
| TEST_CASE_NAME         | String   |
| PROJECT_ID             | Int32    |
| PROJECT_NAME           | String   |
| RELEASE_TYPE_ID        | Int32    |
| RELEASE_TYPE_NAME      | String   |
| EXECUTION_STATUS_ID    | Int32    |
| EXECUTION_DATE         | DateTime |
| ACTUAL_DURATION        | Int32    |

## Requirements
| R_Requirements           | Type     |
| ------------------------ | -------- |
| *REQUIREMENT_ID*         | Int32    |
| AUTHOR_ID                | Int32    |
| OWNER_ID                 | Int32    |
| RELEASE_ID               | Int32    |
| PROJECT_ID               | Int32    |
| IMPORTANCE_ID            | Int32    |
| NAME                     | String   |
| CREATION_DATE            | DateTime |
| INDENT_LEVEL             | String   |
| DESCRIPTION              | String   |
| LAST_UPDATE_DATE         | DateTime |
| COVERAGE_COUNT_TOTAL     | Int32    |
| COVERAGE_COUNT_PASSED    | Int32    |
| COVERAGE_COUNT_FAILED    | Int32    |
| COVERAGE_COUNT_CAUTION   | Int32    |
| COVERAGE_COUNT_BLOCKED   | Int32    |
| TASK_COUNT               | Int32    |
| TASK_ESTIMATED_EFFORT    | Int32    |
| TASK_ACTUAL_EFFORT       | Int32    |
| TASK_PROJECTED_EFFORT    | Int32    |
| TASK_REMAINING_EFFORT    | Int32    |
| TASK_PERCENT_ON_TIME     | Int32    |
| TASK_PERCENT_LATE_FINISH | Int32    |
| TASK_PERCENT_NOT_START   | Int32    |
| TASK_PERCENT_LATE_START  | Int32    |
| IS_DELETED               | Boolean  |
| AUTHOR_NAME              | String   |
| OWNER_NAME               | String   |
| IMPORTANCE_NAME          | String   |
| RELEASE_VERSION_NUMBER   | String   |
| PROJECT_NAME             | String   |
| PROJECT_GROUP_ID         | Int32    |
| CUST_01 ... CUST_99      | String   |
| REQUIREMENT_TYPE_ID      | Int32    |
| REQUIREMENT_STATUS_ID    | Int32    |
| COMPONENT_ID             | Int32    |
| IS_SUMMARY               | Boolean  |
| IS_ATTACHMENTS           | Boolean  |
| CONCURRENCY              | Int64    |
| REQUIREMENT_STATUS_NAME  | String   |
| REQUIREMENT_TYPE_NAME    | String   |
| COMPONENT_NAME           | String   |
| ESTIMATE_POINTS          | Decimal  |
| ESTIMATED_EFFORT         | Int32    |
| RANK                     | Int32    |
| GOAL_ID                  | Int32    |
| START_DATE               | DateTime |
| END_DATE                 | DateTime |
| PERCENT_COMPLETE         | Int32    |
| TAGS                     | String   |
| IS_SUSPECT               | Boolean  |

## Requirement Importances
| R_Requirement_Importance | Type    |
| ------------------------ | ------- |
| *IMPORTANCE_ID*          | Int32   |
| PROJECT_TEMPLATE_ID      | Int32   |
| NAME                     | String  |
| IS_ACTIVE                | Boolean |
| COLOR                    | String  |
| SCORE                    | Int32   |

## Requirement Incidents
| R_RequirementIncidents | Type    |
| ---------------------- | ------- |
| REQUIREMENT_ID         | Int32   |
| INCIDENT_ID            | Int32   |
| DETECTED_RELEASE_ID    | Int32   |
| IS_OPEN_STATUS         | Boolean |

## Requirement Incidents - Extended
For normal use we strongly recommend using the standard artifact association view above. This extended view adds the artifact names, which can be very helpful, but will make the reports using it run much slower. 

| R_RequirementIncidentExtended | Type    |
| ----------------------------- | ------- |
| REQUIREMENT_ID                | Int32   |
| INCIDENT_ID                   | Int32   |
| DETECTED_RELEASE_ID           | Int32   |
| IS_OPEN_STATUS                | Boolean |
| REQUIREMENT_NAME              | String  |
| INCIDENT_NAME                 | String  |

## Requirement Steps
| R_RequirementSteps           | Type     |
| ---------------------------- | -------- |
| REQUIREMENT_ID               | Int32    |
| POSITION                     | Int32    |
| DESCRIPTION                  | String   |
| IS_DELETED                   | Boolean  |
| CREATION_DATE                | DateTime |
| LAST_UPDATE_DATE             | DateTime |
| CONCURRENCY                  | Int64    |
| REQUIREMENT_NAME             | String   |
| REQUIREMENT_LAST_UPDATE_DATE | DateTime |
| PROJECT_IS_ACTIVE            | Boolean  |
| PROJECT_PROJECT_GROUP_ID     | Int32    |
| PROJECT_NAME                 | String   |
| REQUIREMENT_STEP_ID          | Int32    |

## Requirement Test Case Coverage
| R_RequirementTestCases | Type   |
| ---------------------- | ------ |
| REQUIREMENT_ID         | Int32  |
| TEST_CASE_ID           | Int32  |
| REQUIREMENT_NAME       | String |
| TEST_CASE_NAME         | String |
| PROJECT_ID             | Int32  |
| PROJECT_NAME           | String |

## Requirement Test Step Coverage
| R_RequirementTestSteps | Type   |
| ---------------------- | ------ |
| TEST_STEP_ID           | Int32  |
| REQUIREMENT_NAME       | String |
| POSITION               | Int32  |
| STEP_DESCRIPTION       | String |
| EXPECTED_RESULT        | String |
| SAMPLE_DATA            | String |
| PROJECT_ID             | Int32  |
| PROJECT_NAME           | String |
| REQUIREMENT_ID         | Int32  |

## Requirement Types
| R_RequirementTypes      | Type    |
| ----------------------- | ------- |
| *REQUIREMENT_TYPE_ID*   | Int32   |
| REQUIREMENT_WORKFLOW_ID | Int32   |
| PROJECT_TEMPLATE_ID     | Int32   |
| NAME                    | String  |
| ICON                    | String  |
| IS_ACTIVE               | Boolean |
| IS_STEPS                | Boolean |
| IS_DEFAULT              | Boolean |
| IS_KEY_TYPE             | Boolean |
| PROJECT_TEMPLATE_NAME   | String  |

## Risks
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_Risks                  | Type     |
| ------------------------ | -------- |
| *RISK_ID*                | Int32    |
| RISK_IMPACT_ID           | Int32    |
| RISK_STATUS_ID           | Int32    |
| RISK_PROBABILITY_ID      | Int32    |
| RISK_TYPE_ID             | Int32    |
| PROJECT_ID               | Int32    |
| CREATOR_ID               | Int32    |
| OWNER_ID                 | Int32    |
| PROJECT_GROUP_ID         | Int32    |
| RELEASE_ID               | Int32    |
| COMPONENT_ID             | Int32    |
| NAME                     | String   |
| DESCRIPTION              | String   |
| IS_DELETED               | Boolean  |
| CREATION_DATE            | DateTime |
| LAST_UPDATE_DATE         | DateTime |
| CONCURRENCY              | Int64    |
| REVIEW_DATE              | DateTime |
| GOAL_ID                  | Int32    |
| CLOSED_DATE              | DateTime |
| IS_ATTACHMENTS           | Boolean  |
| RISK_PROBABILITY_NAME    | String   |
| RISK_PROBABILITY_COLOR   | String   |
| RISK_PROBABILITY_SCORE   | Int32    |
| RISK_IMPACT_NAME         | String   |
| RISK_IMPACT_COLOR        | String   |
| RISK_IMPACT_SCORE        | Int32    |
| RISK_EXPOSURE            | Int32    |
| RISK_STATUS_NAME         | String   |
| RISK_STATUS_IS_OPEN      | Boolean  |
| RISK_TYPE_NAME           | String   |
| CREATOR_NAME             | String   |
| OWNER_NAME               | String   |
| RELEASE_VERSION_NUMBER   | String   |
| RELEASE_NAME             | String   |
| COMPONENT_NAME           | String   |
| GOAL_NAME                | String   |
| PROJECT_IS_ACTIVE        | Boolean  |
| PROJECT_PROJECT_GROUP_ID | Int32    |
| PROJECT_NAME             | String   |
| CUST_01 ... CUST_99      | String   |
| TAGS                     | String   |
| RISK_DETECTABILITY_ID    | Int32    |
| RANK                     | Int32    |

## Risk Impacts
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_RiskImpacts         | Type    |
| --------------------- | ------- |
| *RISK_IMPACT_ID*      | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| NAME                  | String  |
| COLOR                 | String  |
| IS_ACTIVE             | Boolean |
| POSITION              | Int32   |
| SCORE                 | Int32   |
| PROJECT_TEMPLATE_NAME | String  |

## Risk Mitigations
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_RiskMitigations        | Type     |
| ------------------------ | -------- |
| RISK_ID                  | Int32    |
| *RISK_MITIGATION_ID*     | Int32    |
| POSITION                 | Int32    |
| DESCRIPTION              | String   |
| IS_DELETED               | Boolean  |
| CREATION_DATE            | DateTime |
| LAST_UPDATE_DATE         | DateTime |
| CONCURRENCY              | Int64    |
| IS_ACTIVE                | Boolean  |
| REVIEW_DATE              | DateTime |
| RISK_NAME                | String   |
| RISK_REVIEW_DATE         | DateTime |
| PROJECT_IS_ACTIVE        | Boolean  |
| PROJECT_PROJECT_GROUP_ID | Int32    |
| PROJECT_NAME             | String   |
| PROJECT_ID               | Int32    |

## Risk Probabilities
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_RiskProbabilities   | Type    |
| --------------------- | ------- |
| *RISK_PROBABILITY_ID* | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| NAME                  | String  |
| COLOR                 | String  |
| IS_ACTIVE             | Boolean |
| POSITION              | Int32   |
| SCORE                 | Int32   |
| PROJECT_TEMPLATE_NAME | String  |

## Risk Statuses
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_RiskStatuses        | Type    |
| --------------------- | ------- |
| *RISK_STATUS_ID*      | Int32   |
| NAME                  | String  |
| IS_ACTIVE             | Boolean |
| IS_DEFAULT            | Boolean |
| IS_OPEN               | Boolean |
| POSITION              | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| PROJECT_TEMPLATE_NAME | String  |

## Risk Types
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_RiskTypes           | Type    |
| --------------------- | ------- |
| *RISK_TYPE_ID*        | Int32   |
| NAME                  | String  |
| IS_ACTIVE             | Boolean |
| IS_DEFAULT            | Boolean |
| PROJECT_TEMPLATE_ID   | Int32   |
| RISK_WORKFLOW_ID      | Int32   |
| PROJECT_TEMPLATE_NAME | String  |

## Source Code Associations
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_SourceCodeAssociations         | Type     |
| -------------------------------- | -------- |
| ARTIFACT_SOURCE_CODE_REVISION_ID | Int32    |
| ARTIFACT_TYPE_ID                 | Int32    |
| ARTIFACT_ID                      | Int32    |
| REVISION_KEY                     | String   |
| COMMENT                          | String   |
| CREATION_DATE                    | DateTime |
| ARTIFACT_TYPE_NAME               | String   |
| ARTIFACT_TYPE_PREFIX             | String   |


## Source Code Commits
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_SourceCodeCommits                | Type     |
| ---------------------------------- | -------- |
| VERSION_CONTROL_SYSTEM_ID          | Int32    |
| PROJECT_ID                         | Int32    |
| *REVISION_ID*                      | Int32    |
| NAME                               | String   |
| REVISION_KEY                       | String   |
| AUTHOR_NAME                        | String   |
| MESSAGE                            | String   |
| UPDATE_DATE                        | DateTime |
| CONTENT_CHANGED                    | Boolean  |
| PROPERTIES_CHANGED                 | Boolean  |
| VERSION_CONTROL_SYSTEM_NAME        | String   |
| VERSION_CONTROL_SYSTEM_DESCRIPTION | String   |
| VERSION_CONTROL_SYSTEM_IS_ACTIVE   | Boolean  |
| PROJECT_NAME                       | String   |
| BRANCH_NAME                        | String   |
| BRANCH_PATH                        | String   |
| BRANCH_IS_HEAD                     | Boolean  |

## Tasks
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_Tasks                | Type     |
| ---------------------- | -------- |
| *TASK_ID*              | Int32    |
| TASK_STATUS_ID         | Int32    |
| PROJECT_ID             | Int32    |
| REQUIREMENT_ID         | Int32    |
| RELEASE_ID             | Int32    |
| CREATOR_ID             | Int32    |
| OWNER_ID               | Int32    |
| TASK_PRIORITY_ID       | Int32    |
| NAME                   | String   |
| DESCRIPTION            | String   |
| CREATION_DATE          | DateTime |
| LAST_UPDATE_DATE       | DateTime |
| START_DATE             | DateTime |
| END_DATE               | DateTime |
| COMPLETION_PERCENT     | Int32    |
| ESTIMATED_EFFORT       | Int32    |
| ACTUAL_EFFORT          | Int32    |
| PROJECTED_EFFORT       | Int32    |
| REMAINING_EFFORT       | Int32    |
| IS_DELETED             | Boolean  |
| TASK_STATUS_NAME       | String   |
| OWNER_NAME             | String   |
| CREATOR_NAME           | String   |
| TASK_PRIORITY_NAME     | String   |
| PROJECT_NAME           | String   |
| PROJECT_GROUP_ID       | Int32    |
| RELEASE_VERSION_NUMBER | String   |
| CUST_01 ... CUST_99    | String   |
| TASK_TYPE_ID           | Int32    |
| TASK_FOLDER_ID         | Int32    |
| IS_ATTACHMENTS         | Boolean  |
| CONCURRENCY            | Int64    |
| REQUIREMENT_NAME       | String   |
| TASK_TYPE_NAME         | String   |
| COMPONENT_ID           | Int32    |
| COMPONENT_NAME         | String   |
| RISK_ID                | Int32    |
| TAGS                   | String   |
| RANK                   | Int32    |

## Task Folders
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_TaskFolders         | Type   |
| --------------------- | ------ |
| *TASK_FOLDER_ID*      | Int32  |
| PROJECT_ID            | Int32  |
| NAME                  | String |
| PARENT_TASK_FOLDER_ID | Int32  |
| HIERARCHY_LEVEL       | Int32  |
| INDENT_LEVEL          | String |

## Task Priorities
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_TaskPriorities      | Type    |
| --------------------- | ------- |
| *TASK_PRIORITY_ID*    | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| NAME                  | String  |
| IS_ACTIVE             | Boolean |
| COLOR                 | String  |
| SCORE                 | Int32   |
| PROJECT_TEMPLATE_NAME | String  |

## Task Types
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_TaskTypes           | Type    |
| --------------------- | ------- |
| *TASK_TYPE_ID*        | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| TASK_WORKFLOW_ID      | Int32   |
| NAME                  | String  |
| POSITION              | Int32   |
| IS_ACTIVE             | Boolean |
| IS_DEFAULT            | Boolean |
| IS_PULL_REQUEST       | Boolean |
| PROJECT_TEMPLATE_NAME | String  |

## Teams
!!! abstract "Available in SpiraPlan only"

| R_Teams     | Type    |
| ----------- | ------- |
| *TEAM_ID*   | Int32   |
| NAME        | String  |
| DESCRIPTION | String  |
| IS_ACTIVE   | Boolean |
| IS_DELETED  | Boolean |

## Test Cases
| R_TestCases              | Type     |
| ------------------------ | -------- |
| *TEST_CASE_ID*           | Int32    |
| EXECUTION_STATUS_ID      | Int32    |
| TEST_CASE_PRIORITY_ID    | Int32    |
| PROJECT_ID               | Int32    |
| AUTHOR_ID                | Int32    |
| NAME                     | String   |
| OWNER_ID                 | Int32    |
| DESCRIPTION              | String   |
| EXECUTION_DATE           | DateTime |
| CREATION_DATE            | DateTime |
| LAST_UPDATE_DATE         | DateTime |
| AUTOMATION_ENGINE_ID     | Int32    |
| AUTOMATION_ATTACHMENT_ID | Int32    |
| ESTIMATED_DURATION       | Int32    |
| IS_DELETED               | Boolean  |
| EXECUTION_STATUS_NAME    | String   |
| TEST_CASE_PRIORITY_NAME  | String   |
| AUTHOR_NAME              | String   |
| OWNER_NAME               | String   |
| AUTOMATION_ENGINE_NAME   | String   |
| PROJECT_NAME             | String   |
| PROJECT_GROUP_ID         | Int32    |
| CUST_01 ... CUST_99      | String   |
| CONCURRENCY              | Int64    |
| TEST_CASE_STATUS_ID      | Int32    |
| TEST_CASE_TYPE_ID        | Int32    |
| TEST_CASE_FOLDER_ID      | Int32    |
| IS_ATTACHMENTS           | Boolean  |
| IS_TEST_STEPS            | Boolean  |
| ACTUAL_DURATION          | Int32    |
| TEST_CASE_STATUS_NAME    | String   |
| TEST_CASE_TYPE_NAME      | String   |
| COMPONENT_IDS            | String   |
| IS_SUSPECT               | Boolean  |
| TAGS                     | String   |
| RANK                     | Int32    |

## Test Case Folders
| R_TestCaseFolders          | Type     |
| -------------------------- | -------- |
| *TEST_CASE_FOLDER_ID*      | Int32    |
| PARENT_TEST_CASE_FOLDER_ID | Int32    |
| PROJECT_ID                 | Int32    |
| NAME                       | String   |
| DESCRIPTION                | String   |
| EXECUTION_DATE             | DateTime |
| LAST_UPDATE_DATE           | DateTime |
| ESTIMATED_DURATION         | Int32    |
| ACTUAL_DURATION            | Int32    |
| COUNT_PASSED               | Int32    |
| COUNT_FAILED               | Int32    |
| COUNT_BLOCKED              | Int32    |
| COUNT_CAUTION              | Int32    |
| COUNT_NOT_RUN              | Int32    |
| COUNT_NOT_APPLICABLE       | Int32    |
| PROJECT_NAME               | String   |
| PROJECT_GROUP_ID           | Int32    |
| HIERARCHY_LEVEL            | Int32    |
| INDENT_LEVEL               | String   |

## Test Case Incidents
| R_TestCaseIncidents | Type    |
| ------------------- | ------- |
| TEST_CASE_ID        | Int32   |
| INCIDENT_ID         | Int32   |
| DETECTED_RELEASE_ID | Int32   |
| RESOLVED_RELEASE_ID | Int32   |
| VERIFIED_RELEASE_ID | Int32   |
| IS_OPEN_STATUS      | Boolean |

## Test Case Priorities
| R_TestCasePriorities  | Type    |
| --------------------- | ------- |
| TEST_CASE_PRIORITY_ID | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| NAME                  | String  |
| IS_ACTIVE             | Boolean |
| COLOR                 | String  |
| SCORE                 | Int32   |

## Test Case Types
| R_TestCaseTypes       | Type    |
| --------------------- | ------- |
| *TEST_CASE_TYPE_ID*   | Int32   |
| PROJECT_TEMPLATE_ID   | Int32   |
| TEST_CASE_WORKFLOW_ID | Int32   |
| NAME                  | String  |
| IS_ACTIVE             | Boolean |
| POSITION              | Int32   |
| IS_DEFAULT            | Boolean |
| IS_EXPLORATORY        | Boolean |
| IS_BDD                | Boolean |
| PROJECT_TEMPLATE_NAME | String  |

## Test Configuration Entries
| R_TestConfigurationEntries       | Type    |
| -------------------------------- | ------- |
| TEST_CONFIGURATION_ID            | Int32   |
| TEST_CONFIGURATION_SET_ID        | Int32   |
| POSITION                         | Int32   |
| TEST_CONFIGURATION_SET_NAME      | String  |
| IS_TEST_CONFIGURATION_SET_ACTIVE | Boolean |
| CUSTOM_PROPERTY_VALUE_ID         | Int32   |
| TEST_CASE_PARAMETER_NAME         | String  |
| TEST_CASE_PARAMETER_VALUE        | String  |
| PROJECT_NAME                     | String  |
| PROJECT_GROUP_ID                 | Int32   |
| PROJECT_ID                       | Int32   |

## Test Configuration Sets
| R_TestConfigurationSets     | Type     |
| --------------------------- | -------- |
| *TEST_CONFIGURATION_SET_ID* | Int32    |
| PROJECT_ID                  | Int32    |
| NAME                        | String   |
| DESCRIPTION                 | String   |
| IS_ACTIVE                   | Boolean  |
| IS_DELETED                  | Boolean  |
| CREATION_DATE               | DateTime |
| LAST_UPDATED_DATE           | DateTime |
| CONCURRENCY                 | Int64    |
| PROJECT_NAME                | String   |
| PROJECT_GROUP_ID            | Int32    |

## Test Runs
Note that the TEST_RUN_TYPE_ID can have two values: 1 = Manual, 2 = Automated

| R_TestRuns             | Type     |
| ---------------------- | -------- |
| *TEST_RUN_ID*          | Int32    |
| TEST_CASE_ID           | Int32    |
| NAME                   | String   |
| DESCRIPTION            | String   |
| ESTIMATED_DURATION     | Int32    |
| ACTUAL_DURATION        | Int32    |
| TEST_RUN_TYPE_ID       | Int32    |
| TESTER_ID              | Int32    |
| EXECUTION_STATUS_ID    | Int32    |
| START_DATE             | DateTime |
| END_DATE               | DateTime |
| RUNNER_NAME            | String   |
| RUNNER_TEST_NAME       | String   |
| RUNNER_ASSERT_COUNT    | Int32    |
| RUNNER_MESSAGE         | String   |
| RUNNER_STACK_TRACE     | String   |
| EXECUTION_STATUS_NAME  | String   |
| TESTER_NAME            | String   |
| TEST_RUNS_PENDING_ID   | Int32    |
| RELEASE_ID             | Int32    |
| TEST_SET_ID            | Int32    |
| TEST_SET_TEST_CASE_ID  | Int32    |
| RELEASE_NAME           | String   |
| RELEASE_VERSION_NUMBER | String   |
| TEST_SET_NAME          | String   |
| TEST_RUN_TYPE_NAME     | String   |
| AUTOMATION_HOST_ID     | Int32    |
| AUTOMATION_HOST_NAME   | String   |
| AUTOMATION_ENGINE_ID   | Int32    |
| BUILD_ID               | Int32    |
| BUILD_NAME             | String   |
| TEST_RUN_FORMAT_ID     | Int32    |
| PROJECT_NAME           | String   |
| PROJECT_GROUP_ID       | Int32    |
| CUST_01 ... CUST_99    | String   |
| IS_ATTACHMENTS         | Boolean  |
| IS_DELETED             | Boolean  |
| CONCURRENCY            | Int64    |
| PROJECT_ID             | Int32    |
| CHANGESET_ID           | Int64    |
| TEST_CONFIGURATION_ID  | Int32    |
| TAGS                   | String   |

## Test Run Incidents
| R_TestRunIncidents  | Type    |
| ------------------- | ------- |
| TEST_RUN_ID         | Int32   |
| INCIDENT_ID         | Int32   |
| DETECTED_RELEASE_ID | Int32   |
| RESOLVED_RELEASE_ID | Int32   |
| VERIFIED_RELEASE_ID | Int32   |
| IS_OPEN_STATUS      | Boolean |
| TEST_STEP_ID        | Int32   |
| TEST_RUN_STEP_ID    | Int32   |

## Test Run Steps
| R_TestRunSteps        | Type     |
| --------------------- | -------- |
| *TEST_RUN_STEP_ID*    | Int32    |
| EXECUTION_STATUS_ID   | Int32    |
| TEST_CASE_ID          | Int32    |
| TEST_STEP_ID          | Int32    |
| TEST_RUN_ID           | Int32    |
| DESCRIPTION           | String   |
| POSITION              | Int32    |
| EXPECTED_RESULT       | String   |
| SAMPLE_DATA           | String   |
| ACTUAL_RESULT         | String   |
| EXECUTION_STATUS_NAME | String   |
| TEST_CASE_NAME        | String   |
| PROJECT_ID            | Int32    |
| PROJECT_NAME          | String   |
| PROJECT_GROUP_ID      | Int32    |
| START_DATE            | DateTime |
| END_DATE              | DateTime |
| ACTUAL_DURATION       | Int32    |

## Test Sets
| R_TestSets                  | Type     |
| --------------------------- | -------- |
| *TEST_SET_ID*               | Int32    |
| PROJECT_ID                  | Int32    |
| RELEASE_ID                  | Int32    |
| TEST_SET_STATUS_ID          | Int32    |
| CREATOR_ID                  | Int32    |
| OWNER_ID                    | Int32    |
| AUTOMATION_HOST_ID          | Int32    |
| TEST_RUN_TYPE_ID            | Int32    |
| RECURRENCE_ID               | Int32    |
| NAME                        | String   |
| DESCRIPTION                 | String   |
| CREATION_DATE               | DateTime |
| PLANNED_DATE                | DateTime |
| LAST_UPDATE_DATE            | DateTime |
| IS_DELETED                  | Boolean  |
| CONCURRENCY                 | Int64    |
| RELEASE_VERSION_NUMBER      | String   |
| PROJECT_NAME                | String   |
| TEST_CASE_COUNT             | Int32    |
| TEST_SET_STATUS_NAME        | String   |
| CREATOR_NAME                | String   |
| OWNER_NAME                  | String   |
| PROJECT_ACTIVE_YN           | String   |
| PROJECT_IS_ACTIVE           | Boolean  |
| AUTOMATION_HOST_NAME        | String   |
| TEST_RUN_TYPE_NAME          | String   |
| RECURRENCE_NAME             | String   |
| PROJECT_GROUP_ID            | Int32    |
| CUST_01 ... CUST_99         | String   |
| TEST_SET_FOLDER_ID          | Int32    |
| IS_ATTACHMENTS              | Boolean  |
| BUILD_EXECUTE_TIME_INTERVAL | Int32    |
| ESTIMATED_DURATION          | Int32    |
| ACTUAL_DURATION             | Int32    |
| COUNT_PASSED                | Int32    |
| COUNT_FAILED                | Int32    |
| COUNT_CAUTION               | Int32    |
| COUNT_BLOCKED               | Int32    |
| COUNT_NOT_RUN               | Int32    |
| COUNT_NOT_APPLICABLE        | Int32    |
| EXECUTION_DATE              | DateTime |
| IS_DYNAMIC                  | Boolean  |
| DYNAMIC_QUERY               | String   |
| IS_AUTO_SCHEDULED           | Boolean  |
| TEST_CONFIGURATION_SET_ID   | Int32    |
| TAGS                        | String   |
| RANK                        | Int32    |

## Test Set Folders
| R_TestSetFolders          | Type     |
| ------------------------- | -------- |
| *TEST_SET_FOLDER_ID*      | Int32    |
| PROJECT_ID                | Int32    |
| PARENT_TEST_SET_FOLDER_ID | Int32    |
| NAME                      | String   |
| DESCRIPTION               | String   |
| CREATION_DATE             | DateTime |
| LAST_UPDATE_DATE          | DateTime |
| EXECUTION_DATE            | DateTime |
| ESTIMATED_DURATION        | Int32    |
| ACTUAL_DURATION           | Int32    |
| COUNT_PASSED              | Int32    |
| COUNT_FAILED              | Int32    |
| COUNT_CAUTION             | Int32    |
| COUNT_BLOCKED             | Int32    |
| COUNT_NOT_RUN             | Int32    |
| COUNT_NOT_APPLICABLE      | Int32    |
| PROJECT_NAME              | String   |
| PROJECT_GROUP_ID          | Int32    |
| HIERARCHY_LEVEL           | Int32    |
| INDENT_LEVEL              | String   |

## Test Set Incidents
| R_TestSetIncidents  | Type    |
| ------------------- | ------- |
| TEST_SET_ID         | Int32   |
| INCIDENT_ID         | Int32   |
| DETECTED_RELEASE_ID | Int32   |
| RESOLVED_RELEASE_ID | Int32   |
| VERIFIED_RELEASE_ID | Int32   |
| IS_OPEN_STATUS      | Boolean |

## Test Set Test Cases
| R_TestSetTestCases      | Type     |
| ----------------------- | -------- |
| *TEST_SET_TEST_CASE_ID* | Int32    |
| TEST_SET_ID             | Int32    |
| TEST_CASE_ID            | Int32    |
| OWNER_ID                | Int32    |
| POSITION                | Int32    |
| TEST_SET_NAME           | String   |
| TEST_CASE_NAME          | String   |
| OWNER_NAME              | String   |
| PROJECT_ID              | Int32    |
| PROJECT_NAME            | String   |
| PLANNED_DATE            | DateTime |
| IS_SETUP_TEARDOWN       | Boolean  |

## Test Steps
| R_TestSteps           | Type     |
| --------------------- | -------- |
| *TEST_STEP_ID*        | Int32    |
| TEST_CASE_ID          | Int32    |
| EXECUTION_STATUS_ID   | Int32    |
| DESCRIPTION           | String   |
| LINKED_TEST_CASE_ID   | Int32    |
| POSITION              | Int32    |
| EXPECTED_RESULT       | String   |
| SAMPLE_DATA           | String   |
| LAST_UPDATE_DATE      | DateTime |
| IS_DELETED            | Boolean  |
| EXECUTION_STATUS_NAME | String   |
| TEST_CASE_NAME        | String   |
| PROJECT_ID            | Int32    |
| PROJECT_NAME          | String   |
| PROJECT_GROUP_ID      | Int32    |
| CUST_01 ... CUST_99   | String   |
| IS_ATTACHMENTS        | Boolean  |
| CONCURRENCY           | Int64    |
| PRECONDITION          | String   |


## Timesheets
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_Timesheets          | Type     |
| --------------------- | -------- |
| *TIMESHEET_ID*        | Int32    |
| SUBMITTER_USER_ID     | Int32    |
| SUBMITTER_USER_NAME   | String   |
| APPROVER_USER_ID      | Int32    |
| APPROVER_USER_NAME    | String   |
| TIMESHEET_STATUS_ID   | Int32    |
| TIMESHEET_STATUS_NAME | String   |
| CREATION_DATE         | DateTime |
| APPROVAL_DATE         | DateTime |
| LAST_UPDATE_DATE      | DateTime |
| START_DATE            | DateTime |
| END_DATE              | DateTime |
| COMMENTS              | String   |
| APPROVER_COMMENTS     | String   |

## Timesheet Entries
!!! abstract "Available in SpiraTeam and SpiraPlan only"

| R_TimesheetEntries   | Type     |
| -------------------- | -------- |
| *TIMESHEET_ENTRY_ID* | Int32    |
| TIMESHEET_ID         | Int32    |
| USER_ID              | Int32    |
| USER_NAME            | String   |
| ARTIFACT_TYPE_ID     | Int32    |
| ARTIFACT_TYPE_NAME   | String   |
| ARTIFACT_ID          | Int32    |
| ARTIFACT_NAME        | String   |
| EFFORT_MINUTES       | Int32    |
| EFFORT_DATE          | DateTime |
| PROJECT_ID           | Int32    |
| PROJECT_NAME         | String   |
| PROJECT_GROUP_ID     | Int32    |
| PROJECT_GROUP_NAME   | String   |
| RESOURCE_CATEGORY_ID | Int32    |

## Timesheet Statuses
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_TimesheetStatuses   | Type    |
| --------------------- | ------- |
| *TIMESHEET_STATUS_ID* | Int32   |
| TIMESHEET_STATUS_NAME | String  |
| IS_ACTIVE             | Boolean |
| IS_OPEN               | Boolean |

## Timesheets with Entries
!!! abstract "Available in SpiraTeam and SpiraPlan only"

This table combines the information from the timesheets table and the timesheet entries table to give a unified view of a timesheet and all of its key information. 

| R_TimesheetWithEntries | Type     |
| ---------------------- | -------- |
| *TIMESHEET_ID*         | Int32    |
| SUBMITTER_USER_ID      | Int32    |
| SUBMITTER_USER_NAME    | String   |
| APPROVER_USER_ID       | Int32    |
| APPROVER_USER_NAME     | String   |
| TIMESHEET_STATUS_ID    | Int32    |
| TIMESHEET_STATUS_NAME  | String   |
| CREATION_DATE          | DateTime |
| APPROVAL_DATE          | DateTime |
| LAST_UPDATE_DATE       | DateTime |
| START_DATE             | DateTime |
| END_DATE               | DateTime |
| COMMENTS               | String   |
| APPROVER_COMMENTS      | String   |
| TIMESHEET_ENTRY_ID     | Int32    |
| ARTIFACT_TYPE_ID       | Int32    |
| ARTIFACT_TYPE_NAME     | String   |
| ARTIFACT_ID            | Int32    |
| ARTIFACT_NAME          | String   |
| EFFORT_MINUTES         | Int32    |
| EFFORT_DATE            | DateTime |
| PROJECT_ID             | Int32    |
| PROJECT_NAME           | String   |
| PROJECT_GROUP_ID       | Int32    |
| PROJECT_GROUP_NAME     | String   |
| RESOURCE_CATEGORY_ID   | Int32    |


## Users
| R_Users                         | Type     |
| ------------------------------- | -------- |
| *USER_ID*                       | Int32    |
| USER_NAME                       | String   |
| EMAIL_ADDRESS                   | String   |
| IS_ACTIVE                       | Boolean  |
| CREATION_DATE                   | DateTime |
| LDAP_DN                         | String   |
| FIRST_NAME                      | String   |
| LAST_NAME                       | String   |
| MIDDLE_INITIAL                  | String   |
| DEPARTMENT                      | String   |
| LAST_UPDATE_DATE                | DateTime |
| TIMEZONE                        | String   |
| LAST_OPENED_PROJECT_ID          | Int32    |
| IS_APPROVED                     | Boolean  |
| LAST_LOGIN_DATE                 | DateTime |
| LAST_ACTIVITY_DATE              | DateTime |
| ORGANIZATION                    | String   |
| LAST_OPENED_PROJECT_GROUP_ID    | Int32    |
| LAST_OPENED_PROJECT_TEMPLATE_ID | Int32    |
| IS_ADMIN                        | Boolean  |
| IS_REPORT_ADMIN                 | Boolean  |
| IS_RESOURCE_ADMIN               | Boolean  |
| IS_PORTFOLIO_ADMIN              | Boolean  |
| LAST_PASSWORD_CHANGED_DATE      | DateTime |
| LOGIN_PROVIDER_NAME             | String   |
| IS_TIMESHEET_MANAGER            | Boolean  |
