from flask import Flask, request, jsonify
from ipaddress import ip_address
from db.db import query_db, init_db

app = Flask(__name__)

app.config.from_object('conf.flask_conf.ProductionConfig')
init_db(app)

@app.get("/")
def index():
    return "", 200

@app.get("/list-ip")
def list_ip():
    limit = request.args.get('limit', 5, int)
    offset = request.args.get('offset', 0, int)
    result = query_db(f"SELECT ip, message FROM malicious_ip LIMIT {limit} OFFSET {offset}")
    return jsonify(
        [{"ip": ip, "message": message} for ip, message in result]
    )

@app.get("/check-ip")
def check_ip():
    ip = request.args.get('ip', None, ip_address)
    if ip is not None:
        result = query_db(f"SELECT ip, message FROM malicious_ip WHERE ip = '{ip}'")
        return jsonify(
            [{"ip": ip, "message": message} for ip, message in result]
        )
    else:
        return "invalid IP, now your IP seems suspicious", 400

@app.route("/report-ip")
def report_ip():
    return "maybe next time?", 200
    
