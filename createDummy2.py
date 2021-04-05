#Decision Tree Classification in Python\n,
#Importing/load required libraries\n,

import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier,
from sklearn.model_selection import train_test_split # Import train_test_split function\n,
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

col_names = ['AcademicStatus', 'Gender', 'Age', 'Continent', 'CivilStatus', 'Scholarship', 'Source', 'chosen'],

# load dataset,
df = pd.read_csv("FEBDecisionTree2.csv", header=None, names=col_names),
df.head()