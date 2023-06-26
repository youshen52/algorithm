import hashlib
import random


def mgf1(seed, mask_len, hash_algorithm):
    # Generate a mask using MGF1 (Mask Generation Function 1)
    mask = b""
    hash_size = get_hash_size(hash_algorithm)
    counter = 0

    while len(mask) < mask_len:
        counter_bytes = counter.to_bytes(4, byteorder="big")
        hash_output = hash_algorithm(seed + counter_bytes).digest()
        mask += hash_output
        counter += 1

    return mask[:mask_len]


def get_hash_size(hash_algorithm):
    # Get the size of the hash output in bytes
    if hash_algorithm == "sha1":
        return 20
    elif hash_algorithm == "sha256":
        return 32
    elif hash_algorithm == "sha512":
        return 64
    else:
        raise ValueError("Unsupported hash algorithm")


def pkcs1_pss_pad(message, key_length, hash_algorithm, salt_length):
    # Calculate the maximum message length
    em_len = (key_length // 8) - 1
    h_len = get_hash_size(hash_algorithm)
    s_len = salt_length

    if len(message) > em_len - h_len - s_len - 2:
        raise ValueError("Message too long for the given key length")

    # Generate salt
    salt = bytes([random.randint(0, 255) for _ in range(s_len)])

    # Calculate the hash of the message
    m_hash = hashlib.new(hash_algorithm, message).digest()

    # Construct the maskedDB
    masked_db = bytes([0x00] * (em_len - h_len - 1 - s_len - 1)) + bytes([0x01]) + salt

    # Calculate H = Hash(m_hash || ps || 0x01 || salt)
    h_input = m_hash + masked_db
    h = hashlib.new(hash_algorithm, h_input).digest()

    # Construct the DB
    db = masked_db + h

    # Generate the mask
    mask = mgf1(h, em_len - h_len - 1, hash_algorithm)

    # Apply the mask to the DB
    masked_db = bytes([db[i] ^ mask[i] for i in range(len(db))])

    # Set the most significant bit of the leftmost byte to zero
    masked_db = bytes([masked_db[0] & 0x7F]) + masked_db[1:]

    # Construct the padded message
    padded_message = b"\x00" + masked_db

    return padded_message


def pkcs1_pss_unpad(padded_message, key_length, hash_algorithm, salt_length):
    # Get the size of the hash output
    h_len = get_hash_size(hash_algorithm)

    # Check if the padded message has the correct format
    if len(padded_message) != (key_length // 8) or padded_message[0] != 0x00:
        raise ValueError("Invalid PKCS#1 PSS padding")

    # Get the masked DB
    masked_db = padded_message[1:]

    # Recover the DB by applying the mask
    mask = mgf1(masked_db[:h_len], len(masked_db) - h_len, hash_algorithm)
    db = bytes([masked_db[i] ^ mask[i] for i in range(len(masked_db))])

    # Check the most significant bit of the leftmost byte
    if db[0] & 0x80 != 0:
        raise ValueError("Invalid PKCS#1 PSS padding")

    # Find the salt and message hash in the recovered DB
    salt = db[-salt_length:]
    m_hash = db[-salt_length - h_len : -salt_length]

    # Verify the hash value
    h_input = m_hash + masked_db[:-h_len]
    h_verify = hashlib.new(hash_algorithm, h_input).digest()

    if h_verify != m_hash:
        raise ValueError("Invalid PKCS#1 PSS padding - Hash verification failed")

    return salt, m_hash
