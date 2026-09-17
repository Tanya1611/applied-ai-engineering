# Tokenization

## Problem

An LLM cannot directly process raw human text.

## What is Tokenization?

Tokenization converts text into model-readable tokens.

## Why it matters?

- Context window
- Cost
- Latency
- RAG context
- Prompt size

## Experiment!

Compared tokenization across:
- natural language
- technical text
- code
- identifiers

## Observation!

Token boundaries don't necessarily correspond to human words.

## Engineering implication

When designing prompts or RAG systems, token count needs to be treated as an engineering constraint.
