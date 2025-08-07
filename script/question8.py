import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/dna_cleaned.csv")

# Top N Values
print("Top 5 samples with highest kmer_3_freq and Disease_Risk ='High'")
high_risk_samples = df[df["Disease_Risk_Encoded"] == 2].sort_values(by="kmer_3_freq",ascending=False)
top_5_samples = high_risk_samples[["Sample_ID","Sequence","kmer_3_freq"]].head(5)
print(top_5_samples)