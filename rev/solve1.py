from pathlib import Path

ye = Path('flag.enc')  
out = Path('flag.dec') 
m = 55
kd = [91, 92, 85, 86, 85, 82, 91, 26, 69, 84, 3, 26, 5, 7, 5, 1]

def _get_key():
    return bytes((x ^ m for x in kd))

def wud(data, key):
    
    s = list(range(256))
    j = 0
    for i in range(256):
        j = j + s[i] + key[i % len(key)] & 255
        s[i], s[j] = (s[j], s[i])
        
    out = bytearray()
    i = 0
    j = 0
    
    for byte in data:
        i = i + 1 & 255
        j = j + s[i] & 255
        s[i], s[j] = (s[j], s[i])
        k = s[s[i] + s[j] & 255]
        out.append(byte ^ k)
    return bytes(out)

def main():
    if not ye.exists():
        print('no flag.enc found!')
    else:
        encrypted_data = ye.read_bytes()
        decrypted = wud(encrypted_data, _get_key())
        out.write_bytes(decrypted)
        print(f'Decryption successful. Saved to {out.name}')

if __name__ == '__main__':
    main()
