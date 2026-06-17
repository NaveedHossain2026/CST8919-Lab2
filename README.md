# CST8919 Lab 2: Building a Web App with Threat Detection using Azure Monitor and KQL

## Demo Video
https://youtu.be/g1aqiQYCliQ

### What I Learned

- How Azure streams real-time application logs into a Log Analytics Workspace for monitoring.
- How to use KQL queries to detect suspicious activity and trigger email alerts by Action Groups.

### Challenges Faced

- Azure validation errors when creating alert rules due to missing or strict threshold settings.
- VS Code “Restricted Mode” blocks API requests until workspace trust is enabled. 

### Real-World Improvements

- Using structured logs (JSON) to make it easier to detect real attacks vs normal user mistakes.
- Automating response actions (like blocking IPs using Logic Apps) instead of just sending email alerts.

### KQL Query Explained

```txt
AppServiceConsoleLogs
| where ResultDescription has "FAILED_LOGIN"
```
- AppServiceConsoleLogs: Gets log data from the Azure App Service.
-|: Passes data to the next step.
- where ResultDescription has "FAILED_LOGIN": Filters logs to only show failed login attempts.
  
