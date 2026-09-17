# LLM Inference

## What

Inference is the process of using a trained model to produce an output for new input.

## Simplified flow

Prompt
→ tokens
→ model computation
→ next-token probabilities
→ selected token
→ repeat
→ final response

## Important observation

Autoregressive generation produces output incrementally.

## Applied AI relevance

This has implications for:
- latency
- token usage
- streaming
- context size
- inference cost

## Next investigation

Prefill
Decode
KV Cache
TTFT