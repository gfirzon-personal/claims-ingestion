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

def get_test_search_params(vector_search_profile_name:str, algorithm_configuration_name:str):
    #vector_search_dimensions = 1536
    vector_search_dimensions = 384
    
    fields = [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        #SearchableField(name="content", type=SearchFieldDataType.String),
        SearchableField(name="content", type=SearchFieldDataType.String, filterable=True),  # Make 'content' both searchable and filterable
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
