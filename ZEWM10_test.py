import pandas as pd

# Compare case count from python created excel and manually created excel
df1 = pd.read_excel(r'C:\Users\l619072\Downloads\2HQI\Book1.xlsx')
df2 = pd.read_excel(r'C:\Users\l619072\Downloads\2HQI\2HQI ZEWM10 upload.xlsx')

# add the cases from df2 to df1
df1['CV_Count'] = df2['Available Qty.']
 
# create new column in df1 to check if cases match
df1['CV_Matching'] = np.where(df1['CV_Count'] == df2['Available Qty.'], 'True', 'False') 

# Export dataframe as excel in current working directory
file_name = 'Check_matching_CV.xlsx'
df1.to_excel(file_name, index=False)
print('DataFrame is successfully exported as an excel file!')