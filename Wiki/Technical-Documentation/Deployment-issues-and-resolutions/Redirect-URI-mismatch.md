## Redirect URI mismatch upon sign in.

### Context
When signing in on the app and encountered a redirect uri mismatch error.

Sample Error:
```
[https://uat.spectia-envr.com/api/auth/signin/azure-ad-b2c?error=redirect_uri_mismatch&error_description=AADB2C90006%3a+The+redirect+URI+%27https%3a%2f%2fuat.spectia-envr.com%2fapi%2fauth%2fcallback%2fazure-ad-b2c%27+provided+in+the+request+is+not+registered+for+the+client+id+%275272dc87-d922-49a4-8fdf-c6653cf50262%27.%0d%0aCorrelation+ID%3a+6bd0a843-56a4-4ddc-830d-0fb5b8a05d5c%0d%0aTimestamp%3a+2024-11-26+08%3a05%3a06Z%0d%0a&state=FwNw8_h7eCH4I7iWZ0PsC-DuRN7PqG-yxSabfTdg1Xo](https://uat.spectia-envr.com/api/auth/signin/azure-ad-b2c?error=redirect_uri_mismatch&error_description=AADB2C90006%3a+The+redirect+URI+%27https%3a%2f%2fuat.spectia-envr.com%2fapi%2fauth%2fcallback%2fazure-ad-b2c%27+provided+in+the+request+is+not+registered+for+the+client+id+%275272dc87-d922-49a4-8fdf-c6653cf50262%27.%0d%0aCorrelation+ID%3a+6bd0a843-56a4-4ddc-830d-0fb5b8a05d5c%0d%0aTimestamp%3a+2024-11-26+08%3a05%3a06Z%0d%0a&state=FwNw8_h7eCH4I7iWZ0PsC-DuRN7PqG-yxSabfTdg1Xo "https://uat.spectia-envr.com/api/auth/signin/azure-ad-b2c?error=redirect_uri_mismatch&error_description=aadb2c90006%3a+the+redirect+uri+%27https%3a%2f%2fuat.spectia-envr.com%2fapi%2fauth%2fcallback%2fazure-ad-b2c%27+provided+in+the+request+is+not+registered+for+the+client+id+%275272dc87-d922-49a4-8fdf-c6653cf50262%27.%0d%0acorrelation+id%3a+6bd0a843-56a4-4ddc-830d-0fb5b8a05d5c%0d%0atimestamp%3a+2024-11-26+08%3a05%3a06z%0d%0a&state=fwnw8_h7ech4i7iwz0psc-durn7pqg-yxsabftdg1xo")
```

### Issue
Frontend uri needs to be whitelisted in azure b2c.

### How to fix.
1. Go to Azure B2C for the target environment. (Might need to switch the directory)
2. Go to App Registrations > All applications > frontend > Authentication
3. Here you can see the Redirect URIs list.
4. Add Uri, in this case its `https://uat.spectia-envr.com/api/auth/callback/azure-ad-b2c`

This process may take time to take effect. (5 - 10 minutes ish)

Additionally, you can execute a sample login flow by following these steps.
1. Go to Azure B2C for the target environment. (Might need to switch the directory)
2. Go to App Registrations > Identity Experience Framework > B2C_1A_SIGNIN 
3. Select `frontend` for the application
4. Select `https://uat.spectia-envr.com/api/auth/callback/azure-ad-b2c` for reply url
5. Click `Run now`
6. This will open up a sign in page, just follow through.


Incident History
-----------------
11/26/2024


