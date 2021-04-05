import pandas as pd
import numpy as np

import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split

x = pd.read_csv("mortgage.csv")
y = np.arange(len(x))

print("x: " + str(x))
print("y: " + str(y))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
print("x_train: " + str(x_train))
print("x_test: " + str(x_test))
print("y_train: " + str(y_train))
print("y_test: " + str(y_test))