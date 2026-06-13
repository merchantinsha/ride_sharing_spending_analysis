"""
Impact of Ride-Sharing & Food Delivery Apps on Student Spending
================================================================
Analysed survey data from 200+ students to understand how apps
like Uber, Ola, Swiggy, and Zomato affect spending behaviour,
budget management, and financial habits among young adults.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. Load and clean dataset ────────────────────────────────

df = pd.read_csv("student_spending_survey.csv")

# Shorten column headings for readability
df.columns = df.columns.str.strip().str.replace(r"\s+", "_", regex=True)

# Drop rows with missing values
df.dropna(inplace=True)

print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# ── 2. Objective 1: Budget management styles ─────────────────

print("\n── Objective 1: How do students manage their budgets? ──")

budget_counts = df["funding_source"].value_counts()
print(budget_counts)

plt.figure(figsize=(7, 7))
colours = ["#4C72B0", "#55A868", "#C44E52", "#8172B2"]
plt.pie(budget_counts.values, labels=budget_counts.index,
        autopct="%1.1f%%", startangle=140, colors=colours)
plt.title("Student Budget Management — Funding Source")
plt.tight_layout()
plt.savefig("funding_source_pie.png", dpi=150)
plt.show()

# ── 3. Objective 2: Usage frequency ──────────────────────────

print("\n── Objective 2: How often do students use these apps? ──")

usage_cols = ["ride_sharing_frequency", "food_delivery_frequency"]
usage_data = df[usage_cols].apply(pd.Series.value_counts).fillna(0)
print(usage_data)

usage_data.plot(kind="bar", figsize=(10, 6), edgecolor="black")
plt.xlabel("Usage Frequency")
plt.ylabel("Number of Students")
plt.title("Usage Frequency: Ride-Sharing vs Food Delivery Apps")
plt.legend(["Ride-Sharing", "Food Delivery"])
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("usage_frequency_bar.png", dpi=150)
plt.show()

# ── 4. Objective 3: Spending correlation ─────────────────────

print("\n── Objective 3: Relationship between ride & food spending ──")

plt.figure(figsize=(9, 6))
plt.scatter(df["monthly_ride_spend"], df["monthly_food_spend"],
            alpha=0.5, c="#4C72B0", edgecolors="white", linewidth=0.5)
plt.xlabel("Monthly Ride-Sharing Spend (₹)")
plt.ylabel("Monthly Food Delivery Spend (₹)")
plt.title("Ride-Sharing vs Food Delivery — Monthly Spending")
plt.tight_layout()
plt.savefig("spending_scatter.png", dpi=150)
plt.show()

# Correlation
corr = df["monthly_ride_spend"].corr(df["monthly_food_spend"])
print(f"Correlation between ride and food spending: {corr:.3f}")

# ── 5. Summary statistics ────────────────────────────────────

print("\n── Summary Statistics ──")
spend_cols = ["monthly_ride_spend", "monthly_food_spend"]
print(df[spend_cols].describe())

print("\nAnalysis complete. Charts saved.")
