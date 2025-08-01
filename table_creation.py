import sqlite3

def initialize_database(db_path="hr_portal.db"):
    schema = """
CREATE TABLE IF NOT EXISTS Organization (
OrganizationID INTEGER PRIMARY KEY,
Name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Department (
DepartmentID INTEGER PRIMARY KEY,
Name TEXT NOT NULL,
OrganizationID INTEGER NOT NULL,
FOREIGN KEY (OrganizationID) REFERENCES Organization(OrganizationID)
);

CREATE TABLE IF NOT EXISTS Employee (
EmployeeID INTEGER PRIMARY KEY,
FirstName TEXT NOT NULL,
LastName TEXT NOT NULL,
DepartmentID INTEGER NOT NULL,
HireDate TEXT NOT NULL,
Email TEXT UNIQUE,
FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

CREATE TABLE IF NOT EXISTS Trainer (
TrainerID INTEGER PRIMARY KEY,
EmployeeID INTEGER UNIQUE NOT NULL,
Specialty TEXT,
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE IF NOT EXISTS Team (
TeamID INTEGER PRIMARY KEY,
Name TEXT NOT NULL,
DepartmentID INTEGER NOT NULL,
FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

CREATE TABLE IF NOT EXISTS EmployeeTeam (
EmployeeID INTEGER NOT NULL,
TeamID INTEGER NOT NULL,
PRIMARY KEY (EmployeeID, TeamID),
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
FOREIGN KEY (TeamID) REFERENCES Team(TeamID)
);

CREATE TABLE IF NOT EXISTS Project (
ProjectID INTEGER PRIMARY KEY,
Name TEXT NOT NULL,
DepartmentID INTEGER NOT NULL,
StartDate TEXT,
EndDate TEXT,
FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

CREATE TABLE IF NOT EXISTS EmployeeProject (
EmployeeID INTEGER NOT NULL,
ProjectID INTEGER NOT NULL,
PRIMARY KEY (EmployeeID, ProjectID),
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID)
);

CREATE TABLE IF NOT EXISTS Payroll (
PayrollID INTEGER PRIMARY KEY,
EmployeeID INTEGER NOT NULL,
Salary REAL NOT NULL,
PayDate TEXT NOT NULL,
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE IF NOT EXISTS PerformanceReview (
ReviewID INTEGER PRIMARY KEY,
EmployeeID INTEGER NOT NULL,
ReviewDate TEXT NOT NULL,
Score INTEGER,
Comments TEXT,
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE IF NOT EXISTS DisciplinaryAction (
ActionID INTEGER PRIMARY KEY,
EmployeeID INTEGER NOT NULL,
ActionDate TEXT NOT NULL,
Description TEXT,
FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
"""
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        cursor.executescript(schema)
        conn.commit()
        print(f"Database initialized at {db_path}")
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_database()