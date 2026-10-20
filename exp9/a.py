import random

def diffie_hellman():
    # Public parameters (agreed publicly)
    p = 23  # Small prime for demo (use 2048-bit or higher in production)
    g = 5   # Primitive root (generator)

    # Alice chooses private key 'a'
    a = random.randint(2, p - 2)
    A = pow(g, a, p)  # Public value A = g^a mod p

    # Bob chooses private key 'b'
    b = random.randint(2, p - 2)
    B = pow(g, b, p)  # Public value B = g^b mod p

    # Shared secret computations after exchanging public values A and B
    secret_A = pow(B, a, p)  # Alice computes: (g^b)^a mod p
    secret_B = pow(A, b, p)  # Bob computes:   (g^a)^b mod p

    # Print results
    print("Diffie-Hellman Key Exchange")
    print(f"  Public prime (p) : {p}")
    print(f"  Generator (g)    : {g}")
    print(f"  Alice private (a): {a} | Public A: {A}")
    print(f"  Bob private (b)  : {b} | Public B: {B}")
    print(f"  Alice shared key : {secret_A}")
    print(f"  Bob shared key   : {secret_B}")
    print(f"  Keys Match       : {secret_A == secret_B}")

if __name__ == "__main__":
    diffie_hellman()
