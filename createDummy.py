import pandas as pd
# import numpy as np
# import statsmodels.api as sm

students = pd.read_excel('students2.xlsx', sheet_name='students')

# Create dummies
# cat_vars = ['Description', 'Date', 'Continent', 'AcademicYear', 'Status', 'Category', 'StudentCode', 'Scholarship', 'ScholarshipCategory', 'Chosen']
cat_vars = ['Chosen']
for var in cat_vars:
    cat_list = pd.get_dummies(students[var], prefix=var, drop_first=True)
    students = students.join(cat_list)
    students.drop(columns=var, inplace=True)

print("Chosen: " + str(students.info()))

Y = students[['Chosen_Yes']]
X = students.drop(columns='Chosen_Yes')

print("X: " + str(X))
print("Y\\: " + str(Y))
#
# logit_model = sm.Logit(Y, X)
# result = logit_model.fit()
# print(result.summary())

corrMatrix = X.corr(method ='pearson')
corrMatrix.to_excel(excel_writer = "students_output.xlsx")



# print (corrMatrix)
# print("corrMatrix: " + str(corrMatrix))
# print (corrMatrix.info())
#
# import xlsxwriter
# workbook = xlsxwriter.Workbook('students_output.xlsx')
# worksheet = workbook.add_worksheet()
# row = 0
# for col, data in enumerate(corrMatrix):
#     worksheet.write_column(row, col, data)
#
# workbook.close()
#
#
