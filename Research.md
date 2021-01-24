# Purpose
This is the documentation for the coding that I have learned in the creation of my SQLite database.

## Monster requirements.
* Characteristics: Ex- Neutral, Medium, Animal
* Skills: Ex- Acrobatics: +9, Steath: +8
* Attributes: Ex- Strength: +3, Dexterity +4 etc.
* Armor Class (AC): Ex- 19
* Fortitude: Ex- +8
* Reflex: Ex- +11
* Will: Ex- +6
* Hit Points: Ex- 26
* Speed: Ex 20 feet, climb - 20 feet
* Attacks: Ex Melee: fangs (put text info here),
                     coil....

[Example monster here](https://2e.aonprd.com/Monsters.aspx?ID=799)

## Tables
Each table has rows that describe the thing.




[Example three of SQLite queries](https://repl.it/@JPNobody/CSE310SQLDBWorkshop2#main.py)


## Tuples

This is how you "add" values to tuples. You end up creating a new tuple.

```python
t = (1,2,3)
t = t + (1,)
print t
(1,2,3,1)
```


## Variables in SQL queries 

(From site https://docs.python.org/3/library/sqlite3.html)
"
Usually your SQL operations will need to use values from Python variables. You shouldn’t assemble your query using Python’s string operations because doing so is insecure; it makes your program vulnerable to an SQL injection attack (see https://xkcd.com/327/ for humorous example of what can go wrong).

Instead, use the DB-API’s parameter substitution. Put ? as a placeholder wherever you want to use a value, and then provide a tuple of values as the second argument to the cursor’s execute() method. (Other database modules may use a different placeholder, such as %s or :1.) For example:
```python
# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
```
"


# Inner Join 

ex from https://www.sqlitetutorial.net/sqlite-join/
```sql
SELECT
    l.Title, 
    r.Name
FROM
    albums l
INNER JOIN artists r ON -- r is an alias
    r.ArtistId = l.ArtistId;
```

# Other Notes
list(cursor.description) creates a list of the table column names.