from flask import Flask, request
from services.openai.chatgpt import get_openai_response
from Modules.pptx_generator import create_presentation
from Modules.elevenlabs import generate_audio
from Utilities.slide_to_image import save_pptx_as_png

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, Flask!'


@app.route('/gpt')
def getResponse():
    topic = request.args.get('topic')
    total_slides = int(request.args.get('total_slides'))
    return get_openai_response(topic, total_slides)




if __name__ == '__main__':
	app.run(debug=True)