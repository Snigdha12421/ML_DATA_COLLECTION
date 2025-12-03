import pandas as pd

print("Reading data from CSV file...\n")
df_csv = pd.read_csv("sample.csv")
print("---- CSV Data ----")
print(df_csv)
print("\n")


print("Reading data from Excel file...\n")
df_excel = pd.read_excel("sample.xlsx")
print("---- Excel Data ----")
print(df_excel)
print("\n")
