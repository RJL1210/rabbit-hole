import hashlib
import time

def mine(prefix_zeros=4):
    prefix = "0" * prefix_zeros
    nonce = 0
    start = time.time()
    while True:
        text = f"block-data|nonce={nonce}"
        h = hashlib.sha256(text.encode()).hexdigest()
        if h.startswith(prefix):
            return nonce, h, time.time() - start
        nonce += 1

for zeros in (2,3,4):
    nonce, h, elapsed = mine(zeros)
    print(f"zeros={zeros} -> nonce={nonce}, hash={h}, time={elapsed:.3f}s")
