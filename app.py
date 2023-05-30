from flask import Flask, request, jsonify, send_from_directory
import random
import logging
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger UI configuration
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Random Array API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/swagger.json", methods=["GET"])
def swagger_json():
    return send_from_directory("static", "swagger.json")


@app.route("/random_array", methods=["POST"])
def random_array():
    """
    Generate a random 500-dimensional array of floats
    ---
    parameters:
      - name: sentence
        in: formData
        type: string
        required: true
        description: Input sentence
    responses:
      200:
        description: Random 500-dimensional array of floats
        schema:
          type: array
          items:
            type: number
      400:
        description: Bad Request
    """
    sentence = request.form.get("sentence")
    if sentence.isdigit() or sentence.replace(".", "").isdigit():
        logger.error("Invalid sentence type. Expected string.")
        return jsonify({"error": "Invalid sentence type. Expected string."}), 400

    words = sentence.split()
    if len(words) < 2:
        logger.error("Invalid sentence. Please provide a sentence with multiple words.")
        return (
            jsonify(
                {
                    "error": "Invalid sentence. Please provide a sentence with multiple words."
                }
            ),
            400,
        )

    if not sentence:
        logger.error("No sentence provided.")
        return jsonify({"error": "No sentence provided."}), 400

    if not isinstance(sentence, str):
        logger.error("Invalid sentence type. Expected string.")
        return jsonify({"error": "Invalid sentence type. Expected string."}), 400

    try:
        # Process the sentence and generate a random array of floats
        random_array = generate_random_array()
        logger.info("Random array generated successfully.")
        return jsonify({"result": random_array}), 200

    except Exception as e:
        logger.exception("An error occurred during array generation.")
        return jsonify({"error": str(e)}), 500


def generate_random_array():
    random_array = [random.random() for _ in range(500)]
    return random_array


if __name__ == "__main__":
    app.run()
