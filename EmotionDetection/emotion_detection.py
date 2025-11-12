import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends the input text to the Watson NLP EmotionPredict API,
    extracts emotions and returns the formatted dictionary.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)

    # Convert the response text into a Python dictionary
    response_dict = json.loads(response.text)

    # Extract emotion scores
    emotion_scores = response_dict['emotionPredictions'][0]['emotion']

    anger_score = emotion_scores['anger']
    disgust_score = emotion_scores['disgust']
    fear_score = emotion_scores['fear']
    joy_score = emotion_scores['joy']
    sadness_score = emotion_scores['sadness']

    # Find the dominant emotion (max score)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the formatted dictionary
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
