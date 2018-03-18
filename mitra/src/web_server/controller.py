from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/testing", methods=["GET", "POST"])
def home():
	return jsonify({"msg": "success"})


@app.route("/getTagsForImage", methods=["POST", "GET"])
def get_tags_for_image():
	request_data = request.files
	print(request_data)
	return jsonify({"msg": "success"})


if __name__ == "__main__":
	app.run(debug=True)
