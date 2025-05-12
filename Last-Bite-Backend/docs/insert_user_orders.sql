INSERT INTO user_order (user_id, cart_id, creation_date, status, billed_date, total_price, enabled) VALUES
(1, 1, '2025-03-13', 'ACTIVE', NULL, 59.99, 1),
(2, 2, '2025-03-13', 'PAYMENT_PROGRESS', NULL, 89.50, 1),
(3, 3, '2025-03-13', 'BILLED', '2025-03-14', 120.75, 0),
(4, 4, '2025-03-13', 'BILLED', '2025-03-14', 45.25, 0),
(5, 5, '2025-03-13', 'DISABLED', NULL, 67.80, 0),
(6, 6, '2025-03-13', 'ACTIVE', NULL, 99.99, 1),
(7, 7, '2025-03-13', 'PAYMENT_PROGRESS', NULL, 150.00, 1),
(8, 8, '2025-03-13', 'BILLED', '2025-03-14', 200.45, 0),
(9, 9, '2025-03-13', 'BILLED', '2025-03-14', 25.60, 0),
(10, 10, '2025-03-13', 'PAYMENT_DECLINED', NULL, 75.99, 0),
(11, 11, '2025-03-13', 'ACTIVE', NULL, 99.99, 1);
