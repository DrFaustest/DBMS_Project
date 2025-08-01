
# Application Description

**Application Scenario: Human Resources (HR) Portal**
    
    This project implements a comprehensive HR portal for a large organization. The portal manages a wide range of HR-related data, including Employees, Trainers, Organizations, Teams, Projects, Payroll, Performance, Employment Data, Records, Disciplinary Actions, and Performance Reviews. The system is designed to support complex queries and reporting, making it suitable for both day-to-day HR operations and strategic decision-making.
    
**Data Stored:**
    - Employee personal and employment details
    - Trainer profiles and training sessions
    - Organizational structure (departments, teams, projects)
    - Payroll and compensation records
    - Performance reviews and disciplinary actions
    - Employment history and records
    - Team assignments and project participation
    
**Expected Query Types:**
    - Retrieve employee details, team memberships, and project assignments
    - Aggregate payroll data by department or project
    - List employees with recent performance reviews or disciplinary actions
    - Find trainers and their training sessions
    - Generate reports on team performance, project staffing, or organizational structure
    - Nested queries for identifying top performers, employees with no disciplinary actions, or those eligible for promotion
    - Set operations to compare employees across teams or projects
    
**E-R Diagram and Modeling Decisions:**
    - The E-R diagram will include entities such as Employee, Trainer (specialization of Employee), Team, Project, Department, Payroll, PerformanceReview, DisciplinaryAction, and Organization.
    - Relationships will capture team assignments, project participation, reporting structure, and training sessions.
    - Weak entities (e.g., PerformanceReview, DisciplinaryAction) will be modeled with identifying relationships to Employee.
    - Specialization/generalization will be used for Employee/Trainer roles.
    - Participation constraints and mapping cardinalities will be explicitly shown (e.g., each employee must belong to at least one team, but can participate in multiple projects).
    
**Correspondence Between E-R Model and Relational Model:**
    - Each strong entity becomes a table with a primary key (e.g., EmployeeID, TeamID).
    - Weak entities use composite keys or foreign keys referencing their owner entity (e.g., PerformanceReviewID + EmployeeID).
    - Mapping cardinalities are enforced via foreign keys and, where necessary, junction tables (e.g., EmployeeTeam for many-to-many relationships).
    - Participation constraints are enforced using NOT NULL and foreign key constraints.
    - Specialization is implemented using either table-per-hierarchy or table-per-subclass approaches (e.g., Trainer table with EmployeeID as FK/PK).
    - All E-R features are mapped to relational constructs, with comments in the SQL DDL explaining each mapping decision.

# Summary

## Project File Roles

- `table_creation.py`: Initializes the SQLite database (`hr_portal.db`) and creates all tables using SQL DDL statements. Run this file first to set up the schema.
- `data_insertion.py`: Populates the database with sample data for all tables. Run after `table_creation.py` to insert realistic data for testing and queries.
- `query.sql`: Contains 25+ diverse SQL queries (with comments) that demonstrate constraints, joins, aggregation, set operations, nested queries, and DML (insert, update, delete). Can be run in bulk or one-by-one for analysis and grading.
- `main.py`: Python script that connects to the database, runs 5 key queries, and prints formatted results to the console. Demonstrates programmatic access and reporting.
- `requirments.txt`: Lists required Python packages (e.g., `sqlite3` is part of the standard library, but this file can be expanded for other dependencies).
- `DBML.txt`: Contains the schema in DBML format for use with dbdiagram.io to visualize the ERD.

## How to Spin Up the Database from Scratch

1. (Optional) Create and activate a Python virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```
2. Run the schema creation script:
   ```powershell
   python table_creation.py
   ```
3. Populate the database with sample data:
   ```powershell
   python data_insertion.py
   ```
4. (Optional) Run all queries and save results:
   ```powershell
   Get-Content query.sql | sqlite3 hr_portal.db | Out-File results.txt
   ```
5. Run the main Python reporting script:
   ```powershell
   python main.py
   ```

## Methods Used in Each File

- **table_creation.py**: Uses `sqlite3.connect()` and `cursor.executescript()` to execute a multi-statement SQL string that defines all tables, primary keys, and foreign keys.
- **data_insertion.py**: Uses `cursor.executemany()` to efficiently insert multiple rows into each table, with data generated programmatically for realistic structure and relationships.
- **query.sql**: Contains SQL statements with comments. Demonstrates a wide range of SQL features, including constraints, joins, aggregation, set operations, nested queries, and DML operations. Can be run in SQLite CLI or piped to a file.
- **main.py**: Uses `sqlite3.connect()` and `cursor.execute()` to run hard-coded queries, fetches results, and prints them in a formatted table for easy reading. No user input is required; all queries are hard-coded for demonstration.
- **DBML.txt**: Provides a DBML schema for ERD visualization at dbdiagram.io.

This structure ensures the project is easy to set up, test, and grade, and demonstrates a full range of SQL and Python database skills.