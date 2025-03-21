INSERT INTO user_subscription (product_id, user_id, subscription_type, start_date, end_date) VALUES
    (5, 1, 'MONTH', date('now'), date('now', '+30 days')),
    (7, 1, 'YEAR', date('now'), date('now', '+365 days')),
    (5, 4, 'MONTH', date('now'), date('now', '+30 days')),
    (7, 4, 'YEAR', date('now'), date('now', '+365 days'));