"""import all from flask"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """request code and print in the page"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    correct_message = f"For the given statement, the system response is {response}"
    if response['dominant_emotion'] is None:
        return 'invalid text! Please try again!'
    return correct_message

@app.route("/")
def render_index_page():
    """render the index"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
