import hashlib

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()

base = "hello world"
variants = [base, base+"!", base[:-1], base.replace("h","H"), base + "x"]

for v in variants:
    h = sha256_hex(v)
    print(f"input: {v!r}\nhash:  {h}\n")
