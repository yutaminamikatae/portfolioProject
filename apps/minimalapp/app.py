from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "flask test12"

# jsonify({
#         "flask test"
#     })