from os import environ
from flask import Flask, request, jsonify
import redis
from .agent import Agent
from .models import Purchase
from .watson import Watson
from .wrapper import Wrapper

app = Flask(__name__)
app.config["client_id"] = environ.get("CLIENT_ID")
app.config["client_secret"] = environ.get("CLIENT_SECRET")
app.config["watson_key"] = environ.get("WATSON_KEY")
app.config["workspace_id"] = environ.get("WORKSPACE_ID")


@app.route("/")
def home():
    print(app.config["client_id"])
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

    try:
        w = Watson(app.config["watson_key"], app.config["workspace_id"])
        r = w.messsage(text, context)
        assert r
    except:
        return "Watson error!", 500

    output_text = r["output"]["generic"][0]["text"]
    agent = Agent(app.config["client_id"], app.config["client_secret"])
    processed_output = agent.proccess_watson(output_text)

    if processed_output:
        output_text = processed_output

    
    response = {"output": output_text, "context": r["context"]}

    if "foi confirmada" in output_text:
        response["lat"] = -22.715079
        response["lng"] = -47.647826

    return jsonify(response)


@app.route("/purchases")
def purchases():
    data = Purchase.select()
    data = [
        {"date": i.date, "price": i.price, "station": i.station, "qtd": i.qtd, "product": i.product}
        for i in data
    ]
    
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
