file = open('input.txt', 'r') # read lines
input = file.readlines()
rows = list([row[:-1] for row in input])
rope_length = 2
rope = [[0,0] for x in range(0, rope_length)] 

t_pos_list = [[0,0]]
head = []
tail = []

for row in rows:
    dir = row.split(' ')[0]
    dist = int(row.split(' ')[1])
    print('Command: ' + str(row))
    print('Starting Rope: ' + str(rope))
    for x in range(0,dist):
        ## main thing missing for part 2 is accounting for when dist != rope length. current syntax asusme whole rope moves every time.
       
        for n in range(0, rope_length-1):
            
                head.append(rope[n][:])
                tail.append(rope[n+1][:])
            
                if dir == 'U':
                    rope[n][1]+=1
                elif dir == 'D':
                    rope[n][1]-=1
                elif dir == 'R':
                    rope[n][0]+=1
                elif dir == 'L':
                    rope[n][0]-=1
            
                y_dif = abs(rope[n+1][1] - rope[n][1])
                x_dif = abs(rope[n+1][0] - rope[n][0])
                if ((x_dif >= 2) | (y_dif >= 2)):
                    new_tail = rope[n+1][:]
                    rope[n+1] = head[0]

                    """
                    new_y_dif = abs(new_tail[1] - rope[n+1][1])
                    new_x_dif = abs(new_tail[0] - rope[n+1][0])
                    
                    if ((new_y_dif >= 2) | (new_x_dif >= 2)):
                        rope[n+1] = new_tail
                    """   

                    print('New Tail: ' + str(rope[n+1]))

                    if list(rope[n+1]) not in t_pos_list:
                        t_pos_list.append(rope[n+1])
                else:
                    rope[n+1] = tail[0]
                    print('No Tail Movement')

                head.pop(0)
                tail.pop(0)
            
           

print('Answer: ' + str(len(t_pos_list)))   
    
            

        
        
   

