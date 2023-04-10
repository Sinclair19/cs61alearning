SELECT Name FROM records WHERE Supervisor = 'Oliver Warbucks';
SELECT * FROM records WHERE Name = Supervisor;
SELECT Name FROM records WHERE Salary > 50000 ORDER BY Name;

SELECT m.Day, m.Time FROM meetings AS m, records AS r 
        WHERE m.Division = r.Division AND r.Supervisor = 'Oliver Warbucks';

SELECT a.Name, b.Name FROM meetings AS a, meetings AS b 
        WHERE a.Name > b.Name AND a.Day = b.Day AND a.Time = b.Time;

SELECT a.Name FROM records AS a, records AS b 
        WHERE a.Supervisor = b.Name AND a.Division != b.Division;

SELECT a.Supervisor, SUM(a.Salary) FROM records AS a GROUP BY a.Supervisor;

SELECT m.Day FROM meetings AS m, records AS r 
        WHERE r.Division = m.Division GROUP BY m.Day HAVING COUNT(*) < 5;

SELECT a.Division, a.Name, b.Name FROM records AS a, records AS b 
        WHERE a.Name < b.Name AND a.Division = b.Division 
        GROUP BY a.Division HAVING SUM(a.Salary + b.Salary) < 100000;

CREATE TABLE num_taught AS
    SELECT professor, course, COUNT(*) AS times FROM course GROUP BY professor, course;

SELECT a.Professor, b.professor, a.course FROM num_taught AS a, num_taught AS b 
        WHERE a.professor < b.professor AND a.course = b.course AND a.times = b.times;

SELECT a.professor, b.professor FROM course AS a, course AS b 
        WHERE a.professor < b.professor AND a.semester = b.semester 
        GROUP BY a.course, a.professor, b.professor HAVING COUNT(*) > 1;