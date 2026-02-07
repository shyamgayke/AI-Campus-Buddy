from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    assignment_text = data.get('text', '')
    if not assignment_text:
        return jsonify({'error': 'No text provided'}), 400

    # Mock feedback for demonstration
    feedback_json = {
        "overall_evaluation": "This is a mock evaluation for demonstration purposes.",
        "strengths": "Mock strengths: Well-structured content.",
        "areas_for_improvement": "Mock improvement: Add more details.",
        "language_clarity": "Mock clarity: Clear and concise.",
        "score_out_of_10": 7
    }
    return jsonify(feedback_json)

if __name__ == '__main__':
    app.run(debug=True)
