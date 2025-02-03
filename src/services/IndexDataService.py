from factories.SearchClientFactory import SearchClientFactory

class IndexDataService:
    """Service to manage data for the search index"""
    def __init__(self, index_name: str):
        self.search_client = SearchClientFactory().create(index_name)
        

    def delete_all_docs(self):
        """Delete all documents from the index"""
        key_field_name = "id"

        # Retrieve all document IDs
        delete_batch = []
        for doc in self.search_client.search(search_text="*", select=[key_field_name]):  
            if key_field_name in doc:  # Ensure key field exists in response
                delete_batch.append({
                    "@search.action": "delete",
                    key_field_name: doc[key_field_name]
                })

        count = 0

        # Execute batch delete if documents exist
        if delete_batch:
            response = self.search_client.upload_documents(documents=delete_batch)
            count = len(response)
            print(f"Deleted {count} documents")
            # print("Deleted documents:", response)
        else:
            print("No documents found in index.") 

        return count    