from pydantic import BaseModel
from typing import Optional, Any, Dict

class PharmaRecord(BaseModel):
    PrescriptionRefNo: str
    PatientFirstName: str
    PatientLastName: str
    PatientDOB: str
    PrescriberID: str
    ProductServiceID: str
    QuantityDispensed: str
    DateRxWritten: str
    DateOfService: str
    DaysSupply: str
    FillNumber: Optional[str] = None  # Make FillNumber nullable
    BINNumber: str
    ProcessorControlNo: str
    GroupNo: str
    TransactionCode: str
    OtherCoverageCode: str
    PatientPayAmount: str
    TotalAmountPaid: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PharmaRecord":
        return cls(**data)    