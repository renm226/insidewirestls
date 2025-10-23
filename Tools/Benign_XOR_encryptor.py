from pathlib import Path
def repeating_xor(data: bytes, key: bytes) -> bytes:
    if not key:
        raise ValueError("Key must be non-empty")
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def encrypt_file(in_path: str, out_path: str, key: str):
    p = Path(in_path)
    if not p.exists():
        raise FileNotFoundError(in_path)
    data = p.read_bytes()
    out = repeating_xor(data, key.encode('utf-8'))
    Path(out_path).write_bytes(out)
    print(f"Encrypted {in_path} -> {out_path} (key length={len(key)})")

if __name__ == "__main__":
    encrypt_file("lab/payload.txt", "payload.enc", "labkey")
