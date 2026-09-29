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

<img src="visualizations/ipl/01_team_win_percentage.png" width="200">

<img src="visualizations/ipl/02_matches_per_season.png" width="200">

<img src="visualizations/ipl/03_toss_decision_pie.png" width="200">

<img src="visualizations/ipl/04_toss_impact.png" width="200">

<img src="visualizations/ipl/05_player_of_match.png" width="200">

<img src="visualizations/ipl/06_top_run_scorers.png" width="200">

<img src="visualizations/ipl/07_top_wicket_takers.png" width="200">

<img src="visualizations/ipl/08_top_venues.png" width="200">

<img src="visualizations/ipl/09_matches_by_team.png" width="200">

<img src="visualizations/ipl/10_team_wins.png" width="200">

<img src="visualizations/ipl/11_toss_by_season.png" width="200">

<img src="visualizations/ipl/12_team_season_trend.png" width="200">

<img src="visualizations/ipl/13_batter_run_distribution.png" width="200">

<img src="visualizations/ipl/14_dismissal_types.png" width="200">

<img src="visualizations/ipl/15_correlation_heatmap.png" width="200">

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

## Focus Areas

**Team Performance · Player Statistics · Batting · Bowling · Match Outcomes · Toss Analysis · Venue Analysis · Season Trends**
