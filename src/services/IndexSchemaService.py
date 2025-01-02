from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex
)

from factories.SearchIndexClientFactory import SearchIndexClientFactory
from providers.test_search_provider import get_test_search_params
from providers.pharma_search_provider import get_pharma_search_params

#--------------------------------------------------------------------------------
class IndexSchemaService:
    def __init__(self):
        self.client:SearchIndexClient = SearchIndexClientFactory.create_search_index_client()

    #--------------------------------------------------------------------------------
    def create_index_with_vector_field(self, 
            index_name:str, 
            index_type:str, 
            vector_search_profile_name:str, 
            algorithm_configuration_name:str):
        
        if index_type == "pharma":
            fields, vector_search = get_pharma_search_params(vector_search_profile_name, algorithm_configuration_name)
        else:      
            fields, vector_search = get_test_search_params(vector_search_profile_name, algorithm_configuration_name)

        index = SearchIndex(name=index_name, fields=fields, vector_search=vector_search)
        self.client.create_index(index)  

    #--------------------------------------------------------------------------------
    def delete_index(self, index_name: str):
        self.client.delete_index(index_name)       

    #--------------------------------------------------------------------------------
    def list_indexes(self):
        return list(self.client.list_indexes())
