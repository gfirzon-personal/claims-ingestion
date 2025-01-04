Request to search for record in existing Azure AI Search service index

Url: http://localhost:8000/searching/record-text-search
Method: POST

```json
{
    "index_name": "pharma-index",
    "record": {
        "PrescriptionRefNo": "I86K4NBSAHHF",
        "PatientFirstName": "",
        "PatientLastName": "Bailey",
        "PatientDOB": "",
        "PrescriberID": "",
        "ProductServiceID": "FA3WOSXLSNSFH7GPOU7",
        "QuantityDispensed": "",
        "DateRxWritten": "2020-10-10 04:44:07",
        "DateOfService": "2021-04-25 23:01:14",
        "DaysSupply": "349.4",
        "FillNumber": null,
        "BINNumber": "2YNC25",
        "ProcessorControlNo": "HN941NSCSU",
        "GroupNo": "",
        "TransactionCode": "VP",
        "OtherCoverageCode": "NC",
        "PatientPayAmount": "",
        "TotalAmountPaid": "355.13"
    }
}
```