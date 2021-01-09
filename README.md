# Overwatch_PUGS_Matchmake
- This program helps to matchmake the available people gathered for pugs into 2 teams
- Each team consists of 6 players each.
- Remaining players are made to spectate
- Each time the program is run, a new combination of teams is provided

### Input requirement: txt file with the name "matchup.txt"

Each line should contain 
1. The name of the player(ensure no spaces in between the full name)
2. followed by space
3. followed by their sr
```
Ironut_Gaming 3600
Adam_Saudagar 3500
Pewdiepie 9999
```
### Output

 - The program will create "teams.txt"
 - which will list the members of both teams and the spectators.
 - It will also mention the sr difference between the two teams


### Limitations
will be removed in future commits
1. If the program cannot find a combination of teams with sr difference less than 100, it will crash.