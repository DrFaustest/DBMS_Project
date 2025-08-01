import sqlite3

def run_queries(db_path="hr_portal.db"):
    queries = [
        ("Total number of employees per organization", '''\
            SELECT o.Name AS Organization, COUNT(e.EmployeeID) AS EmployeeCount
            FROM Organization o
            JOIN Department d ON o.OrganizationID = d.OrganizationID
            JOIN Employee e ON d.DepartmentID = e.DepartmentID
            GROUP BY o.OrganizationID;
        '''),
        ("Average salary by department", '''\
            SELECT d.Name AS Department, AVG(p.Salary) AS AvgSalary
            FROM Department d
            JOIN Employee e ON d.DepartmentID = e.DepartmentID
            JOIN Payroll p ON e.EmployeeID = p.EmployeeID
            GROUP BY d.DepartmentID;
        '''),
        ("Employees with the highest performance score in each department", '''\
            SELECT d.Name AS Department, e.FirstName, e.LastName, pr.Score
            FROM Department d
            JOIN Employee e ON d.DepartmentID = e.DepartmentID
            JOIN PerformanceReview pr ON e.EmployeeID = pr.EmployeeID
            WHERE pr.Score = (
                SELECT MAX(pr2.Score)
                FROM Employee e2
                JOIN PerformanceReview pr2 ON e2.EmployeeID = pr2.EmployeeID
                WHERE e2.DepartmentID = d.DepartmentID
            );
        '''),
        ("Employees with no disciplinary actions", '''\
            SELECT e.EmployeeID, e.FirstName, e.LastName
            FROM Employee e
            LEFT JOIN DisciplinaryAction da ON e.EmployeeID = da.EmployeeID
            WHERE da.ActionID IS NULL;
        '''),
        ("Number of employees per team", '''\
            SELECT t.Name AS Team, COUNT(et.EmployeeID) AS EmployeeCount
            FROM Team t
            JOIN EmployeeTeam et ON t.TeamID = et.TeamID
            GROUP BY t.TeamID;
        ''')
    ]

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for desc, q in queries:
        print(f"\n--- {desc} ---")
        cursor.execute(q)
        rows = cursor.fetchall()
        col_names = [description[0] for description in cursor.description]
        # Calculate column widths
        col_widths = [len(col) for col in col_names]
        for row in rows:
            for i, item in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(item)))
        # Print header
        header = " | ".join(col_names[i].ljust(col_widths[i]) for i in range(len(col_names)))
        print(header)
        print("-+-".join("-" * w for w in col_widths))
        # Print rows
        for row in rows:
            print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))
    conn.close()

if __name__ == "__main__":
    run_queries()
