from azure.search.documents.indexes import SearchIndexClient
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

from factories.SearchIndexClientFactory import SearchIndexClientFactory

#--------------------------------------------------------------------------------
class IndexSchemaService:
    def __init__(self):
        self.client:SearchIndexClient = SearchIndexClientFactory.create_search_index_client()

    #--------------------------------------------------------------------------------
    def create_index_with_vector_field(self, index_name:str, vector_search_profile_name:str, algorithm_configuration_name:str):
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

        index = SearchIndex(name=index_name, fields=fields, vector_search=vector_search)
        self.client.create_index(index)  

    #--------------------------------------------------------------------------------
    def delete_index(self, index_name: str):
        self.client.delete_index(index_name)       

    #--------------------------------------------------------------------------------
    def list_indexes(self):
        return list(self.client.list_indexes())
