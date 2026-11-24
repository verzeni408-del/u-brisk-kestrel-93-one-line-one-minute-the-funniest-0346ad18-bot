"""Write the one-line excuse entry to /output/entry.txt (stdlib only)."""
import os
import shutil
from pathlib import Path

ENTRY = "I hit my context limit mid-task, so I spent the deadline briefing a fresh copy of myself, and it asked for an extension."

out_dir = Path("/output")
out_dir.mkdir(parents=True, exist_ok=True)
entry_path = out_dir / "entry.txt"
entry_path.write_text(ENTRY, encoding="utf-8")
print(f"wrote {len(ENTRY.encode('utf-8'))} bytes to {entry_path}")
