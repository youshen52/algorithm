import struct


def md5(message):
    # Initialize variables
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476

    # Constants
    s = [
        0xD76AA478,
        0xE8C7B756,
        0x242070DB,
        0xC1BDCEEE,
        0xF57C0FAF,
        0x4787C62A,
        0xA8304613,
        0xFD469501,
        0x698098D8,
        0x8B44F7AF,
        0xFFFF5BB1,
        0x895CD7BE,
        0x6B901122,
        0xFD987193,
        0xA679438E,
        0x49B40821,
        0xF61E2562,
        0xC040B340,
        0x265E5A51,
        0xE9B6C7AA,
        0xD62F105D,
        0x02441453,
        0xD8A1E681,
        0xE7D3FBC8,
        0x21E1CDE6,
        0xC33707D6,
        0xF4D50D87,
        0x455A14ED,
        0xA9E3E905,
        0xFCEFA3F8,
        0x676F02D9,
        0x8D2A4C8A,
        0xFFFA3942,
        0x8771F681,
        0x6D9D6122,
        0xFDE5380C,
        0xA4BEEA44,
        0x4BDECFA9,
        0xF6BB4B60,
        0xBEBFBC70,
        0x289B7EC6,
        0xEAA127FA,
        0xD4EF3085,
        0x04881D05,
        0xD9D4D039,
        0xE6DB99E5,
        0x1FA27CF8,
        0xC4AC5665,
        0xF4292244,
        0x432AFF97,
        0xAB9423A7,
        0xFC93A039,
        0x655B59C3,
        0x8F0CCC92,
        0xFFEFF47D,
        0x85845DD1,
        0x6FA87E4F,
        0xFE2CE6E0,
        0xA3014314,
        0x4E0811A1,
        0xF7537E82,
        0xBD3AF235,
        0x2AD7D2BB,
        0xEB86D391,
    ]

    # Pre-processing
    padded_message = preprocess(message)

    # Process message in 16-word blocks
    for i in range(0, len(padded_message), 64):
        block = padded_message[i : i + 64]
        words = struct.unpack("<16I", block)

        a = h0
        b = h1
        c = h2
        d = h3

        # Main loop
        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * j) % 16

            temp = d
            d = c
            c = b
            b = b + left_rotate((a + f + s[j] + words[g]), 7)
            a = temp

        # Update hash values
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF

    # Produce the final hash
    digest = struct.pack("<4I", h0, h1, h2, h3)
    return digest.hex()


def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF


def preprocess(message):
    # Append the bit '1' to the message
    message += b"\x80"

    # Append zeros until message length is congruent to 56 (mod 64)
    while len(message) % 64 != 56:
        message += b"\x00"

    # Append length of the message as a 64-bit little-endian integer
    length = struct.pack("<Q", 8 * len(message))
    message += length

    return message


if __name__ == "__main__":
    message = "Hello, world!"
    hash_value = md5(message.encode("utf-8"))
    print(hash_value)
