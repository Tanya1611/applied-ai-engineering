# Deeper into LLM inference

## The story here is:
To understand what actually happens after a request is sent — and why an LLM can feel slow even when the model itself is working correctly.

## Main investigation in LLM Inference is:

Request → Prefill → TTFT → Decode → Tokens/sec → KV Cache → Total latency


## Problem

Prompt: "Explain how a mortgage works." to an LLM.
Process:
Request sent
       ↓
...waiting...
       ↓
First token appears
       ↓
More tokens stream
       ↓
Response complete

- But what happened during the waiting period?
- Also, If the model has already processed the prompt, why does generating 500 output tokens still take time?

## The Mental Model 

               LLM REQUEST
                    │
                    ▼
             Input tokenization
                    │
                    ▼
                 PREFILL
                    │
          Process input tokens
                    │
                    ▼
            First token generated
                    │
                    ▼
                  TTFT
                    │
                    ▼
                 DECODE
                    │
        ┌───────────┴───────────┐
        │                       │
   Generate token         Update KV cache
        │                       │
        └───────────┬───────────┘
                    │
                    ▼
                Next token
                    │
                   ...
                    │
                    ▼
             Final response

## The key distinction:

Prefill processes the prompt. Decode generates the response.

'User says:
"LLM is slow."

Don't immediately:
→ change model

Instead:

1. Measure TTFT
2. Measure generation latency
3. Check prompt/context length
4. Check output length
5. Check queueing/concurrency
6. Check model/serving configuration
7. Check network overhead
8. Identify bottleneck
9. Change one variable
10. Measure again