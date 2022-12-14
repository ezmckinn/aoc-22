file = open('input.txt', 'r') # read lines
line = file.readline()
lst = []
for letter in line:
    lst.append(letter)
letter_count=4
eom_found = False
som_found = False
for letter in lst[3:]:
    last_four = lst[letter_count-4:letter_count]
    last_fourteen = lst[letter_count-14:letter_count]
    if eom_found == False:
        if len(set(last_four)) == 4:
            print('End of Message Answer: ' + str(letter_count))
            eom_found = True
    if som_found == False:
        if len(set(last_fourteen)) == 14:
            print('Start of Message Answer: ' + str(letter_count))
            som_found = True
    if eom_found & som_found:
        break
    letter_count+=1
