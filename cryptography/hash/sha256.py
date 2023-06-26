# Helper functions
def right_rotate(x, n):
    return (x >> n) | (x << (32 - n))


def sha256(message):
    # Initialize hash values
    h0 = 0x6A09E667
    h1 = 0xBB67AE85
    h2 = 0x3C6EF372
    h3 = 0xA54FF53A
    h4 = 0x510E527F
    h5 = 0x9B05688C
    h6 = 0x1F83D9AB
    h7 = 0x5BE0CD19

    # Initialize round constants
    k = [
        0x428A2F98,
        0x71374491,
        0xB5C0FBCF,
        0xE9B5DBA5,
        0x3956C25B,
        0x59F111F1,
        0x923F82A4,
        0xAB1C5ED5,
        0xD807AA98,
        0x12835B01,
        0x243185BE,
        0x550C7DC3,
        0x72BE5D74,
        0x80DEB1FE,
        0x9BDC06A7,
        0xC19BF174,
        0xE49B69C1,
        0xEFBE4786,
        0x0FC19DC6,
        0x240CA1CC,
        0x2DE92C6F,
        0x4A7484AA,
        0x5CB0A9DC,
        0x76F988DA,
        0x983E5152,
        0xA831C66D,
        0xB00327C8,
        0xBF597FC7,
        0xC6E00BF3,
        0xD5A79147,
        0x06CA6351,
        0x14292967,
        0x27B70A85,
        0x2E1B2138,
        0x4D2C6DFC,
        0x53380D13,
        0x650A7354,
        0x766A0ABB,
        0x81C2C92E,
        0x92722C85,
        0xA2BFE8A1,
        0xA81A664B,
        0xC24B8B70,
        0xC76C51A3,
        0xD192E819,
        0xD6990624,
        0xF40E3585,
        0x106AA070,
        0x19A4C116,
        0x1E376C08,
        0x2748774C,
        0x34B0BCB5,
        0x391C0CB3,
        0x4ED8AA4A,
        0x5B9CCA4F,
        0x682E6FF3,
        0x748F82EE,
        0x78A5636F,
        0x84C87814,
        0x8CC70208,
        0x90BEFFFA,
        0xA4506CEB,
        0xBEF9A3F7,
        0xC67178F2,
    ]

    # Pre-processing
    original_message_length = len(message)
    message += b"\x80"  # Add padding (bit '1' appended after message)

    while len(message) % 64 != 56:
        message += b"\x00"  # Pad until message length % 64 == 56

    message_bit_length = original_message_length * 8
    message += message_bit_length.to_bytes(
        8, byteorder="big"
    )  # Append original message length (in bits)

    # Process the message in successive 512-bit chunks
    for chunk_start in range(0, len(message), 64):
        chunk = message[chunk_start : chunk_start + 64]

        # Initialize working variables
        w = [0] * 64
        for i in range(16):
            w[i] = int.from_bytes(chunk[i * 4 : i * 4 + 4], byteorder="big")

        # Extend the first 16 words into the remaining 48 words
        for i in range(16, 64):
            s0 = (
                right_rotate(w[i - 15], 7)
                ^ right_rotate(w[i - 15], 18)
                ^ (w[i - 15] >> 3)
            )
            s1 = (
                right_rotate(w[i - 2], 17)
                ^ right_rotate(w[i - 2], 19)
                ^ (w[i - 2] >> 10)
            )
            w[i] = (w[i - 16] + s0 + w[i - 7] + s1) & 0xFFFFFFFF

        # Initialize working variables to the current hash value
        a, b, c, d, e, f, g, h = h0, h1, h2, h3, h4, h5, h6, h7

        # Compression function
        for i in range(64):
            s1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
            ch = (e & f) ^ (~e & g)
            temp1 = (h + s1 + ch + k[i] + w[i]) & 0xFFFFFFFF
            s0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (s0 + maj) & 0xFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        # Add the compressed chunk to the current hash value
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        h5 = (h5 + f) & 0xFFFFFFFF
        h6 = (h6 + g) & 0xFFFFFFFF
        h7 = (h7 + h) & 0xFFFFFFFF

    # Produce the final hash value (big-endian)
    hash_value = (
        h0.to_bytes(4, byteorder="big")
        + h1.to_bytes(4, byteorder="big")
        + h2.to_bytes(4, byteorder="big")
        + h3.to_bytes(4, byteorder="big")
        + h4.to_bytes(4, byteorder="big")
        + h5.to_bytes(4, byteorder="big")
        + h6.to_bytes(4, byteorder="big")
        + h7.to_bytes(4, byteorder="big")
    )

    hex_value = "".join(format(byte, "02x") for byte in hash_value)

    return hex_value


if __name__ == "__main__":
    message = b"Hello, world!"
    hash_value = sha256(message)
    print(hash_value)
