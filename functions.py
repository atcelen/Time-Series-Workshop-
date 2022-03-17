import numpy as np
import pandas as pd

def mape (y_true, y_pred):
    ape = 0
    for i in range(len(y_true)):
        ape += np.abs((y_true[i]-y_pred[i])/y_true[i])
    return (1/len(y_true)) * ape

def smape(y_true, y_pred):
  numerator = np.abs(y_true - y_pred)
  denominator = (np.abs(y_true) + np.abs(y_pred)) / 2
  ratio = numerator / denominator
  return ratio.mean()

def macd(data, slow, fast, smooth):
    fast_ewm = data["close"].ewm(span = fast, adjust = False).mean()
    slow_ewm = data["close"].ewm(span = slow, adjust = False).mean()
    macd = fast_ewm - slow_ewm
    signal = macd.ewm(span = smooth, adjust = False).mean()
    return macd, signal