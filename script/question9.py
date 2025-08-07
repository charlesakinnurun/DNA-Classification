import pandas as pd

# Load the datasets
df = pd.read_csv("datasets/dna_cleaned.csv")

# Total Counts
print("\n9. Total count of each nucleotide across all samples:")
nucleotide_columns = ['Num_A', 'Num_T', 'Num_C', 'Num_G']
total_counts = df[nucleotide_columns].sum()
print(total_counts)