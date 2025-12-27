# Database Testing – Library Management System (MySQL)

Simple **database testing** project demonstrating SQL queries used in QA to validate data and business rules in a library system.

*All data is fictional and created for testing purposes.*

## Why this theme?
This project validates loans, returns, overdue books, and rules like "maximum active loans per member".

## Structure
- `members` – library members
- `books` – available books
- `loans` – loan records and returns

## How to use
1. Run `schema.sql` to create tables.
2. Run `sample_data.sql` to insert test data.
3. Run queries in `test_queries.sql` to see QA validations.

## Tests included
- Overdue loans detection
- Members with multiple active loans
- Currently loaned books
- Most popular book
- Available books

## Skills Demonstrated
- SQL queries (SELECT, JOIN, GROUP BY, COUNT)
- Data validation and business rule testing
- Database design basics
- QA mindset for backend testing
## Query Results Examples

### Total Loans per Month in 2025
![Total Loans per Month](total_loans.png)

### Overdue Loans Detection
![Overdue Loans](overdue_loans.png)

### Available Books for Loan
![Available Books](available_books.png)

