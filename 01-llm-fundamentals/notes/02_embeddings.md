# Embeddings

## Problem

A list of integer token IDs lacks semantic meaning or directional relationships for an LLM.

## What is Embedding?

Embeddings convert discrete token IDs into dense, multi-dimensional numerical vectors that capture meaning.

## Why it matters?

- Semantic similarity
- Conceptual clustering
- Dimensionality control
- Vector search efficiency
- Transfer learning

## Experiment!

Compared vector spaces across:
- natural language
- technical text
- code
- identifiers

## Observation!

- Synonyms returned high scores.
- Context shifts drops scores significantly, proving model contextual awareness.
- Opposites often still score relatively high because they share the same topical domain.


## Engineering implication

Embeddings are useful for retrieval, but similarity alone does not guarantee that a retrieved document is actually sufficient to answer the user's question. 
Cosine similarity is highly effective for topical matching, but thresholding requires careful tuning to separate true semantic alignment from general domain relevance.