import time

from flask import Flask

app = Flask(__name__)

start_time = time.time()

@app.route("/")
def hello():
    return "Hello Docker"

@app.route("/health")
def health():
    uptime = start_time - time.time()
    status = "healthy" if uptime > 0 else "unhealthy"
    return {"status": status, "uptime_seconds": uptime}

if __name__ == "__main__":
    app.run(host="0.0.0.0")
