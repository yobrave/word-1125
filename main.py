# Invent a Word: coin + one-line definition, gate/export (edition 4).
import json
import os
import pathlib

WORD_LIMIT = 140
BADGE = "wod4-invent-word-r4"

data = pathlib.Path("entry.txt").read_text(encoding="utf-8").strip()
size = len(data)
result = {"badge": BADGE, "size": size}

if 1 <= size <= WORD_LIMIT:
    dest = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out")) / "entry.txt"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes((data + "\n").encode("utf-8"))
    result["verdict"] = "shipped"
    result["limit"] = WORD_LIMIT
    result["coined"] = True
else:
    result["verdict"] = "rejected"

print(json.dumps(result))
