# Emotion Detection Application using Watson NLP

This project implements an emotion detection application using the Watson NLP emotion model and deploys it through Flask.

## Project Structure

- EmotionDetection/
  - __init__.py
  - emotion_detection.py
- templates/
  - index.html
- server.py
- test_emotion_detection.py
- requirements.txt
- evidence/
  - terminal output text files for grading activities

## Features

- Detect emotions from input text:
  - anger
  - disgust
  - fear
  - joy
  - sadness
  - dominant_emotion
- Handles blank/invalid input gracefully
- Flask web interface for deployment testing
- Unit tests for dominant emotion scenarios
- Static code analysis using pylint

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run the Flask app

```bash
python server.py
```

Open:

http://127.0.0.1:5000

## Run unit tests

```bash
python -m unittest -v
```

## Run static code analysis

```bash
python -m pylint server.py
```

## Required screenshots

- 6b_deployment_test.png
- 7c_error_handling_interface.png
