file = open('input.txt', 'r') # read lines
lines = file.readlines()
contain_count = 0
overlap_count = 0
for line in lines:
    line = line[:-1].replace('-', ',')
    part_1a, part_1b, part_2a, part_2b, = int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2]), int(line.split(',')[3]) 
    if ((part_1a >= part_2a) & (part_1a <= part_2b)) | ((part_1b >= part_2a) & (part_1b <= part_2b)) | ((part_2b >= part_1a) & (part_2b <= part_1b)) | ((part_2a >= part_1a) & (part_2a <= part_1b)) :
        overlap_count+=1
        print('Overlap: ' + str(part_1a) + ' ' + str(part_1b) + ' ' + str(part_2a) + ' ' + str(part_2b))
    if ((part_1a >= part_2a) & (part_1b <= part_2b)) | ((part_2a >= part_1a) & (part_2b <= part_1b)): 
        contain_count+=1
        print('Contain: ' + str(part_1a) + ' ' + str(part_1b) + ' ' + str(part_2a) + ' ' + str(part_2b))

print('Contain Match Count: ' + str(contain_count))
print('Overlap Match Count: ' + str(overlap_count))