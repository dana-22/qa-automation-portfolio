USE qa_library;

-- 1. Currently loaned books (not returned)
SELECT b.title, m.name, l.loan_date, l.due_date
FROM loans l
JOIN books b ON l.book_id = b.id
JOIN members m ON l.member_id = m.id
WHERE l.return_date IS NULL;

-- 2. Overdue loans
SELECT m.name, b.title, l.due_date, DATEDIFF(CURDATE(), l.due_date) AS days_overdue
FROM loans l
JOIN members m ON l.member_id = m.id
JOIN books b ON l.book_id = b.id
WHERE l.return_date IS NULL AND l.due_date < CURDATE();

-- 3. Members with more than 1 active loan
SELECT m.name, COUNT(l.id) AS active_loans
FROM members m
JOIN loans l ON m.id = l.member_id
WHERE l.return_date IS NULL
GROUP BY m.id, m.name
HAVING active_loans > 1;

-- 4. Most popular book
SELECT b.title, b.author, COUNT(l.id) AS total_loans
FROM books b
LEFT JOIN loans l ON b.id = l.book_id
GROUP BY b.id, b.title, b.author
ORDER BY total_loans DESC
LIMIT 1;

-- 5. Available books
SELECT title, author, available_copies FROM books WHERE available_copies > 0;

-- 6. Loans per month in 2025
SELECT MONTH(loan_date) AS month, COUNT(id) AS total_loans
FROM loans
WHERE YEAR(loan_date) = 2025
GROUP BY MONTH(loan_date)
ORDER BY month;
