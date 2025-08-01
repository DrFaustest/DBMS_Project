import sqlite3

def insert_sample_data(db_path="hr_portal.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()


    # Insert Organizations
    orgs = [(1, 'Acme Corp'), (2, 'Beta Inc')]
    cursor.executemany("INSERT INTO Organization (OrganizationID, Name) VALUES (?, ?)", orgs)

    # Insert Departments
    departments = []
    dept_names = ['HR', 'Engineering', 'Sales', 'Marketing']
    dept_id = 1
    for org_id in [1, 2]:
        for name in dept_names:
            departments.append((dept_id, f"{name} {org_id}", org_id))
            dept_id += 1
    cursor.executemany("INSERT INTO Department (DepartmentID, Name, OrganizationID) VALUES (?, ?, ?)", departments)

    # Insert Employees
    employees = []
    emp_id = 1
    for dept in departments:
        for i in range(5):
            fname = f"Emp{emp_id}"
            lname = f"Last{emp_id}"
            hire_date = f"2023-01-{(i+1):02d}"
            email = f"emp{emp_id}@org{dept[2]}.com"
            employees.append((emp_id, fname, lname, dept[0], hire_date, email))
            emp_id += 1
    cursor.executemany("INSERT INTO Employee (EmployeeID, FirstName, LastName, DepartmentID, HireDate, Email) VALUES (?, ?, ?, ?, ?, ?)", employees)

    # Insert Trainers (every 10th employee is a trainer)
    trainers = []
    for i in range(1, emp_id):
        if i % 10 == 0:
            trainers.append((i//10, i, f"Specialty {i//10}"))
    cursor.executemany("INSERT INTO Trainer (TrainerID, EmployeeID, Specialty) VALUES (?, ?, ?)", trainers)

    # Insert Projects (2 per org, assign to first 2 depts of each org)
    projects = []
    proj_id = 1
    for org_id in [1, 2]:
        org_depts = [d for d in departments if d[2] == org_id][:2]
        for i, dept in enumerate(org_depts):
            projects.append((proj_id, f"Project {org_id}-{i+1}", dept[0], f"2024-01-01", f"2027-12-31"))
            proj_id += 1
    cursor.executemany("INSERT INTO Project (ProjectID, Name, DepartmentID, StartDate, EndDate) VALUES (?, ?, ?, ?, ?)", projects)

    # Insert Teams (4 per project, assign to same dept as project)
    teams = []
    team_id = 1
    for proj in projects:
        for i in range(4):
            teams.append((team_id, f"Team {proj[0]}-{i+1}", proj[2]))
            team_id += 1
    cursor.executemany("INSERT INTO Team (TeamID, Name, DepartmentID) VALUES (?, ?, ?)", teams)

    # Insert EmployeeTeam (assign employees to teams, 5 per team)
    empteam = []
    team_idx = 0
    for t in teams:
        # Get employees from the same department as the team
        dept_emps = [e for e in employees if e[3] == t[2]]
        for i in range(5):
            empteam.append((dept_emps[i % len(dept_emps)][0], t[0]))
        team_idx += 1
    cursor.executemany("INSERT INTO EmployeeTeam (EmployeeID, TeamID) VALUES (?, ?)", empteam)

    # Insert EmployeeProject (assign each employee in the department to the project, no duplicates)
    empproj = []
    for proj in projects:
        dept_emps = [e for e in employees if e[3] == proj[2]]
        for emp in dept_emps:
            empproj.append((emp[0], proj[0]))
    cursor.executemany("INSERT INTO EmployeeProject (EmployeeID, ProjectID) VALUES (?, ?)", empproj)

    # Insert Payroll (one per employee)
    payroll = []
    for e in employees:
        payroll.append((e[0], e[0], 50000 + 1000 * (e[0] % 10), f"2024-07-01"))
    cursor.executemany("INSERT INTO Payroll (PayrollID, EmployeeID, Salary, PayDate) VALUES (?, ?, ?, ?)", payroll)

    # Insert PerformanceReview (one per employee)
    reviews = []
    for e in employees:
        reviews.append((e[0], e[0], f"2025-06-15", (e[0] % 5) + 1, f"Review for {e[1]}"))
    cursor.executemany("INSERT INTO PerformanceReview (ReviewID, EmployeeID, ReviewDate, Score, Comments) VALUES (?, ?, ?, ?, ?)", reviews)

    # Insert DisciplinaryAction (for every 8th employee)
    actions = []
    for e in employees:
        if e[0] % 8 == 0:
            actions.append((e[0], e[0], f"2025-05-10", f"Disciplinary action for {e[1]}"))
    cursor.executemany("INSERT INTO DisciplinaryAction (ActionID, EmployeeID, ActionDate, Description) VALUES (?, ?, ?, ?)", actions)

    conn.commit()
    print("Sample data inserted successfully.")
    conn.close()

if __name__ == "__main__":
    insert_sample_data()
