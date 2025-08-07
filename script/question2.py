import pandas as pd

# Load the Dataset
df = pd.read_csv("datasets/dna_cleaned.csv")

# Conditional Filtering
print("Average kmer_3_freq for samples with Mutation_Flag = 1")
avg_kmer_mutation = df[df["Mutation_Flag"] == 1]["kmer_3_freq"].mean()
print(f"Average kmer_3_freq for samples with a mutation flag: {avg_kmer_mutation:.4f}")