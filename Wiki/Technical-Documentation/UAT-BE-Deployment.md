#AO
- `add note that this might be applicable to another wholesaler as well`
## Account Service
- Ensure that IG company, account and bonus is generated in environment
```sql
script here
```

## Price Service
### Upload of prices
1. File repository
- Copy the price file for AO in this Sharepoint link: [Prices](https://globalappsportal.sharepoint.com/:f:/r/sites/DigitalThinkingMerkle/Shared%20Documents/General/Documents%20shared%20with%20IG/Integration/AO/Prices?csf=1&web=1&e=sHLLrw)
2. Upload Price file
- Upload the price file on the environment's storage account. [Storage Structure](https://dev.azure.com/merkleprojects/Installat%C3%B8rgruppen/_wiki/wikis/Installat%C3%B8rgruppen.wiki/98/Azure-Storage-Accounts)
3. Get pending price imports
- After uploading and the processing is done, this will create a PriceImport entry on the price service. Check postman and execute the `GET GetPendingPriceImports` to confirm.
4. Set price import to ready
-  Get the PriceImport Id from the previous step and use it as a payload for setting the price import to ready. 
- You also need to set the `validFrom` to a previous date, this will make the prices to be valid.
- Execute the request from postman `POST SetPriceImportToImportReady`. This request might take time since it's importing the price file to the price db.

## Invoice Service
### Upload of invoices
1. File repository
- Copy the invoice files for AO in this Sharepoint link: [Invoices](https://globalappsportal.sharepoint.com/:f:/r/sites/DigitalThinkingMerkle/Shared%20Documents/General/Documents%20shared%20with%20IG/Integration/AO/Invoices?csf=1&web=1&e=Ks68Ab)
2. Upload Invoice files
- Special case for AO, edit the invoice files and remove the first 2 rows (temporary fix)
- Upload the price file on the environment's storage account. [Storage Structure](https://dev.azure.com/merkleprojects/Installat%C3%B8rgruppen/_wiki/wikis/Installat%C3%B8rgruppen.wiki/98/Azure-Storage-Accounts)
3. After uploading, the import function will trigger and save the invoices to DB.
4. Verify invoice and invoice lines in DB, initial status should be 0 (Pending).
5. Invoice control which is a timed trigger will run through the pending invoice lines.
