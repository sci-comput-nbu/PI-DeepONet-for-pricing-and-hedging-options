"""Verify the per-file SHA-256 manifest in an extracted data/code release."""
from pathlib import Path
import hashlib,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
count=0
for line in (root/'MANIFEST.sha256').read_text(encoding='utf-8').splitlines():
    digest,name=line.split('  ',1)
    path=(root/name).resolve()
    assert path.is_relative_to(root),name
    assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,name
    count+=1
print(f'All {count} manifest entries match.')
