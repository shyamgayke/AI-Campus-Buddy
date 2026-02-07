from flask import Flask, request, jsonify, render_template
from inference import get_feedback
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        data = request.get_json()
        assignment_text = data.get('text', '')
        if not assignment_text:
            return jsonify({'error': 'No text provided'}), 400

        # Real ML-based feedback
        feedback_json = get_feedback(assignment_text)
        return jsonify(feedback_json)
    except Exception as e:
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
