# Flipkart E-Commerce Analytics

An exploratory data analysis project focused on understanding **e-commerce product performance, pricing, ratings, reviews, categories, and customer engagement** using Python and SQL.

---

## Overview

This project analyzes Flipkart product data to identify patterns and relationships across products, categories, prices, ratings, reviews, and other available attributes.

The analysis combines **Python-based exploratory analysis, SQL querying, and data visualization** to turn raw e-commerce data into meaningful insights.

## Objectives

* Analyze product and category performance
* Explore pricing and discount patterns
* Examine product ratings and reviews
* Identify patterns in customer engagement
* Compare products and categories
* Generate data-driven business insights

## Tech Stack

* **Python** — Pandas, NumPy
* **Visualization** — Matplotlib, Seaborn
* **SQL** — MySQL / PostgreSQL
* **Analysis** — Exploratory Data Analysis (EDA)

---

## Analysis Workflow

```text
Raw Data
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
SQL Analysis
   ↓
Data Visualization
   ↓
Insights
```

---

## Visual Gallery

The project contains **14 visualizations** covering different aspects of the Flipkart dataset.

<div align="center">

<img src="visualizations/flipkart/01_products_by_category.png" width="200">

<img src="visualizations/flipkart/02_average_discount_category.png" width="200">

<img src="visualizations/flipkart/03_discount_distribution.png" width="200">

<img src="visualizations/flipkart/04_retail_price_distribution.png" width="200">

<img src="visualizations/flipkart/05_discounted_price_distribution.png" width="200">

<img src="visualizations/flipkart/06_price_comparison.png" width="200">

<img src="visualizations/flipkart/07_price_vs_discount.png" width="200">

<img src="visualizations/flipkart/08_discount_boxplot.png" width="200">

<img src="visualizations/flipkart/09_price_boxplot.png" width="200">

<img src="visualizations/flipkart/10_top_discounts.png" width="200">

<img src="visualizations/flipkart/11_rating_distribution.png" width="200">

<img src="visualizations/flipkart/12_discount_vs_rating.png" width="200">

<img src="visualizations/flipkart/13_correlation_heatmap.png" width="200">

<img src="visualizations/flipkart/14_discount_pie.png" width="200">

</div>

---

## SQL Analysis

SQL queries used for the analysis are available in:

```text
queries.sql
```

The dataset can be loaded into **MySQL or PostgreSQL** and the queries can then be executed against the imported table.

---

## Run

Install the required Python packages:

```bash
pip install pandas numpy matplotlib seaborn
```

Run the analysis:

```bash
cd flipkart
python analysis.py
```

## Focus Areas

**Product Performance · Category Analysis · Pricing · Ratings · Reviews · Discounts · Customer Engagement**

---

## Dataset

The analysis uses the CSV dataset included in this project:

```text
flipkart.csv
```

---

## Key Takeaway

The project demonstrates an end-to-end workflow for analyzing e-commerce data — from **data preparation and SQL analysis to visualization and insight generation**.
