WITH ranked_campaigns AS (
    SELECT 
        user_id,
        rk_id,
        SUM(CASE WHEN sum > 0 THEN sum ELSE 0 END) AS total_payment,
        ROW_NUMBER() OVER (PARTITION BY user_id, date ORDER BY rk_id DESC) AS rk_rank
    FROM payment_date
    WHERE sum > 0
    GROUP BY user_id, date, rk_id
),
filtered_campaigns AS (
    SELECT 
        user_id,
        rk_id,
        total_payment
    FROM ranked_campaigns
    WHERE rk_rank = 1
),
main_campaigns AS (
    SELECT 
        user_id,
        MAX(rk_id) AS main_rk_id
    FROM advertising_companies
    WHERE is_main = 1
    GROUP BY user_id
)
SELECT 
    COALESCE(u.name, 'Company ' || u.id) AS company_name,
    SUM(p.total_payment) AS total_payment
FROM users u
LEFT JOIN filtered_campaigns p ON u.id = p.user_id
LEFT JOIN main_campaigns m ON u.id = m.user_id
WHERE u.owner_id IS NULL OR u.owner_id = ''
AND (p.rk_id = m.main_rk_id OR m.main_rk_id IS NULL)
GROUP BY company_name
ORDER BY company_name;