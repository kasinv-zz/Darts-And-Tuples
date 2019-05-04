"""
Moves pokemon from the given position the specified number of steps in the
specified direction
Not allowed to go outside the border (below 0 or past 150)
"""
def move_pokemon(position, direction, steps):
    if direction.lower() == 'n':
        position = (int(position[0] - steps), position[1])
        if position[0] < 0:
            position = (0, position[1])
        return position
    elif direction.lower() == 's':
        position = (int(position[0] + steps), position[1])
        if position[0] > 150:
            position = (150, position[1])
        return position 
    elif direction.lower() == 'e':
        position = (position[0], int(position[1] + steps))
        if position[1] > 150:
            position = (position[0], 150)
        return position
    elif direction.lower() == 'w':
        position = (position[0], int(position[1] - steps))
        if position[1] < 0:
            position = (position[0], 0)
        return position
    else:
        return position

#sets starting position into a tuple  
row = 75
column = 75
position = (row, column) 

#asks the user for information about the game details they would like
num_turns = int(input("How many turns? => "))
print(num_turns)

pname = input("What is the name of your pikachu? => ")
print(pname)

pturns = int(input("How often do we see a Pokemon (turns)? => "))
print(pturns)

psteps = 5

print()
print("Starting simulation, turn 1", pname, "at", position)

"""
Asks user for direction to move pokemon, calculates new position
After specified number of turns, displays number of turns passed and position of
pokemon. Asks user what type of pokemon to face. 
Records wins/losses/no pokemon and new position given result of battle
"""
record = [] 
turns = 0
i = 0
while i < num_turns: 
    direction = input("What direction does " + pname + " walk? => ")
    print(direction)
    pdirection = direction.lower()
    position = move_pokemon(position, pdirection, psteps)
    i += 1
    turns += 1
    if turns % pturns == 0:
        print("Turn " + str(turns) + ",", pname, "at", position)
        ptype = input("What type of pokemon do you meet (W)ater, (G)round? => ")
        print(ptype)
        if ptype.lower() == 'w':
            position = move_pokemon(position, pdirection, 1)
            print(pname, "wins and moves to", position)
            record.append('Win')
        elif ptype.lower() == 'g':
            position = move_pokemon(position, pdirection, -10)
            print(pname, "runs away to", position)
            record.append('Lose')
        else:
            record.append('No Pokemon')
            
#final position and total record versus other pokemon       
print(pname, "ends up at " + str(position) + ", Record:", record)