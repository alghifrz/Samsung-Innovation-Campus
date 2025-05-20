import tensorflow as tf
import numpy as np
from utils.data_processing import preprocess_data

def load_model():
    return tf.keras.models.load_model('model/dance_mons_model.h5')

def generate_challenge(raw_sensor_data):
    model = load_model()
    processed_data = preprocess_data(np.array([raw_sensor_data]))
    prediction = model.predict(processed_data)
    challenge_class = np.argmax(prediction)
    return adapt_challenge_based_on_prediction(challenge_class)

def adapt_challenge_based_on_prediction(prediction):
    challenges = ['Challenge 1', 'Challenge 2', 'Challenge 3', 'Challenge 4', 'Challenge 5', 
                  'Challenge 6', 'Challenge 7', 'Challenge 8', 'Challenge 9', 'Challenge 10']
    return challenges[prediction]
