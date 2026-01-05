# Expense Tracker CLI


## Description

This is a lightweight command-line interface (CLI) application for tracking expenses. Users can add, update, delete, list and get summaries of expenses.    

--- 

## Features
- **Add a Expense** → Create expenses with descriptions. Each expense gets a unique ID and a default `todo` status.
- **Update a Expense** → Modify the description or amount of an expense.
- **List Expense** → List all expenses, can be filtered by price inequality (<=, <, >=, >)
- **Summary** → Get a summary of either all expenses, expenses in certain month of this year, certain year or certain year and month

  ## Installation

  Can install Task Cli directly from GitHub:

  ```bash
  pip install git+https://github.com/ter-h/Expense-Tracker.git
  ```

  ## Usage

```bash
expense-tracker add -d <description> -a <amount>
```
```bash
expense_tracker update <id> [-d <description>] [-a <amount>]
```
```bash
expense_tracker delete <id>
```
```bash
expense_tracker list [-a "<op><amount>"]
```
```bash
expense_tracker summary [-y <year>] [-m <month>]
```