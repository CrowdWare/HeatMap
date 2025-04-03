
from flask import Flask, request, send_from_directory
from heatmap import add_spot

app = Flask(__name__)

@app.route("/wake", methods=["POST"])
def wake():
    data = request.get_json()
    lat = data.get("lat")
    lon = data.get("lon")
    if lat is not None and lon is not None:
        add_spot(lat, lon)
        return {"status": "ok"}, 200
    return {"error": "invalid data"}, 400

@app.route("/map.png")
def serve_map():
    return send_from_directory("static", "map.png")
