# =========================
# IPL VISUALIZATIONS
# =========================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
os.makedirs("visualizations/ipl", exist_ok=True)

m = pd.read_csv("../data/ipl_matches.csv").drop_duplicates()
d = pd.read_csv("../data/ipl_players.csv")

matches_played = pd.concat([m.team1, m.team2]).value_counts()
wins = m.winner.value_counts()

win_pct = (
    wins / matches_played * 100
).round(1).sort_values(ascending=False)


# 1. Team win percentage
plt.figure(figsize=(12, 7))
win_pct.sort_values().plot(kind="barh")
plt.title("IPL Team Win Percentage")
plt.xlabel("Win Percentage (%)")
plt.ylabel("Team")
plt.tight_layout()
plt.savefig("visualizations/ipl/01_team_win_percentage.png", dpi=300, bbox_inches="tight")
plt.close()


# 2. Matches per season
season_matches = m.groupby("season").size()

plt.figure(figsize=(12, 6))
season_matches.plot(kind="bar")
plt.title("Number of IPL Matches by Season")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/ipl/02_matches_per_season.png", dpi=300, bbox_inches="tight")
plt.close()


# 3. Toss decision
plt.figure(figsize=(7, 7))
m.toss_decision.value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Toss Decision Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/ipl/03_toss_decision_pie.png", dpi=300, bbox_inches="tight")
plt.close()


# 4. Toss winner vs match winner
toss_result = (m.toss_winner == m.winner).value_counts()

plt.figure(figsize=(7, 7))
toss_result.plot(
    kind="pie",
    labels=["Toss Winner Lost", "Toss Winner Won"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Toss Winner vs Match Winner")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/ipl/04_toss_impact.png", dpi=300, bbox_inches="tight")
plt.close()


# 5. Player of the match
pom = m.player_of_match.value_counts().head(10)

plt.figure(figsize=(12, 6))
pom.sort_values().plot(kind="barh")
plt.title("Top 10 Player of the Match Award Winners")
plt.xlabel("Awards")
plt.ylabel("Player")
plt.tight_layout()
plt.savefig("visualizations/ipl/05_player_of_match.png", dpi=300, bbox_inches="tight")
plt.close()


# 6. Top run scorers
top_batters = (
    d.groupby("batter")
    .batsman_runs.sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_batters.sort_values().plot(kind="barh")
plt.title("Top 10 IPL Run Scorers")
plt.xlabel("Total Runs")
plt.ylabel("Batter")
plt.tight_layout()
plt.savefig("visualizations/ipl/06_top_run_scorers.png", dpi=300, bbox_inches="tight")
plt.close()


# 7. Top wicket takers
wkts = d[
    (d.is_wicket == 1)
    &
    (~d.dismissal_kind.isin([
        "run out",
        "retired hurt",
        "obstructing the field"
    ]))
]

top_bowlers = (
    wkts.groupby("bowler")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_bowlers.sort_values().plot(kind="barh")
plt.title("Top 10 IPL Wicket Takers")
plt.xlabel("Wickets")
plt.ylabel("Bowler")
plt.tight_layout()
plt.savefig("visualizations/ipl/07_top_wicket_takers.png", dpi=300, bbox_inches="tight")
plt.close()


# 8. Top venues
venues = m.venue.value_counts().head(10)

plt.figure(figsize=(12, 7))
venues.sort_values().plot(kind="barh")
plt.title("Top 10 IPL Venues by Number of Matches")
plt.xlabel("Matches")
plt.ylabel("Venue")
plt.tight_layout()
plt.savefig("visualizations/ipl/08_top_venues.png", dpi=300, bbox_inches="tight")
plt.close()


# 9. Matches by team
plt.figure(figsize=(12, 7))
matches_played.sort_values().plot(kind="barh")
plt.title("Number of Matches Played by Team")
plt.xlabel("Matches")
plt.ylabel("Team")
plt.tight_layout()
plt.savefig("visualizations/ipl/09_matches_by_team.png", dpi=300, bbox_inches="tight")
plt.close()


# 10. Team wins
plt.figure(figsize=(12, 7))
wins.sort_values().plot(kind="barh")
plt.title("Total Matches Won by Team")
plt.xlabel("Wins")
plt.ylabel("Team")
plt.tight_layout()
plt.savefig("visualizations/ipl/10_team_wins.png", dpi=300, bbox_inches="tight")
plt.close()


# 11. Toss decision by season
toss_season = pd.crosstab(m.season, m.toss_decision)

toss_season.plot(kind="bar", figsize=(12, 7))
plt.title("Toss Decisions by Season")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/ipl/11_toss_by_season.png", dpi=300, bbox_inches="tight")
plt.close()


# 12. Team season trend
teams = sorted(set(m.team1.dropna()) | set(m.team2.dropna()))
team_season = pd.DataFrame(index=sorted(m.season.unique()))

for team in teams:
    team_season[team] = (
        ((m.team1 == team) | (m.team2 == team))
        .groupby(m.season)
        .sum()
    )

team_season.plot(figsize=(14, 8), marker="o")
plt.title("Team Matches Played Across IPL Seasons")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.tight_layout()
plt.savefig("visualizations/ipl/12_team_season_trend.png", dpi=300, bbox_inches="tight")
plt.close()


# 13. Batter run distribution
batter_runs = d.groupby("batter").batsman_runs.sum()

plt.figure(figsize=(10, 6))
sns.histplot(batter_runs, bins=30, kde=True)
plt.title("Distribution of Total Runs Among Batters")
plt.xlabel("Total Runs")
plt.ylabel("Number of Batters")
plt.tight_layout()
plt.savefig("visualizations/ipl/13_batter_run_distribution.png", dpi=300, bbox_inches="tight")
plt.close()


# 14. Dismissal types
dismissals = d[d.is_wicket == 1].dismissal_kind.value_counts()

plt.figure(figsize=(10, 7))
dismissals.sort_values().plot(kind="barh")
plt.title("Distribution of Dismissal Types")
plt.xlabel("Number of Dismissals")
plt.ylabel("Dismissal Type")
plt.tight_layout()
plt.savefig("visualizations/ipl/14_dismissal_types.png", dpi=300, bbox_inches="tight")
plt.close()


# 15. Correlation heatmap
numeric = m.select_dtypes(include="number")

if len(numeric.columns) > 1:
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        numeric.corr(),
        annot=True,
        fmt=".2f",
        cmap="coolwarm"
    )
    plt.title("IPL Match Data Correlation")
    plt.tight_layout()
    plt.savefig("visualizations/ipl/15_correlation_heatmap.png", dpi=300, bbox_inches="tight")
    plt.close()