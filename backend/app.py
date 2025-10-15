from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from .config import HOST, PORT, DEBUG
from .led_controller import led
from .patterns_store import list_all, create, delete

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return render_template("index.html")

@app.get("/api/health")
def health():
    return jsonify(ok=True)

@app.get("/api/state")
def get_state():
    return jsonify(led.get_state())

@app.post("/api/state")
def set_state():
    """
    Payload JSON:
    {
      "brightness": 0..100,       # optionnel
      "colors": ["#RRGGBB", ...]  # optionnel (>=1 couleur)
    }
    """
    data = request.get_json(force=True) or {}
    state = led.apply(colors=data.get("colors"), brightness=data.get("brightness"))
    return jsonify(state), 202

@app.get("/api/patterns")
def patterns_list():
    return jsonify(list_all())

@app.post("/api/patterns")
def patterns_add():
    """
    Payload JSON:
    { "name":"Warm", "brightness":65, "colors":["#FFD7A3","#FFE9C2","#FFF6E5"] }
    """
    p = request.get_json(force=True) or {}
    item = {
        "name": p.get("name", "Preset"),
        "brightness": int(p.get("brightness", 50)),
        "colors": [c if c.startswith("#") else f"#{c}" for c in (p.get("colors") or ["#FFFFFF"])]
    }
    return jsonify(create(item)), 201

@app.delete("/api/patterns/<pid>")
def patterns_del(pid):
    return jsonify(delete(pid)), 200

if __name__ == "__main__":
    # rpi_ws281x exige souvent root (GPIO18 PWM).
    app.run(HOST, PORT, debug=DEBUG)
