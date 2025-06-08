from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "flask test1"

# jsonify({
#         "flask test"
#     })