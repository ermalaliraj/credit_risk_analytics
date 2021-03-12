import pandas as pd
import statsmodels.formula.api as smf

mortgage = pd.read_csv("mortgage.csv")
print("*** file content ***")
print(mortgage)

fileType = type(mortgage)

print("fileType: " + str(fileType))

print("\nmortgage.info():")
print(mortgage.info())

# Access column by name
# LTV_time = mortgage.LTV_time
LTV_time = mortgage["LTV_time"]
# LTV_time = mortgage.loc[:, "LTV_time"]
print("LTV_time: " + str(LTV_time))

# Access column by index
col5 = mortgage.iloc[:, 5]
print("pos1: " + str(col5))

mortgage_temp = mortgage.query("FICO_orig_time >= 74")
print("mortgage_temp: " + str(mortgage_temp))



