import psutil
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    if psutil.cpu_percent() > 80 or psutil.virtual_memory().percent > 80:
        Message = "High CPU and memory utilization. Please scale up."
    elif psutil.cpu_percent() > 80:
        Message = "High CPU utilization. Please scale up."
    elif psutil.virtual_memory().percent > 80:
        Message = "High memory utilization. Please scale up."
    return render_template("index.html", cpu_metric=psutil.cpu_percent(), mem_metric=psutil.virtual_memory().percent, message=Message)


@app.route("/data")
def get_data():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    data = {"cpu_percent": cpu_percent, "mem_percent": mem_percent}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
