import random


def pkcs1_v15_pad(message, key_length):
    # Calculate the maximum message length
    max_length = key_length // 8 - 11

    # Check if the message length exceeds the maximum length
    if len(message) > max_length:
        raise ValueError("Message too long for the given key length")

    # Calculate the padding length
    padding_length = max_length - len(message)

    # Generate random non-zero padding bytes
    padding = bytes([random.randint(1, 255) for _ in range(padding_length)])

    # Build the padded message
    padded_message = b"\x00\x02" + padding + b"\x00" + message

    return padded_message


def pkcs1_v15_unpad(padded_message):
    # Check if the padded message starts with the correct bytes
    if padded_message[:2] != b"\x00\x02":
        raise ValueError("Invalid PKCS#1 v1.5 padding")

    # Find the end of padding by searching for the first zero byte after the second byte
    padding_end = padded_message.find(b"\x00", 2)

    # Ensure that a zero byte exists
    if padding_end == -1:
        raise ValueError("Invalid PKCS#1 v1.5 padding")

    # Extract the message after the padding
    message = padded_message[padding_end + 1 :]

    return message


# Example usage
message = b"Hello, world!"
key_length = 1024

# Padding
padded_message = pkcs1_v15_pad(message, key_length)
print("Padded message:", padded_message.hex())

# Unpadding
unpadded_message = pkcs1_v15_unpad(padded_message)
print("Unpadded message:", unpadded_message.decode("utf-8"))
