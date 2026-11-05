# Available Custom Reports Tables
!!! abstract "Available in SpiraTest, SpiraTeam, SpiraPlan"

!!! info "How to use this page"
    Spira has a number of database views available for creating custom reports using ESQL queries. Below, each available table is listed with all of their exact field names. 

    Many tables have a single field shown in *italic* - these are the Primary Keys for that table, which means that field can be used as the unique identifier for each row of data. 

    The Type column gives the data type the view returns. This matters for custom graphs: the first column you select is the category label and can be any type, but the second and later columns are plotted as series and must be numeric.

    Custom property fields are listed as a range, for example `CUST_01 ... CUST_99`, meaning every field in that range exists. They are all String, whatever the property's display type, so a numeric custom property has to be cast before it can be plotted.

## Artifact Associations
**System-level.** Links between any two artifacts, by id and type.
| R_ArtifactAssociations    | Type     | Links to |
| ------------------------- | -------- | -------- |
| ARTIFACT_LINK_TYPE_ID     | Int32    |  |
| SOURCE_ARTIFACT_ID        | Int32    |  |
| SOURCE_ARTIFACT_TYPE_ID   | Int32    | R_ArtifactTypes.ARTIFACT_TYPE_ID |
| DEST_ARTIFACT_ID          | Int32    |  |
| DEST_ARTIFACT_TYPE_ID     | Int32    | R_ArtifactTypes.ARTIFACT_TYPE_ID |
| CREATOR_ID                | Int32    | R_Users.USER_ID |
| CREATION_DATE             | DateTime |  |
| COMMENT                   | String   |  |
| SOURCE_ARTIFACT_TYPE_NAME | String   |  |
| DEST_ARTIFACT_TYPE_NAME   | String   |  |
| CREATOR_NAME              | String   |  |
| ARTIFACT_LINK_TYPE_NAME   | String   |  |
| *ARTIFACT_LINK_ID*        | Int32    |  |

## Artifact Associations - Extended
**System-level.** Links between any two artifacts, including the name of each one.
Prefer R_ArtifactAssociations unless the artifact names are needed. Resolving the names makes this view substantially slower.
| R_ArtifactAssociationExtended | Type     | Links to |
| ----------------------------- | -------- | -------- |
| ARTIFACT_LINK_TYPE_ID         | Int32    |  |
| SOURCE_ARTIFACT_ID            | Int32    |  |
| SOURCE_ARTIFACT_TYPE_ID       | Int32    |  |
| DEST_ARTIFACT_ID              | Int32    |  |
| DEST_ARTIFACT_TYPE_ID         | Int32    |  |
| CREATOR_ID                    | Int32    |  |
| CREATION_DATE                 | DateTime |  |
| COMMENT                       | String   |  |
| SOURCE_ARTIFACT_TYPE_NAME     | String   |  |
| DEST_ARTIFACT_TYPE_NAME       | String   |  |
| CREATOR_NAME                  | String   |  |
| ARTIFACT_LINK_TYPE_NAME       | String   |  |
| SOURCE_ARTIFACT_NAME          | String   |  |
| DEST_ARTIFACT_NAME            | String   |  |
| ARTIFACT_LINK_ID              | Int32    |  |

## Artifact Attachments
**Product-level.** Which attachments are attached to which artifacts.
| R_ArtifactAttachments | Type     | Links to |
| --------------------- | -------- | -------- |
| ARTIFACT_TYPE_ID      | Int32    | R_ArtifactTypes.ARTIFACT_TYPE_ID |
| ARTIFACT_ID           | Int32    | R_AutomationHosts.AUTOMATION_HOST_ID |
| ARTIFACT_TYPE_NAME    | String   |  |
| ARTIFACT_NAME         | String   |  |
| COMMENT               | String   |  |
| CREATOR_ID            | Int32    |  |
| CREATION_DATE         | DateTime |  |
| CREATOR_NAME          | String   |  |
| ATTACHMENT_ID         | Int32    |  |
| PROJECT_ID            | Int32    |  |
| ARTIFACT_STATUS_NAME  | String   |  |
| ARTIFACT_LINK_ID      | Int32    |  |

## Artifact Tags
**Product-level.** Tags applied to artifacts.
| R_ArtifactTags     | Type   | Links to |
| ------------------ | ------ | -------- |
| ARTIFACT_ID        | Int32  |  |
| ARTIFACT_TYPE_ID   | Int32  |  |
| TAGS               | String |  |
| PROJECT_ID         | Int32  |  |
| PROJECT_NAME       | String |  |
| ARTIFACT_TYPE_NAME | String |  |

## Artifact Types
**System-level.** Lookup of the artifact types in Spira, such as Requirement or Incident.
| R_ArtifactTypes    | Type   | Links to |
| ------------------ | ------ | -------- |
| *ARTIFACT_TYPE_ID* | Int32  |  |
| NAME               | String |  |
| PREFIX             | String |  |

## Attachments
**Product-level.** Documents and attached files, with their current version metadata.
| R_Attachments                  | Type     | Links to |
| ------------------------------ | -------- | -------- |
| *ATTACHMENT_ID*                | Int32    |  |
| ATTACHMENT_TYPE_ID             | Int32    |  |
| AUTHOR_ID                      | Int32    |  |
| EDITOR_ID                      | Int32    |  |
| FILENAME                       | String   |  |
| DESCRIPTION                    | String   |  |
| UPLOAD_DATE                    | DateTime |  |
| EDITED_DATE                    | DateTime |  |
| SIZE                           | Int32    |  |
| CURRENT_VERSION                | String   |  |
| PROJECT_ID                     | Int32    | R_Projects.PROJECT_ID |
| PROJECT_ATTACHMENT_FOLDER_ID   | Int32    | R_AttachmentFolders.PROJECT_ATTACHMENT_FOLDER_ID |
| CONCURRENCY                    | Int64    |  |
| DOCUMENT_STATUS_ID             | Int32    |  |
| DOCUMENT_TYPE_ID               | Int32    | R_DocumentTypes.DOCUMENT_TYPE_ID |
| DOCUMENT_STATUS_NAME           | String   |  |
| DOCUMENT_TYPE_NAME             | String   |  |
| TAGS                           | String   |  |
| CUST_01 ... CUST_99            | String   |  |
| IS_KEY_DOCUMENT                | Boolean  |  |
| DOCUMENT_STATUS_IS_OPEN_STATUS | Boolean  |  |
| PROJECT_IS_ACTIVE              | Boolean  |  |
| PROJECT_GROUP_ID               | Int32    |  |
| PROJECT_NAME                   | String   |  |
| AUTHOR_NAME                    | String   |  |
| EDITOR_NAME                    | String   |  |
| ATTACHMENT_TYPE_NAME           | String   |  |
| PROJECT_ATTACHMENT_FOLDER_NAME | String   |  |

## Attachment Folders
**Product-level.** Folder structure organising a product's documents.
| R_AttachmentFolders                 | Type   | Links to |
| ----------------------------------- | ------ | -------- |
| *PROJECT_ATTACHMENT_FOLDER_ID*      | Int32  |  |
| PROJECT_ID                          | Int32  | R_Projects.PROJECT_ID |
| PARENT_PROJECT_ATTACHMENT_FOLDER_ID | Int32  |  |
| NAME                                | String |  |
| PROJECT_NAME                        | String |  |
| PROJECT_GROUP_ID                    | Int32  |  |

## Attachment Versions
**Product-level.** Version history of a document, one row per uploaded version.
| R_AttachmentVersions    | Type     | Links to |
| ----------------------- | -------- | -------- |
| *ATTACHMENT_VERSION_ID* | Int32    |  |
| ATTACHMENT_ID           | Int32    |  |
| AUTHOR_ID               | Int32    | R_Users.USER_ID |
| FILENAME                | String   |  |
| DESCRIPTION             | String   |  |
| UPLOAD_DATE             | DateTime |  |
| SIZE                    | Int32    |  |
| VERSION_NUMBER          | String   |  |
| IS_CURRENT              | Boolean  |  |
| CHANGESET_ID            | Int64    |  |
| AUTHOR_NAME             | String   |  |
| ATTACHMENT_TYPE_ID      | Int32    |  |
| PROJECT_ID              | Int32    |  |

## Automation Hosts
**Product-level.** Machines registered to run automated tests.
| R_AutomationHosts    | Type     | Links to |
| -------------------- | -------- | -------- |
| *AUTOMATION_HOST_ID* | Int32    |  |
| PROJECT_ID           | Int32    | R_Projects.PROJECT_ID |
| NAME                 | String   |  |
| DESCRIPTION          | String   |  |
| TOKEN                | String   |  |
| LAST_UPDATE_DATE     | DateTime |  |
| IS_DELETED           | Boolean  |  |
| CUST_01 ... CUST_99  | String   |  |
| PROJECT_NAME         | String   |  |
| PROJECT_GROUP_ID     | Int32    |  |
| IS_ACTIVE            | Boolean  |  |
| IS_ATTACHMENTS       | Boolean  |  |
| CONCURRENCY          | Int64    |  |
| LAST_CONTACT_DATE    | DateTime |  |

## Baselines
**Product-level.** Snapshots of a product's artifacts taken at a point in time.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
Worked examples of reporting on baselines are in Inflectra KB550.
| R_Baselines             | Type     | Links to |
| ----------------------- | -------- | -------- |
| *BASELINE_ID*           | Int32    |  |
| PROJECT_ID              | Int32    |  |
| CREATOR_USER_ID         | Int32    | R_Users.USER_ID |
| CHANGESET_ID            | Int64    | R_HistoryChangeSets.CHANGESET_ID |
| RELEASE_ID              | Int32    |  |
| NAME                    | String   |  |
| DESCRIPTION             | String   |  |
| IS_ACTIVE               | Boolean  |  |
| IS_APPROVED             | Boolean  |  |
| IS_DELETED              | Boolean  |  |
| CREATION_DATE           | DateTime |  |
| LAST_UPDATE_DATE        | DateTime |  |
| CONCURRENCY             | Int64    |  |
| BASELINE_CREATOR_LOGIN  | String   |  |
| CHANGESET_CREATOR_ID    | Int32    |  |
| CHANGESET_CREATOR_LOGIN | String   |  |
| ARTIFACT_TYPE_ID        | Int32    |  |
| ARTIFACT_TYPE_NAME      | String   |  |
| CHANGESET_DATE          | DateTime |  |
| CHANGESET_TYPE_ID       | Int32    |  |
| CHANGESET_TYPE_NAME     | String   |  |

## Builds
**Product-level.** Builds reported by a continuous integration server against a release.
BUILD_STATUS_ID: 1 = Failed, 2 = Succeeded, 3 = Unstable, 4 = Aborted
| R_Builds               | Type     | Links to |
| ---------------------- | -------- | -------- |
| *BUILD_ID*             | Int32    |  |
| BUILD_STATUS_ID        | Int32    |  |
| RELEASE_ID             | Int32    | R_Releases.RELEASE_ID |
| PROJECT_ID             | Int32    | R_Projects.PROJECT_ID |
| NAME                   | String   |  |
| DESCRIPTION            | String   |  |
| IS_DELETED             | Boolean  |  |
| CREATION_DATE          | DateTime |  |
| LAST_UPDATE_DATE       | DateTime |  |
| RELEASE_NAME           | String   |  |
| RELEASE_VERSION_NUMBER | String   |  |
| PROJECT_NAME           | String   |  |
| PROJECT_GROUP_ID       | Int32    |  |

## Build Statuses
**System-level.** Lookup of build outcome names.
| R_BuildStatuses   | Type    | Links to |
| ----------------- | ------- | -------- |
| *BUILD_STATUS_ID* | Int32   |  |
| NAME              | String  |  |
| IS_ACTIVE         | Boolean |  |

## Capabilities
**Program-level.** Capabilities planned at program level, above product requirements.
!!! abstract "Available in SpiraPlan only"
| R_ProjectGroup_Capabilities | Type     | Links to |
| --------------------------- | -------- | -------- |
| *CAPABILITY_ID*             | Int32    |  |
| PROJECT_GROUP_ID            | Int32    | R_ProjectGroups.PROJECT_GROUP_ID |
| MILESTONE_ID                | Int32    | R_ProjectGroup_Milestones.PROJECT_GROUP_MILESTONE_ID |
| STATUS_ID                   | Int32    | R_ProjectGroup_Capability_Statuses.STATUS_ID |
| TYPE_ID                     | Int32    | R_ProjectGroup_Capability_Types.TYPE_ID |
| PRIORITY_ID                 | Int32    | R_ProjectGroup_Capability_Priorities.PRIORITY_ID |
| NAME                        | String   |  |
| DESCRIPTION                 | String   |  |
| IS_DELETED                  | Boolean  |  |
| PERCENT_COMPLETE            | Int32    |  |
| PROJECT_REQUIREMENT_COUNT   | Int32    |  |
| INDENT_LEVEL                | String   |  |
| CONCURRENCY                 | Int64    |  |
| CREATOR_ID                  | Int32    |  |
| OWNER_ID                    | Int32    |  |
| CREATION_DATE               | DateTime |  |
| LAST_UPDATED_DATE           | DateTime |  |
| IS_SUMMARY                  | Boolean  |  |
| STATUS_NAME                 | String   |  |
| STATUS_IS_OPEN              | Boolean  |  |
| TYPE_NAME                   | String   |  |
| PRIORITY_NAME               | String   |  |
| PRIORITY_COLOR              | String   |  |
| PRIORITY_SCORE              | Int32    |  |
| MILESTONE_NAME              | String   |  |
| CREATOR_NAME                | String   |  |
| OWNER_NAME                  | String   |  |
| PROJECT_GROUP_NAME          | String   |  |
| CUST_01 ... CUST_30         | String   |  |
| CREATOR_LOGIN               | String   |  |
| OWNER_LOGIN                 | String   |  |

## Capability Priorities
**System-level.** Lookup of capability priority names.
!!! abstract "Available in SpiraPlan only"
Capability priorities, not incident or task priorities. PRIORITY_ID is also the key of R_IncidentPriorities, so take care which one a query means.
| R_ProjectGroup_Capability_Priorities | Type    | Links to |
| ------------------------------------ | ------- | -------- |
| *PRIORITY_ID*                        | Int32   |  |
| NAME                                 | String  |  |
| COLOR                                | String  |  |
| IS_ACTIVE                            | Boolean |  |
| IS_DELETED                           | Boolean |  |
| SCORE                                | Int32   |  |

## Capability Requirement Associations
**System-level.** Which product requirements deliver which program capability.
!!! abstract "Available in SpiraPlan only"
| R_ProjectGroup_Capability_Project_Requirements | Type   | Links to |
| ---------------------------------------------- | ------ | -------- |
| CAPABILITY_ID                                  | Int32  | R_ProjectGroup_Capabilities.CAPABILITY_ID |
| REQUIREMENT_ID                                 | Int32  |  |
| ARTIFACT_LINK_TYPE_ID                          | Int32  |  |
| CAPABILITY_NAME                                | String |  |
| REQUIREMENT_NAME                               | String |  |
| ARTIFACT_LINK_TYPE_NAME                        | String |  |

## Capability Statuses
**System-level.** Lookup of capability status names.
!!! abstract "Available in SpiraPlan only"
STATUS_ID is also the key of R_ProjectGroup_Milestone_Statuses. These are different sets of values.
| R_ProjectGroup_Capability_Statuses | Type    | Links to |
| ---------------------------------- | ------- | -------- |
| *STATUS_ID*                        | Int32   |  |
| NAME                               | String  |  |
| POSITION                           | Int32   |  |
| IS_ACTIVE                          | Boolean |  |
| IS_DELETED                         | Boolean |  |
| IS_DEFAULT                         | Boolean |  |
| IS_OPEN                            | Boolean |  |
| ON_BOARD                           | Boolean |  |

## Capability Types
**System-level.** Lookup of capability type names.
!!! abstract "Available in SpiraPlan only"
TYPE_ID is also the key of R_ProjectGroup_Milestone_Types.
| R_ProjectGroup_Capability_Types | Type    | Links to |
| ------------------------------- | ------- | -------- |
| *TYPE_ID*                       | Int32   |  |
| NAME                            | String  |  |
| IS_ACTIVE                       | Boolean |  |
| IS_DELETED                      | Boolean |  |
| IS_DEFAULT                      | Boolean |  |

## Comments
**System-level.** Comments posted on any artifact.
| R_Comments         | Type     | Links to |
| ------------------ | -------- | -------- |
| ARTIFACT_TYPE_ID   | Int32    |  |
| ARTIFACT_ID        | Int32    |  |
| CREATOR_ID         | Int32    |  |
| COMMENT_TEXT       | String   |  |
| CREATION_DATE      | DateTime |  |
| CREATOR_NAME       | String   |  |
| ARTIFACT_TYPE_NAME | String   |  |


## Components
**Product-level.** Components a product is divided into.
| R_Components     | Type    | Links to |
| ---------------- | ------- | -------- |
| *COMPONENT_ID*   | Int32   |  |
| PROJECT_ID       | Int32   | R_Projects.PROJECT_ID |
| NAME             | String  |  |
| IS_DELETED       | Boolean |  |
| IS_ACTIVE        | Boolean |  |
| PROJECT_NAME     | String  |  |
| PROJECT_GROUP_ID | Int32   |  |

## Custom Lists
**Product-level.** Custom lists defined in a product template.
| R_CustomLists             | Type    | Links to |
| ------------------------- | ------- | -------- |
| *CUSTOM_PROPERTY_LIST_ID* | Int32   |  |
| PROJECT_ID                | Int32   |  |
| NAME                      | String  |  |
| IS_ACTIVE                 | Boolean |  |
| IS_SORTED_ON_VALUE        | Boolean |  |
| PROJECT_NAME              | String  |  |
| PROJECT_IS_ACTIVE         | Boolean |  |
| PROJECT_TEMPLATE_ID       | Int32   |  |

## Custom List Values
**Product-level.** The selectable values of a product-template custom list.
| R_CustomListValues                | Type    | Links to |
| --------------------------------- | ------- | -------- |
| *CUSTOM_PROPERTY_VALUE_ID*        | Int32   |  |
| CUSTOM_PROPERTY_LIST_ID           | Int32   | R_CustomLists.CUSTOM_PROPERTY_LIST_ID |
| NAME                              | String  |  |
| PROJECT_ID                        | Int32   |  |
| CUSTOM_PROPERTY_LIST_NAME         | String  |  |
| CUSTOM_PROPERTY_LIST_IS_ACTIVE    | Boolean |  |
| PROJECT_NAME                      | String  |  |
| PROJECT_IS_ACTIVE                 | Boolean |  |
| IS_ACTIVE                         | Boolean |  |
| IS_DELETED                        | Boolean |  |
| DEPENDENT_CUSTOM_PROPERTY_LIST_ID | Int32   |  |
| PARENT_CUSTOM_PROPERTY_VALUE_ID   | Int32   |  |

## Custom Property Definitions
**Product-level.** Which CUST_nn column each product-template custom property occupies, and what the customer calls it.
This is how a customer-facing custom property name resolves to a CUST_nn column. The mapping is per product template, so it differs between products.
| R_CustomPropertyDefinitions  | Type    | Links to |
| ---------------------------- | ------- | -------- |
| *CUSTOM_PROPERTY_ID*         | Int32   |  |
| CUSTOM_PROPERTY_TYPE_ID      | Int32   |  |
| PROJECT_ID                   | Int32   |  |
| ARTIFACT_TYPE_ID             | Int32   | R_ArtifactTypes.ARTIFACT_TYPE_ID |
| NAME                         | String  |  |
| PROPERTY_NUMBER              | Int32   |  |
| IS_DELETED                   | Boolean |  |
| CUSTOM_PROPERTY_LIST_ID      | Int32   | R_CustomLists.CUSTOM_PROPERTY_LIST_ID |
| LEGACY_NAME                  | String  |  |
| PROJECT_NAME                 | String  |  |
| PROJECT_IS_ACTIVE            | Boolean |  |
| ARTIFACT_TYPE_NAME           | String  |  |
| CUSTOM_PROPERTY_TYPE_NAME    | String  |  |
| CUSTOM_PROPERTY_LIST_NAME    | String  |  |
| DEPENDENT_CUSTOM_PROPERTY_ID | Int32   |  |
| PROJECT_TEMPLATE_ID          | Int32   |  |
| POSITION                     | Int32   |  |
| DESCRIPTION                  | String  |  |

## Document Statuses
**System-level.** Lookup of document status names.
| R_DocumentStatuses    | Type    | Links to |
| --------------------- | ------- | -------- |
| *DOCUMENT_STATUS_ID*  | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| NAME                  | String  |  |
| POSITION              | Int32   |  |
| IS_ACTIVE             | Boolean |  |
| IS_OPEN_STATUS        | Boolean |  |
| IS_DEFAULT            | Boolean |  |
| PROJECT_TEMPLATE_NAME | String  |  |

## Document Types
**System-level.** Lookup of document type names.
| R_DocumentTypes       | Type    | Links to |
| --------------------- | ------- | -------- |
| *DOCUMENT_TYPE_ID*    | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| DOCUMENT_WORKFLOW_ID  | Int32   |  |
| NAME                  | String  |  |
| DESCRIPTION           | String  |  |
| IS_ACTIVE             | Boolean |  |
| IS_DEFAULT            | Boolean |  |
| PROJECT_TEMPLATE_NAME | String  |  |

## Events
**System-level.** Audit trail of system events.
| R_Events                 | Type     | Links to |
| ------------------------ | -------- | -------- |
| EVENT_TYPE_ID            | Int32    |  |
| EVENT_TIME_UTC           | DateTime |  |
| EVENT_TIME               | DateTime |  |
| EVENT_CATEGORY           | String   |  |
| EVENT_SEQUENCE           | Decimal  |  |
| EVENT_OCCURRENCE         | Decimal  |  |
| EVENT_CODE               | Int32    |  |
| EVENT_DETAIL_CODE        | Int32    |  |
| MESSAGE                  | String   |  |
| APPLICATION_PATH         | String   |  |
| APPLICATION_VIRTUAL_PATH | String   |  |
| MACHINE_NAME             | String   |  |
| REQUEST_URL              | String   |  |
| EXCEPTION_TYPE           | String   |  |
| DETAILS                  | String   |  |
| EVENT_TYPE_NAME          | String   |  |
| *EVENT_ID*               | String   |  |

## Global / System Custom Property Definitions
**System-level.** Custom property definitions that apply system-wide rather than per template.
System-wide equivalent of R_CustomPropertyDefinitions.
| R_GlobalCustomPropertyDefinitions | Type    | Links to |
| --------------------------------- | ------- | -------- |
| *CUSTOM_PROPERTY_ID*              | Int32   |  |
| CUSTOM_PROPERTY_TYPE_ID           | Int32   |  |
| CUSTOM_PROPERTY_TYPE_NAME         | String  |  |
| WORKSPACE_TYPE_ID                 | Int32   | R_ArtifactTypes.ARTIFACT_TYPE_ID |
| WORKSPACE_TYPE_NAME               | String  |  |
| NAME                              | String  |  |
| PROPERTY_NUMBER                   | Int32   |  |
| IS_DELETED                        | Boolean |  |
| CUSTOM_PROPERTY_LIST_ID           | Int32   | R_GlobalCustomLists.CUSTOM_PROPERTY_LIST_ID |
| CUSTOM_PROPERTY_LIST_NAME         | String  |  |
| POSITION                          | Int32   |  |
| DESCRIPTION                       | String  |  |

## Global / System Custom Property Lists
**System-level.** Custom lists defined once for the whole system.
System-wide equivalent of R_CustomLists, which is per product template.
| R_GlobalCustomLists       | Type    | Links to |
| ------------------------- | ------- | -------- |
| *CUSTOM_PROPERTY_LIST_ID* | Int32   |  |
| NAME                      | String  |  |
| IS_ACTIVE                 | Boolean |  |
| IS_SORTED_ON_VALUE        | Boolean |  |

## Global / System Custom Property List Values
**System-level.** The selectable values of a system-wide custom list.
System-wide equivalent of R_CustomListValues, which is per product template.
| R_GlobalCustomListValues       | Type    | Links to |
| ------------------------------ | ------- | -------- |
| *CUSTOM_PROPERTY_VALUE_ID*     | Int32   |  |
| NAME                           | String  |  |
| IS_ACTIVE                      | Boolean |  |
| IS_DELETED                     | Boolean |  |
| CUSTOM_PROPERTY_LIST_ID        | Int32   | R_GlobalCustomLists.CUSTOM_PROPERTY_LIST_ID |
| CUSTOM_PROPERTY_LIST_NAME      | String  |  |
| CUSTOM_PROPERTY_LIST_IS_ACTIVE | Boolean |  |

## Global / System History Change-Sets
**System-level.** Change sets recording edits to system-level administrative data.
Covers administrative objects rather than product artifacts. For artifact edits use R_HistoryChangeSets.
| R_Global_HistoryChangeSets | Type     | Links to |
| -------------------------- | -------- | -------- |
| *CHANGESET_ID*             | Int64    |  |
| USER_ID                    | Int32    |  |
| CHANGE_DATE                | DateTime |  |
| CHANGETYPE_ID              | Int32    |  |
| ARTIFACT_TYPE_ID           | Int32    | R_ArtifactTypes.ARTIFACT_TYPE_ID |
| ARTIFACT_ID                | Int32    |  |
| ARTIFACT_DESC              | String   |  |
| WORKSPACE_TYPE_ID          | Int32    |  |
| WORKSPACE_ID               | Int32    |  |
| CHANGETYPE_NAME            | String   |  |
| USER_NAME                  | String   |  |
| ARTIFACT_TYPE_NAME         | String   |  |
| WORKSPACE_TYPE_NAME        | String   |  |

## Global / System History Details
**System-level.** Field-level before and after values for system-level changes.
System-level counterpart of R_HistoryDetails.
| R_Global_HistoryDetails | Type     | Links to |
| ----------------------- | -------- | -------- |
| *ARTIFACT_HISTORY_ID*   | Int64    |  |
| FIELD_NAME              | String   |  |
| OLD_VALUE               | String   |  |
| NEW_VALUE               | String   |  |
| CHANGESET_ID            | Int64    | R_Global_HistoryChangeSets.CHANGESET_ID |
| FIELD_TYPE_ID           | Int32    |  |
| CUSTOM_PROPERTY_ID      | Int32    |  |
| ARTIFACT_ID             | Int32    |  |
| USER_ID                 | Int32    |  |
| ARTIFACT_TYPE_ID        | Int32    |  |
| CHANGE_DATE             | DateTime |  |
| USER_NAME               | String   |  |
| CHANGE_NAME             | String   |  |
| CHANGETYPE_ID           | Int32    |  |
| ARTIFACT_FIELD_TYPE_ID  | Int32    |  |
| ARTIFACT_TYPE_NAME      | String   |  |

## History Change-Sets
**Product-level.** One row per save against a product artifact, grouping the fields changed.
| R_HistoryChangeSets | Type     | Links to |
| ------------------- | -------- | -------- |
| *CHANGESET_ID*      | Int32    |  |
| USER_ID             | Int32    | R_Users.USER_ID |
| ARTIFACT_TYPE_ID    | Int32    | R_ArtifactTypes.ARTIFACT_TYPE_ID |
| ARTIFACT_ID         | Int32    |  |
| CHANGE_DATE         | DateTime |  |
| CHANGETYPE_ID       | Int32    |  |
| PROJECT_ID          | Int32    |  |
| REVERT_ID           | Int32    |  |
| ARTIFACT_DESC       | String   |  |
| CHANGETYPE_NAME     | String   |  |
| USER_NAME           | String   |  |
| ARTIFACT_TYPE_NAME  | String   |  |
| SIGNATURE_HASH      | String   |  |
| MEANING             | String   |  |
| CHANGEAREA_ID       | Int32    |  |

## History Details
**System-level.** Field-level before and after values for each artifact change.
| R_HistoryDetails       | Type     | Links to |
| ---------------------- | -------- | -------- |
| FIELD_NAME             | String   |  |
| OLD_VALUE              | String   |  |
| FIELD_CAPTION          | String   |  |
| NEW_VALUE              | String   |  |
| OLD_VALUE_INT          | Int32    |  |
| OLD_VALUE_DATE         | DateTime |  |
| NEW_VALUE_INT          | Int32    |  |
| NEW_VALUE_DATE         | DateTime |  |
| CHANGESET_ID           | Int32    | R_HistoryChangeSets.CHANGESET_ID |
| FIELD_ID               | Int32    |  |
| CUSTOM_PROPERTY_ID     | Int32    |  |
| ARTIFACT_ID            | Int32    |  |
| USER_ID                | Int32    |  |
| ARTIFACT_TYPE_ID       | Int32    |  |
| CHANGE_DATE            | DateTime |  |
| CHANGER_NAME           | String   |  |
| CHANGE_NAME            | String   |  |
| CHANGETYPE_ID          | Int32    |  |
| *ARTIFACT_HISTORY_ID*  | Int32    |  |
| ARTIFACT_FIELD_TYPE_ID | Int32    |  |

## Incidents
**Product-level.** Incidents - bugs, issues and other defects raised against a product.
| R_Incidents                     | Type     | Links to |
| ------------------------------- | -------- | -------- |
| *INCIDENT_ID*                   | Int32    | R_ArtifactTags.ARTIFACT_ID |
| PROJECT_ID                      | Int32    | R_Projects.PROJECT_ID |
| PRIORITY_ID                     | Int32    | R_IncidentPriorities.PRIORITY_ID |
| SEVERITY_ID                     | Int32    | R_IncidentSeverities.SEVERITY_ID |
| INCIDENT_STATUS_ID              | Int32    | R_IncidentStatuses.INCIDENT_STATUS_ID |
| INCIDENT_TYPE_ID                | Int32    | R_IncidentTypes.INCIDENT_TYPE_ID |
| OPENER_ID                       | Int32    | R_Users.USER_ID |
| OWNER_ID                        | Int32    | R_Users.USER_ID |
| DESCRIPTION                     | String   |  |
| CREATION_DATE                   | DateTime |  |
| CLOSED_DATE                     | DateTime |  |
| LAST_UPDATE_DATE                | DateTime |  |
| DETECTED_RELEASE_ID             | Int32    | R_Releases.RELEASE_ID |
| RESOLVED_RELEASE_ID             | Int32    | R_Releases.RELEASE_ID |
| START_DATE                      | DateTime |  |
| COMPLETION_PERCENT              | Int32    |  |
| ESTIMATED_EFFORT                | Int32    |  |
| ACTUAL_EFFORT                   | Int32    |  |
| REMAINING_EFFORT                | Int32    |  |
| PROJECTED_EFFORT                | Int32    |  |
| IS_DELETED                      | Boolean  |  |
| VERIFIED_RELEASE_ID             | Int32    | R_Releases.RELEASE_ID |
| PRIORITY_NAME                   | String   |  |
| PRIORITY_COLOR                  | String   |  |
| SEVERITY_NAME                   | String   |  |
| SEVERITY_COLOR                  | String   |  |
| INCIDENT_STATUS_NAME            | String   |  |
| INCIDENT_TYPE_NAME              | String   |  |
| OPENER_NAME                     | String   |  |
| OWNER_NAME                      | String   |  |
| DETECTED_RELEASE_VERSION_NUMBER | String   |  |
| RESOLVED_RELEASE_VERSION_NUMBER | String   |  |
| VERIFIED_RELEASE_VERSION_NUMBER | String   |  |
| PROJECT_GROUP_ID                | Int32    |  |
| PROJECT_NAME                    | String   |  |
| CUST_01 ... CUST_99             | String   |  |
| NAME                            | String   |  |
| IS_ATTACHMENTS                  | Boolean  |  |
| COMPONENT_IDS                   | String   |  |
| INCIDENT_STATUS_IS_OPEN_STATUS  | Boolean  |  |
| PROJECT_IS_ACTIVE               | Boolean  |  |
| INCIDENT_TYPE_IS_ISSUE          | Boolean  |  |
| INCIDENT_TYPE_IS_RISK           | Boolean  |  |
| CONCURRENCY                     | Int64    |  |
| RANK                            | Int32    |  |
| END_DATE                        | DateTime |  |
| DETECTED_BUILD_ID               | Int32    | R_Builds.BUILD_ID |
| RESOLVED_BUILD_ID               | Int32    | R_Builds.BUILD_ID |
| DETECTED_BUILD_NAME             | String   |  |
| RESOLVED_BUILD_NAME             | String   |  |
| TAGS                            | String   |  |

## Incident Priorities
**System-level.** Lookup of incident priority names.
| R_IncidentPriorities  | Type    | Links to |
| --------------------- | ------- | -------- |
| *PRIORITY_ID*         | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| NAME                  | String  |  |
| COLOR                 | String  |  |
| IS_ACTIVE             | Boolean |  |
| SCORE                 | Int32   |  |
| PROJECT_TEMPLATE_NAME | String  |  |

## Incident Severities
**System-level.** Lookup of incident severity names.
| R_IncidentSeverities  | Type    | Links to |
| --------------------- | ------- | -------- |
| *SEVERITY_ID*         | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| NAME                  | String  |  |
| COLOR                 | String  |  |
| IS_ACTIVE             | Boolean |  |
| SCORE                 | Int32   |  |
| PROJECT_TEMPLATE_NAME | String  |  |

## Incident Statuses
**System-level.** Lookup of incident status names, and whether each one counts as open.
| R_IncidentStatuses    | Type    | Links to |
| --------------------- | ------- | -------- |
| *INCIDENT_STATUS_ID*  | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| NAME                  | String  |  |
| IS_ACTIVE             | Boolean |  |
| IS_OPEN_STATUS        | Boolean |  |
| IS_DEFAULT            | Boolean |  |
| PROJECT_TEMPLATE_NAME | String  |  |
| POSITION              | Int32   |  |
| ON_BOARD              | Boolean |  |

## Incident Types
**System-level.** Lookup of incident type names, such as Bug or Enhancement.
| R_IncidentTypes       | Type    | Links to |
| --------------------- | ------- | -------- |
| *INCIDENT_TYPE_ID*    | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| WORKFLOW_ID           | Int32   |  |
| NAME                  | String  |  |
| IS_ACTIVE             | Boolean |  |
| IS_ISSUE              | Boolean |  |
| IS_DEFAULT            | Boolean |  |
| PROJECT_TEMPLATE_NAME | String  |  |

## Pending Test Runs
**Product-level.** Test runs started but not yet completed.
| R_PendingTestRuns      | Type     | Links to |
| ---------------------- | -------- | -------- |
| *TEST_RUNS_PENDING_ID* | Int32    |  |
| PROJECT_ID             | Int32    | R_Projects.PROJECT_ID |
| TEST_SET_ID            | Int32    | R_TestSets.TEST_SET_ID |
| TESTER_ID              | Int32    |  |
| NAME                   | String   |  |
| CREATION_DATE          | DateTime |  |
| LAST_UPDATE_DATE       | DateTime |  |
| COUNT_PASSED           | Int32    |  |
| COUNT_FAILED           | Int32    |  |
| COUNT_BLOCKED          | Int32    |  |
| COUNT_CAUTION          | Int32    |  |
| COUNT_NOT_RUN          | Int32    |  |
| COUNT_NOT_APPLICABLE   | Int32    |  |
| TESTER_LOGIN           | String   |  |
| TESTER_FULLNAME        | String   |  |
| TEST_SET_NAME          | String   |  |
| PROJECT_NAME           | String   |  |

## Portfolios
**System-level.** Portfolios grouping programs together.
!!! abstract "Available in SpiraPlan only"
| R_Portfolios      | Type     | Links to |
| ----------------- | -------- | -------- |
| *PORTFOLIO_ID*    | Int32    |  |
| NAME              | String   |  |
| DESCRIPTION       | String   |  |
| IS_ACTIVE         | Boolean  |  |
| START_DATE        | DateTime |  |
| END_DATE          | DateTime |  |
| PERCENT_COMPLETE  | Int32    |  |
| REQUIREMENT_COUNT | Int32    |  |

## Program Milestones
**Program-level.** Milestones planned at program level.
!!! abstract "Available in SpiraPlan only"
| R_ProjectGroup_Milestones       | Type     | Links to |
| ------------------------------- | -------- | -------- |
| *PROJECT_GROUP_MILESTONE_ID*    | Int32    |  |
| PROJECT_GROUP_ID                | Int32    | R_ProjectGroups.PROJECT_GROUP_ID |
| TYPE_ID                         | Int32    | R_ProjectGroup_Milestone_Types.TYPE_ID |
| STATUS_ID                       | Int32    | R_ProjectGroup_Milestone_Statuses.STATUS_ID |
| NAME                            | String   |  |
| DESCRIPTION                     | String   |  |
| IS_DELETED                      | Boolean  |  |
| START_DATE                      | DateTime |  |
| END_DATE                        | DateTime |  |
| PERCENT_COMPLETE                | Int32    |  |
| CHILDREN_START_DATE             | DateTime |  |
| CHILDREN_END_DATE               | DateTime |  |
| PROJECT_RELEASE_COUNT           | Int32    |  |
| PROJECT_GROUP_REQUIREMENT_COUNT | Int32    |  |
| CONCURRENCY                     | Int64    |  |
| CREATOR_ID                      | Int32    |  |
| OWNER_ID                        | Int32    |  |
| CREATION_DATE                   | DateTime |  |
| LAST_UPDATED_DATE               | DateTime |  |
| STATUS_NAME                     | String   |  |
| STATUS_IS_OPEN                  | Boolean  |  |
| TYPE_NAME                       | String   |  |
| CREATOR_NAME                    | String   |  |
| OWNER_NAME                      | String   |  |
| PROJECT_GROUP_NAME              | String   |  |
| CUST_01 ... CUST_30             | String   |  |

## Program Milestone Releases
**System-level.** Which product releases roll up to which program milestone.
!!! abstract "Available in SpiraPlan only"
| R_ProjectGroup_Milestone_Project_Releases | Type   | Links to |
| ----------------------------------------- | ------ | -------- |
| *PROJECT_GROUP_MILESTONE_ID*              | Int32  | R_ProjectGroup_Milestones.PROJECT_GROUP_MILESTONE_ID |
| RELEASE_ID                                | Int32  | R_Releases.RELEASE_ID |
| ARTIFACT_LINK_TYPE_ID                     | Int32  |  |
| PROJECT_GROUP_MILESTONE_NAME              | String |  |
| RELEASE_NAME                              | String |  |
| ARTIFACT_LINK_TYPE_NAME                   | String |  |

## Program Milestone Statuses
**System-level.** Lookup of program milestone status names.
!!! abstract "Available in SpiraPlan only"
| R_ProjectGroup_Milestone_Statuses | Type    | Links to |
| --------------------------------- | ------- | -------- |
| *STATUS_ID*                       | Int32   |  |
| NAME                              | String  |  |
| IS_ACTIVE                         | Boolean |  |
| IS_DELETED                        | Boolean |  |
| IS_DEFAULT                        | Boolean |  |
| IS_OPEN                           | Boolean |  |

## Program Milestone Types
**System-level.** Lookup of program milestone type names.
!!! abstract "Available in SpiraPlan only"
| R_ProjectGroup_Milestone_Types | Type    | Links to |
| ------------------------------ | ------- | -------- |
| *TYPE_ID*                      | Int32   |  |
| NAME                           | String  |  |
| IS_ACTIVE                      | Boolean |  |
| IS_DELETED                     | Boolean |  |
| IS_DEFAULT                     | Boolean |  |

## Project Artifacts Sharing 
**System-level.** Artifacts shared between products.
| R_ProjectArtifactSharings | Type   | Links to |
| ------------------------- | ------ | -------- |
| SOURCE_PROJECT_ID         | Int32  | R_Projects.PROJECT_ID |
| DEST_PROJECT_ID           | Int32  | R_Projects.PROJECT_ID |
| ARTIFACT_TYPE_ID          | Int32  | R_ArtifactTypes.ARTIFACT_TYPE_ID |
| SOURCE_PROJECT_NAME       | String |  |
| DEST_PROJECT_NAME         | String |  |
| ARTIFACT_TYPE_NAME        | String |  |
| ARTIFACT_TYPE_PREFIX      | String |  |

## Projects (Products)
**System-level.** Products, called projects in the database. The main scoping table.
| R_Projects                  | Type     | Links to |
| --------------------------- | -------- | -------- |
| *PROJECT_ID*                | Int32    |  |
| PROJECT_GROUP_ID            | Int32    | R_ProjectGroups.PROJECT_GROUP_ID |
| NAME                        | String   |  |
| DESCRIPTION                 | String   |  |
| CREATION_DATE               | DateTime |  |
| WEBSITE                     | String   |  |
| WORKING_HOURS               | Int32    |  |
| WORKING_DAYS                | Int32    |  |
| NON_WORKING_HOURS           | Int32    |  |
| TASK_DEFAULT_EFFORT         | Int32    |  |
| PROJECT_GROUP_NAME          | String   |  |
| PROJECT_GROUP_DESCRIPTION   | String   |  |
| IS_ACTIVE                   | Boolean  |  |
| IS_TIME_TRACK_INCIDENTS     | Boolean  |  |
| IS_TIME_TRACK_TASKS         | Boolean  |  |
| IS_EFFORT_INCIDENTS         | Boolean  |  |
| IS_EFFORT_TASKS             | Boolean  |  |
| IS_TASKS_AUTO_CREATE        | Boolean  |  |
| REQ_DEFAULT_ESTIMATE        | Decimal  |  |
| REQ_POINT_EFFORT            | Int32    |  |
| IS_REQ_STATUS_BY_TASKS      | Boolean  |  |
| IS_REQ_STATUS_BY_TEST_CASES | Boolean  |  |
| IS_EFFORT_TEST_CASES        | Boolean  |  |
| IS_REQ_STATUS_AUTO_PLANNED  | Boolean  |  |
| PROJECT_TEMPLATE_ID         | Int32    |  |
| START_DATE                  | DateTime |  |
| END_DATE                    | DateTime |  |
| PERCENT_COMPLETE            | Int32    |  |
| REQUIREMENT_COUNT           | Int32    |  |
| INFLECTRA_AI_ENABLED        | String   |  |
| CUST_01 ... CUST_30         | String   |  |
| CONCURRENCY                 | Int64    |  |

## Project Groups (Programs)
**System-level.** Programs, each grouping a set of products.
| R_ProjectGroups     | Type     | Links to |
| ------------------- | -------- | -------- |
| *PROJECT_GROUP_ID*  | Int32    |  |
| NAME                | String   |  |
| DESCRIPTION         | String   |  |
| WEBSITE             | String   |  |
| PROJECT_TEMPLATE_ID | Int32    |  |
| IS_ACTIVE           | Boolean  |  |
| IS_DEFAULT          | Boolean  |  |
| PERCENT_COMPLETE    | Int32    |  |
| START_DATE          | DateTime |  |
| END_DATE            | DateTime |  |
| PORTFOLIO_ID        | Int32    |  |
| REQUIREMENT_COUNT   | Int32    |  |

## Project Group Membership (Program Membership)
**Program-level.** Which users belong to which program.
!!! abstract "Available in SpiraPlan only"
| R_ProjectGroup_MembershipUsers | Type    | Links to |
| ------------------------------ | ------- | -------- |
| PROJECT_GROUP_ID               | Int32   | R_ProjectGroups.PROJECT_GROUP_ID |
| PROJECT_GROUP_NAME             | String  |  |
| PROJECT_GROUP_IS_ACTIVE        | Boolean |  |
| PROJECT_GROUP_ROLE_ID          | Int32   |  |
| PROJECT_GROUP_ROLE_NAME        | String  |  |
| PROJECT_GROUP_ROLE_ISACTIVE    | Boolean |  |
| USER_ID                        | Int32   |  |
| USER_NAME                      | String  |  |
| USER_FULLNAME                  | String  |  |

## Project (Product) Membership
**Product-level.** Which users belong to which product, and in which role.
| R_ProjectMembership | Type    | Links to |
| ------------------- | ------- | -------- |
| PROJECT_ID          | Int32   | R_Projects.PROJECT_ID |
| USER_ID             | Int32   | R_Users.USER_ID |
| PROJECT_ROLE_ID     | Int32   | R_ProjectRoles.PROJECT_ROLE_ID |
| PROJECT_NAME        | String  |  |
| PROJECT_ROLE_NAME   | String  |  |
| USER_NAME           | String  |  |
| FIRST_NAME          | String  |  |
| LAST_NAME           | String  |  |
| DEPARTMENT          | String  |  |
| IS_SYSTEM_ADMIN     | Boolean |  |

## Project Release Resources
**Product-level.** Resource allocation figures per product release.
| R_ProjectReleaseResources | Type  | Links to |
| ------------------------- | ----- | -------- |
| *PROJECT_ID*              | Int32 |  |
| USER_ID                   | Int32 |  |
| RELEASE_ID                | Int32 |  |
| INCIDENT_EFFORT           | Int32 |  |
| TASK_EFFORT               | Int32 |  |

## Project Roles
**System-level.** Roles a product member can hold, with their permissions.
| R_ProjectRoles           | Type    | Links to |
| ------------------------ | ------- | -------- |
| *PROJECT_ROLE_ID*        | Int32   |  |
| NAME                     | String  |  |
| IS_ACTIVE                | Boolean |  |
| DESCRIPTION              | String  |  |
| IS_ADMIN                 | Boolean |  |
| IS_DISCUSSIONS_ADD       | Boolean |  |
| IS_SOURCE_CODE_VIEW      | Boolean |  |
| IS_SOURCE_CODE_EDIT      | Boolean |  |
| IS_DOCUMENT_FOLDERS_EDIT | Boolean |  |
| IS_LIMITED_VIEW          | Boolean |  |
| IS_TEMPLATE_ADMIN        | Boolean |  |
| ARTIFACT_TYPE_ID         | Int32   |  |
| ARTIFACT                 | String  |  |
| PERMISSION               | String  |  |

## Project (Product) Tags
**Product-level.** Tags applied to products.
| R_ProjectTags | Type   | Links to |
| ------------- | ------ | -------- |
| PROJECT_ID    | Int32  |  |
| TAG           | String |  |
| PROJECT_NAME  | String |  |

## Project Teams Users
**Product-level.** Which users belong to which team within a product.
!!! abstract "Available in SpiraPlan only"
| R_ProjectTeamUsers | Type   | Links to |
| ------------------ | ------ | -------- |
| PROJECT_ID         | Int32  | R_Projects.PROJECT_ID |
| PROJECT_NAME       | String |  |
| USER_ID            | Int32  | R_Users.USER_ID |
| USER_NAME          | String |  |
| TEAM_ID            | Int32  | R_Teams.TEAM_ID |
| TEAM_NAME          | String |  |

## Project (Product) Templates
**System-level.** Templates products draw their types, statuses and custom properties from.
| R_ProjectTemplates    | Type    | Links to |
| --------------------- | ------- | -------- |
| *PROJECT_TEMPLATE_ID* | Int32   |  |
| NAME                  | String  |  |
| DESCRIPTION           | String  |  |
| IS_ACTIVE             | Boolean |  |

## Releases
**Product-level.** Releases, sprints and phases a product is delivered in.
| R_Releases               | Type     | Links to |
| ------------------------ | -------- | -------- |
| *RELEASE_ID*             | Int32    | R_ArtifactTags.ARTIFACT_ID |
| PROJECT_ID               | Int32    | R_Projects.PROJECT_ID |
| CREATOR_ID               | Int32    | R_Users.USER_ID |
| NAME                     | String   |  |
| VERSION_NUMBER           | String   |  |
| DESCRIPTION              | String   |  |
| INDENT_LEVEL             | String   |  |
| CREATION_DATE            | DateTime |  |
| LAST_UPDATE_DATE         | DateTime |  |
| START_DATE               | DateTime |  |
| END_DATE                 | DateTime |  |
| RESOURCE_COUNT           | Decimal  |  |
| DAYS_NON_WORKING         | Decimal  |  |
| PLANNED_EFFORT           | Int32    |  |
| AVAILABLE_EFFORT         | Int32    |  |
| COUNT_BLOCKED            | Int32    |  |
| COUNT_CAUTION            | Int32    |  |
| COUNT_FAILED             | Int32    |  |
| COUNT_NOT_APPLICABLE     | Int32    |  |
| COUNT_NOT_RUN            | Int32    |  |
| COUNT_PASSED             | Int32    |  |
| TASK_COUNT               | Int32    |  |
| TASK_PERCENT_ON_TIME     | Int32    |  |
| TASK_PERCENT_LATE_FINISH | Int32    |  |
| TASK_PERCENT_NOT_START   | Int32    |  |
| TASK_PERCENT_LATE_START  | Int32    |  |
| TASK_ESTIMATED_EFFORT    | Int32    |  |
| TASK_ACTUAL_EFFORT       | Int32    |  |
| TASK_PROJECTED_EFFORT    | Int32    |  |
| TASK_REMAINING_EFFORT    | Int32    |  |
| IS_DELETED               | Boolean  |  |
| CREATOR_NAME             | String   |  |
| FULL_NAME                | String   |  |
| PROJECT_NAME             | String   |  |
| PROJECT_GROUP_ID         | Int32    |  |
| CUST_01 ... CUST_99      | String   |  |
| RELEASE_TYPE_ID          | Int32    |  |
| RELEASE_STATUS_ID        | Int32    |  |
| OWNER_ID                 | Int32    | R_Users.USER_ID |
| IS_SUMMARY               | Boolean  |  |
| IS_ATTACHMENTS           | Boolean  |  |
| OWNER_NAME               | String   |  |
| RELEASE_TYPE_NAME        | String   |  |
| RELEASE_STATUS_NAME      | String   |  |
| CONCURRENCY              | Int64    |  |
| PERCENT_COMPLETE         | Int32    |  |
| PLANNED_POINTS           | Decimal  |  |
| REQUIREMENT_POINTS       | Decimal  |  |
| REQUIREMENT_COUNT        | Int32    |  |
| TAGS                     | String   |  |
| BRANCH_ID                | Int32    |  |

## Release Test Case Mapping
**Product-level.** Which test cases are assigned to which release.
| R_ReleaseTestCases     | Type     | Links to |
| ---------------------- | -------- | -------- |
| RELEASE_ID             | Int32    | R_Releases.RELEASE_ID |
| TEST_CASE_ID           | Int32    | R_TestCases.TEST_CASE_ID |
| RELEASE_NAME           | String   |  |
| RELEASE_VERSION_NUMBER | String   |  |
| TEST_CASE_NAME         | String   |  |
| PROJECT_ID             | Int32    |  |
| PROJECT_NAME           | String   |  |
| RELEASE_TYPE_ID        | Int32    |  |
| RELEASE_TYPE_NAME      | String   |  |
| EXECUTION_STATUS_ID    | Int32    |  |
| EXECUTION_DATE         | DateTime |  |
| ACTUAL_DURATION        | Int32    |  |

## Requirements
**Product-level.** Requirements - the features and user stories planned for a product.
| R_Requirements           | Type     | Links to |
| ------------------------ | -------- | -------- |
| *REQUIREMENT_ID*         | Int32    | R_ArtifactTags.ARTIFACT_ID |
| AUTHOR_ID                | Int32    | R_Users.USER_ID |
| OWNER_ID                 | Int32    | R_Users.USER_ID |
| RELEASE_ID               | Int32    | R_Releases.RELEASE_ID |
| PROJECT_ID               | Int32    | R_Projects.PROJECT_ID |
| IMPORTANCE_ID            | Int32    | R_Requirement_Importance.IMPORTANCE_ID |
| NAME                     | String   |  |
| CREATION_DATE            | DateTime |  |
| INDENT_LEVEL             | String   |  |
| DESCRIPTION              | String   |  |
| LAST_UPDATE_DATE         | DateTime |  |
| COVERAGE_COUNT_TOTAL     | Int32    |  |
| COVERAGE_COUNT_PASSED    | Int32    |  |
| COVERAGE_COUNT_FAILED    | Int32    |  |
| COVERAGE_COUNT_CAUTION   | Int32    |  |
| COVERAGE_COUNT_BLOCKED   | Int32    |  |
| TASK_COUNT               | Int32    |  |
| TASK_ESTIMATED_EFFORT    | Int32    |  |
| TASK_ACTUAL_EFFORT       | Int32    |  |
| TASK_PROJECTED_EFFORT    | Int32    |  |
| TASK_REMAINING_EFFORT    | Int32    |  |
| TASK_PERCENT_ON_TIME     | Int32    |  |
| TASK_PERCENT_LATE_FINISH | Int32    |  |
| TASK_PERCENT_NOT_START   | Int32    |  |
| TASK_PERCENT_LATE_START  | Int32    |  |
| IS_DELETED               | Boolean  |  |
| AUTHOR_NAME              | String   |  |
| OWNER_NAME               | String   |  |
| IMPORTANCE_NAME          | String   |  |
| RELEASE_VERSION_NUMBER   | String   |  |
| PROJECT_NAME             | String   |  |
| PROJECT_GROUP_ID         | Int32    |  |
| CUST_01 ... CUST_99      | String   |  |
| REQUIREMENT_TYPE_ID      | Int32    | R_RequirementTypes.REQUIREMENT_TYPE_ID |
| REQUIREMENT_STATUS_ID    | Int32    |  |
| COMPONENT_ID             | Int32    | R_Components.COMPONENT_ID |
| IS_SUMMARY               | Boolean  |  |
| IS_ATTACHMENTS           | Boolean  |  |
| CONCURRENCY              | Int64    |  |
| REQUIREMENT_STATUS_NAME  | String   |  |
| REQUIREMENT_TYPE_NAME    | String   |  |
| COMPONENT_NAME           | String   |  |
| ESTIMATE_POINTS          | Decimal  |  |
| ESTIMATED_EFFORT         | Int32    |  |
| RANK                     | Int32    |  |
| GOAL_ID                  | Int32    |  |
| START_DATE               | DateTime |  |
| END_DATE                 | DateTime |  |
| PERCENT_COMPLETE         | Int32    |  |
| TAGS                     | String   |  |
| IS_SUSPECT               | Boolean  |  |

## Requirement Importances
**System-level.** Lookup of requirement importance names.
| R_Requirement_Importance | Type    | Links to |
| ------------------------ | ------- | -------- |
| *IMPORTANCE_ID*          | Int32   |  |
| PROJECT_TEMPLATE_ID      | Int32   |  |
| NAME                     | String  |  |
| IS_ACTIVE                | Boolean |  |
| COLOR                    | String  |  |
| SCORE                    | Int32   |  |

## Requirement Incidents
**System-level.** Links between requirements and incidents, by id.
| R_RequirementIncidents | Type    | Links to |
| ---------------------- | ------- | -------- |
| REQUIREMENT_ID         | Int32   |  |
| INCIDENT_ID            | Int32   |  |
| DETECTED_RELEASE_ID    | Int32   |  |
| IS_OPEN_STATUS         | Boolean |  |

## Requirement Incidents - Extended
**System-level.** Links between requirements and incidents, including the name of each.
Prefer R_RequirementIncidents unless the names are needed. Resolving them makes this view slower.
| R_RequirementIncidentExtended | Type    | Links to |
| ----------------------------- | ------- | -------- |
| REQUIREMENT_ID                | Int32   |  |
| INCIDENT_ID                   | Int32   |  |
| DETECTED_RELEASE_ID           | Int32   |  |
| IS_OPEN_STATUS                | Boolean |  |
| REQUIREMENT_NAME              | String  |  |
| INCIDENT_NAME                 | String  |  |

## Requirement Steps
**System-level.** The individual steps or scenarios recorded against a requirement.
| R_RequirementSteps           | Type     | Links to |
| ---------------------------- | -------- | -------- |
| REQUIREMENT_ID               | Int32    |  |
| POSITION                     | Int32    |  |
| DESCRIPTION                  | String   |  |
| IS_DELETED                   | Boolean  |  |
| CREATION_DATE                | DateTime |  |
| LAST_UPDATE_DATE             | DateTime |  |
| CONCURRENCY                  | Int64    |  |
| REQUIREMENT_NAME             | String   |  |
| REQUIREMENT_LAST_UPDATE_DATE | DateTime |  |
| PROJECT_IS_ACTIVE            | Boolean  |  |
| PROJECT_PROJECT_GROUP_ID     | Int32    |  |
| PROJECT_NAME                 | String   |  |
| *REQUIREMENT_STEP_ID*        | Int32    |  |

## Requirement Test Case Coverage
**Product-level.** Which test cases cover which requirements.
| R_RequirementTestCases | Type   | Links to |
| ---------------------- | ------ | -------- |
| REQUIREMENT_ID         | Int32  |  |
| TEST_CASE_ID           | Int32  | R_TestCases.TEST_CASE_ID |
| REQUIREMENT_NAME       | String |  |
| TEST_CASE_NAME         | String |  |
| PROJECT_ID             | Int32  |  |
| PROJECT_NAME           | String |  |

## Requirement Test Step Coverage
**Product-level.** Test steps generated from requirement steps.
| R_RequirementTestSteps | Type   | Links to |
| ---------------------- | ------ | -------- |
| TEST_STEP_ID           | Int32  | R_TestSteps.TEST_STEP_ID |
| REQUIREMENT_NAME       | String |  |
| POSITION               | Int32  |  |
| STEP_DESCRIPTION       | String |  |
| EXPECTED_RESULT        | String |  |
| SAMPLE_DATA            | String |  |
| PROJECT_ID             | Int32  |  |
| PROJECT_NAME           | String |  |
| REQUIREMENT_ID         | Int32  |  |

## Requirement Types
**System-level.** Lookup of requirement type names, such as Feature or User Story.
| R_RequirementTypes      | Type    | Links to |
| ----------------------- | ------- | -------- |
| *REQUIREMENT_TYPE_ID*   | Int32   |  |
| REQUIREMENT_WORKFLOW_ID | Int32   |  |
| PROJECT_TEMPLATE_ID     | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| NAME                    | String  |  |
| ICON                    | String  |  |
| IS_ACTIVE               | Boolean |  |
| IS_STEPS                | Boolean |  |
| IS_DEFAULT              | Boolean |  |
| IS_KEY_TYPE             | Boolean |  |
| PROJECT_TEMPLATE_NAME   | String  |  |

## Risks
**Product-level.** Risks identified against a product.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_Risks                  | Type     | Links to |
| ------------------------ | -------- | -------- |
| *RISK_ID*                | Int32    | R_ArtifactTags.ARTIFACT_ID |
| RISK_IMPACT_ID           | Int32    | R_RiskImpacts.RISK_IMPACT_ID |
| RISK_STATUS_ID           | Int32    | R_RiskStatuses.RISK_STATUS_ID |
| RISK_PROBABILITY_ID      | Int32    | R_RiskProbabilities.RISK_PROBABILITY_ID |
| RISK_TYPE_ID             | Int32    | R_RiskTypes.RISK_TYPE_ID |
| PROJECT_ID               | Int32    | R_Projects.PROJECT_ID |
| CREATOR_ID               | Int32    | R_Users.USER_ID |
| OWNER_ID                 | Int32    | R_Users.USER_ID |
| PROJECT_GROUP_ID         | Int32    |  |
| RELEASE_ID               | Int32    | R_Releases.RELEASE_ID |
| COMPONENT_ID             | Int32    | R_Components.COMPONENT_ID |
| NAME                     | String   |  |
| DESCRIPTION              | String   |  |
| IS_DELETED               | Boolean  |  |
| CREATION_DATE            | DateTime |  |
| LAST_UPDATE_DATE         | DateTime |  |
| CONCURRENCY              | Int64    |  |
| REVIEW_DATE              | DateTime |  |
| GOAL_ID                  | Int32    |  |
| CLOSED_DATE              | DateTime |  |
| IS_ATTACHMENTS           | Boolean  |  |
| RISK_PROBABILITY_NAME    | String   |  |
| RISK_PROBABILITY_COLOR   | String   |  |
| RISK_PROBABILITY_SCORE   | Int32    |  |
| RISK_IMPACT_NAME         | String   |  |
| RISK_IMPACT_COLOR        | String   |  |
| RISK_IMPACT_SCORE        | Int32    |  |
| RISK_EXPOSURE            | Int32    |  |
| RISK_STATUS_NAME         | String   |  |
| RISK_STATUS_IS_OPEN      | Boolean  |  |
| RISK_TYPE_NAME           | String   |  |
| CREATOR_NAME             | String   |  |
| OWNER_NAME               | String   |  |
| RELEASE_VERSION_NUMBER   | String   |  |
| RELEASE_NAME             | String   |  |
| COMPONENT_NAME           | String   |  |
| GOAL_NAME                | String   |  |
| PROJECT_IS_ACTIVE        | Boolean  |  |
| PROJECT_PROJECT_GROUP_ID | Int32    |  |
| PROJECT_NAME             | String   |  |
| CUST_01 ... CUST_99      | String   |  |
| TAGS                     | String   |  |
| RISK_DETECTABILITY_ID    | Int32    |  |
| RANK                     | Int32    |  |

## Risk Impacts
**System-level.** Lookup of risk impact names.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_RiskImpacts         | Type    | Links to |
| --------------------- | ------- | -------- |
| *RISK_IMPACT_ID*      | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| NAME                  | String  |  |
| COLOR                 | String  |  |
| IS_ACTIVE             | Boolean |  |
| POSITION              | Int32   |  |
| SCORE                 | Int32   |  |
| PROJECT_TEMPLATE_NAME | String  |  |

## Risk Mitigations
**System-level.** Mitigation actions recorded against a risk.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_RiskMitigations        | Type     | Links to |
| ------------------------ | -------- | -------- |
| RISK_ID                  | Int32    | R_Risks.RISK_ID |
| *RISK_MITIGATION_ID*     | Int32    |  |
| POSITION                 | Int32    |  |
| DESCRIPTION              | String   |  |
| IS_DELETED               | Boolean  |  |
| CREATION_DATE            | DateTime |  |
| LAST_UPDATE_DATE         | DateTime |  |
| CONCURRENCY              | Int64    |  |
| IS_ACTIVE                | Boolean  |  |
| REVIEW_DATE              | DateTime |  |
| RISK_NAME                | String   |  |
| RISK_REVIEW_DATE         | DateTime |  |
| PROJECT_IS_ACTIVE        | Boolean  |  |
| PROJECT_PROJECT_GROUP_ID | Int32    |  |
| PROJECT_NAME             | String   |  |
| PROJECT_ID               | Int32    |  |

## Risk Probabilities
**System-level.** Lookup of risk probability names.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_RiskProbabilities   | Type    | Links to |
| --------------------- | ------- | -------- |
| *RISK_PROBABILITY_ID* | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| NAME                  | String  |  |
| COLOR                 | String  |  |
| IS_ACTIVE             | Boolean |  |
| POSITION              | Int32   |  |
| SCORE                 | Int32   |  |
| PROJECT_TEMPLATE_NAME | String  |  |

## Risk Statuses
**System-level.** Lookup of risk status names.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_RiskStatuses        | Type    | Links to |
| --------------------- | ------- | -------- |
| *RISK_STATUS_ID*      | Int32   |  |
| NAME                  | String  |  |
| IS_ACTIVE             | Boolean |  |
| IS_DEFAULT            | Boolean |  |
| IS_OPEN               | Boolean |  |
| POSITION              | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| PROJECT_TEMPLATE_NAME | String  |  |

## Risk Types
**System-level.** Lookup of risk type names.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_RiskTypes           | Type    | Links to |
| --------------------- | ------- | -------- |
| *RISK_TYPE_ID*        | Int32   |  |
| NAME                  | String  |  |
| IS_ACTIVE             | Boolean |  |
| IS_DEFAULT            | Boolean |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| RISK_WORKFLOW_ID      | Int32   |  |
| PROJECT_TEMPLATE_NAME | String  |  |

## Source Code Associations
**System-level.** Links between artifacts and source code revisions.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_SourceCodeAssociations           | Type     | Links to |
| ---------------------------------- | -------- | -------- |
| *ARTIFACT_SOURCE_CODE_REVISION_ID* | Int32    |  |
| ARTIFACT_TYPE_ID                   | Int32    | R_ArtifactTypes.ARTIFACT_TYPE_ID |
| ARTIFACT_ID                        | Int32    |  |
| REVISION_KEY                       | String   |  |
| COMMENT                            | String   |  |
| CREATION_DATE                      | DateTime |  |
| ARTIFACT_TYPE_NAME                 | String   |  |
| ARTIFACT_TYPE_PREFIX               | String   |  |


## Source Code Commits
**Product-level.** Commits read from a connected source control provider.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_SourceCodeCommits                | Type     | Links to |
| ---------------------------------- | -------- | -------- |
| VERSION_CONTROL_SYSTEM_ID          | Int32    |  |
| PROJECT_ID                         | Int32    | R_Projects.PROJECT_ID |
| *REVISION_ID*                      | Int32    |  |
| NAME                               | String   |  |
| REVISION_KEY                       | String   |  |
| AUTHOR_NAME                        | String   |  |
| MESSAGE                            | String   |  |
| UPDATE_DATE                        | DateTime |  |
| CONTENT_CHANGED                    | Boolean  |  |
| PROPERTIES_CHANGED                 | Boolean  |  |
| VERSION_CONTROL_SYSTEM_NAME        | String   |  |
| VERSION_CONTROL_SYSTEM_DESCRIPTION | String   |  |
| VERSION_CONTROL_SYSTEM_IS_ACTIVE   | Boolean  |  |
| PROJECT_NAME                       | String   |  |
| BRANCH_NAME                        | String   |  |
| BRANCH_PATH                        | String   |  |
| BRANCH_IS_HEAD                     | Boolean  |  |

## Tasks
**Product-level.** Tasks - the development work breaking down a requirement.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_Tasks                | Type     | Links to |
| ---------------------- | -------- | -------- |
| *TASK_ID*              | Int32    | R_ArtifactTags.ARTIFACT_ID |
| TASK_STATUS_ID         | Int32    |  |
| PROJECT_ID             | Int32    | R_Projects.PROJECT_ID |
| REQUIREMENT_ID         | Int32    |  |
| RELEASE_ID             | Int32    | R_Releases.RELEASE_ID |
| CREATOR_ID             | Int32    | R_Users.USER_ID |
| OWNER_ID               | Int32    | R_Users.USER_ID |
| TASK_PRIORITY_ID       | Int32    | R_TaskPriorities.TASK_PRIORITY_ID |
| NAME                   | String   |  |
| DESCRIPTION            | String   |  |
| CREATION_DATE          | DateTime |  |
| LAST_UPDATE_DATE       | DateTime |  |
| START_DATE             | DateTime |  |
| END_DATE               | DateTime |  |
| COMPLETION_PERCENT     | Int32    |  |
| ESTIMATED_EFFORT       | Int32    |  |
| ACTUAL_EFFORT          | Int32    |  |
| PROJECTED_EFFORT       | Int32    |  |
| REMAINING_EFFORT       | Int32    |  |
| IS_DELETED             | Boolean  |  |
| TASK_STATUS_NAME       | String   |  |
| OWNER_NAME             | String   |  |
| CREATOR_NAME           | String   |  |
| TASK_PRIORITY_NAME     | String   |  |
| PROJECT_NAME           | String   |  |
| PROJECT_GROUP_ID       | Int32    |  |
| RELEASE_VERSION_NUMBER | String   |  |
| CUST_01 ... CUST_99    | String   |  |
| TASK_TYPE_ID           | Int32    | R_TaskTypes.TASK_TYPE_ID |
| TASK_FOLDER_ID         | Int32    |  |
| IS_ATTACHMENTS         | Boolean  |  |
| CONCURRENCY            | Int64    |  |
| REQUIREMENT_NAME       | String   |  |
| TASK_TYPE_NAME         | String   |  |
| COMPONENT_ID           | Int32    |  |
| COMPONENT_NAME         | String   |  |
| RISK_ID                | Int32    |  |
| TAGS                   | String   |  |
| RANK                   | Int32    |  |

## Task Folders
**Product-level.** Folder structure organising a product's tasks.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_TaskFolders         | Type   | Links to |
| --------------------- | ------ | -------- |
| *TASK_FOLDER_ID*      | Int32  |  |
| PROJECT_ID            | Int32  |  |
| NAME                  | String |  |
| PARENT_TASK_FOLDER_ID | Int32  |  |
| HIERARCHY_LEVEL       | Int32  |  |
| INDENT_LEVEL          | String |  |

## Task Priorities
**System-level.** Lookup of task priority names.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_TaskPriorities      | Type    | Links to |
| --------------------- | ------- | -------- |
| *TASK_PRIORITY_ID*    | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| NAME                  | String  |  |
| IS_ACTIVE             | Boolean |  |
| COLOR                 | String  |  |
| SCORE                 | Int32   |  |
| PROJECT_TEMPLATE_NAME | String  |  |

## Task Types
**System-level.** Lookup of task type names.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_TaskTypes           | Type    | Links to |
| --------------------- | ------- | -------- |
| *TASK_TYPE_ID*        | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| TASK_WORKFLOW_ID      | Int32   |  |
| NAME                  | String  |  |
| POSITION              | Int32   |  |
| IS_ACTIVE             | Boolean |  |
| IS_DEFAULT            | Boolean |  |
| IS_PULL_REQUEST       | Boolean |  |
| PROJECT_TEMPLATE_NAME | String  |  |

## Teams
**System-level.** Teams defined within a product.
!!! abstract "Available in SpiraPlan only"
| R_Teams     | Type    | Links to |
| ----------- | ------- | -------- |
| *TEAM_ID*   | Int32   |  |
| NAME        | String  |  |
| DESCRIPTION | String  |  |
| IS_ACTIVE   | Boolean |  |
| IS_DELETED  | Boolean |  |

## Test Cases
**Product-level.** Test cases defined for a product.
| R_TestCases              | Type     | Links to |
| ------------------------ | -------- | -------- |
| *TEST_CASE_ID*           | Int32    | R_ArtifactTags.ARTIFACT_ID |
| EXECUTION_STATUS_ID      | Int32    |  |
| TEST_CASE_PRIORITY_ID    | Int32    | R_TestCasePriorities.TEST_CASE_PRIORITY_ID |
| PROJECT_ID               | Int32    | R_Projects.PROJECT_ID |
| AUTHOR_ID                | Int32    | R_Users.USER_ID |
| NAME                     | String   |  |
| OWNER_ID                 | Int32    | R_Users.USER_ID |
| DESCRIPTION              | String   |  |
| EXECUTION_DATE           | DateTime |  |
| CREATION_DATE            | DateTime |  |
| LAST_UPDATE_DATE         | DateTime |  |
| AUTOMATION_ENGINE_ID     | Int32    |  |
| AUTOMATION_ATTACHMENT_ID | Int32    |  |
| ESTIMATED_DURATION       | Int32    |  |
| IS_DELETED               | Boolean  |  |
| EXECUTION_STATUS_NAME    | String   |  |
| TEST_CASE_PRIORITY_NAME  | String   |  |
| AUTHOR_NAME              | String   |  |
| OWNER_NAME               | String   |  |
| AUTOMATION_ENGINE_NAME   | String   |  |
| PROJECT_NAME             | String   |  |
| PROJECT_GROUP_ID         | Int32    |  |
| CUST_01 ... CUST_99      | String   |  |
| CONCURRENCY              | Int64    |  |
| TEST_CASE_STATUS_ID      | Int32    |  |
| TEST_CASE_TYPE_ID        | Int32    | R_TestCaseTypes.TEST_CASE_TYPE_ID |
| TEST_CASE_FOLDER_ID      | Int32    |  |
| IS_ATTACHMENTS           | Boolean  |  |
| IS_TEST_STEPS            | Boolean  |  |
| ACTUAL_DURATION          | Int32    |  |
| TEST_CASE_STATUS_NAME    | String   |  |
| TEST_CASE_TYPE_NAME      | String   |  |
| COMPONENT_IDS            | String   |  |
| IS_SUSPECT               | Boolean  |  |
| TAGS                     | String   |  |
| RANK                     | Int32    |  |

## Test Case Folders
**Product-level.** Folder structure organising a product's test cases.
| R_TestCaseFolders          | Type     | Links to |
| -------------------------- | -------- | -------- |
| *TEST_CASE_FOLDER_ID*      | Int32    |  |
| PARENT_TEST_CASE_FOLDER_ID | Int32    |  |
| PROJECT_ID                 | Int32    | R_Projects.PROJECT_ID |
| NAME                       | String   |  |
| DESCRIPTION                | String   |  |
| EXECUTION_DATE             | DateTime |  |
| LAST_UPDATE_DATE           | DateTime |  |
| ESTIMATED_DURATION         | Int32    |  |
| ACTUAL_DURATION            | Int32    |  |
| COUNT_PASSED               | Int32    |  |
| COUNT_FAILED               | Int32    |  |
| COUNT_BLOCKED              | Int32    |  |
| COUNT_CAUTION              | Int32    |  |
| COUNT_NOT_RUN              | Int32    |  |
| COUNT_NOT_APPLICABLE       | Int32    |  |
| PROJECT_NAME               | String   |  |
| PROJECT_GROUP_ID           | Int32    |  |
| HIERARCHY_LEVEL            | Int32    |  |
| INDENT_LEVEL               | String   |  |

## Test Case Incidents
**System-level.** Which incidents were raised from which test cases.
| R_TestCaseIncidents | Type    | Links to |
| ------------------- | ------- | -------- |
| TEST_CASE_ID        | Int32   |  |
| INCIDENT_ID         | Int32   |  |
| DETECTED_RELEASE_ID | Int32   |  |
| RESOLVED_RELEASE_ID | Int32   |  |
| VERIFIED_RELEASE_ID | Int32   |  |
| IS_OPEN_STATUS      | Boolean |  |

## Test Case Priorities
**System-level.** Lookup of test case priority names.
| R_TestCasePriorities    | Type    | Links to |
| ----------------------- | ------- | -------- |
| *TEST_CASE_PRIORITY_ID* | Int32   |  |
| PROJECT_TEMPLATE_ID     | Int32   |  |
| NAME                    | String  |  |
| IS_ACTIVE               | Boolean |  |
| COLOR                   | String  |  |
| SCORE                   | Int32   |  |

## Test Case Types
**System-level.** Lookup of test case type names.
| R_TestCaseTypes       | Type    | Links to |
| --------------------- | ------- | -------- |
| *TEST_CASE_TYPE_ID*   | Int32   |  |
| PROJECT_TEMPLATE_ID   | Int32   | R_ProjectTemplates.PROJECT_TEMPLATE_ID |
| TEST_CASE_WORKFLOW_ID | Int32   |  |
| NAME                  | String  |  |
| IS_ACTIVE             | Boolean |  |
| POSITION              | Int32   |  |
| IS_DEFAULT            | Boolean |  |
| IS_EXPLORATORY        | Boolean |  |
| IS_BDD                | Boolean |  |
| PROJECT_TEMPLATE_NAME | String  |  |

## Test Configuration Entries
**System-level.** The individual parameter values making up a test configuration set.
| R_TestConfigurationEntries       | Type    | Links to |
| -------------------------------- | ------- | -------- |
| *TEST_CONFIGURATION_ID*          | Int32   |  |
| TEST_CONFIGURATION_SET_ID        | Int32   | R_TestConfigurationSets.TEST_CONFIGURATION_SET_ID |
| POSITION                         | Int32   |  |
| TEST_CONFIGURATION_SET_NAME      | String  |  |
| IS_TEST_CONFIGURATION_SET_ACTIVE | Boolean |  |
| CUSTOM_PROPERTY_VALUE_ID         | Int32   |  |
| TEST_CASE_PARAMETER_NAME         | String  |  |
| TEST_CASE_PARAMETER_VALUE        | String  |  |
| PROJECT_NAME                     | String  |  |
| PROJECT_GROUP_ID                 | Int32   |  |
| PROJECT_ID                       | Int32   |  |

## Test Configuration Sets
**Program-level.** Sets of parameter combinations a test set can be run against.
| R_TestConfigurationSets     | Type     | Links to |
| --------------------------- | -------- | -------- |
| *TEST_CONFIGURATION_SET_ID* | Int32    |  |
| PROJECT_ID                  | Int32    | R_Projects.PROJECT_ID |
| NAME                        | String   |  |
| DESCRIPTION                 | String   |  |
| IS_ACTIVE                   | Boolean  |  |
| IS_DELETED                  | Boolean  |  |
| CREATION_DATE               | DateTime |  |
| LAST_UPDATED_DATE           | DateTime |  |
| CONCURRENCY                 | Int64    |  |
| PROJECT_NAME                | String   |  |
| PROJECT_GROUP_ID            | Int32    |  |

## Test Runs
**Product-level.** Executions of a test case, with their result and timing.
TEST_RUN_TYPE_ID: 1 = Manual, 2 = Automated
| R_TestRuns             | Type     | Links to |
| ---------------------- | -------- | -------- |
| *TEST_RUN_ID*          | Int32    | R_ArtifactTags.ARTIFACT_ID |
| TEST_CASE_ID           | Int32    | R_TestCases.TEST_CASE_ID |
| NAME                   | String   |  |
| DESCRIPTION            | String   |  |
| ESTIMATED_DURATION     | Int32    |  |
| ACTUAL_DURATION        | Int32    |  |
| TEST_RUN_TYPE_ID       | Int32    |  |
| TESTER_ID              | Int32    | R_Users.USER_ID |
| EXECUTION_STATUS_ID    | Int32    |  |
| START_DATE             | DateTime |  |
| END_DATE               | DateTime |  |
| RUNNER_NAME            | String   |  |
| RUNNER_TEST_NAME       | String   |  |
| RUNNER_ASSERT_COUNT    | Int32    |  |
| RUNNER_MESSAGE         | String   |  |
| RUNNER_STACK_TRACE     | String   |  |
| EXECUTION_STATUS_NAME  | String   |  |
| TESTER_NAME            | String   |  |
| TEST_RUNS_PENDING_ID   | Int32    |  |
| RELEASE_ID             | Int32    | R_Releases.RELEASE_ID |
| TEST_SET_ID            | Int32    | R_TestSets.TEST_SET_ID |
| TEST_SET_TEST_CASE_ID  | Int32    |  |
| RELEASE_NAME           | String   |  |
| RELEASE_VERSION_NUMBER | String   |  |
| TEST_SET_NAME          | String   |  |
| TEST_RUN_TYPE_NAME     | String   |  |
| AUTOMATION_HOST_ID     | Int32    | R_AutomationHosts.AUTOMATION_HOST_ID |
| AUTOMATION_HOST_NAME   | String   |  |
| AUTOMATION_ENGINE_ID   | Int32    |  |
| BUILD_ID               | Int32    | R_Builds.BUILD_ID |
| BUILD_NAME             | String   |  |
| TEST_RUN_FORMAT_ID     | Int32    |  |
| PROJECT_NAME           | String   |  |
| PROJECT_GROUP_ID       | Int32    |  |
| CUST_01 ... CUST_99    | String   |  |
| IS_ATTACHMENTS         | Boolean  |  |
| IS_DELETED             | Boolean  |  |
| CONCURRENCY            | Int64    |  |
| PROJECT_ID             | Int32    |  |
| CHANGESET_ID           | Int64    |  |
| TEST_CONFIGURATION_ID  | Int32    |  |
| TAGS                   | String   |  |

## Test Run Incidents
**System-level.** Which incidents were raised from which test runs.
| R_TestRunIncidents  | Type    | Links to |
| ------------------- | ------- | -------- |
| *TEST_RUN_ID*       | Int32   |  |
| INCIDENT_ID         | Int32   |  |
| DETECTED_RELEASE_ID | Int32   |  |
| RESOLVED_RELEASE_ID | Int32   |  |
| VERIFIED_RELEASE_ID | Int32   |  |
| IS_OPEN_STATUS      | Boolean |  |
| TEST_STEP_ID        | Int32   |  |
| TEST_RUN_STEP_ID    | Int32   |  |

## Test Run Steps
**Product-level.** The result recorded for each step of a test run.
| R_TestRunSteps        | Type     | Links to |
| --------------------- | -------- | -------- |
| *TEST_RUN_STEP_ID*    | Int32    |  |
| EXECUTION_STATUS_ID   | Int32    |  |
| TEST_CASE_ID          | Int32    |  |
| TEST_STEP_ID          | Int32    |  |
| TEST_RUN_ID           | Int32    |  |
| DESCRIPTION           | String   |  |
| POSITION              | Int32    |  |
| EXPECTED_RESULT       | String   |  |
| SAMPLE_DATA           | String   |  |
| ACTUAL_RESULT         | String   |  |
| EXECUTION_STATUS_NAME | String   |  |
| TEST_CASE_NAME        | String   |  |
| PROJECT_ID            | Int32    |  |
| PROJECT_NAME          | String   |  |
| PROJECT_GROUP_ID      | Int32    |  |
| START_DATE            | DateTime |  |
| END_DATE              | DateTime |  |
| ACTUAL_DURATION       | Int32    |  |

## Test Sets
**Product-level.** Test sets - groups of test cases scheduled to be run together.
| R_TestSets                  | Type     | Links to |
| --------------------------- | -------- | -------- |
| *TEST_SET_ID*               | Int32    | R_ArtifactTags.ARTIFACT_ID |
| PROJECT_ID                  | Int32    | R_Projects.PROJECT_ID |
| RELEASE_ID                  | Int32    | R_Releases.RELEASE_ID |
| TEST_SET_STATUS_ID          | Int32    |  |
| CREATOR_ID                  | Int32    | R_Users.USER_ID |
| OWNER_ID                    | Int32    | R_Users.USER_ID |
| AUTOMATION_HOST_ID          | Int32    | R_AutomationHosts.AUTOMATION_HOST_ID |
| TEST_RUN_TYPE_ID            | Int32    |  |
| RECURRENCE_ID               | Int32    |  |
| NAME                        | String   |  |
| DESCRIPTION                 | String   |  |
| CREATION_DATE               | DateTime |  |
| PLANNED_DATE                | DateTime |  |
| LAST_UPDATE_DATE            | DateTime |  |
| IS_DELETED                  | Boolean  |  |
| CONCURRENCY                 | Int64    |  |
| RELEASE_VERSION_NUMBER      | String   |  |
| PROJECT_NAME                | String   |  |
| TEST_CASE_COUNT             | Int32    |  |
| TEST_SET_STATUS_NAME        | String   |  |
| CREATOR_NAME                | String   |  |
| OWNER_NAME                  | String   |  |
| PROJECT_ACTIVE_YN           | String   |  |
| PROJECT_IS_ACTIVE           | Boolean  |  |
| AUTOMATION_HOST_NAME        | String   |  |
| TEST_RUN_TYPE_NAME          | String   |  |
| RECURRENCE_NAME             | String   |  |
| PROJECT_GROUP_ID            | Int32    |  |
| CUST_01 ... CUST_99         | String   |  |
| TEST_SET_FOLDER_ID          | Int32    |  |
| IS_ATTACHMENTS              | Boolean  |  |
| BUILD_EXECUTE_TIME_INTERVAL | Int32    |  |
| ESTIMATED_DURATION          | Int32    |  |
| ACTUAL_DURATION             | Int32    |  |
| COUNT_PASSED                | Int32    |  |
| COUNT_FAILED                | Int32    |  |
| COUNT_CAUTION               | Int32    |  |
| COUNT_BLOCKED               | Int32    |  |
| COUNT_NOT_RUN               | Int32    |  |
| COUNT_NOT_APPLICABLE        | Int32    |  |
| EXECUTION_DATE              | DateTime |  |
| IS_DYNAMIC                  | Boolean  |  |
| DYNAMIC_QUERY               | String   |  |
| IS_AUTO_SCHEDULED           | Boolean  |  |
| TEST_CONFIGURATION_SET_ID   | Int32    |  |
| TAGS                        | String   |  |
| RANK                        | Int32    |  |

## Test Set Folders
**Product-level.** Folder structure organising a product's test sets.
| R_TestSetFolders          | Type     | Links to |
| ------------------------- | -------- | -------- |
| *TEST_SET_FOLDER_ID*      | Int32    |  |
| PROJECT_ID                | Int32    | R_Projects.PROJECT_ID |
| PARENT_TEST_SET_FOLDER_ID | Int32    |  |
| NAME                      | String   |  |
| DESCRIPTION               | String   |  |
| CREATION_DATE             | DateTime |  |
| LAST_UPDATE_DATE          | DateTime |  |
| EXECUTION_DATE            | DateTime |  |
| ESTIMATED_DURATION        | Int32    |  |
| ACTUAL_DURATION           | Int32    |  |
| COUNT_PASSED              | Int32    |  |
| COUNT_FAILED              | Int32    |  |
| COUNT_CAUTION             | Int32    |  |
| COUNT_BLOCKED             | Int32    |  |
| COUNT_NOT_RUN             | Int32    |  |
| COUNT_NOT_APPLICABLE      | Int32    |  |
| PROJECT_NAME              | String   |  |
| PROJECT_GROUP_ID          | Int32    |  |
| HIERARCHY_LEVEL           | Int32    |  |
| INDENT_LEVEL              | String   |  |

## Test Set Incidents
**System-level.** Which incidents were raised from which test sets.
| R_TestSetIncidents  | Type    | Links to |
| ------------------- | ------- | -------- |
| TEST_SET_ID         | Int32   |  |
| INCIDENT_ID         | Int32   |  |
| DETECTED_RELEASE_ID | Int32   |  |
| RESOLVED_RELEASE_ID | Int32   |  |
| VERIFIED_RELEASE_ID | Int32   |  |
| IS_OPEN_STATUS      | Boolean |  |

## Test Set Test Cases
**System-level.** Which test cases belong to which test set, and in what order.
| R_TestSetTestCases      | Type     | Links to |
| ----------------------- | -------- | -------- |
| *TEST_SET_TEST_CASE_ID* | Int32    |  |
| TEST_SET_ID             | Int32    | R_TestSets.TEST_SET_ID |
| TEST_CASE_ID            | Int32    | R_TestCases.TEST_CASE_ID |
| OWNER_ID                | Int32    | R_Users.USER_ID |
| POSITION                | Int32    |  |
| TEST_SET_NAME           | String   |  |
| TEST_CASE_NAME          | String   |  |
| OWNER_NAME              | String   |  |
| PROJECT_ID              | Int32    |  |
| PROJECT_NAME            | String   |  |
| PLANNED_DATE            | DateTime |  |
| IS_SETUP_TEARDOWN       | Boolean  |  |

## Test Steps
**Product-level.** The individual steps making up a test case.
| R_TestSteps           | Type     | Links to |
| --------------------- | -------- | -------- |
| *TEST_STEP_ID*        | Int32    |  |
| TEST_CASE_ID          | Int32    | R_TestCases.TEST_CASE_ID |
| EXECUTION_STATUS_ID   | Int32    |  |
| DESCRIPTION           | String   |  |
| LINKED_TEST_CASE_ID   | Int32    |  |
| POSITION              | Int32    |  |
| EXPECTED_RESULT       | String   |  |
| SAMPLE_DATA           | String   |  |
| LAST_UPDATE_DATE      | DateTime |  |
| IS_DELETED            | Boolean  |  |
| EXECUTION_STATUS_NAME | String   |  |
| TEST_CASE_NAME        | String   |  |
| PROJECT_ID            | Int32    |  |
| PROJECT_NAME          | String   |  |
| PROJECT_GROUP_ID      | Int32    |  |
| CUST_01 ... CUST_99   | String   |  |
| IS_ATTACHMENTS        | Boolean  |  |
| CONCURRENCY           | Int64    |  |
| PRECONDITION          | String   |  |


## Timesheets
**System-level.** Weekly timesheets submitted for approval.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
One row per timesheet. For the time booked within one, use R_TimesheetEntries.
| R_Timesheets          | Type     | Links to |
| --------------------- | -------- | -------- |
| *TIMESHEET_ID*        | Int32    |  |
| SUBMITTER_USER_ID     | Int32    | R_Users.USER_ID |
| SUBMITTER_USER_NAME   | String   |  |
| APPROVER_USER_ID      | Int32    | R_Users.USER_ID |
| APPROVER_USER_NAME    | String   |  |
| TIMESHEET_STATUS_ID   | Int32    | R_TimesheetStatuses.TIMESHEET_STATUS_ID |
| TIMESHEET_STATUS_NAME | String   |  |
| CREATION_DATE         | DateTime |  |
| APPROVAL_DATE         | DateTime |  |
| LAST_UPDATE_DATE      | DateTime |  |
| START_DATE            | DateTime |  |
| END_DATE              | DateTime |  |
| COMMENTS              | String   |  |
| APPROVER_COMMENTS     | String   |  |

## Timesheet Entries
**System-level.** Individual time entries booked against an artifact.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_TimesheetEntries   | Type     | Links to |
| -------------------- | -------- | -------- |
| *TIMESHEET_ENTRY_ID* | Int32    |  |
| TIMESHEET_ID         | Int32    |  |
| USER_ID              | Int32    | R_Users.USER_ID |
| USER_NAME            | String   |  |
| ARTIFACT_TYPE_ID     | Int32    | R_ArtifactTypes.ARTIFACT_TYPE_ID |
| ARTIFACT_TYPE_NAME   | String   |  |
| ARTIFACT_ID          | Int32    | R_Incidents.INCIDENT_ID, R_Tasks.TASK_ID |
| ARTIFACT_NAME        | String   |  |
| EFFORT_MINUTES       | Int32    |  |
| EFFORT_DATE          | DateTime |  |
| PROJECT_ID           | Int32    | R_Projects.PROJECT_ID |
| PROJECT_NAME         | String   |  |
| PROJECT_GROUP_ID     | Int32    | R_ProjectGroups.PROJECT_GROUP_ID |
| PROJECT_GROUP_NAME   | String   |  |
| RESOURCE_CATEGORY_ID | Int32    |  |

## Timesheet Statuses
**System-level.** Lookup of timesheet status names.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
| R_TimesheetStatuses   | Type    | Links to |
| --------------------- | ------- | -------- |
| *TIMESHEET_STATUS_ID* | Int32   |  |
| TIMESHEET_STATUS_NAME | String  |  |
| IS_ACTIVE             | Boolean |  |
| IS_OPEN               | Boolean |  |

## Timesheets with Entries
**System-level.** One row per time entry, with its parent timesheet's fields joined on.
!!! abstract "Available in SpiraTeam and SpiraPlan only"
Combines R_Timesheets and R_TimesheetEntries. One row per entry, not per timesheet, so summing a timesheet-level column over this view double counts.
| R_TimesheetWithEntries | Type     | Links to |
| ---------------------- | -------- | -------- |
| TIMESHEET_ID           | Int32    | R_Timesheets.TIMESHEET_ID |
| SUBMITTER_USER_ID      | Int32    |  |
| SUBMITTER_USER_NAME    | String   |  |
| APPROVER_USER_ID       | Int32    |  |
| APPROVER_USER_NAME     | String   |  |
| TIMESHEET_STATUS_ID    | Int32    |  |
| TIMESHEET_STATUS_NAME  | String   |  |
| CREATION_DATE          | DateTime |  |
| APPROVAL_DATE          | DateTime |  |
| LAST_UPDATE_DATE       | DateTime |  |
| START_DATE             | DateTime |  |
| END_DATE               | DateTime |  |
| COMMENTS               | String   |  |
| APPROVER_COMMENTS      | String   |  |
| *TIMESHEET_ENTRY_ID*   | Int32    |  |
| ARTIFACT_TYPE_ID       | Int32    | R_ArtifactTypes.ARTIFACT_TYPE_ID |
| ARTIFACT_TYPE_NAME     | String   |  |
| ARTIFACT_ID            | Int32    | R_Incidents.INCIDENT_ID, R_Tasks.TASK_ID |
| ARTIFACT_NAME          | String   |  |
| EFFORT_MINUTES         | Int32    |  |
| EFFORT_DATE            | DateTime |  |
| PROJECT_ID             | Int32    | R_Projects.PROJECT_ID |
| PROJECT_NAME           | String   |  |
| PROJECT_GROUP_ID       | Int32    | R_ProjectGroups.PROJECT_GROUP_ID |
| PROJECT_GROUP_NAME     | String   |  |
| RESOURCE_CATEGORY_ID   | Int32    |  |


## Users
**System-level.** User accounts, with their profile details.
| R_Users                         | Type     | Links to |
| ------------------------------- | -------- | -------- |
| *USER_ID*                       | Int32    |  |
| USER_NAME                       | String   |  |
| EMAIL_ADDRESS                   | String   |  |
| IS_ACTIVE                       | Boolean  |  |
| CREATION_DATE                   | DateTime |  |
| LDAP_DN                         | String   |  |
| FIRST_NAME                      | String   |  |
| LAST_NAME                       | String   |  |
| MIDDLE_INITIAL                  | String   |  |
| DEPARTMENT                      | String   |  |
| LAST_UPDATE_DATE                | DateTime |  |
| TIMEZONE                        | String   |  |
| LAST_OPENED_PROJECT_ID          | Int32    |  |
| IS_APPROVED                     | Boolean  |  |
| LAST_LOGIN_DATE                 | DateTime |  |
| LAST_ACTIVITY_DATE              | DateTime |  |
| ORGANIZATION                    | String   |  |
| LAST_OPENED_PROJECT_GROUP_ID    | Int32    |  |
| LAST_OPENED_PROJECT_TEMPLATE_ID | Int32    |  |
| IS_ADMIN                        | Boolean  |  |
| IS_REPORT_ADMIN                 | Boolean  |  |
| IS_RESOURCE_ADMIN               | Boolean  |  |
| IS_PORTFOLIO_ADMIN              | Boolean  |  |
| LAST_PASSWORD_CHANGED_DATE      | DateTime |  |
| LOGIN_PROVIDER_NAME             | String   |  |
| IS_TIMESHEET_MANAGER            | Boolean  |  |
