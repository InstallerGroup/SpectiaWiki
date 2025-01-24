# Customized login page int Azure AD B2C 

## Frontend:
To keep track of the sign in and reset password html styles.
```
/public/custom-aadb2c-pages
|-sign-in.html
|-reset-password.html
|-template.html
```
1. Use the `template.html` file to apply styling changes
2. Once the styling is finalized, copy the styles to either `sign-in.html` or `reset-password.html`
3. Push to repository

## Upload to public storage account 
1. Upload the file that has been change to the storage account in Azure portal
2. Storage Account > stspectiadevpublic (this might change depending on the environment) > Containers > $web 
3. Upload the file(s)
4. Test the file if publicly accessible: `https://stspectiadevpublic.z6.web.core.windows.net/sign-in.html`
5. Try the sign-in flow.

(Other static files needed by the UI should be uploaded as well. E.g. icon, images)

## Build custom policy
1. Clone repo: [merkle-ne-installatorgruppen/installergroup-b2c-custom-policies](https://github.com/merkle-ne-installatorgruppen/installergroup-b2c-custom-policies)
2. Using VSCode, Install Azure AD B2C extension
3. Execute Build all policy.
![image.png](/.attachments/image-6370ca83-7322-4689-9a23-1a3f50dc11ab.png)
4. This will generate folder per environment with the appropriate policies and settings.


## Upload custom policy to Azure AD B2C Directory.
1. Go to Azure portal
2. Switch to the appropriate Azure AD Directory (Top right)
DEV = Spectia - B2C Development
UAT = Spectia - B2C Acceptance
PROD = Spectia - B2C Production
3. Go to Azure AD B2C > Identity Experience Framework > Custom Policies
4. Select and download policy (for backup purposes)
5. Upload custom policy {Environment}/{policy-file}.xml
6. Test changes by selecting B2C_1A_SIGNIN > Run Now.

Link to azure storage accounts: [Storage accounts - Microsoft Azure](https://portal.azure.com/#browse/Microsoft.Storage%2FStorageAccounts)


### References:
[https://learn.microsoft.com/en-us/azure/active-directory-b2c/customize-ui-with-html?pivots=b2c-custom-policy#custom-html-and-css-overview](https://learn.microsoft.com/en-us/azure/active-directory-b2c/customize-ui-with-html?pivots=b2c-custom-policy#custom-html-and-css-overview)
