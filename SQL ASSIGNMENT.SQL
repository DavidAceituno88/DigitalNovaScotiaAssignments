CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(255),
    Department VARCHAR(255),
    Salary DECIMAL(10, 2),
	HireDate DATE
);

CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    Name VARCHAR(255),
    Department VARCHAR(255),
    StartDate DATE,
	EndDate DATE
);

CREATE TABLE Assignments (
    AssignmentID INT PRIMARY KEY,
    EmployeeID INT,
    ProjectID INT,
    HoursWorked DECIMAL(8, 2),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);


INSERT INTO Employees(EmployeeID, Name, Department, Salary, HireDate)
VALUES 
    (1, 'John Doe', 'Engineering', 60000, '2022-01-05'),
    (2, 'Alice Smith', 'Marketing', 55000, '2022-03-12'),
    (3, 'Bob Johnson', 'Engineering', 65000, '2023-05-20'),
	(4, 'Sarah Williams', 'HR', 50000, '2022-09-10'),
	(5, 'Michael Brown', 'Finance', 70000, '2021-11-15');


INSERT INTO Projects(ProjectID, Name, Department, StartDate, EndDate)
VALUES 
    (1, 'Website Redesign', 'Engineering', '2022-02-10', '2022-08-15'),
    (2, 'Product Launch', 'Marketing', '2021-05-20', '2021-10-30'),
    (3, 'Infrastructure Upgrade', 'Engineering', '2023-01-15', '2023-07-30'),
	(4, 'Employee Training Program', 'HR', '2022-10-01', '2023-03-31'),
    (5, 'Budget Planning', 'Finance', '2022-12-05', '2023-06-30');

INSERT INTO Assignments(AssignmentID, EmployeeID, ProjectID, HoursWorked)
VALUES 
    (1, 1, 1, 120.5),
    (2, 2, 2, 90.0),
    (3, 3, 1, 150.25),
	(4, 4, 4, 80.75),
    (5, 5, 5, 110.0);

/*Calculate the total hours worked by each employee. Retrive the name and total hours worked*/
SELECT e.Name, a.HoursWorked
FROM Employees e
JOIN Assignments a
ON e.EmployeeId = a.EmployeeId;

/*Calculate the average salary by department*/
SELECT Department, CAST(AVG(Salary) AS DECIMAL(10,2)) AS Average_Salary
FROM Employees
GROUP BY Department;

/*Calculate the maximum hours worked on each project*/

/*Retrive the names of the employees in the Engineering Department*/
SELECT Name,Department
FROM Employees
WHERE Department LIKE '%Engineering%';

/*Retrive the names of projects started after 2022*/ ***********
SELECT Name
FROM Projects
WHERE StartDate >'2022-12-31'

/*Show all assignments details where the number of hours worked exeeds 100 */
SELECT *
FROM Assignments
WHERE HoursWorked > 100;

/*Retrive employee Name along with the name of project assigned and the hours worked on each project*/
SELECT e.Name AS Employee_Name, p.Name AS Project_Name, SUM(hoursWorked) AS Total_Hours_Worked
FROM Employees e
JOIN Assignments a 
ON e.EmployeeID = a.AssignmentID
JOIN Projects p 
ON p.ProjectID = a.ProjectID
GROUP BY e.Name,p.Name;

/*Who are the top 3 employees with the highest Salary*/
SELECT TOP 3 Name, Department, Salary
FROM Employees
ORDER BY Salary DESC;

/*Retrive the names of Employees who have not been assigned to projects starting with the letter P
  and have worked more than 100 hours*/
SELECT e.Name as Employee_Name, p.Name AS Project_Name, a.HoursWorked
FROM Employees e
JOIN Assignments a
ON e.employeeId = a.employeeId
JOIN Projects p
ON p.projectId = a.projectId
WHERE p.Name NOT Like 'P%' AND a.HoursWorked > 100

/*Retrive the department names where the average salary is above the company-wide average salary*/
WITH CTE AS (
SELECT AVG(SALARY) AS avg_salary
FROM Employees)

SELECT Department, CAST(AVG(Salary) AS DECIMAL(10,2)) AS Average_Salary
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > (SELECT avg_salary FROM CTE)

/*Retrive employee name who have worked on projects that started after 2022 and  ended before 2024*/
Select e.Name, p.Name AS Project_Name , StartDate,EndDate
FROM Employees e
JOIN Assignments a
ON e.employeeId = a.employeeId
JOIN Projects p
ON p.projectId = a.projectId
WHERE p.StartDate > '2022-01-01' AND p.EndDate < '2024-01-01'

/*Retrive the names of employees whose names containt the letter 'a' and have
worked on projects where the project name starts with 'P'. Display their names along with the total
number of hours worked on those projects*/
Select e.Name AS Employee_Name, p.Name AS Project_Name , SUM(a.HoursWorked) AS Total_Hours_Worked
FROM Employees e
JOIN Assignments a
ON e.employeeId = a.employeeId
JOIN Projects p
ON p.projectId = a.projectId
WHERE e.name LIKE '%a%' AND p.name LIKE 'P%'
GROUP BY e.Name,p.Name
