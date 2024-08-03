import pandas as pd

df1=pd.read_csv(r'C:/VIT/stu_data1.csv')
df2 = pd.read_csv(r'C:/VIT/stu_data.csv')  
print("Displaying CSV file created trough Excel:")
print()
print(df1)
print()
print("Displaying CSV file exported through SQL Server")
print()
print(df2)
print()

are_equal = df1.equals(df2)
print("Are the DataFrames equal?", are_equal)

# Rows unique to the first DataFrame
unique_to_df1 = df1[~df1.isin(df2)].dropna()

# Rows unique to the second DataFrame
unique_to_df2 = df2[~df2.isin(df1)].dropna()

print("Rows unique to df1:")
print(unique_to_df1)

print("Rows unique to df2:")
print(unique_to_df2)

