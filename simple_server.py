import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/magic', methods=['GET'])
def api_id():
    result = [{"result": 5}]
    return jsonify(result)
app.run(port=5000, host='0.0.0.0')

