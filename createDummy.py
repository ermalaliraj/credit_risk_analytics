import pandas as pd
# import numpy as np
# import statsmodels.api as sm

kulchoice = pd.read_excel('students.xlsx',sheet_name='Data')

# Create dummies
cat_vars = ['Continent','Beurs']
for var in cat_vars:
    cat_list = pd.get_dummies(kulchoice[var], prefix=var, drop_first=True)
    kulchoice = kulchoice.join(cat_list)
    kulchoice.drop(columns=var, inplace=True)

Y = kulchoice[['Beurs']]
X = kulchoice.drop(columns='Beurs')
