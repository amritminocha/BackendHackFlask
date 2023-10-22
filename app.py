from flask import Flask, request, jsonify, send_file, url_for
from services.openai.chatgpt import get_openai_response
from Modules.pptx_generator import create_presentation
from Modules.elevenlabs import generate_audio
# from Utilities.slide_to_image import save_pptx_as_png
import os

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, Flask!'


@app.route('/gpt')
def getResponse():
    topic = request.args.get('topic')
    total_slides = int(request.args.get('total_slides'))
    return get_openai_response(topic, total_slides)

@app.route('/get_images', methods=['GET'])
def get_images():
    image_folder = 'images'
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.JPG')]
    image_urls = [url_for('serve_image', filename=f) for f in image_files]
    return jsonify({'image_urls': image_urls})

# @app.route('/get_images-list', methods=['GET'])
# def get_images():
#     filename = 'images/Slide1.JPG'
#     return send_file(filename, mimetype="application/json")

@app.route('/images/<filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory('images', filename)


if __name__ == '__main__':
	app.run(debug=True)