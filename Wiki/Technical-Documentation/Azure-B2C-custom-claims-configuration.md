### Overview:

Currently, we use the `/GetUserClaims` endpoint of the Accounts service to fetch user details for authentication. These details are included in the token passed between systems. To enable Azure B2C to access this endpoint, we must expose it securely by using Basic Authentication. The steps below outline how to configure Azure B2C to interact with this endpoint.

Step-by-Step Setup Process:
---------------------------

### 1. Access the Azure B2C Identity Experience Framework

*   Log in to the **Azure Portal**.
*   Navigate to **Azure Active Directory** > **Azure AD B2C**.
*   Under the **Identity Experience Framework** section, access the **Identity Experience Framework** settings.

### 2. Upload the Latest Trust Framework Extensions File

*   Navigate to the **Identity Experience Framework** section.
*   Upload the latest version of the `B2C_1A_TRUSTFRAMEWORKEXTENSIONS` file.
*   This file should match the environment build you are working with. For reference, check the relevant file from the repository.

### 3. Configure Policy Keys for Basic Authentication

#### 3.1 Create the Username Policy Key

*   Under **Manage**, go to **Policy Keys**.
*   Click **Add** to create a new key.
*   In the **Add a Key** window, select **Manual** for key creation.
*   Fill in the following details:
    *   **Name**: `RestApiUserName`
    *   **Secret**: Enter the **username** that will be used for Basic Authentication.
    *   **Key Usage**: Select **Encryption**.
*   Click **Create** to save the policy key.

#### 3.2 Create the Password Policy Key

*   Repeat the process from step 3.1 to create another policy key:
    *   **Name**: `RestApiPassword`
    *   **Secret**: Enter the **super secret password** for Basic Authentication.
    *   **Key Usage**: Select **Encryption**.
*   Click **Create** to save the password policy key.

### 4. Test the Policy

*   Navigate to **Custom Policies** > **B2C_1A_SIGNIN**.
*   Click **Run now** to test the policy.
*   Ensure that the authentication process works successfully without errors.

### 5. Verify Endpoint Access

*   Ensure that Azure B2C can successfully communicate with the `/GetUserClaims` endpoint using Basic Authentication.
*   Ensure the user details are correctly included in the authentication token.

Resources: 
[Secure APIs used for API connectors in Azure AD B2C - Azure AD B2C | Microsoft Learn](https://learn.microsoft.com/en-us/azure/active-directory-b2c/secure-rest-api?tabs=windows&pivots=b2c-custom-policy)
