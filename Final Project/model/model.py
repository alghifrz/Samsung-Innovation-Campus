import tensorflow as tf

def load_model():
    return tf.keras.models.load_model('dance_mons_model.h5')

def generate_challenge(sensor_data):
    model = load_model()
    prediction = model.predict(sensor_data)
    challenge = adapt_challenge_based_on_prediction(prediction)
    return challenge
