# Expenses-Manager
A table generator for expenses among a group of people 

# Instructions

- Enter Name of all the users in the transaction history first
 ``` 
Enter user name : A
Enter user name : B
Enter user name : C
Enter user name : D
```

- Enter the user that has paid and the user paid for (`User`/`All`)
```
Enter who paid (User name): A  
Enter who all has to pay (User/All): All
Amount to be paid: 10
```

- After all the payments are uploaded, hit `Enter` and the Final Transaction is produced

The table is read as follow :


Y - Axis user has to pay X- Axis user amount in (x,y) cell

```
*** Final transaction ***
+-----+-----+-----+-----+-----+
|     |   A |   B |   C |   D |
+=====+=====+=====+=====+=====+
| A   |   0 |  10 |   0 |   0 |
+-----+-----+-----+-----+-----+
| B   |   0 |   0 |   0 |   0 |
+-----+-----+-----+-----+-----+
| C   |  30 |  70 |   0 |   0 |
+-----+-----+-----+-----+-----+
| D   |  20 |  30 |  10 |   0 |
+-----+-----+-----+-----+-----+

A has to pay B - 10
C has to pay A - 30
C has to pay B - 70
D has to pay A - 20
D has to pay B - 30
D has to pay C - 10
```
