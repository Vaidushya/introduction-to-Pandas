# -- Homework --#

import pandas as pd
import numpy as np

# creating dictionary
employee_data = {
    "ID": [1, 2, 3, 4],
    "Name": ['Pankaj', 'Meghna', 'David', 'Lisa'],
    "Role": ['CEO'],
    "Salary": [100, 200]
}

# creating Datsa frame
df = pd.DataFrame(employee_data)

print("First 2 rows:")
print(df.head(2))
print("\nLast 2 rows:")
print(df.tail(2))

# checking the total number of null values in the dataframe
print("\nNumber of null values in each column:")
print(df.isnull().sum())

# detailed information about the dataframe
print("\nDetailed information about the DataFrame:")
print(df.describe())

# dropping all the rows with null values, storing the result in a new dataframe and printing it
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with null values:")
print(df_dropped)
print("\nData types of each column:")
print(df.dtypes)
print("\nNumber of non-null entries in each column:")
print(df.count())

# dropping all the columns with null values, storing the result in a new dataframe and printing it
df_dropped_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with null values:")
print(df_dropped_cols)
print("\nData types of each column:")
print(df.dtypes)
print("\nNumber of non-null entries in each column:")
print(df.count())

# filling null values of the salary column with the value 300 and printing the updated dataframe
df_filled = df.copy()
df_filled['Salary'].fillna(300, inplace=True)
print("\nDataFrame after filling null values in 'Salary' column with 300:")
print(df_filled)

# filling null values of the role column with the value CEO and printing the updated dataframe
df_filled['Role'].fillna('CEO', inplace=True)
print("\nDataFrame after filling null values in 'Role' column with 'CEO':")
print(df_filled)
