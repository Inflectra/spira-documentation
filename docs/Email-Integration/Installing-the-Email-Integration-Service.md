# Installing the Email Integration Service

!!! info ""
    This email integration service is able to integrate with both KronoDesk and Spira.

## Installation
Depending on your environment you can install the email integration service on:

1. Your Spira application server
2. Your corporate mail server
3. A separate workstation that can connect to both Spira and your mail server

If your Spira installation is installed on-premise, you can use options (1), (2) or (3).

if your Spira installation is cloud hosted by Inflectra, you can use options (2) or (3).

After downloading the Spira email integration installation package (InflectraEmailIntegration.msi) from the Inflectra website onto the relevant machine, double-click it to run the Windows installer package. Installation is automatic, and will install the configuration and service into default locations.

Once the installation has completed, you will see the following new service listed in the Control Panel > Administrative Tools > Windows Services section:

![](img/install_1.png)

The service should be listed to run in Automatic mode and should already be started.


## Next Steps
1. [Configure the email integration](./Configuring-the-Email-Integration-Service.md)
2. [Use the email integration](./Using-the-Email-Integration-Service-with-SpiraTeam.md)
