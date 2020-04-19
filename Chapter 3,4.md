# Chapter 3
1. Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update.
2. The code in a function executes when the function is called, not when the function is defined.
3. The def statement defines (that is, creates) a function.
4. A function consists of the def statement and the code in its def clause. A function call is what moves the program execution into the function, and the function call evaluates to the function's return value. 
5. There is one global scope, and a local scope is created whenever a function is called.
6. When a function returns, the local scope is detroyed, and all the variables in it are forgotten. 
7. A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.
8. If there is no return statement for a function, its return value is None.
9. A global statement will force a variable in a function to refer to the global variable 
10. The data type of None is NoneType. 
11. That import statement imports a module named areallyourpetsnamederic. (This is not a real module)
12. THis function can be called with spam.bacon().
13. Place the line of code that might cause an error in a try clause.
14. The code that could potentially cause an error goes in the try clause. The code that executes if an error happens goes in the except clause.
# Chapter 4
1. The empty list value, which is a list value that contains no items. This is similar to how''is the empty string value.
2.spam[2]='hello'
3. 'd' 
4. 'd'
5. ['a'.'b']
6.1
7.[3.14,'cat',11,'cat',True,99]
8.[3.14,11,'cat',True,99]
9.The operator for list conccatenation is +, while the operator for replication is*.
10.While append() will add values only to the end of a list, insert() can add them anywhere in the list.
11.The del statement and the remove() list method are two ways to remove values from a list.
12. Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not on operators.
13. Lists are mutable; they can have values added,removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, (and), while lists use the square brackets,[and].
14. (42,)
15.The tuple() and list() functions, respectively
16. They contain references to list values.
The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy()function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.
