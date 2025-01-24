#Storage Accounts Structure

##Storage account

DEV - stspectiadev
UAT - stspectiauat
PROD - TBD ( each wholesaler has its own storage account)


##Container name

{wholesaler}-import

E.g:
- `ao-import`
- `bd-import`
##Container structure in Storage Accounts
```
{wholesaler}-import (container)
|-Pricelists (price receive trigger folder)
|-Pricelists-imported (this gets generated if there is actual imported file)
|-Pricelists-processed (this gets generated if there is actual processed file)
|-Invoices (invoice receive trigger folder)
|-Invoices-imported (this gets generated if there is actual imported file)
```


Example for AO:
```
ao-import
|-Pricelists
  |- ao-price-file.csv
|-Pricelists-imported
  |- ao-price-file.csv (after import)
|-Pricelists-processed
  |- ao-price-file.csv (after processed not imported yet)
|-Invoices
  |- ao-invoice-file.csv
|-Invoices-imported
  |- ao-invoice-file.csv (after import)
```

##Initial file repo:
[Digital Thinking & Merkle - Integration - All Documents](https://globalappsportal.sharepoint.com/sites/DigitalThinkingMerkle/Shared%20Documents/Forms/AllItems.aspx?e=5%3A4fe5da311ab04ad7ae93923f776c5c23&sharingv2=true&fromShare=true&at=9&CID=a18cd732%2D39a4%2D62df%2D5251%2D2c808adb17fd&FolderCTID=0x012000ACF3171DDD63AE4DB12F72070CC4E3F6&OR=Teams%2DHL&CT=1731498925306&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNDEwMjAwMTMxNiIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D&id=%2Fsites%2FDigitalThinkingMerkle%2FShared%20Documents%2FGeneral%2FDocuments%20shared%20with%20IG%2FIntegration&viewid=a3028032%2Dc4ef%2D4dd9%2Da70f%2Ddfc59b62828f)