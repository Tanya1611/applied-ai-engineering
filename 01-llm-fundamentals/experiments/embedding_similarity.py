from dotenv import load_dotenv
from openai import OpenAI
import numpy as np
import math

load_dotenv()

client = OpenAI()

def get_embeddings(inputText, model="text-embedding-3-small"):

    # Generates an embedding vector for the given text using OpenAI.
    response = client.embeddings.create(
        input = inputText,
        model = model)

    return response.data[0].embedding

# Cosine Similarity Search in Pure Python
def cosine_similarity_python(vec1, vec2):

    dot_prod = sum(a*b for a,b in zip(vec1, vec2))
    mag_vec1 = math.sqrt(sum(x**2 for x in vec1))
    mag_vec2 = math.sqrt(sum(y**2 for y in vec2))

    if mag_vec1 == 0 or mag_vec2 == 0:
        return 0.0
    return dot_prod/(mag_vec1*mag_vec2)


# Cosine Similarity Search in NumPy
def cosine_similarity_numpy(vec1, vec2):

    dot_prod = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)

    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0
    return dot_prod/(norm_vec1*norm_vec2)

# Texts to compare from Query Text
queryText = "I want to apply for a home loan."
text1 = "I need a mortgage."
text2 = "I want to order a pizza."

statement1 = "COVID-19 vaccines are highly effective"
statement2 = "COVID-19 vaccines are completely ineffective"


# Generate Embeddings
query_embedding = get_embeddings(queryText)
embedding1 = get_embeddings(text1)
embedding2 = get_embeddings(text2)

embedding_statement_1 = get_embeddings(statement1)
embedding_statement_2 = get_embeddings(statement2)

# Benchmark cosine similarity in python 
result1 = cosine_similarity_python(query_embedding, embedding1)
result2 = cosine_similarity_python(query_embedding, embedding2)

resultOfStatements = cosine_similarity_python(embedding_statement_1, embedding_statement_2)

print("="*120)
print("Using Pure Python")
print(f"Cosine Similarity search of \"{queryText}\" with \"{text1}\" is {result1:.4f}")
print(f"Cosine Similarity search of \"{queryText}\" with \"{text2}\" is {result2:.4f}")

print(f"Cosine Similarity search of \"{statement1}\" with \"{statement2}\" is {resultOfStatements:.4f}")

# Benchmark cosine similarity in NumPy
outcome1 = cosine_similarity_numpy(query_embedding, embedding1)
outcome2 = cosine_similarity_numpy(query_embedding, embedding2)

outcomeOfStatements = cosine_similarity_numpy(embedding_statement_1, embedding_statement_2)

print("="*120)
print("Using NumPy")
print(f"Cosine Similarity search of \"{queryText}\" with \"{text1}\" is {outcome1:.4f}")
print(f"Cosine Similarity search of \"{queryText}\" with \"{text2}\" is {outcome2:.4f}")

print(f"Cosine Similarity search of \"{statement1}\" with \"{statement2}\" is {outcomeOfStatements:.4f}")
print("="*120)


'''
-------------------------------------------------INSIGHT-----------------------------------------------------------------

Embedding models map text into a vector space where similarity metrics can be used to identify semantically related content.
> This is what makes embeddings useful for retrieval.
> But similarity alone does not guarantee that a retrieved document is actually sufficient to answer the user's question.

--------------------------------------------------OUTPUT-----------------------------------------------------------------
========================================================================================================================
Using Pure Python
Cosine Similarity search of "I want to apply for a home loan." with "I need a mortgage." is 0.6946
Cosine Similarity search of "I want to apply for a home loan." with "I want to order a pizza." is 0.2795
Cosine Similarity search of "COVID-19 vaccines are highly effective" with "COVID-19 vaccines are completely ineffective" is 0.7282
========================================================================================================================
Using NumPy
Cosine Similarity search of "I want to apply for a home loan." with "I need a mortgage." is 0.6946
Cosine Similarity search of "I want to apply for a home loan." with "I want to order a pizza." is 0.2795
Cosine Similarity search of "COVID-19 vaccines are highly effective" with "COVID-19 vaccines are completely ineffective" is 0.7282
========================================================================================================================
'''