import pandas as pd 
import sklearn
from sklearn.linear_model import Ridge
import numpy as np

teamBox = pd.read_csv("team.csv")
oldPlayer = pd.read_csv("player12131415.csv")
newPlayer = pd.read_csv("player161718.csv")

newPlayer = newPlayer.dropna()


