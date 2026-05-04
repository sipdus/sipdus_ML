import pandas as pd

def load_signal(path):
    signal = pd.read_csv(path, header=None).values.squeeze()
    return signal