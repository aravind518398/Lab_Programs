import pandas as pd

df = pd.read_csv("../Program1/Book1.csv")


print("Orginal data \n", df)

mode_salary = df["Salary"].mode()[0]

df.fillna({"Salary":mode_salary}, inplace=True)

print(df)