#Using the Pandas library, load a CSV file and perform basic data analysis tasks, such as calculating the average of a selected column. Additionally, use Matplotlib to create visualizations, including bar charts, scatter plots, and heatmaps, to analyze the data. Provide insights and observations based on the analysis and visualizations.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Users\Arbaj Anis Tamboli\Documents\Desktop\python\internship_1\laptop_price.csv",
    encoding="latin1"
)

# Data cleaning
df["Weight"] = df["Weight"].str.replace("kg", "", regex=False).astype(float)
df["Ram"] = df["Ram"].str.replace("GB", "", regex=False).astype(int)

# First 5 rows
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Average Price
avg_price = df["Price_euros"].mean()
print("\nAverage Laptop Price (Euros):", round(avg_price, 2))

# Bar Chart: Company-wise Average Price
company_price = df.groupby("Company")["Price_euros"].mean()

plt.figure(figsize=(10, 5))
company_price.sort_values().plot(kind="bar", color="skyblue")
plt.title("Average Laptop Price by Company")
plt.xlabel("Company")
plt.ylabel("Average Price (Euros)")
plt.tight_layout()
plt.show()

# Scatter Plot: Screen Size vs Price
plt.figure(figsize=(8, 5))
plt.scatter(df["Inches"], df["Price_euros"], alpha=0.6)
plt.title("Screen Size vs Laptop Price")
plt.xlabel("Screen Size (Inches)")
plt.ylabel("Price (Euros)")
plt.tight_layout()
plt.show()

# Scatter Plot: Weight vs Price
plt.figure(figsize=(8, 5))
plt.scatter(df["Weight"], df["Price_euros"], alpha=0.6, color="green")
plt.title("Laptop Weight vs Price")
plt.xlabel("Weight (kg)")
plt.ylabel("Price (Euros)")
plt.tight_layout()
plt.show()

# Heatmap
corr = df[["Inches", "Ram", "Weight", "Price_euros"]].corr()

plt.figure(figsize=(7, 6))
plt.imshow(corr, cmap="coolwarm", aspect="auto")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=30, ha="right")
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
