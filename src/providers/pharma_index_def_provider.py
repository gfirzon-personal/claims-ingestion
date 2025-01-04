from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchField,
    SearchFieldDataType,
    SearchableField,
    VectorSearch,
    VectorSearchProfile,
    HnswAlgorithmConfiguration,
    VectorSearchAlgorithmConfiguration
)

def get_fields_definitions(vector_search_profile_name:str, algorithm_configuration_name:str):
    """
    Returns the fields and vector search definitions for the Pharma index
    """
    #vector_search_dimensions = 1536
    vector_search_dimensions = 384
    
    fields = [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="PrescriptionRefNo", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="PatientFirstName", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="PatientLastName", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="PatientDOB", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="PrescriberID", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="ProductServiceID", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="QuantityDispensed", type=SearchFieldDataType.Double, filterable=True),
        SearchableField(name="DateRxWritten", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="DateOfService", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="DaysSupply", type=SearchFieldDataType.Double, filterable=True),
        SearchableField(name="FillNo", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="BINNumber", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="ProcessorControlNo", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="GroupNo", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="TransactionCode", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="OtherCoverageCode", type=SearchFieldDataType.String, filterable=True),
        SearchableField(name="PatientPayAmount", type=SearchFieldDataType.Double, filterable=True),
        SearchableField(name="TotalAmountPaid", type=SearchFieldDataType.Double, filterable=True),
        #SearchableField(name="content", type=SearchFieldDataType.String, filterable=True),  # Make 'content' both searchable and filterable
        SearchField(name="content_vector", 
                    type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                    searchable=True, 
                    vector_search_dimensions=vector_search_dimensions, 
                    vector_search_profile_name=vector_search_profile_name)
    ]

    vector_search = VectorSearch(
        profiles=[
            VectorSearchProfile(name=vector_search_profile_name,
            algorithm_configuration_name=algorithm_configuration_name)
        ],
        algorithms=[HnswAlgorithmConfiguration(name=algorithm_configuration_name)],
    )

    return fields, vector_search    
