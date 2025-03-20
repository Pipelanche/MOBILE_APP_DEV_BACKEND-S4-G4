INSERT INTO cart (user_id, creation_date, status, status_date) VALUES
(1, DATE('now', '-1 day'), 'ACTIVE', DATE('now')),
(2, DATE('now', '-2 day'), 'PAYMENT_PROGRESS', DATE('now', '-1 day')),
(3, DATE('now', '-3 days'), 'BILLED', DATE('now', '-2 days')),
(4, DATE('now', '-4 days'), 'DISABLED', DATE('now', '-3 days')),
(5, DATE('now', '-5 days'), 'ACTIVE', DATE('now', '-4 days')),
(6, DATE('now', '-6 days'), 'PAYMENT_PROGRESS', DATE('now', '-5 days')),
(7, DATE('now', '-7 days'), 'BILLED', DATE('now', '-6 days')),
(8, DATE('now', '-8 days'), 'DISABLED', DATE('now', '-7 days')),
(9, DATE('now', '-9 days'), 'ACTIVE', DATE('now', '-8 days')),
(10, DATE('now', '-10 days'), 'PAYMENT_PROGRESS', DATE('now', '-9 days'));
