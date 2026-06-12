SELECT * FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

SELECT strftime('%Y-%m', date) AS month,
AVG(nav)
FROM fact_nav
GROUP BY month;

SELECT state,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state;

SELECT *
FROM dim_fund
WHERE expense_ratio_pct < 1;

SELECT category,
COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category;

SELECT fund_house,
COUNT(*) AS schemes
FROM dim_fund
GROUP BY fund_house;

SELECT MAX(nav)
FROM fact_nav;

SELECT MIN(nav)
FROM fact_nav;

SELECT AVG(amount)
FROM fact_transactions;

SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;