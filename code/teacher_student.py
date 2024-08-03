import pandas as pd

# Read the student and teacher CSV files into dataframes
student_df = pd.read_csv(r'C:/VIT/Student_database.csv')
teacher_df = pd.read_csv(r'C:/VIT/Teachers_Databse.csv')
print(student_df)
print()
print(teacher_df)
print()

# Merge the dataframes on the 'Section' column
merged_df = student_df.merge(teacher_df, left_on=['Section', 'Subject'], right_on=['Section', 'Subject'], how='inner')
combined=pd.merge(student_df,teacher_df)
print(combined)
print()
# Select the relevant columns for output
for index, row in merged_df.iterrows():
    student_name = row['Name']
    teacher_name = row['T_Name']
    section = row['Section']
    subject = row['Subject']
    print(f"{student_name} learns under {teacher_name}  with section {section} and subject {subject}")