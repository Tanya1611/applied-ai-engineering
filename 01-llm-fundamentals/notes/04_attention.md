# Self-Attention

## Problem

The meaning of a token often depends on other tokens.

Consider:
"The customer cancelled the order because it was delayed."

- To interpret it, the model needs information from the surrounding sequence.
- A simple independent word-by-word representation would not be enough.

# What is Self-Attention?

Self-attention allows each token to determine how much information it should incorporate from other tokens in the same sequence.

Conceptually:

Input Tokens
     ↓
  Q, K, V
     ↓
Attention Scores
     ↓
Attention Weights
     ↓
Weighted Values
     ↓
Updated Token Representations

# Query, Key and Value

Self-attention creates three representations for each token:

Query (Q): Represents what the current token is looking for.
Key (K): Represents what each token can be matched against.
Value (V): Contains the information that can be passed forward if that token receives attention.

# Attention Score
A query is compared with keys to determine how strongly the tokens should interact.

# Self-Attention vs Similarity Search

Self-Attention -> Used inside the Transformer.
Token representations
        ↓
    Q / K / V
        ↓
Contextual representations

It determines how token information interacts during model computation.

Vector Similarity Search -> Used in systems such as RAG.
Query embedding
       ↓
Vector database
       ↓
Similar document vectors

- It determines which stored items are candidates for retrieval.
- They both involve comparing vectors, but they solve different problems.

# Multi-Head Attention

Instead of using a single attention operation, Transformers can use multiple attention heads.
- Different heads can learn different types of relationships.

# Why Understand Attention?

- Context Dependence: The same token can receive different contextual representations depending on surrounding text.
- Long Prompts: More tokens create more relationships for the model to process.
- Prompt Design: The structure and placement of information can influence model behavior.
- RAG: Retrieved information becomes part of the model's context.

# Engineering Insight

Self-attention computes learned interactions between token representations and produces contextualized representations by weighting information from different positions.
