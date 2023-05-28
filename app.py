import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, url_for, request, send_file, json
from flask_cors import CORS
from database import Dataset


app = Flask(__name__)
CORS(app)

@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/dataset", methods=["POST"])
def create_dataset():
    try:
        content = request.get_json()
        dataset_id = Dataset.create_dataset(content=content)
        response = {"datasetId": dataset_id}
        response = app.response_class(
            response = json.dumps(response),
            status = 200,
            mimetype = 'application/json'
        )
        return response
    except Exception as e:
        logging.error(f"Error while creating dataset {e}")
        response = {"message": "Failed to create dataset"}
        response = app.response_class(
            response = json.dumps(response),
            status = 400,
            mimetype = 'application/json'
        )
        return response


@app.route("/api/dataset/<dataset_id>/heatmap")
def send_heatmap(dataset_id):
    try:
        dataset = Dataset.get_dataset_by_id(dataset_id)
        path = f"/tmp/{dataset['name']}/heatmap.jpeg"
        return send_file(path_or_file = path, mimetype = 'image/jpeg')
    except Exception as e:
        logging.error(f"Error while sending heatmap {e}")
        response = {"message": "Failed to send heatmap"}
        response = app.response_class(
            response = json.dumps(response),
            status = 400,
            mimetype = 'application/json'
        )
        return response



if __name__ == "__main__":
    version = "0.1"
    logging.basicConfig(
        handlers=[
            RotatingFileHandler("logs/backend.log", maxBytes=5000000, backupCount=10, mode="a")
        ],
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    app.run()
