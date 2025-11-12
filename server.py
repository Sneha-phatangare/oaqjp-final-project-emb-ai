"""
Flask web server for Emotion Detection Application.
This app provides an endpoint to analyze emotions from user input text.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """
    Render the main homepage with the input form.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Handle GET requests for emotion detection.
    It retrieves user input, processes it, and displays the detected emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    # Handle invalid or blank text
    if response['dominant_emotion'] is None:
        return render_template(
            'index.html',
            result="Invalid text! Please try again!"
        )

    # Format the valid response
    result_text = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return render_template("index.html", result=result_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
