
file = open('input.txt', 'r') # read lines
lines = file.readlines()

# clean up lines
lines = [line[:-1] for line in lines] 

# set up placeholders
new_list = []
cal_counts = []

for line in lines:
    #load values into a list...
    new_list.append(str(line))
    #until you hit a linebreak...
    if line == '':
        #sum up the lines 
        elf_sum = sum([int(x) for x in new_list[:-1]])
        cal_counts.append(elf_sum)
        new_list = []  

cal_counts.sort(reverse=True)

print(max(cal_counts))   
print(sum(cal_counts[0:3]))
        







    

