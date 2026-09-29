-- table: flipkart(product, category, mrp, price, rating)
SELECT category, ROUND(AVG(price)) AS avg_price, ROUND(AVG((mrp-price)*100.0/mrp),1) AS avg_discount_pct FROM flipkart GROUP BY category;
SELECT product, category, ROUND((mrp-price)*100.0/mrp,1) AS discount_pct, rating FROM flipkart ORDER BY discount_pct DESC LIMIT 10;
SELECT COUNT(*) AS risky_deals FROM flipkart WHERE (mrp-price)*100.0/mrp > 50 AND rating < 3.5;
SELECT category, product, price, rating FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY category ORDER BY (mrp-price)/mrp DESC, rating DESC) rn FROM flipkart) t WHERE rn<=3;
