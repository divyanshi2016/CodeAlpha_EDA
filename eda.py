import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("EDA Project Started")

df = pd.read_csv("dataset.csv")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nBasic Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nCorrelation:")
print(df.corr(numeric_only=True))

# Visualization
sns.histplot(df["Marks"], kde=True)
plt.title("Distribution of Marks")
plt.show()

sns.scatterplot(data=df, x="StudyHours", y="Marks")
plt.title("Study Hours vs Marks")
plt.show()

print("\nEDA Completed Successfully!")
