import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/dna_cleaned.csv")

# String Manipulation
print("Number of samples containing the DNA sequence 'GATTACA'")
gattaca_count = df["Sequence"].str.contains("GATTACA",na=False).sum()
print(f"Number of smaples containing 'GATTACA': {gattaca_count}")