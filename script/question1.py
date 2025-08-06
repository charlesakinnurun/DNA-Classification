import pandas as pd

# Load the DataFrame
df = pd.read_csv("datasets/dna_cleaned.csv")

# Grouping and Aggregation
print("Average GC_Content and AT_Content for each Class_Label")
class_columns = [col for col in df.columns if col.startswith("Class_")]
df_agg = df.groupby(class_columns)["GC_Content","AT_Content"].mean()
print(df_agg)