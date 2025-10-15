import json, os, uuid

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "data", "patterns.json")
DATA_PATH = os.path.abspath(DATA_PATH)

def _read():
    if not os.path.exists(DATA_PATH): return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        try: return json.load(f)
        except: return []

def _write(items):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

def list_all(): return _read()

def create(item):
    items = _read()
    item["id"] = str(uuid.uuid4())
    items.append(item); _write(items)
    return item

def delete(pid):
    items = _read()
    items = [i for i in items if i.get("id") != pid]
    _write(items)
    return {"deleted": pid}
