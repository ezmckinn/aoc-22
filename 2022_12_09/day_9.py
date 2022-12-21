
file = open('input.txt', 'r') # read lines
input = file.readlines()
rows = list([row[:-1] for row in input])
rope_length = 10 #update value to "2" for part 1 or "10" for part 2
rope = [[0,0] for x in range(0, rope_length)] #build rope

t_pos_list = []

"""
helper function to define movement of each knlot in response to next one.
"""
def find_next(dif): 
    if dif > 1:
        return dif-1
    elif dif < -1:
        return dif+1
    else:
        return dif

for row in rows:
    dir = row.split(' ')[0]
    dist = int(row.split(' ')[1])
    
    print('Starting Rope: ' + str(rope))
    print('Command: ' + str(row))

    for x in range(0,dist): 
        #first, move the head

        if dir == 'U':
            rope[0][1]+=1
        elif dir == 'D':
            rope[0][1]-=1
        elif dir == 'R':
            rope[0][0]+=1
        elif dir == 'L':
            rope[0][0]-=1   

        for n in range(1, rope_length): # next, loop through the tail
            #measure initial difference between head and next knot
            y_dif = rope[n-1][1] - rope[n][1]
            x_dif = rope[n-1][0] - rope[n][0]

            if ((abs(x_dif) < 2) & (abs(y_dif) < 2)): #if any given knot is close to the next one, stop moving tail.
                break
            elif ((abs(x_dif) > 2) | (abs(y_dif) > 2)):
                print('Error! Rope broken!') # if the head gets too far from the tail, the rope is broken.
                break
            else: 
                #measure movement
                next_y_dif = find_next(y_dif)
                next_x_dif = find_next(x_dif)
                #update position of this knot
                rope[n][0]+=next_x_dif
                rope[n][1]+=next_y_dif
                
        #once the whole rope has shifted, see if the tail is on a new spot.

        if list(rope[-1]) not in t_pos_list:
            t_pos_list.append(list(rope[-1]))                    

#print number of unique tail values.
print('Answer with rope of length {}: '.format(rope_length) + str(len(t_pos_list)))   


    
            

        
        
   

