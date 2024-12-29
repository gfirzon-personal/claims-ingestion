from sentence_transformers import SentenceTransformer

class EmbeddingsService:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def get_embeddings(self, sentences):
        return self.model.encode(sentences)

    # def get_similarity(self, sentence1, sentence2):
    #     embeddings = self.get_embeddings([sentence1, sentence2])
    #     return 1 - spatial.distance.cosine(embeddings[0], embeddings[1])

    # def get_similarity_batch(self, sentence1, sentences):
    #     embeddings = self.get_embeddings([sentence1] + sentences)
    #     return [1 - spatial.distance.cosine(embeddings[0], embedding) for embedding in embeddings[1:]]

    # def get_similarity_matrix(self, sentences):
    #     embeddings = self.get_embeddings(sentences)
    #     return cosine_similarity(embeddings)

    # def get_similarity_matrix_batch(self, sentences1, sentences2):
    #     embeddings1 = self.get_embeddings(sentences1)
    #     embeddings2 = self.get_embeddings(sentences2)
    #     return cosine_similarity(embeddings1, embeddings2)

    # def get_similarity_matrix_batch(self, sentences1, sentences2):
    #     embeddings1 = self.get_embeddings(sentences1)
    #     embeddings2 = self.get_embeddings(sentences2)
    #     return cosine_similarity(embeddings1, embeddings2)

    # def get_similarity_matrix_batch(self, sentences1, sentences2):
    #     embeddings1 = self.get_embeddings(sentences1)
    #     embeddings2 = self.get_embeddings(sentences2)
    #     return cosine_similarity(embeddings1, embeddings2)

    # def get_similarity_matrix_batch(self, sentences1, sentences2):
    #     embeddings1 = self.get_embeddings(sentences1)
    #     embeddings2 = self.get_embeddings(sentences2)
    #     return cosine_similarity(embeddings1, embeddings2)

    # def get_similarity_matrix_batch(self, sentences1, sentences2):
    #     embeddings1 = self.get_embeddings(sentences1)
    #     embeddings2 = self.get_embeddings(sentences2)
    #     return cosine_similarity(embeddings1, embeddings2)

    # def get_similarity_matrix_batch(self, sentences1, sentences2):
    #     embeddings1 = self.get_embeddings(sentences1)
    #     embeddings2 = self.get_embeddings(sentences2)
    #     return cosine_similarity(embeddings1, embeddings2)

    # def get_similarity_matrix_batch(self, sentences1, sentences2):
    #     embeddings1 = self.get_embeddings(sentences1)
    #     embeddings2 = self.get_embeddings(sentences2)
    #     return cosine_similarity(embeddings1, embeddings2)

    # def get_similarity_matrix_batch(self, sentences1, sentences2):