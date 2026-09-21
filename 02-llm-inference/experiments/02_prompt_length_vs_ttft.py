''' 
Calculate Time taken in Prompt Processing -> Time to First Token
'''

import time

def simulate_prefill(prompt_tokens: int):
    start_time = time.perf_counter()

    # Simulate more computation for longer prompts
    time.sleep(prompt_tokens * 0.0005)

    end_time = time.perf_counter()

    return end_time - start_time


prompt_sizes = [100, 500, 1000, 2000, 5000]

for tokens in prompt_sizes:
    ttft = simulate_prefill(tokens)

    print(
        f"Prompt tokens: {tokens:5d} | "
        f"Simulated TTFT: {ttft:.3f}s"
    )

'''
-------------------------------------------------------OUTPUT-------------------------------------------------------------

Prompt tokens:   100 | Simulated TTFT: 0.051s
Prompt tokens:   500 | Simulated TTFT: 0.251s
Prompt tokens:  1000 | Simulated TTFT: 0.501s
Prompt tokens:  2000 | Simulated TTFT: 1.000s
Prompt tokens:  5000 | Simulated TTFT: 2.500s

-------------------------------------------------------INSIGHT------------------------------------------------------------

This experiment is a simplified simulation used to understand how prompt processing can contribute to time-to-first-token. 
Actual latency depends on model architecture, hardware, serving system, batching and implementation

--------------------------------------------------------------------------------------------------------------------------
'''