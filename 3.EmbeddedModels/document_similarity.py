from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)
documents=[
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership",
    "Sachin Tendulkar is a legendary Indian cricketer often referred to as the 'God of Cricket'",
    "M.S. Dhoni is a former Indian cricketer and captain, known for his calm demeanor and finishing abilities",
    "Rohit Sharma is an Indian cricketer known for his elegant batting style and ability to score big centuries",
    "Jasprit Bumrah is an Indian cricketer known for his unique bowling action and ability to bowl yorkers consistently"
    ]

query="Tell me about virat kohli"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)


similarity_scores = cosine_similarity([query_embedding], doc_embeddings)[0]
most_similar_doc_index = np.argmax(similarity_scores)
most_similar_doc = documents[most_similar_doc_index]

print("Query:", query)
print("Similarity scores:", similarity_scores)
print("Most similar document:", most_similar_doc)
