# Lesson 04 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message:
- Commit 2 hash + message:
- Optional Commit 3 hash + message:

## Run evidence
- Command run:
- Terminal output pasted below:

## Typed-work confirmation
- Briefly describe how you typed your changes step-by-step (including at least one pause to run and check output):

## Prediction before run
- Query version:
- My prediction (filtered rows, order, or count): The QUERY will probably produce:
```
('Ava', 10)
Total students: 3
```
- What actually happened:
```
('Ava', 10)
Total students: 3
```

## SQL/Python changes I made
- Change 1: I changed year_group value to 11 
- Change 2: Switched the order of name and year_group in the SELECT statement
- Why these changes were mine (not just starter code): I did it using my own brain and made these changes manually.

## Error and fix
- Error I hit: I hit the following error:
```
PS C:\Users\arisa.komatsu\OneDrive - NSW Department of Education\Documents\GitHub\9CT-Task-3\SQL-Tutorials-10SE> python Python-Files/lesson4_filter.py
Traceback (most recent call last):
  File "C:\Users\arisa.komatsu\OneDrive - NSW Department of Education\Documents\GitHub\9CT-Task-3\SQL-Tutorials-10SE\Python-Files\lesson4_filter.py", line 11, in <module>
    cursor.execute(
    ~~~~~~~~~~~~~~^
        "SELECT name, year_group FROM students WHERE year_group = ? ORDER BY name",
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        (year_group))
        ^^^^^^^^^^^^^
```
- How I fixed it: Figured out I wrote the code wrong and you need a comma inside the year_group bracket.

## Understanding check (answer in your own words)
1. What does `WHERE` do?
WHERE creates a parameter that filters rows.
2. Why is `?` used in the query?
Used as a placeholder to check if a specified column's value is the same as the target value in year_group.

3. What does `COUNT(*)` tell you in this lesson?
COUNT(*) counts the amount of rows in the database.

## Quality checklist
- [✔] Script runs without unhandled errors
- [✔] I included at least 2 lesson commits
- [✔] I included filtered/sorted summary evidence
- [✔] I showed a prediction and compared it to actual output
- [✔] I made at least 2 personal changes to the starter work
- [✔] I answered all questions in my own words
