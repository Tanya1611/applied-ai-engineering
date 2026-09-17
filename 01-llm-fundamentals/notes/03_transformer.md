# Transformer

## Problem

Language understanding requires relationships between tokens across a sequence.

## What?

The Transformer is an architecture built around attention and feed-forward components, repeated across layers.

## High-level flow

Tokens
→ representations
→ Transformer blocks
→ output representation
→ next-token prediction

## Important components

- Self-attention -> Self-attention allows each token representation to incorporate information from other tokens in the same sequence. 
- Feed-forward network -> After attention, each token representation is further transformed through a feed-forward network.
- Residual connections -> Residual connections allow information from an earlier representation to be carried forward.
- Normalization -> Normalization helps keep activations in a manageable range during network computation.

## Applied AI relevance

Understanding the architecture helps explain:
- context
- inference
- token generation
- latency
- model limitations
