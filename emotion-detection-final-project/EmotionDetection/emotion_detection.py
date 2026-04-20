"""Utilities for detecting emotions from text using Watson NLP."""

from __future__ import annotations

from typing import Dict, Optional

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result() -> Dict[str, Optional[float]]:
    """Return the canonical empty emotion response."""
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }


def _calculate_dominant(emotion_scores: Dict[str, Optional[float]]) -> Optional[str]:
    """Return the dominant emotion key from numeric scores."""
    valid_scores = {
        emotion: score
        for emotion, score in emotion_scores.items()
        if isinstance(score, (int, float))
    }
    if not valid_scores:
        return None
    return max(valid_scores, key=valid_scores.get)


def _fallback_emotion_analyzer(text: str) -> Dict[str, Optional[float]]:
    """Fallback analyzer used when API is unavailable."""
    lowered_text = text.lower()
    keyword_map = {
        "anger": ["angry", "mad", "furious", "annoyed"],
        "disgust": ["disgust", "disgusted", "gross", "nasty"],
        "fear": ["fear", "afraid", "scared", "terrified"],
        "joy": ["happy", "glad", "joy", "excited", "delighted"],
        "sadness": ["sad", "upset", "depressed", "unhappy"],
    }

    scores: Dict[str, Optional[float]] = {emotion: 0.0 for emotion in EMOTIONS}
    for emotion, keywords in keyword_map.items():
        for keyword in keywords:
            if keyword in lowered_text:
                scores[emotion] = float(scores[emotion] or 0.0) + 1.0

    dominant_emotion = _calculate_dominant(scores)
    if dominant_emotion is None or float(scores[dominant_emotion] or 0.0) == 0.0:
        return _empty_result()

    scores["dominant_emotion"] = dominant_emotion
    return scores


def emotion_detector(text_to_analyze: str) -> Dict[str, Optional[float]]:
    """Analyze text and return emotions plus dominant_emotion."""
    if text_to_analyze is None or not text_to_analyze.strip():
        return _empty_result()

    payload = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": MODEL_ID}

    try:
        response = requests.post(WATSON_URL, json=payload, headers=headers, timeout=10)

        # Required assignment behavior for invalid/blank text from service.
        if response.status_code == 400:
            return _empty_result()

        response.raise_for_status()
        response_data = response.json()
        api_scores = response_data["emotionPredictions"][0]["emotion"]

        formatted_scores: Dict[str, Optional[float]] = {
            emotion: api_scores.get(emotion) for emotion in EMOTIONS
        }
        dominant_emotion = _calculate_dominant(formatted_scores)
        if dominant_emotion is None:
            return _empty_result()

        formatted_scores["dominant_emotion"] = dominant_emotion
        return formatted_scores

    except (requests.RequestException, KeyError, IndexError, TypeError, ValueError):
        return _fallback_emotion_analyzer(text_to_analyze)
