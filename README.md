[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5388051&assignment_repo_type=AssignmentRepo)
# Exercise 4.29 Sporting statistics

In this exercise, we'll be working with files stored in CSV format. Each line of the file contains the home team, visiting team, home team points, and visiting team points, all separated by commas.

You can see an example below of the file's contents. The file shown below is also included in the exercise template with the name "data.csv".

```plaintext
ENCE,Vitality,9,16
ENCE,Vitality,16,12
ENCE,Vitality,9,16
ENCE,Heroic,10,16
SJ,ENCE,0,16
SJ,ENCE,3,16
FURIA,NRG,7,16
FURIA,Prospects,16,1
```

Write a program that prompts the user for a filename, after which it reads the match statistics from the file. The program then prompts the user for the name of a team, and prints the data specified in the following parts for that team.

## Games Played

Implement the ability to output the number of games played by any given team. We're using the above-mentioned **data.csv** file.

```plaintext
File:
**data.csv**
Team:
**FURIA**
Games: 2
```

```plaintext
File:
**data.csv**
Team:
**ENCE**
Games: 6
```

## Wins and Losses

Extend the program so that it has the ability to print the number of wins and losses of a given team. The winner of a game is the team that has gained more points from it.

You may assume that the games cannot be tied. Below, we're using the above-mentioned **data.csv** file.

```plaintext
File:
**data.csv**
Team:
**FURIA**
Games: 2
Wins: 1
Losses: 1
```

```plaintext
File:
**data.csv**
Name:
**ENCE**
Games: 6
Wins: 3
Losses: 3
```
