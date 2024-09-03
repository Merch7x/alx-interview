#!/usr/bin/python3
"""Utf-8 validation python"""


def validUTF8(data):
    """Determines if a given dataset represents a valid UTF-8 encoding"""
    num_bytes = 0

    # Masks to check the first few bits of a byte
    mask1 = 1 << 7    # 10000000
    mask2 = 1 << 6    # 01000000

    for byte in data:
        # Check only the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1's to determine the byte length
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # If num_bytes is 0, it's a single-byte character
            if num_bytes == 0:
                continue

            # If num_bytes is more than 4 or 1, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if it starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes to be processed
        num_bytes -= 1

    # If all bytes are processed correctly, num_bytes should be 0
    return num_bytes == 0
