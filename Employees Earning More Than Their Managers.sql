#write a solution to find the employees who earn more than their managers
select e.name AS Employee
from Employee AS e, Employee m
where e.managerId =m.id And
e.salary > m.salary
