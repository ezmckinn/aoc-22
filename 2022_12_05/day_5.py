file = open('input.txt', 'r') # read lines
lines = file.readlines()
#clean up lines
lines = [line[:-1] for line in lines]
# set up container
stacks = {int(x):[] for x in lines[8] if x != ' '}

# build stacks into dictionary
for line in lines[0:8]:
    for y in range(1,len(line)):
        if ((line[y] != ' ') & (line[y] != '[') & (line[y] != ']')):
            stacks[int(lines[8][y])].append(line[y])
#reverse each list in dictionary so that "top" box is last 
for key in stacks:
    stacks[key].reverse()
line_count = 10
#execute re-arrange
for line in lines[10:]:
   # print('Working on line: ' + str(line_count))
    instructions = line.split(' ') #split line
    num_to_move = int(instructions[1]) # get number tomove 
    from_stack = int(instructions[3]) # get source 
    to_stack = int(instructions[5]) # get destination
    cargo = stacks[from_stack][-num_to_move:] # get cargo from end of list
    cargo.reverse() # reverse it for part 1 so you can append it to the next list in right order
    for box in cargo: 
        stacks[to_stack].append(box) #append it
    stacks[from_stack] = stacks[from_stack][:-num_to_move] #remove from earlier list.
    line_count+=1

#print(stacks)

ans = ''
for x in range(1,10): 
    ans+=stacks[x][-1]

print(ans)
#print answer


