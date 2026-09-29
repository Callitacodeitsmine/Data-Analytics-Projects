# =========================
# FLIPKART VISUALIZATIONS
# =========================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
os.makedirs("visualizations/flipkart", exist_ok=True)

df = pd.read_csv("../data/flipkart.csv").drop_duplicates()

df["retail_price"] = pd.to_numeric(df["retail_price"], errors="coerce")
df["discounted_price"] = pd.to_numeric(df["discounted_price"], errors="coerce")
df["overall_rating"] = pd.to_numeric(df["overall_rating"], errors="coerce")

df = df.dropna(subset=["retail_price", "discounted_price"])
df = df[df.retail_price > 0]
df = df[df.discounted_price >= 0]

df["discount_amt"] = df.retail_price - df.discounted_price
df["discount_pct"] = (
    df["discount_amt"] / df["retail_price"] * 100
).round(1)

df["category"] = (
    df.product_category_tree.astype(str)
    .str.strip('["]')
    .str.split(">>")
    .str[0]
    .str.strip()
)

df = df[df.discount_pct >= 0]

top_cats = df.category.value_counts().head(10).index
rated = df.dropna(subset=["overall_rating"])


# 1. Products by category
plt.figure(figsize=(12, 6))
df.category.value_counts().head(10).sort_values().plot(kind="barh")
plt.title("Top 10 Product Categories by Number of Products")
plt.xlabel("Number of Products")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("visualizations/flipkart/01_products_by_category.png", dpi=300, bbox_inches="tight")
plt.close()


# 2. Average discount by category
cat_discount = (
    df[df.category.isin(top_cats)]
    .groupby("category")
    .discount_pct.mean()
    .sort_values()
)

plt.figure(figsize=(12, 6))
cat_discount.plot(kind="barh")
plt.title("Average Discount by Category")
plt.xlabel("Average Discount (%)")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("visualizations/flipkart/02_average_discount_category.png", dpi=300, bbox_inches="tight")
plt.close()


# 3. Discount distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["discount_pct"], bins=30, kde=True)
plt.title("Distribution of Discount Percentage")
plt.xlabel("Discount (%)")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("visualizations/flipkart/03_discount_distribution.png", dpi=300, bbox_inches="tight")
plt.close()


# 4. Retail price distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["retail_price"], bins=40, kde=True)
plt.title("Distribution of Retail Prices")
plt.xlabel("Retail Price")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("visualizations/flipkart/04_retail_price_distribution.png", dpi=300, bbox_inches="tight")
plt.close()


# 5. Discounted price distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["discounted_price"], bins=40, kde=True)
plt.title("Distribution of Discounted Prices")
plt.xlabel("Discounted Price")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("visualizations/flipkart/05_discounted_price_distribution.png", dpi=300, bbox_inches="tight")
plt.close()


# 6. Retail price vs discounted price
sample = df.sample(min(1000, len(df)), random_state=42)

plt.figure(figsize=(10, 7))
sns.scatterplot(data=sample, x="retail_price", y="discounted_price", alpha=0.5)
plt.title("Retail Price vs Discounted Price")
plt.xlabel("Retail Price")
plt.ylabel("Discounted Price")
plt.tight_layout()
plt.savefig("visualizations/flipkart/06_price_comparison.png", dpi=300, bbox_inches="tight")
plt.close()


# 7. Price vs discount
plt.figure(figsize=(10, 7))
sns.scatterplot(data=sample, x="retail_price", y="discount_pct", alpha=0.5)
plt.title("Retail Price vs Discount Percentage")
plt.xlabel("Retail Price")
plt.ylabel("Discount (%)")
plt.tight_layout()
plt.savefig("visualizations/flipkart/07_price_vs_discount.png", dpi=300, bbox_inches="tight")
plt.close()


# 8. Discount boxplot
plt.figure(figsize=(14, 7))
sns.boxplot(data=df[df.category.isin(top_cats)], x="category", y="discount_pct")
plt.title("Discount Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Discount (%)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("visualizations/flipkart/08_discount_boxplot.png", dpi=300, bbox_inches="tight")
plt.close()


# 9. Price boxplot
plt.figure(figsize=(14, 7))
sns.boxplot(data=df[df.category.isin(top_cats)], x="category", y="discounted_price")
plt.title("Discounted Price Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Discounted Price")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("visualizations/flipkart/09_price_boxplot.png", dpi=300, bbox_inches="tight")
plt.close()


# 10. Top discounts
top_discount = df.nlargest(10, "discount_pct")

plt.figure(figsize=(12, 7))
sns.barplot(data=top_discount, x="discount_pct", y="product_name")
plt.title("Top 10 Products with Highest Discount")
plt.xlabel("Discount (%)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("visualizations/flipkart/10_top_discounts.png", dpi=300, bbox_inches="tight")
plt.close()


# 11. Rating distribution
plt.figure(figsize=(10, 6))
sns.histplot(rated["overall_rating"], bins=20, kde=True)
plt.title("Distribution of Product Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Products")
plt.tight_layout()
plt.savefig("visualizations/flipkart/11_rating_distribution.png", dpi=300, bbox_inches="tight")
plt.close()


# 12. Discount vs rating
plt.figure(figsize=(10, 7))
sns.scatterplot(
    data=rated.sample(min(1000, len(rated)), random_state=42),
    x="discount_pct",
    y="overall_rating",
    alpha=0.5
)
plt.title("Discount Percentage vs Product Rating")
plt.xlabel("Discount (%)")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("visualizations/flipkart/12_discount_vs_rating.png", dpi=300, bbox_inches="tight")
plt.close()


# 13. Correlation heatmap
numeric_cols = [
    "retail_price",
    "discounted_price",
    "discount_amt",
    "discount_pct",
    "overall_rating"
]

plt.figure(figsize=(9, 7))
sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Flipkart Correlation Heatmap")
plt.tight_layout()
plt.savefig("visualizations/flipkart/13_correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.close()


# 14. Discount band pie
df["discount_band"] = pd.cut(
    df["discount_pct"],
    bins=[-1, 10, 25, 50, 75, 100, float("inf")],
    labels=["0-10%", "10-25%", "25-50%", "50-75%", "75-100%", "100%+"]
)

plt.figure(figsize=(8, 8))
df["discount_band"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Products by Discount Band")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/flipkart/14_discount_pie.png", dpi=300, bbox_inches="tight")
plt.close()