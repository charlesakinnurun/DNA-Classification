from numpy import cross
import pandas as pd

# Load the dataset
df = pd.read_csv("datasets/dna_cleaned.csv")

# Cross Tabulation
print("Sample counts for each Class_label and Disease Risk")
class_labels = df.filter(like="Class_").idxmax(axis=1).str.replace("Class_"," ")
crosstab = pd.crosstab(class_labels,df["Disease_Risk_Encoded"])
print(crosstab)