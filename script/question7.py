import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/dna_cleaned.csv")

# Question 7: Data Transformation
print("\n7. Average AT_GC_Ratio for each Class_Label:")
df['AT_GC_Ratio'] = df['AT_Content'] / df['GC_Content']

avg_ratio_per_Class_Bacteria = df.groupby(df["Class_Bacteria"])['AT_GC_Ratio'].mean()
print(avg_ratio_per_Class_Bacteria)

avg_ratio_per_Class_Human = df.groupby(df["Class_Human"])['AT_GC_Ratio'].mean()
print(avg_ratio_per_Class_Human)

avg_ratio_per_Class_Plant = df.groupby(df["Class_Plant"])['AT_GC_Ratio'].mean()
print(avg_ratio_per_Class_Plant)

avg_ratio_per_Class_Plant = df.groupby(df["Class_Human"])['AT_GC_Ratio'].mean()
print(avg_ratio_per_Class_Plant)