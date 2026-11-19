# Self-Assessment Questions

# 1. A boolean filter only selects the rows that meet a certain condition. For example, it can show only sales from the North region.
# 2. df["revenue"] returns a Series. df[["revenue"]] returns a DataFrame with one column. This is important when a function expects a DataFrame instead of a Series.
# 3. I'd pick pandas because it makes working with large datasets easier and faster because it lets me filter and sort data with a few lines of code.

import pandas as pd

# Exercise 1
print("\nExercise 1: Load it")

df = pd.read_csv("data/retail_sales.csv")

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)


# Exercise 2
print("\nExercise 2: Filter by region")

south = df[df["region"] == "South"]

print(len(south))
print(south.head())


# Exercise 3
print("\nExercise 3: Top 5 by revenue")

top_five = df.sort_values("revenue", ascending=False).head(5)

print(top_five)


# Exercise 4
print("\nExercise 4: Two-condition filter")

big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]

print(len(big_south))
print(big_south.head())


# Exercise 5
print("\nExercise 5: A new column")

df["per_unit"] = df["revenue"] / df["quantity"]

print(df.head())
print(df["per_unit"].mean())


# Exercise 6
print("\nExercise 6: Unique values")

print(df["region"].unique())
print(df["region"].value_counts())


# Exercise 7
print("\nExercise 7: Select columns")

selected = df[["region", "product", "revenue"]]

print(selected.shape)


# Exercise 8
print("\nExercise 8: Save")

df.to_csv("data/explored.csv", index=False)

print("Saved data/explored.csv successfully.")
