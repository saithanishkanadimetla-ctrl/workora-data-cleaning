import pandas as pd

# Read the Excel file
df = pd.read_excel("student_data.xlsx")

print("Original Data")
print(df.head())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove extra spaces from text columns
text_columns = df.select_dtypes(include="object").columns
for col in text_columns:
    df[col] = df[col].str.strip()

# Standardize Gender column
df["Gender"] = df["Gender"].str.capitalize()

# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing CGPA with mean
df["CGPA"] = df["CGPA"].fillna(df["CGPA"].mean())

# Fill missing Department
df["Department"] = df["Department"].fillna("Unknown")

# Fill missing Email
df["Email"] = df["Email"].fillna("Not Available")

# Convert Join_Date to Date format
print(df["Join_Date"])
print(df["Join_Date"].dtype)

df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")

print("\nMissing Values:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_excel("cleaned_student_data.xlsx", index=False)

print("\nData cleaning completed successfully!")