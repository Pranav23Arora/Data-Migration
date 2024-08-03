# Data Migration Tasks

This repository contains Python scripts and CSV files for four data migration tasks. These tasks demonstrate various data migration techniques using Python and Microsoft SQL Server.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Tasks Overview](#tasks-overview)
  - [Task 1: Comparing Student Data](#task-1-comparing-student-data)
  - [Task 2: Matching Students and Teachers](#task-2-matching-students-and-teachers)
  - [Task 3: Migrating Company Data](#task-3-migrating-company-data)
  - [Task 4: Joining SQL Tables](#task-4-joining-sql-tables)
- [Usage](#usage)
- [Guide](#guide)
- [Conclusion](#conclusion)
- [License](#license)

## Introduction

This repository provides Python scripts and CSV files to demonstrate data migration tasks. The tasks involve comparing and migrating data between CSV files and SQL Server tables, highlighting the practical application of data migration techniques.

## Prerequisites

- Python 3.x
- Microsoft SQL Server
- Python libraries: `pandas`, `pyodbc`

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/Pranav23Arora/Data_Migration_Pranav_Arora.git
    cd Data_Migration_Pranav_Arora
    ```

2. Install the required Python libraries:
    ```sh
    pip install pandas pyodbc
    ```

## Tasks Overview

### Task 1: Comparing Student Data

- **Description**: Compare two CSV files containing student data. One CSV file is created using Excel and the other using SQL Server.
- **Files**:
  - Python Script: `code/csv_import.py`
  - CSV Files: `CSV/stu_data.csv`, `CSV/stu_data1.csv`

### Task 2: Matching Students and Teachers

- **Description**: Compare two CSV files; one contains student data with subjects, and the other contains teacher data with sections and subjects. Find common subjects and sections.
- **Files**:
  - Python Script: `code/teacher_student.py`
  - CSV Files: `CSV/Student_database.csv`, `CSV/Teachers_Database.csv`

### Task 3: Migrating Company Data

- **Description**: Migrate data from a CSV file to SQL Server tables based on the length of business ro entities.
- **Files**:
  - Python Scripts: `code/org_Entity.py`, `code/org_Unit.py`
  - CSV File: `CSV/carrier.csv`
  - SQL Tables: `resp_org_entity`, `resp_org_unit`

### Task 4: Joining SQL Tables

- **Description**: Link `resp_org_entity` and `resp_org_unit` tables with a third table (`link`) and compare data to find matching business ro entities.
- **Files**:
  - Python Script: `code/link.py`
  - SQL Tables: `resp_org_entity`, `resp_org_unit`, `link`

## Usage

1. **Task 1**: Run the comparison script for student data:
    ```sh
    python code/csv_import.py
    ```

2. **Task 2**: Run the comparison script for students and teachers:
    ```sh
    python code/teacher_student.py
    ```

3. **Task 3**: Run the migration scripts for company data:
    ```sh
    python code/org_Entity.py
    python code/org_Unit.py
    ```

4. **Task 4**: Run the script to join SQL tables and find matching entities:
    ```sh
    python code/link.py
    ```

## Guide

All relevant screenshots, including code snippets, SQL tables, and CSV file structures, are provided in the `Guide` folder for better clarity.

## Conclusion

These tasks demonstrate the integration of Python and Microsoft SQL Server for data migration. The scripts show how to compare and migrate data between CSV files and SQL tables, highlighting key data migration techniques.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
