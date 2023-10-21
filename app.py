from flask import Flask
from services.openai.chatgpt import get_openai_response
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, Flask!'


@app.route('/gpt')
def getResponse():
    return get_openai_response()


if __name__ == '__main__':
	app.run(debug=True)