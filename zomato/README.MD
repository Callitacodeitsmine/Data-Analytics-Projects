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

<table>
<tr>
<td><img src="./docs/images/01.png" width="100%"></td>
<td><img src="./docs/images/02.png" width="100%"></td>
</tr>
<tr>
<td><img src="./docs/images/03.png" width="100%"></td>
<td><img src="./docs/images/04.png" width="100%"></td>
</tr>
<tr>
<td><img src="./docs/images/05.png" width="100%"></td>
<td><img src="./docs/images/06.png" width="100%"></td>
</tr>
<tr>
<td><img src="./docs/images/07.png" width="100%"></td>
<td><img src="./docs/images/08.png" width="100%"></td>
</tr>
<tr>
<td><img src="./docs/images/09.png" width="100%"></td>
<td><img src="./docs/images/10.png" width="100%"></td>
</tr>
<tr>
<td><img src="./docs/images/11.png" width="100%"></td>
<td><img src="./docs/images/12.png" width="100%"></td>
</tr>
<tr>
<td><img src="./docs/images/13.png" width="100%"></td>
<td><img src="./docs/images/14.png" width="100%"></td>
</tr>
<tr>
<td><img src="./docs/images/15.png" width="100%"></td>
<td><img src="./docs/images/16.png" width="100%"></td>
</tr>
<tr>
<td><img src="./docs/images/17.png" width="100%"></td>
<td><img src="./docs/images/18.png" width="100%"></td>
</tr>
<tr>
<td><img src="./docs/images/19.png" width="100%"></td>
<td><img src="./docs/images/20.png" width="100%"></td>
</tr>
</table>

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

## Project Structure

```text
zomato/
├── README.md
├── analysis.py
├── queries.sql
├── zomato.csv
└── docs/
    └── images/
        ├── 01.png
        ├── 02.png
        ├── ...
        └── 20.png
```

## Focus Areas

**Restaurant Ratings · Pricing · Cuisines · Locations · Customer Votes · Online Ordering · Table Booking · Restaurant Performance**
