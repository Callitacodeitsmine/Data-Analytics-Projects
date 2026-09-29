# IPL Data Analytics

## Overview

An analytical exploration of IPL match and player data covering team performance, player statistics, batting, bowling, match outcomes, toss decisions, venues, and season-level trends.

The project uses Python and SQL to analyze structured cricket data and communicate findings through visualization.

## Objectives

* Analyze team and player performance
* Explore batting and bowling statistics
* Examine match outcomes and winning patterns
* Analyze toss decisions and outcomes
* Explore venue and season-level trends
* Compare team and player performance

## Tech Stack

* **Python** — Pandas, NumPy
* **Visualization** — Matplotlib, Seaborn
* **Database** — MySQL / PostgreSQL
* **Analysis** — Exploratory Data Analysis & SQL

## Methodology

```text
Match & Player Data
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
Performance Insights
```

## Visual Gallery

The analysis includes **15 visualizations** covering team, player, match, and performance-level analysis.

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
<td></td>
</tr>
</table>

</div>

## SQL Analysis

SQL queries are available in `queries.sql`.

Load the IPL CSV datasets into MySQL or PostgreSQL and execute the queries.

## Run

Install the required Python packages:

```bash
pip install pandas numpy matplotlib seaborn
```

Run the analysis:

```bash
cd ipl
python analysis.py
```

## Project Structure

```text
ipl/
├── README.md
├── analysis.py
├── queries.sql
├── ipl_matches.csv
├── ipl_players.csv
└── docs/
    └── images/
        ├── 01.png
        ├── 02.png
        ├── ...
        └── 15.png
```

## Focus Areas

**Team Performance · Player Statistics · Batting · Bowling · Match Outcomes · Toss Analysis · Venue Analysis · Season Trends**
