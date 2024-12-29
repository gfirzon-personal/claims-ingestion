# create index and upload docs to azure AI Search

from azure.core.credentials import AzureKeyCredential

from azure.core.pipeline.transport import RequestsTransport

from azure.core.exceptions import ResourceNotFoundError

from azure.search.documents import SearchClient

from azure.search.documents.models import VectorizedQuery

from azure.search.documents.indexes import SearchIndexClient

from azure.search.documents.indexes.models import (

    ComplexField,

    SimpleField,

    SearchFieldDataType,

    SearchableField,

    SearchIndex,

    SemanticConfiguration,

    SemanticField,

    SemanticPrioritizedFields,

    SemanticSearch,

    SearchField,

    VectorSearch,

    VectorSearchProfile,

    HnswAlgorithmConfiguration,

    VectorSearchAlgorithmConfiguration

)

from factories.SearchIndexClientFactory import SearchIndexClientFactory

 

class SearchIndexSchemaService:

    def __init__(self):

        self.search_client: SearchIndexClient = SearchIndexClientFactory().create_search_index_client()

 

    #--------------------------------------------------------------------

    def list(self):

        # Retrieve the list of existing indexes

        indexes = self.search_client.list_indexes()

 

        detailed_index_list = []

        for index in indexes:

            # Debug print to check the attributes of the index

            #print(vars(index))

            stats = self.search_client.get_index_statistics(index.name)

            #print(stats)

 

            detailed_index_list.append({

                "id": getattr(index, 'e_tag', None).replace('"', ''),

                "name": index.name,

                "odata_eta": getattr(index, 'e_tag', None),

                "document_count": stats["document_count"],

                "storage_size": stats["storage_size"],

                "vector_index_size": stats["vector_index_size"]

            })

 

        return detailed_index_list

   

    #--------------------------------------------------------------------

    def get_index_fields(self, index_name: str):

        """Get the fields of an index by name."""

        try:

            # Attempt to get the index

            index = self.search_client.get_index(index_name)

            # Extract fields from the index schema

            fields = index.fields

 

            # Add an id property to each element of fields

            for i, field in enumerate(fields):

                setattr(field, "id", str(i + 1))  # Assign an integer from sequence starting at 1

 

            return fields

        except ResourceNotFoundError:

            # Raise ResourceNotFoundError if the index does not exist

            raise ResourceNotFoundError(f"Index '{index_name}' not found")

   

    # Print details of each index

    # for index in indexes:

    #     print(f"Index Name: {index.name}")

    #     print(f"Fields: {index.fields}")

    #     print(f"Scoring Profiles: {index.scoringProfiles}")

    #     print(f"Default Scoring Profile: {index.defaultScoringProfile}")

    #     print(f"CORS Options: {index.corsOptions}")

    #     print(f"Suggesters: {index.suggesters}")

    #     print(f"Analyzers: {index.analyzers}")

    #     print(f"Tokenizers: {index.tokenizers}")

    #     print(f"Token Filters: {index.tokenFilters}")

    #     print(f"Character Filters: {index.charFilters}")

    #     print(f"Encryption Key: {index.encryptionKey}")

    #     print("-" * 40)

 

    #--------------------------------------------------------------------

    def drop_index(self, index_name: str) -> dict:

        if not self.index_exists(index_name):

            message = f"Index '{index_name}' does not exist."

            return { "error": True, "status-message": message }

 

        self.search_client.delete_index(index_name)

       

        message = f"Index '{index_name}' dropped successfully."

        return { "error": False, "status-message": message }

 

    #--------------------------------------------------------------------

    # the index fields must be modified accordingly to your dataset

    def create_index(self, index_name: str,

                     index_business_type: str,

                     vector_search_profile_name: str,

                     algorithm_configuration_name: str,

                     semantic_config_name: str) -> dict:

        if self.index_exists(index_name):

            message = f"Index '{index_name}' already exists. If needed, please drop it before creating"

            return { "error": True, "status-message": message }

 

        if index_business_type == "transcripts":

            #return self.__create_servicing_index(index_name)

            fields = [

                SimpleField(name="id", type=SearchFieldDataType.String, key=True, sortable=True, filterable=True, facetable=True),

                SimpleField(name="source", type=SearchFieldDataType.String),

                SearchableField(name="content", type=SearchFieldDataType.String),

                SearchField(name="content_vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single),

                            searchable=True, vector_search_dimensions=1536, vector_search_profile_name=vector_search_profile_name),

            ]

        else:

            return { "error": True, "status-message": f"Detected invalid index_business_type: {index_business_type}" }

     

 

        vector_search = VectorSearch(

            profiles=[

                VectorSearchProfile(name=vector_search_profile_name,

                algorithm_configuration_name=algorithm_configuration_name)

            ],

            algorithms=[HnswAlgorithmConfiguration(name=algorithm_configuration_name)],

        )

       

        sematic_config = SemanticConfiguration(

            name=semantic_config_name,

            prioritized_fields=SemanticPrioritizedFields(

                content_fields = [SemanticField(field_name="content")]

            )

        )

 

        semantic_search = SemanticSearch(configurations=[sematic_config])

        index = SearchIndex(name=index_name, fields=fields, vector_search=vector_search, semantic_search=semantic_search)

        self.search_client.create_or_update_index(index)

 

        message = f"Index '{index_name}' created successfully."

        return { "error": False, "status-message": message }

   

    #--------------------------------------------------------------------

    def index_exists(self, index_name: str) -> bool:  

        try:

            # Attempt to get the index

            self.search_client.get_index(index_name)

            return True

        except ResourceNotFoundError:

            # If the index does not exist, a ResourceNotFoundError will be raised

            return False

        # except Exception as e:

        #     return False