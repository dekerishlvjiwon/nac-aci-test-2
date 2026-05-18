from pathlib import Path

files = list(Path(".").rglob("*.yml")) + list(Path(".").rglob("*.yaml"))

changed_files = 0
changed_lines = 0

for f in files:
    if ".terraform" in f.parts:
        continue

    try:
        lines = f.read_text(encoding="utf-8").splitlines(keepends=True)
    except UnicodeDecodeError:
        continue

    new_lines = []
    count = 0

    for line in lines:
        # Preserve Windows or Unix line endings
        newline = ""
        body = line

        if line.endswith("\r\n"):
            newline = "\r\n"
            body = line[:-2]
        elif line.endswith("\n"):
            newline = "\n"
            body = line[:-1]

        # Only change lines that are exactly: description:
        # with optional spaces/tabs around it
        if body.strip() == "description:":
            indent = body[:len(body) - len(body.lstrip(" \t"))]
            new_lines.append(f'{indent}description: ""{newline}')
            count += 1
        else:
            new_lines.append(line)

    if count:
        f.write_text("".join(new_lines), encoding="utf-8")
        changed_files += 1
        changed_lines += count
        print(f"Updated {count}: {f}")

print()
print(f"Updated {changed_lines} blank description(s) across {changed_files} file(s).")