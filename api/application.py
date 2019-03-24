from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Shell Box Express"

@app.route("/voice", methods=["POST"])
def voice():
    print(request.get_json())
    return "olar :D"

if __name__ == "__main__":
    app.run(debug=True)