''' Aim of this module is to initiate the application of emotion detetcion
    to be executed using Flask and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    '''
    This function calls emotion_detector function to analyse provided text 
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return a formatted string
    return f"For the given statement,"\
    f" the system response is 'anger':"\
    f"{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}."\
    f"The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    '''
    rendering template
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
