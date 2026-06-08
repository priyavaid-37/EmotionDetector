# pylint: disable=missing-final-newline,missing-module-docstring,missing-function-docstring

from flask import Flask, request
from EmotionDetector.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    return """
    <h1>Emotion Detector</h1>
    <form action="/emotionDetector">
        <input name="textToAnalyze" type="text">
        <input type="submit" value="Analyze">
    </form>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)