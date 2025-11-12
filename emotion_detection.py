import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze or text_to_analyze.strip() == "":
        # Return None values for blank input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # API endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Request body
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Send request to API
    response = requests.post(url, json=myobj, headers=headers)

    # Handle HTTP 400 (Bad Request)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convert response to JSON
    response_dict = json.loads(response.text)

    # Extract emotion scores
    emotions = response_dict['emotionPredictions'][0]['emotion']

    # Find dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return formatted dictionary
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
