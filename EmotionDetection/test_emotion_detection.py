from emotion_detection import emotion_detector
import unittest

def test_emotion_detector(self):
    # Test case for joy
    result_1 = emotion_detector('I am glad this happened')
    self.assertEqual(result_1['dominant_emotion'], 'joy')
    
    # Test case for anger
    result_2 = emotion_detector('I am really mad about this')
    self.assertEqual(result_2['dominant_emotion'], 'anger')
    
    # Test case for disgust
    result_3 = emotion_detector('I feel disgusted just hearing about this')
    self.assertEqual(result_3['dominant_emotion'], 'disgustL')

     # Test case sadness
    result_4 = emotion_detector('I am so sad about this')
    self.assertEqual(result_3['dominant_emotion'], 'sadness')

         # Test case fear
    result_4 = emotion_detector('I am really afraid that this will happen')
    self.assertEqual(result_3['dominant_emotion'], 'fear')

    
unittest.main()