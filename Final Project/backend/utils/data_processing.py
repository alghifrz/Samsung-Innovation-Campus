import numpy as np

def preprocess_data(raw_data):
    processed_data = (raw_data - np.mean(raw_data)) / np.std(raw_data)
    return processed_data

def load_data():
    raw_train_data = np.load('model/train_data.npy')
    raw_train_labels = np.load('model/train_labels.npy')
    train_data = preprocess_data(raw_train_data)
    train_labels = raw_train_labels
    return train_data, train_labels
