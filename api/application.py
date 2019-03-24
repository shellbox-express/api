from os import environ
from flask import Flask, request, jsonify
from .wrapper import Wrapper

app = Flask(__name__)


@app.route("/")
def home():
    print(app.config['client_id'])
    return "Shell Box Express"


@app.route("/voice", methods=["POST"])
def voice():
    print(request.get_json())
    return "olar :D"


@app.route("/loc")
def loc():
    wrapper = Wrapper(app.config['client_id'], app.config['client_secret'],
                      "https://api-hackaraizen.sensedia.com/sandbox/gestao-lojas/v1")

    r = wrapper.call("/lojas-localizacoes/lojas-localizacoes?_offset=0&_limit=10")
    r.raise_for_status()
    return jsonify(r.json())

if __name__ == "__main__":
    app.config["client_id"] = environ.get("CLIENT_ID")
    app.config["client_secret"] = environ.get("CLIENT_SECRET")
    app.run(debug=True)
