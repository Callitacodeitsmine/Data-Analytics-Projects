# Zomato Restaurant Analytics

## Overview

An exploratory analysis of Zomato restaurant data focused on ratings, pricing, cuisines, locations, customer votes, online ordering, table booking, and restaurant characteristics.

The project combines Python, SQL, and visualization to uncover patterns within restaurant and customer-related data.

## Objectives

* Analyze restaurant ratings and customer engagement
* Explore pricing and cost patterns
* Identify popular cuisines and locations
* Examine online ordering and table booking
* Compare restaurant characteristics
* Extract business-oriented insights from the data

## Tech Stack

* **Python** — Pandas, NumPy
* **Visualization** — Matplotlib, Seaborn
* **Database** — MySQL / PostgreSQL
* **Analysis** — Exploratory Data Analysis & SQL

## Methodology

```text
Raw Restaurant Data
        │
        ▼
Data Cleaning & Preparation
        │
        ▼
Exploratory Data Analysis
        │
        ▼
SQL Analysis
        │
        ▼
Visualization
        │
        ▼
Business Insights
```

## Visual Gallery

The analysis includes **20 visualizations** covering restaurant, pricing, rating, cuisine, location, and customer-level analysis.

<div align="center">

<img src="zomato/01_rating_distribution.png" width="200">

<img src="zomato/02_cost_distribution.png" width="200">

<img src="zomato/03_rating_vs_cost.png" width="200">

<img src="zomato/04_rating_cost_online_order.png" width="200">

<img src="zomato/05_cost_by_location.png" width="200">

<img src="zomato/06_restaurants_by_location.png" width="200">

<img src="zomato/07_rating_by_price_band.png" width="200">

<img src="zomato/08_price_band.png" width="200">

<img src="zomato/09_price_band_pie.png" width="200">

<img src="zomato/10_online_order_pie.png" width="200">

<img src="zomato/11_online_rating.png" width="200">

<img src="zomato/12_online_rating_boxplot.png" width="200">

<img src="zomato/13_top_cuisines.png" width="200">

<img src="zomato/14_cuisine_votes.png" width="200">

<img src="zomato/15_high_rated_price_band.png" width="200">

<img src="zomato/16_top_rated_restaurants.png" width="200">

<img src="zomato/17_most_voted_restaurants.png" width="200">

<img src="zomato/18_rating_vs_votes.png" width="200">

<img src="zomato/19_cost_vs_votes.png" width="200">

<img src="zomato/20_correlation_heatmap.png" width="200">

</div>

## SQL Analysis

SQL queries are available in `queries.sql`.

Load the Zomato CSV dataset into MySQL or PostgreSQL and execute the queries.

## Run

Install the required Python packages:

```bash
pip install pandas numpy matplotlib seaborn
```

Run the analysis:

```bash
cd zomato
python analysis.py
```

## Focus Areas

**Restaurant Ratings · Pricing · Cuisines · Locations · Customer Votes · Online Ordering · Table Booking · Restaurant Performance**
