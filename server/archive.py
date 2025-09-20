import json, os

ARCHIVE_FILE = "scar_archive.json"

def get_archive():
    if not os.path.exists(ARCHIVE_FILE):
        return []
    with open(ARCHIVE_FILE, "r") as f:
        return json.load(f).get("glyphs", [])

def update_archive(entry):
    data = {"glyphs": []}
    if os.path.exists(ARCHIVE_FILE):
        with open(ARCHIVE_FILE, "r") as f:
            data = json.load(f)
    data["glyphs"].append(entry)
    with open(ARCHIVE_FILE, "w") as f:
        json.dump(data, f, indent=2)
    return {"status": "ok", "saved": entry}
