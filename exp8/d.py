import random

def diffie_hellman():
# Public parameters (agreed publicly)
p = 23 # Small prime for demo (use 2048-bit in real)
g = 5 # Primitive root (generator)
# Alice chooses private key a
a = random.randint(2, p - 2) # Private
A = pow(g, a, p) # Public value A = g^a mod p
# Bob chooses private key b
b = random.randint(2, p - 2) # Private
B = pow(g, b, p) # Public value B = g^b mod p
# Exchange public values A and B (sent over network)
# Alice computes shared secret
secret_A = pow(B, a, p) # B^a mod p
# Bob computes shared secret
secret_B = pow(A, b, p) # A^b mod p
print("Diffie-Hellman Key Exchange")
print(f" Public prime (p) : {p}")
print(f" Generator (g) : {g}")
print(f" Alice private (a): {a} Public A: {A}")
print(f" Bob private (b): {b} Public B: {B}")
print(f" Alice shared key : {secret_A}")
print(f" Bob shared key : {secret_B}")
print(f" Keys Match : {secret_A == secret_B}")
diffie_hellman()
