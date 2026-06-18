
from pathlib import Path
ye = Path('flag.txt')
out = Path('flag.enc')
m = 55
kd = [91, 92, 85, 86, 85, 82, 91, 26, 69, 84, 3, 26, 5, 7, 5, 1]
def _get_key():
    return bytes((x ^ m for x in kd))

print(_get_key())