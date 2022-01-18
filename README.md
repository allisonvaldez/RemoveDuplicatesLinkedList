# Coding Practice: Remove Duplicates From Linked List
This project is meant for me to practice coding interview questions with Python.
I am presented with the following task: Given the head node for a 
Singly Linked List with the values sorted in ascending order. Write a function 
that returns a modified version of the Linked List that does not contain any 
nodes with duplicate values. It should be modified in place (a brand-new 
list should not be created), and the modified Linked List should still have 
its nodes sorted in ascending values.

Important Background Information:
Each linked_list node should have an integer value as well as a next node 
pointing to the next node in the list or to None/null if it is the tail of 
the list.

Sample Input:
linked_list = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 (head node is 1)

Sample Output:
1 -> 3 -> 4 -> 5 -> 6 (head node is 1)

The arrays are noted as follows:
competitions = [homeTeam, awayTeam]
results = results[i], is defaulted to keep account of the homeTeam's wins (1 
if win and 0 if lost). A team will only advice if they win.

Sample output: 
competitions = [
["teamOne", "teamTwo",
"teamTwo", "teamThree",
"teamThree", "teamOne""]
]
results = [0,0,1]
Returns: teamThree (as the winner)

It should be read as follows: 
1. teamTwo won against teamOne
2. teamThree won against teamTwo
3. teamThree won against teamOne


## Running The Project
**NOTE: Your IDE may configure the project implicitly as a module. BE SURE TO 
RUN STEP 4 BELOW BEFORE SUBMITTING LABS** 

1. Download and install Python on your computer
2. Navigate to the [TournamentWinner.Mod1]() directory
3. Run the program as a module: `python -m Mod1 -h`. This will print the help 
   message.
4. Run the program as a module (with real inputs): `python -m Mod1`
   a. IE: `python -m Mod1`

The program's output will be displayed in the output.txt file.

### Mod1 Usage:

```commandline
usage: python -m Mod1 [-h] 

optional arguments:
  -h, --help  show a help message and exits the program
```

Usage statements are very formalized

| Symbol    | Meaning   |
| ---           | ---       |
| [var]         | variable var is optional. |
| var           | variable var is required. All positional arguments are required.|
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values |
| *             | This argument consumes 0 or more values |

### Project Layout

The following was my project's package layout:

* TournamentWinner.Mod1/: `The parent or "root" folder containing all of the 
  projecs files`
    * README.md:
      `The README files that describes my programs and the nuances needed 
      to run the program`
    * Mod1/: 
      `The module of my program (per requirement).`
      * __init__.py 
        `This python file details critical functions, variables, and 
        classes that are exposed when scripts import the Lab1 module.`
      * __main__.py 
        `The starting point when the program runs, it handles command line 
        arguments.`
      * *.py 
        `Holds the scripts that perform the code.`