# Handling Configurations in Local Development

## Overview
It’s important to securely manage configurations, particularly user secrets and the `local.settings.json` file. This guide outlines best practices for separating sensitive data from non-sensitive configurations.

## Project Samples (Account Service)
`local.settings.json`
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "dotnet-isolated"
  },
  "GraphClientSettings": {
    "TenantId": "e0ed91a8-889c-4f9f-80bc-0dea55afaf7f",
    "ClientId": "602534cb-6b9a-44aa-adf2-086bd28002a1",
    "ClientSecret": "", (stored in user secrets)
    "Scopes": [
      "https://graph.microsoft.com/.default"
    ],
    "Issuer": "procureesgshs.onmicrosoft.com"
  },
  "EmailSmtpClientSettings": {
    "Host": "sandbox.smtp.mailtrap.io",
    "Port": 2525,
    "Username": "", (stored in user secrets)
    "Password": "", (stored in user secrets)
    "UseLocal": true,
    "LocalPickupDirectory": "C:\\temp\\IG\\emails"
  },
  "EmailSettings": {
    "FromEmail": "no-reply@example.com",
    "SignInUrl": "https://example.com/sign-in"
  }
}
```
`secrets.json`
```json
{
  "ConnectionStrings:AccountContext": "set-actual-value",
  "AzureB2CSettings": {
    "BasicAuthUsername": "set-actual-value",
    "BasicAuthPassword": "set-actual-value"
  },
  "GraphClientSettings": {
    "ClientSecret":  "set-actual-value"
  },
  "EmailSmtpClientSettings": {
    "Username":  "set-actual-value",
    "Password":  "set-actual-value"
  }
} 
```


#Guide:

##Local Development

## Environment variables
###What Is It?
`local.settings.json` stores non-sensitive, environment-specific configurations for Azure Functions.

### Usage
- For Non-Sensitive Data: Store URLs, logging configurations, environment names.

### Example
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "dotnet",
    "MyAppSetting": "SomeValue"
  },
  "ConnectionStrings": {
    "MyDb": "Server=localhost;Database=mydb;"
  }
}
```

## User Secrets

### What Are User Secrets?
User Secrets allow you to store sensitive information securely outside your codebase during local development.

### Usage
- **For Sensitive Data**: Store connection strings, API keys, and credentials.

### Setup
Using Visual Studio, right-click on the project and select manage user secrets. It will open up a `secrets.json` file
1. **Initialize**: 
   ```bash
   dotnet user-secrets init
1. **Adding a setting (basic and complex) **: 
   ```bash
   dotnet user-secrets set "Key" "Value"
   dotnet user-secrets set "MySettings:ServiceUrl" "https://api.example.com
   ```

1. **Access in code (basic and complex)**: 
   ```bash
   var connectionString = Configuration["ConnectionStrings:MyDb"]
   var serviceUrl = Configuration["MySettings:ServiceUrl"]
   ```
## Best Practices
- Keep Secrets Out of local.settings.json: Use User Secrets for sensitive data.
- Environment-Specific Configs: Store non-sensitive configs in local.settings.json.
 - Merge Configurations:
```csharp
   if (hostContext.HostingEnvironment.IsDevelopment())
   {
       config
           .AddJsonFile("local.settings.json", optional: false, reloadOnChange: true)
           .AddUserSecrets<Program>();
   }
```

## On other environments:
Configuration management is currently being handled in Github secrets and variables. 
You can configure it on the Settings section of the repository.


