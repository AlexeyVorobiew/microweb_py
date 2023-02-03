from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>Hello, World!</p>"

@app.route("/message", methods = ["POST"])
def message():
    posted_data = request.get_json()
    data = posted_data['data']
    return  jsonify(str(data))


if __name__ == 'main':
    app.run(debug=True)