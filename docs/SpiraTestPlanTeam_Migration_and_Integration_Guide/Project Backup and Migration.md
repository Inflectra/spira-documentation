#  Project Backup and Migration

This application allows an entire project to be exported to a backup
file, for archiving and offline storage of SpiraTeam projects. The base
minimum SpiraTeam version required is 3.2 (014), and there is some data
that is not backed up, see the section 5.5 for details. Also there are
separate versions of the backup and migration tool for SpiraTeam v3.2,
v4.x and v5.x, and you need to use the appropriate version that matches
your installations.

The migration tool **does not support upgrading versions**, i.e. you
need to have the same version of SpiraTeam for both the import and
export phase. If you have two different versions of SpiraTeam, you must
first upgrade the older installation to the same version as the newer
one.

## Main Screen

When running the application, you will see the main screen, which gives
you three main options: Export, Import, and Transfer:

![main](img/Project_Backup_and_Migration_53.png)




## Project Export

Clicking the Export button will start the Export wizard, allowing you to
save the project to a file.\
![](img/Project_Backup_and_Migration_54.png)




On the first screen, enter in the SpiraTeam server URL, and the
administrator account password. The administrator account must be used,
so make sure that it is an active account (Active: Yes) in the
application. When clicking the 'Next' button, it will verify the server
and login information.

The second screen gives you the selection of the project to export.
Select the project, and then click the 'Next' button.

![](img/Project_Backup_and_Migration_55.png)




On the third screen, select the location and name of the file you wish
to export the project to. If the file already exists, it will be
overwritten.

![](img/Project_Backup_and_Migration_56.png)




The next screen is the verification screen -- make sure you wish to
start the export, and then click the 'Next' button. Once started, you
cannot cancel or change any options. To change an option, click the
'Back' button at any time before starting the process to go back a
screen.

![ready to
export](img/Project_Backup_and_Migration_57.png)




Once finished, your output file will be created. You can store and
backup the file as you need.

## Project Import

To import a project file into a new project in SpiraTeam, select the
Import button on the main screen. This will start the Import wizard:

![](img/Project_Backup_and_Migration_58.png)




On the first screen, enter in the SpiraTeam server URL, and the
administrator account password. The administrator account must be used,
so make sure that it is an active account (Active: Yes) in the
application. When clicking the 'Next' button, it will verify the server
and login information.

![](img/Project_Backup_and_Migration_59.png)




The second screen allows you to enter in a name for the project created.
You can enter in the name of an existing project, but a new project by
that name will be created -- it will not import the project into an
existing project.

The third screen is only present on the SpiraTeam v4.0 version of the
migration tool. This is because the SpiraTeam 4.0 API requires that new
user's be created with passwords of specific strength. Any user in the
project file that is not present in the destination system will be
created with the password that you specify:

![](img/Project_Backup_and_Migration_60.png)




You should enter a password, click the 'Test' button to make sure it
will be accepted by SpiraTeam, and then click the 'Next' button. This
will then display the fourth screen:

![](img/Project_Backup_and_Migration_61.png)




The fourth screen will let you select the PRJ Project file. Select the
file by clicking on the folder button, and the application will verify
the integrity of the file before performing the import:

![](img/Project_Backup_and_Migration_62.png)




The last screen will let you verify your settings before starting the
import. If any changes need to be made, click the Back button. Once
ready to import the project, click the 'Finish button to start the
import.

If any error occurs during import, it's not recommended to use the
project created in the application, although you can log in and view the
data that was imported.

## Project Transfer

Selecting the 'Transfer' button will start the transfer wizard, which
contains screens from both the Import and Export wizards, above.

The first two screens will let you select the SpiraTeam application to
pull the project from, following the same information as the first two
screens in the Export wizard.

The next three screens will ask for the new SpiraTeam application to
create the project in and the default password for any new users that
need to be created. These three screens follow the first three screens
of the Import wizard, above. Note that the application will try to
determine if you're trying to re-import the project into the same
server, and advise that copying the project in the SpiraTeam UI is a
better choice.

The final screen will provide a summary of the chosen settings. Once you
click 'Next', the transfer process will start:

![transfer](img/Project_Backup_and_Migration_63.png)




Once transfer starts, the entire project will be unloaded into a
temporary directory on the computer running the application, and then
the project will be imported into the new system.

## Data Transferred

***Data***               ***SpiraTeam v3.2***   
**Exported**           **Imported**
Incidents                                      
Requirements                                   
Tasks                                          
Releases                                       
Test Cases                                     
Test Sets                                      
Test Runs                                      
Custom Properties                              
Custom Lists                                   
Document Files                                 
Document Folders                               
Document Types                                 
Comments / Resolutions                         
Datasync Mappings                              
Automation Hosts                               
Automation Engines                             
Project Roles                                  
Project Users                                  ^1^

The table on the left shows what data is backed up and restored. Future
versions of the Migration tool and SpiraTeam may support exporting and
importing more data.

The exported project file may be large, since the binary data of all the
attachments are downloaded and contained within the file.

Once an export is completed, the migration tool will not delete the
project from the system -- you must still do that through the UI. Any
changes in the project will not automatically be updated in the export
file; you must re-run the export.

***Notes:***

^1^Users imported back into v3.2 will be marked Active, even if they
were originally inactive.**4B**

