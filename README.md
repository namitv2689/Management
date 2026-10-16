# School Management System

A command-line Python application for managing basic school records in a MySQL database. It supports student records, attendance, achievements, teacher records, fee structures, and a library catalogue.

## Requirements

- Python 3
- MySQL Server
- The MySQL Connector/Python package

Install the connector with:

```bash
python -m pip install mysql-connector-python
```

## Database configuration

Before running the application, configure the MySQL connection credentials in `school.py1.py`. The script connects to MySQL on `127.0.0.1` as `root`, creates a database named `school` if it does not exist, and creates the tables it uses.

## Important data warning

**The current script drops the `school` database when it exits.** This deletes all records in that database, including records that existed before the program started. Do not run the script with data you need to keep. Before using it for real records, remove or disable the `DROP DATABASE school` statement at the end of `school.py1.py`.

## Run

From the project directory, run:

```bash
python school.py1.py
```

Use the numbered menu to choose an operation. Enter `8` to exit.

## Available operations

- Add, list, and remove students
- Add and list student attendance
- Add and list student achievements
- Add and list teachers
- Add fee structures and list each class's total fee
- Add and list library books

The application is an interactive console program. Its current menu does not provide editing or deletion for attendance, achievements, teachers, fee structures, or books.

