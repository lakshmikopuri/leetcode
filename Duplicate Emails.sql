# Duplicate Emails
select email AS Email
from Person 
group by email having count(email) >1
