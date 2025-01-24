## 401 Response code on one of the services, but other service is returning 200
### Context:
 - When invoice service works but account service returns 401.

### Issue:
 - ![image.png](/.attachments/image-9f36d224-8a5a-46f6-9a52-aac79852533b.png)

 ```
IDX10214: Audience validation failed. Audiences: '5272dc87-d922-49a4-8fdf-c6653cf50262'. Did not match: validationParameters.ValidAudience: 'null' or validationParameters.ValidAudiences: '7c422a78-2b66-4569-aea6-8894db021742'. 
```
### How to identify problem:
1. Open application insights in azure
2. Check failures.
3. Check 401 requests returning response code

### Solution: 
1. Go to APIM > API > Select API > All Operations.
2. On the Inbound processing pane, select `validate-jwt`
3. This will open up the policy xml.
4. Verify valid audiences is set correctly for all the services (Invoice API, Accounts API, etc)

DEV:
```
            <audiences>
                <audience>77364209-524c-47aa-9448-3ea6f05f1830</audience>
                <audience>7d0c4a11-7de6-4c7b-aeed-473cc2803219</audience>
            </audiences>
```

UAT:
```
            <audiences>
                <audience>7c422a78-2b66-4569-aea6-8894db021742</audience>
                <audience>5272dc87-d922-49a4-8fdf-c6653cf50262</audience>
            </audiences>
```
5. The audience id is the client id for the apps that we defined in Azure B2C.
e.g. frontend, postman
It is found on the Azure B2C directory > Overview

Incident History
-----------------
11/27/2024