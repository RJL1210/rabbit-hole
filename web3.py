from ecdsa import SigningKey, SECP256k1, VerifyingKey
import hashlib

sk = SigningKey.generate(curve=SECP256k1)
vk = sk.get_verifying_key()
msg = b"send 0.03 ETH to Bob"
sig = sk.sign(msg)
print("signature:", sig.hex())
print("verify:", vk.verify(sig, msg))  # True
