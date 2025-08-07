import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/dna_cleaned.csv")

# Correlation Analysis
print("Correlation between GC_Content and kmer_3_freq")
correlation = df["GC_Content"].corr(df["kmer_3_freq"])
print(f"The correlation coefficient is: {correlation:.4f}")