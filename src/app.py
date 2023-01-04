from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)


def fetchDetails():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return str(hostname), str(local_ip)


@app.route("/")
def Hello_World():
    return "Hello, World!"


@app.route("/health")
def Health():
    return jsonify(
        status="UP"
    )


@app.route("/details")
def Detail():
    hostname, ip = fetchDetails()
    return render_template(
        "index.html", HOSTNAME=hostname, IP=ip
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
