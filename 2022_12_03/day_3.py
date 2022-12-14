file = open('input.txt', 'r') # read lines
lines = file.readlines()
lines = [line[:-1] for line in lines]

alphabet = "abcdefghijklmnopqrstuvwxyz"
priority = {} ## use dictionary constructor
total_score = 0

for x in range(0,26):
    priority[alphabet[x].lower()] = x+1 
    priority[alphabet[x].upper()] = x+27

## Part 1
for line in lines:    
    cmp_1, cmp_2 = line[:len(line)//2], line[len(line)//2:]
    for letter in set(cmp_1):
        if letter in set(cmp_2):
            total_score+=priority[letter]
         
## Part 2
line_count = 0
elf_group = []
new_total_score = 0

for line in lines:    
    
    elf_group.append(line)
    line_count+=1 
    if line_count % 3 == 0:
        for letter in set(elf_group[0]):
            if (letter in set(elf_group[1])) & (letter in set(elf_group[2])):
                new_total_score+=priority[letter]
        elf_group = []


print('Part 1 Total Score: ' + str(total_score))
print('Part 2 Total Score: ' + str(new_total_score))