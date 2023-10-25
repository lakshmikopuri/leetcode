#Classes More Than 5 Students,Write a solution to find all the classes that have at least five students.
#Write your MySQL query statement below
select class from courses
group by class 
having count(student)>=5
