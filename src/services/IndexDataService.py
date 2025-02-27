import uuid
from factories.SearchClientFactory import SearchClientFactory

class IndexDataService:
    """Service to manage data for the search index"""
    def __init__(self, index_name: str):
        self.search_client = SearchClientFactory().create(index_name)
           
    #--------------------------------------------------------------------------------
    def get_all_docs(self):
        """Retrieve all documents from the index"""
        all_docs = []
        results = self.search_client.search(search_text="*")
        for doc in results:
            all_docs.append(doc)
        return all_docs   
    
    def get_doc_by_id(self, doc_id: str):
        """Retrieve a document from the index by ID"""
        results = self.search_client.search(search_text="*", filter=f"id eq '{doc_id}'")
        for doc in results:
            return doc
        print(f"No document found with id '{doc_id}'")
        return None 
        
    #--------------------------------------------------------------------------------
    def add_document(self, request: dict):
        """Add a document to the index"""
        request["id"] = str(uuid.uuid4())  # Add GUID as string to the document
        response = self.search_client.upload_documents(documents=[request])
        count = len(response)
        print(f"Added {count} document(s)")
        return request["id"]    

    #--------------------------------------------------------------------------------
    def update_document(self, request: dict):
        """Update a document in the index"""
        key_field_name = "id"
        #request[key_field_name] = key_field_name
        response = self.search_client.upload_documents(documents=[request])
        count = len(response)
        print(f"Updated {count} document(s) with id '{request[key_field_name]}'")
        return count       
    
    #--------------------------------------------------------------------------------
    def delete_doc_by_id(self, doc_id: str):
        """Delete a document from the index by ID"""
        key_field_name = "id"
        results = self.search_client.search(search_text="*", filter=f"id eq '{doc_id}'")
        
        delete_batch = []
        for doc in results:
            if key_field_name in doc:
                delete_batch.append({
                    "@search.action": "delete",
                    key_field_name: doc[key_field_name]
                })
        
        if delete_batch:
            response = self.search_client.upload_documents(documents=delete_batch)
            count = len(response)
            print(f"Deleted {count} document(s) with id '{doc_id}'")
            return count
        else:
            print(f"No document found with id '{doc_id}'")
            return 0       
        
    #--------------------------------------------------------------------------------
    def delete_all_docs(self):
        """Delete all documents from the index"""
        key_field_name = "id"
        batch_size = 1000  # Adjust the batch size as needed

        count = 0

        while True:
            # Retrieve a batch of document IDs
            delete_batch = []
            for doc in self.search_client.search(search_text="*", select=[key_field_name], top=batch_size):
                if key_field_name in doc:  # Ensure key field exists in response
                    delete_batch.append({
                        "@search.action": "delete",
                        key_field_name: doc[key_field_name]
                    })

            # Execute batch delete if documents exist
            if delete_batch:
                response = self.search_client.upload_documents(documents=delete_batch)
                count += len(response)
                print(f"Deleted {len(response)} documents in this batch")
            else:
                print("No more documents found in index.")
                break

        print(f"Deleted a total of {count} documents")
        return count      