# =========================
# ZOMATO VISUALIZATIONS
# =========================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
os.makedirs("visualizations/zomato", exist_ok=True)

df = pd.read_csv("../data/zomato.csv").drop_duplicates()

df["rate"] = (
    df["rate"]
    .astype(str)
    .str.extract(r"(\d+(?:\.\d+)?)")[0]
)

df["rate"] = pd.to_numeric(df["rate"], errors="coerce")

df["cost_for_two"] = (
    df["approx_cost(for two people)"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df["cost_for_two"] = pd.to_numeric(
    df["cost_for_two"],
    errors="coerce"
)

df = df.dropna(
    subset=["rate", "cost_for_two", "location"]
)

df["price_band"] = pd.cut(
    df.cost_for_two,
    [0, 500, 1000, 2000, 1e6],
    labels=["<500", "500-1k", "1k-2k", "2k+"]
)

sample = df.sample(min(1000, len(df)), random_state=42)


# 1. Rating distribution
plt.figure(figsize=(10, 6))
sns.histplot(df.rate, bins=20, kde=True)
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Rating")
plt.ylabel("Restaurants")
plt.tight_layout()
plt.savefig("visualizations/zomato/01_rating_distribution.png", dpi=300, bbox_inches="tight")
plt.close()


# 2. Cost distribution
plt.figure(figsize=(10, 6))
sns.histplot(df.cost_for_two, bins=30, kde=True)
plt.title("Distribution of Cost for Two")
plt.xlabel("Cost for Two")
plt.ylabel("Restaurants")
plt.tight_layout()
plt.savefig("visualizations/zomato/02_cost_distribution.png", dpi=300, bbox_inches="tight")
plt.close()


# 3. Rating vs cost
plt.figure(figsize=(10, 7))
sns.scatterplot(
    data=sample,
    x="cost_for_two",
    y="rate",
    alpha=0.5
)
plt.title("Restaurant Rating vs Cost for Two")
plt.xlabel("Cost for Two")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("visualizations/zomato/03_rating_vs_cost.png", dpi=300, bbox_inches="tight")
plt.close()


# 4. Rating vs cost by online order
plt.figure(figsize=(10, 7))
sns.scatterplot(
    data=sample,
    x="cost_for_two",
    y="rate",
    hue="online_order",
    alpha=0.6
)
plt.title("Rating vs Cost by Online Ordering")
plt.xlabel("Cost for Two")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("visualizations/zomato/04_rating_cost_online_order.png", dpi=300, bbox_inches="tight")
plt.close()


# 5. Average cost by location
location_cost = (
    df.groupby("location")
    .cost_for_two.mean()
    .sort_values(ascending=False)
    .head(15)
)

plt.figure(figsize=(12, 7))
location_cost.sort_values().plot(kind="barh")
plt.title("Average Restaurant Cost by Location")
plt.xlabel("Average Cost for Two")
plt.ylabel("Location")
plt.tight_layout()
plt.savefig("visualizations/zomato/05_cost_by_location.png", dpi=300, bbox_inches="tight")
plt.close()


# 6. Restaurants by location
location_count = df.location.value_counts().head(15)

plt.figure(figsize=(12, 7))
location_count.sort_values().plot(kind="barh")
plt.title("Top Locations by Number of Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("Location")
plt.tight_layout()
plt.savefig("visualizations/zomato/06_restaurants_by_location.png", dpi=300, bbox_inches="tight")
plt.close()


# 7. Rating by price band
plt.figure(figsize=(10, 6))
sns.boxplot(
    data=df,
    x="price_band",
    y="rate"
)
plt.title("Restaurant Ratings by Price Band")
plt.xlabel("Price Band")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("visualizations/zomato/07_rating_by_price_band.png", dpi=300, bbox_inches="tight")
plt.close()


# 8. Restaurants by price band
plt.figure(figsize=(9, 6))
df.price_band.value_counts().sort_index().plot(kind="bar")
plt.title("Restaurants by Price Band")
plt.xlabel("Price Band")
plt.ylabel("Restaurants")
plt.tight_layout()
plt.savefig("visualizations/zomato/08_price_band.png", dpi=300, bbox_inches="tight")
plt.close()


# 9. Price band pie
plt.figure(figsize=(8, 8))
df.price_band.value_counts().sort_index().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Restaurant Distribution by Price Band")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/zomato/09_price_band_pie.png", dpi=300, bbox_inches="tight")
plt.close()


# 10. Online order pie
plt.figure(figsize=(8, 7))
df.online_order.value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Online Order Availability")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/zomato/10_online_order_pie.png", dpi=300, bbox_inches="tight")
plt.close()


# 11. Online order vs average rating
online_rating = df.groupby("online_order").rate.mean()

plt.figure(figsize=(8, 6))
online_rating.plot(kind="bar")
plt.title("Average Rating by Online Order Availability")
plt.xlabel("Online Order")
plt.ylabel("Average Rating")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("visualizations/zomato/11_online_rating.png", dpi=300, bbox_inches="tight")
plt.close()


# 12. Online order rating boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(
    data=df,
    x="online_order",
    y="rate"
)
plt.title("Rating Distribution by Online Order Availability")
plt.xlabel("Online Order")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("visualizations/zomato/12_online_rating_boxplot.png", dpi=300, bbox_inches="tight")
plt.close()


# Cuisine data
cuisines = df.assign(
    cuisines=df.cuisines.astype(str).str.split(",")
).explode("cuisines")

cuisines["cuisines"] = cuisines["cuisines"].str.strip()


# 13. Top cuisines
top_cuisines = cuisines.cuisines.value_counts().head(15)

plt.figure(figsize=(12, 7))
top_cuisines.sort_values().plot(kind="barh")
plt.title("Top 15 Cuisines by Restaurant Count")
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.savefig("visualizations/zomato/13_top_cuisines.png", dpi=300, bbox_inches="tight")
plt.close()


# 14. Cuisine votes
cuisine_votes = (
    cuisines.groupby("cuisines")
    .votes.sum()
    .sort_values(ascending=False)
    .head(15)
)

plt.figure(figsize=(12, 7))
cuisine_votes.sort_values().plot(kind="barh")
plt.title("Top 15 Cuisines by Total Votes")
plt.xlabel("Total Votes")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.savefig("visualizations/zomato/14_cuisine_votes.png", dpi=300, bbox_inches="tight")
plt.close()


# 15. High-rated restaurants by price band
high_rated = (
    df[df.rate >= 4.2]
    .groupby("price_band", observed=True)
    .size()
)

plt.figure(figsize=(9, 6))
high_rated.plot(kind="bar")
plt.title("High-Rated Restaurants by Price Band")
plt.xlabel("Price Band")
plt.ylabel("Restaurants")
plt.tight_layout()
plt.savefig("visualizations/zomato/15_high_rated_price_band.png", dpi=300, bbox_inches="tight")
plt.close()


# 16. Top rated restaurants
top_rated = (
    df.sort_values(
        ["rate", "votes"],
        ascending=[False, False]
    ).head(15)
)

plt.figure(figsize=(12, 7))
sns.barplot(
    data=top_rated,
    x="rate",
    y="name"
)
plt.title("Top Rated Restaurants")
plt.xlabel("Rating")
plt.ylabel("Restaurant")
plt.tight_layout()
plt.savefig("visualizations/zomato/16_top_rated_restaurants.png", dpi=300, bbox_inches="tight")
plt.close()


# 17. Most voted restaurants
top_voted = (
    df.sort_values(
        "votes",
        ascending=False
    ).head(15)
)

plt.figure(figsize=(12, 7))
sns.barplot(
    data=top_voted,
    x="votes",
    y="name"
)
plt.title("Top 15 Restaurants by Votes")
plt.xlabel("Votes")
plt.ylabel("Restaurant")
plt.tight_layout()
plt.savefig("visualizations/zomato/17_most_voted_restaurants.png", dpi=300, bbox_inches="tight")
plt.close()


# 18. Rating vs votes
plt.figure(figsize=(10, 7))
sns.scatterplot(
    data=sample,
    x="votes",
    y="rate",
    alpha=0.5
)
plt.title("Restaurant Rating vs Number of Votes")
plt.xlabel("Votes")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("visualizations/zomato/18_rating_vs_votes.png", dpi=300, bbox_inches="tight")
plt.close()


# 19. Cost vs votes
plt.figure(figsize=(10, 7))
sns.scatterplot(
    data=sample,
    x="cost_for_two",
    y="votes",
    alpha=0.5
)
plt.title("Cost vs Number of Votes")
plt.xlabel("Cost for Two")
plt.ylabel("Votes")
plt.tight_layout()
plt.savefig("visualizations/zomato/19_cost_vs_votes.png", dpi=300, bbox_inches="tight")
plt.close()


# 20. Correlation heatmap
numeric_cols = [
    "rate",
    "cost_for_two",
    "votes"
]

plt.figure(figsize=(8, 6))
sns.heatmap(
    df[numeric_cols].corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)
plt.title("Zomato Correlation Heatmap")
plt.tight_layout()
plt.savefig("visualizations/zomato/20_correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.close()