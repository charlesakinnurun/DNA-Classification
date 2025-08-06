import pandas as pd

# Load the DataFrame
df = pd.read_csv("datasets/dna.csv")

# --------- Step 1: Verify Data Integrity --------
# Check if the sum of nucleotide counts equals the sequence length
df["sum_nucleotides"] = df["Num_A"] + df["Num_T"] + df["Num_C"] + df["Num_G"]
integrity_check_nucleotides = (df["sum_nucleotides"] == df["Sequence_Length"]).all()
print(f"Nucleotide count integrity check passed: {integrity_check_nucleotides}")

# Check if GC and AT content sum to 100
integrity_check_content = (df["GC_Content"] + df["AT_Content"] == 100.0).all()
print(f"GC/AT content integrity check passed: {integrity_check_content}")

# ------------- Step 2: Handle Categorical Variables -------------

# Perform one-hot encoding on "Class_Label"
df = pd.get_dummies(df,columns=["Class_Label"],prefix="Class")

# Perform label encoding on "Disease Risk".
risk_mapping = {"Low":0, "Medium":1, "High":2}
df["Disease_Risk_Encoded"] = df["Disease_Risk"].map(risk_mapping)
df = df.drop(columns=["Disease_Risk"])
print("Applied one-hot and label encoding to categorical columns")

# ---------------- Step 3: Check for and Remove Duplicates------

# Check for duplicate rows
num_duplicates = df.duplicated().sum()
if num_duplicates > 0:
    print(f"Found {num_duplicates} duplicate rows.Removing them")
    df = df.drop_duplicates()
else:
    print("No duplicate rows found")

# Display the cleaned DataFrame's info and head to confirm the changes
print("Cleaned DataFrame Info")
print(df.info())

print("Cleaned DataFrame Head")
print(df.head())

# Save the Dataset
df.to_csv("datasets/dna_cleaned.csv")
