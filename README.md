1. Pengantar Singkat

RSA adalah algoritma kriptografi asimetris yang diperkenalkan pada tahun 1977 oleh
Ron Rivest,
Adi Shamir, dan
Leonard Adleman.

RSA menggunakan dua kunci berbeda, yaitu:

Public Key → untuk enkripsi

Private Key → untuk dekripsi

Algoritma ini banyak digunakan pada sistem keamanan seperti:

HTTPS

SSL/TLS

Digital signature

Keamanan RSA didasarkan pada kesulitan memfaktorkan bilangan prima yang sangat besar.

2. Pembangkitan Kunci (Key Generation)

Langkah-langkah:

1. Pilih dua bilangan prima

Misalnya:

p = 11
q = 17
2. Hitung nilai n
n = p × q
n = 11 × 17 = 187
3. Hitung fungsi totient

Menggunakan
Euler's Totient Function

φ(n) = (p-1)(q-1)
φ(n) = 10 × 16
φ(n) = 160
4. Pilih kunci publik e

Syarat:

1 < e < φ(n)
gcd(e, φ(n)) = 1

Misalnya:

e = 7
5. Hitung kunci privat d
d × e ≡ 1 mod φ(n)

Hasil:

d = 23
Hasil Key

Public Key

(e,n) = (7,187)

Private Key

(d,n) = (23,187)
3. Proses Enkripsi

Misalkan plaintext:

M = 88

Rumus enkripsi:

C = M^e mod n

Perhitungan:

C = 88^7 mod 187
C = 11

Ciphertext yang dikirim:

11
4. Proses Dekripsi

Rumus dekripsi:

M = C^d mod n

Perhitungan:

M = 11^23 mod 187
M = 88

Plaintext berhasil dikembalikan.

5. Kelebihan dan Kelemahan
Kelebihan

Sistem public key sehingga tidak perlu berbagi kunci rahasia terlebih dahulu.

Digunakan secara luas dalam keamanan internet.

Mendukung digital signature.

Kelemahan

Proses enkripsi lebih lambat dibanding kriptografi simetris.

Jika bilangan prima terlalu kecil maka mudah dipecahkan.

Terancam oleh komputasi kuantum di masa depan.

Contoh Program Python (From Scratch)

Ini tidak memakai library kriptografi sehingga cocok untuk tugas.

# IMPLEMENTASI RSA SEDERHANA

# fungsi mencari gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# fungsi mencari inverse modular
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d


# KEY GENERATION
p = 11
q = 17

n = p * q
phi = (p-1)*(q-1)

e = 7

d = mod_inverse(e, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))


# ENKRIPSI
def encrypt(m, e, n):
    return (m ** e) % n


# DEKRIPSI
def decrypt(c, d, n):
    return (c ** d) % n


plaintext = 88

cipher = encrypt(plaintext, e, n)
print("Ciphertext:", cipher)

decrypted = decrypt(cipher, d, n)
print("Hasil Dekripsi:", decrypted)

Output program:

Public Key: (7,187)
Private Key: (23,187)

Ciphertext: 11
Hasil Dekripsi: 88
