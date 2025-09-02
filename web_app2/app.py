from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route("/api/")
def hello_world():
    data = None
    with open(file="data.json", mode="r") as file:
        data = json.load(file)
    return data



if __name__ == '__main__':
    app.run(debug=True, port=8080)