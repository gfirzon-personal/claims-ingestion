Request to search for record in existing Azure AI Search service index

Url: http://localhost:8000/searching/record-text-search
Method: POST

```json
{
    "index_name": "pharma-index",
    "record": {
        "PrescriptionRefNo":"SD771836363",
        "PatientFirstName":"Peter",
        "PatientLastName":"Smith",
        "PatientDOB":"1941-04-30",
        "PrescriberID":"UH676564270505386",
        "ProductServiceID":"TN545733840388035",
        "QuantityDispensed":"9",
        "DateRxWritten":"2021-02-16 15:44:34",
        "DateOfService":"2023-07-23 17:28:29",
        "DaysSupply":"30",
        "FillNo":"PJ",
        "BINNumber":"GD5617",
        "ProcessorControlNo":"DD611082822",
        "GroupNo":"JR472145718976433",
        "TransactionCode":"VG",
        "OtherCoverageCode":"XG",
        "PatientPayAmount":"85.66",
        "TotalAmountPaid":"6.56"
    }
}
```