-- 1. List all employees (demonstrates PK constraint)
-- Shows all employees with their primary key
SELECT EmployeeID, FirstName, LastName FROM Employee;

-- 2. List all employees with their department and organization (FK constraint)
-- Demonstrates foreign key relationships
SELECT e.EmployeeID, e.FirstName, e.LastName, d.Name AS Department, o.Name AS Organization
FROM Employee e
JOIN Department d ON e.DepartmentID = d.DepartmentID
JOIN Organization o ON d.OrganizationID = o.OrganizationID;

-- 3. List all unique employee emails (unique constraint)
SELECT DISTINCT Email FROM Employee;

-- 4. Employees with a specific email domain (string operation)
SELECT EmployeeID, FirstName, LastName, Email FROM Employee WHERE Email LIKE '%@org1.com';

-- 5. Departments with more than 4 employees (group by, having)
SELECT d.Name, COUNT(e.EmployeeID) AS EmployeeCount
FROM Department d
JOIN Employee e ON d.DepartmentID = e.DepartmentID
GROUP BY d.DepartmentID
HAVING COUNT(e.EmployeeID) > 4;

-- 6. Average salary per department (aggregation)
SELECT d.Name AS Department, AVG(p.Salary) AS AvgSalary
FROM Department d
JOIN Employee e ON d.DepartmentID = e.DepartmentID
JOIN Payroll p ON e.EmployeeID = p.EmployeeID
GROUP BY d.DepartmentID;

-- 7. Employees and their teams (inner join)
SELECT e.FirstName, e.LastName, t.Name AS Team
FROM Employee e
JOIN EmployeeTeam et ON e.EmployeeID = et.EmployeeID
JOIN Team t ON et.TeamID = t.TeamID;

-- 8. All employees and their teams (left outer join)
SELECT e.FirstName, e.LastName, t.Name AS Team
FROM Employee e
LEFT JOIN EmployeeTeam et ON e.EmployeeID = et.EmployeeID
LEFT JOIN Team t ON et.TeamID = t.TeamID;

-- 9. All teams and their employees (right outer join simulated with left join)
SELECT t.Name AS Team, e.FirstName, e.LastName
FROM Team t
LEFT JOIN EmployeeTeam et ON t.TeamID = et.TeamID
LEFT JOIN Employee e ON et.EmployeeID = e.EmployeeID;

-- 10. List all employees and their performance review scores (renaming/alias)
SELECT e.FirstName AS EmpFirst, e.LastName AS EmpLast, pr.Score AS ReviewScore
FROM Employee e
JOIN PerformanceReview pr ON e.EmployeeID = pr.EmployeeID;

-- 11. Employees with 'Emp1' in their name (string operation)
SELECT * FROM Employee WHERE FirstName LIKE '%Emp1%';

-- 12. Employees ordered by salary descending (order by)
SELECT e.FirstName, e.LastName, p.Salary
FROM Employee e
JOIN Payroll p ON e.EmployeeID = p.EmployeeID
ORDER BY p.Salary DESC;

-- 13. Departments with no employees (nested query: empty relation)
SELECT d.Name FROM Department d
WHERE NOT EXISTS (SELECT 1 FROM Employee e WHERE e.DepartmentID = d.DepartmentID);

-- 14. Employees who are not trainers (set difference/minus)
SELECT EmployeeID, FirstName, LastName FROM Employee
WHERE EmployeeID NOT IN (SELECT EmployeeID FROM Trainer);

-- 15. Employees who are trainers (set membership)
SELECT e.EmployeeID, e.FirstName, e.LastName
FROM Employee e
WHERE e.EmployeeID IN (SELECT EmployeeID FROM Trainer);

-- 16. Employees who are in both Project 1 and Project 2 (set intersection)
SELECT ep1.EmployeeID
FROM EmployeeProject ep1
JOIN EmployeeProject ep2 ON ep1.EmployeeID = ep2.EmployeeID
WHERE ep1.ProjectID = 1 AND ep2.ProjectID = 2;

-- 17. List all projects and the number of employees assigned (group by)
SELECT p.Name, COUNT(ep.EmployeeID) AS EmployeeCount
FROM Project p
LEFT JOIN EmployeeProject ep ON p.ProjectID = ep.ProjectID
GROUP BY p.ProjectID;

-- 18. Employees with more than one team (aggregation, having)
SELECT e.EmployeeID, e.FirstName, e.LastName, COUNT(et.TeamID) AS TeamCount
FROM Employee e
JOIN EmployeeTeam et ON e.EmployeeID = et.EmployeeID
GROUP BY e.EmployeeID
HAVING COUNT(et.TeamID) > 1;

-- 19. Employees with no disciplinary actions (nested query, absence of duplicates)
SELECT e.EmployeeID, e.FirstName, e.LastName
FROM Employee e
LEFT JOIN DisciplinaryAction da ON e.EmployeeID = da.EmployeeID
WHERE da.ActionID IS NULL;

-- 20. Insert a new employee (insertion)
INSERT INTO Employee (EmployeeID, FirstName, LastName, DepartmentID, HireDate, Email) VALUES (999, 'Test', 'User', 1, '2025-08-01', 'test.user@acme.com');

-- 21. Update an employee's email (updating)
UPDATE Employee SET Email = 'updated.email@acme.com' WHERE EmployeeID = 1;

-- 22. Delete an employee (deletion)
DELETE FROM Employee WHERE EmployeeID = 999;

-- 23. Insert all employees from department 1 into a new team (inserting from one table to another)
INSERT INTO EmployeeTeam (EmployeeID, TeamID)
SELECT EmployeeID, 1 FROM Employee WHERE DepartmentID = 1;

-- 24. List employees and their highest performance review score (nested query in FROM clause)
SELECT e.EmployeeID, e.FirstName, e.LastName, max_scores.MaxScore
FROM Employee e
JOIN (
    SELECT EmployeeID, MAX(Score) AS MaxScore
    FROM PerformanceReview
    GROUP BY EmployeeID
) AS max_scores ON e.EmployeeID = max_scores.EmployeeID;

-- 25. List all employees and their department, including departments with no employees (full outer join simulation)
SELECT d.Name AS Department, e.FirstName, e.LastName
FROM Department d
LEFT JOIN Employee e ON d.DepartmentID = e.DepartmentID
UNION
SELECT d.Name AS Department, e.FirstName, e.LastName
FROM Employee e
LEFT JOIN Department d ON e.DepartmentID = d.DepartmentID;

-- 1. Total number of employees per organization
SELECT o.Name AS Organization, COUNT(e.EmployeeID) AS EmployeeCount
FROM Organization o
JOIN Department d ON o.OrganizationID = d.OrganizationID
JOIN Employee e ON d.DepartmentID = e.DepartmentID
GROUP BY o.OrganizationID;

-- 2. Average salary by department
SELECT d.Name AS Department, AVG(p.Salary) AS AvgSalary
FROM Department d
JOIN Employee e ON d.DepartmentID = e.DepartmentID
JOIN Payroll p ON e.EmployeeID = p.EmployeeID
GROUP BY d.DepartmentID;

-- 3. Number of projects per organization
SELECT o.Name AS Organization, COUNT(p.ProjectID) AS ProjectCount
FROM Organization o
JOIN Department d ON o.OrganizationID = d.OrganizationID
JOIN Project p ON d.DepartmentID = p.DepartmentID
GROUP BY o.OrganizationID;

-- 4. Number of teams per project
SELECT p.Name AS Project, COUNT(t.TeamID) AS TeamCount
FROM Project p
JOIN Team t ON p.DepartmentID = t.DepartmentID
GROUP BY p.ProjectID;

-- 5. Employees with the highest performance score in each department
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

-- 6. Number of disciplinary actions per department
SELECT d.Name AS Department, COUNT(da.ActionID) AS DisciplinaryActions
FROM Department d
JOIN Employee e ON d.DepartmentID = e.DepartmentID
LEFT JOIN DisciplinaryAction da ON e.EmployeeID = da.EmployeeID
GROUP BY d.DepartmentID;

-- 7. Average performance score by organization
SELECT o.Name AS Organization, AVG(pr.Score) AS AvgScore
FROM Organization o
JOIN Department d ON o.OrganizationID = d.OrganizationID
JOIN Employee e ON d.DepartmentID = e.DepartmentID
JOIN PerformanceReview pr ON e.EmployeeID = pr.EmployeeID
GROUP BY o.OrganizationID;

-- 8. List of trainers and the number of employees they share a department with
SELECT t.TrainerID, e.FirstName, e.LastName, d.Name AS Department, COUNT(e2.EmployeeID) AS Colleagues
FROM Trainer t
JOIN Employee e ON t.EmployeeID = e.EmployeeID
JOIN Department d ON e.DepartmentID = d.DepartmentID
JOIN Employee e2 ON d.DepartmentID = e2.DepartmentID AND e2.EmployeeID != e.EmployeeID
GROUP BY t.TrainerID;

-- 9. Number of employees per team
SELECT t.Name AS Team, COUNT(et.EmployeeID) AS EmployeeCount
FROM Team t
JOIN EmployeeTeam et ON t.TeamID = et.TeamID
GROUP BY t.TeamID;

-- 10. Employees with no disciplinary actions
SELECT e.EmployeeID, e.FirstName, e.LastName
FROM Employee e
LEFT JOIN DisciplinaryAction da ON e.EmployeeID = da.EmployeeID
WHERE da.ActionID IS NULL;
