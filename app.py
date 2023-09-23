from flask import Flask, request, jsonify, render_template
from predict import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def your_model_function(input_text, length=1000):
    output_text = predict_generate(input_text, length)
    return output_text

@app.route('/process', methods=['POST'])
def process_text():
    data = request.json
    input_text = data.get('text', '')
    desired_length = data.get('length', 1000)  # Default to 1000 if not provided
    
    # Process the text with the model
    output_text = your_model_function(input_text, desired_length)
    
    return jsonify({'output_text': output_text})


if __name__ == '__main__':
    app.run(debug=True, port=8000)