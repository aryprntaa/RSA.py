# RSA IMPLEMENTATION

# fungsi gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# mencari inverse modular
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d


# Key Generation
p = 11
q = 17

n = p * q
phi = (p-1)*(q-1)

e = 7
d = mod_inverse(e, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))


# Enkripsi
def encrypt(m, e, n):
    return (m ** e) % n


# Dekripsi
def decrypt(c, d, n):
    return (c ** d) % n


plaintext = 88

cipher = encrypt(plaintext, e, n)
print("Ciphertext:", cipher)

decrypted = decrypt(cipher, d, n)
print("Hasil Dekripsi:", decrypted)
