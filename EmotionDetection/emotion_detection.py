import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    # Extracting sentiment label and score from the response
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    for emotion, score in formatted_response['emotionPredictions'][0]['emotion'].items():
        if score == max(sadness,anger,disgust,fear,joy):
            dominant_emotion=emotion
    
    # Returning a dictionary containing sentiment analysis results
    return {'anger': score, 'disgust': score, 'fear':fear, 'joy':joy,'sadness':sadness, 'dominant_emotion':dominant_emotion}
