bi1 = "10101"
bi2 = "11100"

int1 = int(bi1, 2)
int2 = int(bi2, 2)

print(int1)

combined_int = int1 | int2
print(combined_int)

combined_bi_str = bin(combined_int)[2:]

print(int(combined_bi_str))
