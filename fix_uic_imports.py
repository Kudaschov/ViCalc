from pathlib import Path

UI_DIR = Path(__file__).parent / "vicalc" / "ui"

for py in UI_DIR.glob("*.py"):
    lines = py.read_text(encoding="utf-8").splitlines(keepends=True)

    new_lines = []
    changed = False

    for line in lines:
        stripped = line.strip()

        if stripped == "import resource_rc":
            new_lines.append("from . import resource_rc\n")
            changed = True
        else:
            new_lines.append(line)

    if changed:
        py.write_text("".join(new_lines), encoding="utf-8")
        print(f"fixed: {py.name}")
