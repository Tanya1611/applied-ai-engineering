'''
The experiment is a conceptual simulation demonstrating why reusing previously computed information can reduce repeated work. 
It does not reproduce the actual memory layout or attention computation of a production Transformer.
'''

import time


def without_cache(tokens):
    total_time = 0

    for current_position in range(1, tokens + 1):
        work = current_position

        start = time.perf_counter()

        for _ in range(work * 10000):
            pass

        total_time += time.perf_counter() - start

    return total_time


def with_cache(tokens):
    total_time = 0

    for _ in range(tokens):
        # Simulate approximately constant incremental work
        start = time.perf_counter()

        for _ in range(10000):
            pass

        total_time += time.perf_counter() - start

    return total_time


for tokens in [10, 20, 50, 100]:

    no_cache = without_cache(tokens)
    cache = with_cache(tokens)

    print(f"\nTokens: {tokens}")
    print(f"Without cache: {no_cache:.4f}s")
    print(f"With cache:    {cache:.4f}s")


'''
========OUTPUT==========
Tokens: 10
Without cache: 0.0083s
With cache:    0.0015s

Tokens: 20
Without cache: 0.0360s
With cache:    0.0031s

Tokens: 50
Without cache: 0.2396s
With cache:    0.0084s

Tokens: 100
Without cache: 0.7613s
With cache:    0.0154s
=========================
'''