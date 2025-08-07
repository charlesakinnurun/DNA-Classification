import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/dna_cleaned.csv")

# Multi-level Grouping
print("Average GC_Content for each Class_Label and Disease_Risk")
class_labels_q5 = df.filter(like="Class_").idxmax(axis=1).str.replace("Class_"," ")
grouped_df = pd.DataFrame({
    "Class_Label":class_labels_q5,
    "Disease_Risk": df["Disease_Risk_Encoded"],
    "GC_Content": df["GC_Content"]
})
avg_gc_content = grouped_df.groupby(["Class_Label","Disease_Risk"])["GC_Content"].mean().unstack()
print(avg_gc_content)