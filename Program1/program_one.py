import pandas as pd

df = pd.read_csv("Book1.csv")

print("Original DataFrame: ")
print(df)

median_salary = df["Salary"].median()

df.fillna({"Salary":median_salary}, inplace=True)

print("Imputed dataset: ")
print(df)