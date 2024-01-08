# Write your MySQL query statement below
select student_id , course_id ,grade 
from
(
    SELECT 
      student_id, 
      course_id, 
      grade, 
      DENSE_RANK() OVER (
        PARTITION BY student_id 
        ORDER BY 
          grade DESC, 
          course_id ASC
      ) as rnk
from Enrollments
    ) as ranked
where rnk = 1
 order by student_id 