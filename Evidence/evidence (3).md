# Lesson 03 Evidence Pro-Forma

## Commit evidence (minimum 2)
- Commit 1 hash + message: 
!['Lesson 3 Commits'](./Images/lesson3(commits).png)
- Commit 2 hash + message:
!['Lesson 3 Commits'](./Images/lesson3(commits1).png)
- Optional Commit 3 hash + message:

## Run evidence
- Command run: python `Python-Files/lesson3_select.py`
- Terminal output pasted below: 

```
(1, 'Ava', 10)
(2, 'Isabella Usacheva', 13)
(3, 'Yuna Shin', 7)
```

## Typed-work confirmation
I got rid of everything except for name in cursor.execute and then from lesson 2 I used the cursor.execute function we learnt to inset a new student into the database.

## Prediction before run
- Query version: 
```
# Run a SELECT query to read columns from the students table
cursor.execute("SELECT id, name, year_group FROM students")
# fetchall() returna a list of all rows from the most recent query
rows = cursor.fetchall()
```
- My prediction (rows/columns or sample output):
It will return probably like

```
('Ava')
('Isabella Usacheva')
('Yuna Shin')
```

- What actually happened:
```
('Ava', )
('Isabella Usacheva', )
('Yuna Shin', )
```


## SQL/Python changes I made
- Change 1: change cursor.execute from SELECT id, name, year_group to just SELECT name
- Change 2: add cursor.execute("INSERT INTO students blah blah) to add a student into student database before the cursor.execute(SELECT) statement.
- Why these changes were mine (not just starter code):
I manually removed values because I understand. I also drew knowledge I learnt from lesson 2, which means I made the changes.

## Error and fix
- Error I hit: I hit no errors yay
- How I fixed it:

## Understanding check (answer in your own words)
1. What is the job of `SELECT`?
TO read data from the table
2. What type of value does `fetchall()` return?
fetchall() returns a list of all rows from the most recent query
3. How did your output change when you selected fewer columns?
It removed the columns that were removed and left a comma even though there's only one column being selected.

## Quality checklist
- [✔] Script runs without unhandled errors
- [✔] I included at least 2 lesson commits
- [✔] I included query output evidence
- [✔] I showed a prediction and compared it to actual output
- [✔] I made at least 2 personal changes to the starter work
- [✔] I answered all questions in my own words
