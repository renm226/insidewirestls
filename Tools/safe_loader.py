
#lets try decrypt encrypted payload using the same XOR method
# this is to complement Tools/Benign_XOR_encryptor.py``
from pathlib import Path

def repeating_xor(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def load_embedded_payload(enc_path: str, out_path: str, key: str):
    enc = Path(enc_path).read_bytes()
    keyb = key.encode('utf-8')
    dec = repeating_xor(enc, keyb)
    Path(out_path).write_bytes(dec)
    print(f"Decrypted embedded payload -> {out_path}")

if __name__ == "__main__":
    load_embedded_payload("payload.enc", "payload_decrypted.txt", "labkey")
