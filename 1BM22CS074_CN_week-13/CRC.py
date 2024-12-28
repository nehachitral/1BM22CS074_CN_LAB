def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


def encode(data, key):
    key_len = len(key)
    appended_data = data + '0' * (key_len - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    print(f"Encoded Data: {codeword}")
    return codeword


def decode(data, key):
    remainder = mod2div(data, key)
    print(f"Remainder after decoding: {remainder}")
    if '1' not in remainder:
        print("No error detected in received data")
    else:
        print("Error detected in received data")


# Main function
if __name__ == "__main__":
    data = input("Enter the data bits: ")
    key = input("Enter the key (divisor): ")

    # Encoding
    encoded_data = encode(data, key)

    # Decoding
    print("\nDecoding the encoded data...")
    decode(encoded_data, key)
