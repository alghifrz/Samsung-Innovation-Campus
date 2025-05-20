import numpy as np

def preprocess_data(raw_data):
    # Misalnya, normalisasi data
    processed_data = (raw_data - np.mean(raw_data)) / np.std(raw_data)
    return processed_data

def load_data():
    # Muat data dari file atau database
    raw_train_data = np.load('train_data.npy')
    raw_train_labels = np.load('train_labels.npy')
    
    # Proses data
    train_data = preprocess_data(raw_train_data)
    train_labels = raw_train_labels  # Asumsikan label sudah bersih

    return train_data, train_labels
