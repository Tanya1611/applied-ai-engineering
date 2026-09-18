import time

def simulate_generation(num_tokens: int, delay_per_token: float = 0.05):
    start_time = time.perf_counter()

    for _ in range(num_tokens):
        time.sleep(delay_per_token)

    end_time = time.perf_counter()

    total_latency = end_time - start_time
    tokens_per_second = num_tokens / total_latency

    return total_latency, tokens_per_second


for num_tokens in [10, 50, 100, 200]:
    latency, tokens_per_second = simulate_generation(num_tokens)

    print(
        f"Output tokens: {num_tokens:3d} | "
        f"Latency: {latency:.2f}s | "
        f"Tokens/sec: {tokens_per_second:.2f}"
    )

'''
=======================================OUTPUT====================================================

Output tokens:  10 | Latency: 0.51s | Tokens/sec: 19.76
Output tokens:  50 | Latency: 2.54s | Tokens/sec: 19.68
Output tokens: 100 | Latency: 5.07s | Tokens/sec: 19.73
Output tokens: 200 | Latency: 10.16s | Tokens/sec: 19.68

======================================INSIGHT====================================================

Output length contributes directly to generation time in autoregressive decoding.

Therefore:
Longer output
      ↓
More decoding steps
      ↓
Higher latency

=================================================================================================
'''
