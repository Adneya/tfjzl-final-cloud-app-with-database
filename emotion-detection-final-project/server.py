"""Flask web application for emotion detection."""

from __future__ import annotations

from typing import Dict, Optional

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


def _format_emotion_response(emotions: Dict[str, Optional[float]]) -> str:
    """Create a readable response string for detected emotions."""
    return (
        "For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )


@app.route("/")
def render_index_page() -> str:
    """Render the application home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def analyze_emotion() -> str:
    """Analyze user text and return a formatted emotion string."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!."

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return _format_emotion_response(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
