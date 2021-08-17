#Q1: Oliver Employees
#Write a query that outputs the names of employees that Oliver Warbucks directly supervises.
SELECT name FROM records 
WHERE supervisor = 'Oliver Warbucks';


#Q2: Self Supervisor
#Write a query that outputs all information about employees that supervise themselves.
SELECT * FROM records WHERE supervisor = name;


#Q3: Rich Employees
#Write a query that outputs the names of all employees with salary greater than 50,000 in alphabetical order.
SELECT name FROM records WHERE salary > 50000 ORDER BY name;


#Q4: Oliver Employee Meetings
#Write a query that outputs the meeting days and times of all employees directly supervised by Oliver Warbucks.
SELECT day, time FROM meetings JOIN records USING(division) WHERE supervisor = 'Oliver Warbucks';


#Q5: Different Division
#Write a query that outputs the names of employees whose supervisor is in a different division.
SELECT name FROM records AS a 
JOIN records AS b 
ON a.supervisor = b.name 
WHERE a.division != b.division;


#Q6: Middle Manager
#A middle manager is a person who is both supervising someone and is supervised by someone different. 
#Write a query that outputs the names of all middle managers.
SELECT DISTINCT a.supervisor FROM records AS a 
JOIN records AS b 
ON a.supervisor = b.name 
WHERE a.supervisor != b.supervisor;


#Q7: Supervisor Sum Salary
#Write a query that outputs each supervisor and the sum of salaries of all the employees they supervise
SELECT supervisor, sum(salary) FROM records 
GROUP BY supervisor;


#Q8: Num Meetings
#Write a query that outputs the days of the week for which fewer than 5 employees have a meeting. 
#You may assume no department has more than one meeting on a given day.
SELECT day FROM records JOIN meetings 
USING(division) GROUP BY day HAVING count(name) < 5;



#Q9: Rich Pairs
#Write a query that outputs all divisions for which there is more than one employee, 
#and all pairs of employees within that division that have a combined salary less than 100,000.
SELECT division FROM records AS a 
JOIN records AS b USING(division) 
WHERE a.name < b.name 
GROUP BY division 
HAVING max(a.salary+b.salary)<100000;