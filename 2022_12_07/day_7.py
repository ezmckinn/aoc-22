import json 
file = open('input.txt', 'r') # read lines
lines = file.readlines()
lines = [line[:-1] for line in lines]

folder = {'/': {'count': 0, 'parent': '', 'level':0}}
current_dir = ''
line_index=0

"""
Part 1
"""

for line in lines:
    #print(len('/abc/abc'.split('/')))
    if line[0] == '$':
        try:
            command = line.split(' ')[1]
        except IndexError:
            print('Index Error! Line ' + str(line_index))
        if command == 'cd':
            #print('current dir: ' + current_dir)
            #print(line)
            value = line.split(' ')[2]
            #print("value:" + value)
            if value == '/':
                path = '/'
            elif value == '..':
                if (len(current_dir.split('/')) <= 2):
                    path = '/'
                else:
                    path = ('/'.join(current_dir.split('/')[:-1]))
                #print('one level up path: ' + path)
            else:
                if current_dir == '/':
                    path = '/' + value
                else:
                    path = current_dir + '/' + value
            if path not in folder.keys():
                level = path.count('/')
                folder[path] = {'count': 0, 'parent': current_dir, 'level': level}
                #print('new directory: ' + path + ' with parent dir: ' + current_dir)          
            current_dir = path
            
        elif command == 'ls':
            for next_line in lines[line_index+1:]:
                if next_line[0] == '$':
                    break
                elif next_line.split(' ')[0] == 'dir':
                    value = next_line.split(' ')[1]
                    path = ''
                    if current_dir == '/':
                        path = '/' + value
                    else:
                        path = (current_dir + '/' + value)
                    if path not in folder.keys():
                        level = path.count('/')
                        folder[path] = {'count': 0, 'parent': current_dir, 'level': level}
                        #print('new path! ' + path)
                else:
                    #print(current_dir + ' byte count: ' + str(folder[current_dir]['count']))
                    num_bytes = int(next_line.split(' ')[0])
                    #print(next_line + ': adding ' + str(num_bytes) + ' bytes to' + current_dir)
                    folder[current_dir]['count']+=num_bytes 
                    #print(current_dir + ' byte count: ' + str(folder[current_dir]['count']))
                    pass
        else: 
            print('Error! Unknown Command: ' + command)
            break
    line_index+=1

temp_list = [{'path': key, 'parent': value['parent'], 'level': value['level'], 'count': value['count']} for key, value in folder.items()]
temp_list = sorted(temp_list, key=lambda d: d['level']) 

"""
with open("temp_list.json", "w") as outfile:
    json.dump(temp_list, outfile)
"""
for l in reversed(range(0,13)): ## count up from lowest level of pyramid
        for key in folder: ## loop through all the keys each time
            if folder[key]['level'] == l: # find objects on the right level
                parent = folder[key]['parent'] #3 get the parent
                count = folder[key]['count'] # get the bytes to add 
                if (parent in folder.keys()) & (parent != ""):
                    folder[parent]['count'] += count # add bytes to parent
                    
bytes_to_clear = 0 

for key in folder:
    if folder[key]['count'] <= 100000:
        bytes_to_clear += folder[key]['count'] 

print('Bytes to Clear for Part 1: ' + str(bytes_to_clear))

"""
Part 2:
"""
total_disk_space = 70000000
target_disk_space = 30000000

current_free_space = total_disk_space - folder['/']['count']
target_dir_size = target_disk_space - current_free_space
options = [item['count'] for item in temp_list if item['count'] >= target_dir_size]
options = sorted(options)
print('Target Dir Size for Part 2: ' + str(options[0]))
