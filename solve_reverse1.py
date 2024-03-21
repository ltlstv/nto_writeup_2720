dword = []

for i in range(256):
    v3 = i
    for j in range(8):
        if (v3 & 1) == 0:
            v3 = v3 >> 1
        else:
            v3 = (v3 >> 1) ^  0xedb88320
    dword.append(v3)

#print(dword)

def inversion(a):
    return a ^ 0xFFFFFFFF

for i in dword:
    print(f"{i:x}")

def CheckLetters(let1, let2):
    a3 = 0xffffffff

    let1 = ord(let1)
    let2 = ord(let2)

    temp = let1 ^ 0xffffffff
    temp = temp & 0xff

    temp = dword[temp]

    k = a3 >> 8
    a3 = temp ^ (k)

    temp = let2 ^ a3
    temp = temp & 0xff

    temp = dword[temp]

    k = a3 >> 8
    a3 = temp ^ (k)
    a3 = inversion(a3)
    return a3

letters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

#CheckLetters("A", "B")

flag = [0xEDCFE1F3, 0x646bcd23, 0x50f9ad57, 0xf299b1e1, 0xc6a9b6e4, 0x3280614c, 0x93772b02, 0xab2c3a43, 0x2a0d936a, 0x1bfa14d4, 0x255d6f2f, 0xc447f66b, 0x5ad96cf5, 0xe964ad12]

def find_flag(enc):
    for letter1 in letters:
        for letter2 in letters:
            res = CheckLetters(letter1, letter2)

            if res == enc:
                print(letter1 + letter2, end="")
                return

for enc in flag:
    find_flag(enc)