# Expense_Analyzer
## Overview
Python script that reads transaction data from CSV files, categorizes spending, and calculates totals by category, including income, expenses, and net balance.
## Features
- Reads CSV transaction data.
- Aggregates spending by category using dictionaries.
- Computes total spent, total earned, and net income.
- Prints a clear, formatted summary.
## Example Usage
```bash
python expense_analyzer.py
```
CSV example:  
```csv
date,description,amount,category
2026-01-01,Starbucks,-5.75,food
2026-01-02,Chick-fil-A,-12.40,food
2026-01-03,Amazon Purchase,-45.99,shopping
2026-01-05,Rent Payment,-850.00,rent
2026-01-06,Spotify Subscription,-9.99,entertainment
2026-01-08,Shell Gas Station,-38.20,transportation
2026-01-10,Paycheck,1500.00,income
2026-01-12,Walmart Groceries,-76.54,food
2026-01-15,Electric Bill,-60.00,utilities
2026-01-18,Uber,-18.25,transportation
2026-01-20,Netflix,-15.49,entertainment
2026-01-22,Target,-64.33,shopping
2026-01-25,Water Bill,-30.00,utilities
2026-01-28,Chipotle,-11.80,food
```
Output:  
```code
Spending by Category:
----------------------
rent            $-850.00
shopping        $-110.32
food            $-106.49
utilities       $-90.00
transportation  $-56.45
entertainment   $-25.48
----------------------
Total Spent: $-1238.74
Total Earned: $1500.00
----------------------
Net Income: $261.26
```
## What I Learned
- Working with Python dictionaries and file I/O.
- Aggregating and organizing real-world data.
- Printing clean summaries and tracking totals