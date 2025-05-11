from struct import pack
import re
import subprocess


def xor_decrypt(cipher_bytes, key, shift=0):
    key_bytes = [ord(key[(i + shift) % len(key)]) for i in range(len(key))]
    return "".join(
        chr(b ^ key_bytes[i % len(key_bytes)]) for i, b in enumerate(cipher_bytes)
    )


binary_path = "./chall"

# Disassemble the binary using objdump
objdump_output = subprocess.check_output(
    ["objdump", "-d", "--no-show-raw-insn", binary_path]
).decode()

# Extract movabs $0x... values from the binary
pattern = re.compile(r"movabs\s+\$0x([0-9a-f]+)", re.IGNORECASE)
hex_values = pattern.findall(objdump_output)

# Convert extracted hex values to little-endian bytes
cipher_bytes = b"".join(pack("<Q", int(chunk, 16)) for chunk in hex_values)

# Key used for XOR decryption
key = "GDG_HACK"

# Decrypt everything except the last 10 bytes with default key
first_part = xor_decrypt(cipher_bytes[:-16], key)

# Decrypt the last 10 bytes with key shifted by 3
suffix_part = xor_decrypt(cipher_bytes[-16:], key, shift=3)

# Combine the both part and remove redondant caracters
flag = first_part + suffix_part[5:-1]
print(flag)
