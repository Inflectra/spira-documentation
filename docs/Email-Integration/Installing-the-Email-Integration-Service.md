# Installing the Email Integration Service

This section outlines how to install the SpiraTeam email integration
service onto your environment. Depending on your environment you can
install the email integration service on:

1. Your SpiraTeam application server
1. Your corporate mail server
1. A separate workstation that can connect to both SpiraTeam and your
mail server

If your SpiraTeam installation is installed on-premise, then you can use
options (1), (2) or (3), if your SpiraTeam installation is hosted by
Inflectra as a Software as a Service (SaaS) subscription then you'd need
to use either option (2) or (3).

Once you have downloaded the SpiraTeam email integration installation
package (InflectraEmailIntegration.msi) from the Inflectra website you
should download it onto the appropriate computer and double-click on it
to run the Windows installer package.

Installation is automatic, and will install the configuration and service
into default locations.

Once the installation has completed, you will see the following new
service listed in the Control Panel \> Administrative Tools \> Windows
Services section:

![](img/install_1.png)

The service should be listed to run in Automatic mode and should already
be started.

Note: This email integration service is able to integrate with both
KronoDesk and SpiraTeam from Inflectra, however the focus of this guide
is the integration with SpiraTest, SpiraPlan and SpiraTeam (hereafter
SpiraTeam) only.