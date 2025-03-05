import math

#1. fungsi luas persegi panjang
def LPersegiPanjang (p, l):
    return p + l

#2. fungsi keliling persegi panjang
def KPersegiPanjang (p, l):
    return 2 * (p + l)

#3. fungsi luas bujursangkar
def LBujursangkar(s):
    return s * s
    # return s**2

#4. fungsi Keliling bujursangkar
def KBujursangkar(s):
    return 4 * s

#5. fungsi luas lingkaran
def lingkaran(r):
    return math.pi * r**2
    # return math.pi * r * r

#6. Fungsi keliling lingkaran
def KLingkaran(r):
    return 2 * math.pi * r

#7. fungsi luas segitiga
def lsegitiga(a, t):
    return (a * t) / 2

#8. fungsi keliling segitiga
def Ksegitiga(a, b, c):
    return a + b + c