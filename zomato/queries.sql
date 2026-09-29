-- table: zomato(name, city, cuisine, cost_for_two, rating, votes)
SELECT city, COUNT(*) AS restaurants, ROUND(AVG(cost_for_two)) AS avg_cost, ROUND(AVG(rating),2) AS avg_rating FROM zomato GROUP BY city ORDER BY avg_cost DESC;
SELECT cuisine, SUM(votes) AS total_votes FROM zomato GROUP BY cuisine ORDER BY total_votes DESC LIMIT 5;
SELECT CASE WHEN cost_for_two<500 THEN '<500' WHEN cost_for_two<1000 THEN '500-1k' WHEN cost_for_two<2000 THEN '1k-2k' ELSE '2k+' END AS band,
       COUNT(*) AS n, ROUND(AVG(rating),2) AS avg_rating FROM zomato GROUP BY band;
SELECT name, city, rating, cost_for_two FROM zomato WHERE rating>=4.5 ORDER BY votes DESC LIMIT 10;
