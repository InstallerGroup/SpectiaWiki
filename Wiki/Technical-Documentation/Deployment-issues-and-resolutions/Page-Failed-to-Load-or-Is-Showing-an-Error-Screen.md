Context
-------

This guide provides steps for diagnosing and resolving issues when the front-end application fails to load or displays errors.

Issue
-----

The front-end has encountered internal errors and is unable to recover.

Solution
--------

### Step 1: Manually Trigger Deployment Pipeline

1. Navigate to the **GitHub repository** for the front-end application.
2. Go to **Actions** from the repository menu. 
[Workflow runs · merkle-ne-installatorgruppen/installergroup-frontend](https://github.com/merkle-ne-installatorgruppen/installergroup-frontend/actions)]
3. Trigger the deployment pipeline manually to redeploy the front-end application.
Optionally, the redeploy can be made via cli in azure portal. For more info, Ask Timmi.
```
az staticwebapp update --name <your-static-web-app-name> --resource-group <your-resource-group>
```

### Step 2: Verify the Deployment Status

1.  Ensure that the pipeline completes successfully.
2.  Monitor the logs for any errors or failures during deployment.

Additional Checks
-----------------

### Step 1: Application Insights (If configured)

1.  Verify that **Application Insights** is properly installed and configured in the front-end application.
2.  Check for any logged exceptions or performance issues that could indicate the root cause of the error.
By following these steps, DevOps teams can efficiently diagnose, and address issues related to front-end loading failures.

Incident History
-----------------
12/02/2024
