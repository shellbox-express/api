from os import environ
from flask import Flask, request, jsonify
from .watson import Watson
from .wrapper import Wrapper

app = Flask(__name__)
app.config["client_id"] = environ.get("CLIENT_ID")
app.config["client_secret"] = environ.get("CLIENT_SECRET")
app.config["watson_key"] = environ.get("WATSON_KEY")
app.config["workspace_id"] = environ.get("WORKSPACE_ID")

@app.route("/")
def home():
    print(app.config['client_id'])
    return "Shell Box Express"


@app.route("/voice", methods=["POST"])
def voice():
    # First of all, the request needs to contain a valid JSON body
    if not request.is_json:
        # If it doesn't, it is an 400-Bad Request error
        return "Please provide a valid JSON object!", 400

    data = request.get_json()

    if not "text" in data:
        return "Please provide a text field!", 400

    text = data["text"]
    context = data.get("context")

    w = Watson(app.config["watson_key"], app.config["workspace_id"])
    r = w.messsage(text, context)

    return jsonify(r)


@app.route("/loc")
def loc():
    wrapper = Wrapper(app.config['client_id'], app.config['client_secret'],
                      "https://api-hackaraizen.sensedia.com/sandbox/gestao-lojas/v1")

    r = wrapper.call("/lojas-localizacoes/lojas-localizacoes?_offset=0&_limit=10")
    r.raise_for_status()
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(debug=True)
