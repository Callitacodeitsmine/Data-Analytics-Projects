-- tables: ipl_matches(season,team1,team2,toss_winner,toss_decision,winner,home_team), ipl_players(season,player,team,runs,wickets,price_cr)
SELECT season, COUNT(*) AS matches FROM ipl_matches GROUP BY season ORDER BY season;
SELECT ROUND(100.0*SUM(CASE WHEN toss_winner=winner THEN 1 ELSE 0 END)/COUNT(*),1) AS toss_to_win_pct FROM ipl_matches;
SELECT ROUND(100.0*SUM(CASE WHEN home_team=winner THEN 1 ELSE 0 END)/COUNT(*),1) AS home_win_pct FROM ipl_matches;
SELECT winner AS team, COUNT(*) AS wins FROM ipl_matches GROUP BY winner ORDER BY wins DESC;
SELECT player, SUM(runs) AS runs, SUM(wickets) AS wickets FROM ipl_players GROUP BY player ORDER BY runs DESC LIMIT 5;
SELECT season, ROUND(AVG(price_cr),2) AS avg_price_cr FROM ipl_players GROUP BY season ORDER BY season;
