Tips for Sentence Transformers
Choosing a Model:
all-MiniLM-L6-v2: Faster, smaller embeddings (384 dimensions).
multi-qa-mpnet-base-dot-v1: More accurate, larger embeddings (768 dimensions).
Batch Processing:
Use model.encode(list_of_texts, batch_size=32) to process multiple texts efficiently.