import pandas as pd

from script.question5 import class_labels_q5

# Load the dataset
df = pd.read_csv("datasets/dna_cleaned.csv")

# Counting and Sorting
print("Class_Label with the highest number of samples:")
class_counts = class_labels_q5.value.counts()
most_common_class = class_counts.idmax()
print(f"The Class with the most samples is '{most_common_class} with {class_counts.max()}")