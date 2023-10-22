from flask import Flask, request, jsonify, send_file, url_for
from services.openai.chatgpt import get_openai_response
from Modules.pptx_generator import create_presentation
# from Modules.elevenlabs import generate_audio
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

@app.route('/generate_presentation')
def generate_presentation_route():
    json_value = request.json
    template_index = int(request.args.get('tindex'))
    print(template_index)
    create_presentation(json_value, template_index)
    # save_pptx_as_png("images", "NewModified_Presentation.pptx", True)
    return "Presentation Generated and Converted to PNG!"

# @app.route('/get_images', methods=['GET'])
# def get_images():
#     image_folder = 'images'
#     image_files = [f for f in os.listdir(image_folder) if f.endswith('.JPG')]
#     image_urls = [url_for('serve_image', filename=f) for f in image_files]
#     return jsonify({'image_urls': image_urls})

if __name__ == '__main__':
	app.run(debug=True)