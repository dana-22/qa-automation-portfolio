USE qa_library;

-- Members
INSERT INTO members (name, email, join_date) VALUES
('Mariana Silva', 'mariana.silva@email.pt', '2024-01-10'),
('Bruno Costa', 'bruno@email.pt', '2024-03-15'),
('Diana Oliveira', 'diana@email.pt', '2024-06-20'),
('Diogo Mendes', NULL, '2024-09-01');

-- Books
INSERT INTO books (title, author, isbn, available_copies) VALUES
('O Senhor dos Anéis', 'J.R.R. Tolkien', '978-0261103252', 3),
('1984', 'George Orwell', '978-0451524935', 5),
('Dom Casmurro', 'Machado de Assis', '978-0195103083', 2),
('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', '978-0439708180', 4),
('A Revolução dos Bichos', 'George Orwell', '978-0451526342', 1);

-- Loans
INSERT INTO loans (member_id, book_id, loan_date, due_date, return_date) VALUES
(1, 1, '2025-11-01', '2025-11-15', NULL),  -- still on loan
(1, 2, '2025-12-01', '2025-12-15', NULL),  -- still on loan
(2, 3, '2025-11-20', '2025-12-10', NULL),  -- overdue
(3, 4, '2025-12-10', '2025-12-24', '2025-12-20'),  -- returned
(4, 5, '2025-12-15', '2025-12-20', NULL);  -- overdue
