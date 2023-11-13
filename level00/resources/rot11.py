import string

chrs = string.ascii_lowercase
enc_pwd = "cdiiddwpgswtgt"
pwd = ""

for c in enc_pwd:
    i = (chrs.index(c) + 11) % 26
    pwd += chrs[i]
print(f"Password is: {pwd}")
