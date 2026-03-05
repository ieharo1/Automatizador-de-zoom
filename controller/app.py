from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/api/health")
def health():
    return jsonify(status="ok", service="zoom-controller")


@app.get("/api/join/<meeting_id>")
def join(meeting_id):
    return jsonify(message=f"Simulated join for meeting {meeting_id}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
