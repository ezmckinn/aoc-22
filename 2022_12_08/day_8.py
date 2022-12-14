import numpy

file = open('input.txt', 'r') # read lines
input = file.readlines()
rows = [row[:-1] for row in input]

row_index = 0
tree_count = 0
max_viz_score = 0

def count_visible_trees(list, num):
    view = 0
    for tree in list:
        view+=1
        if tree >= num:
            break
    return view 
       
for row in rows:
    col_index = 0
    for num in row:
        column = [r[col_index] for r in rows]
        if (row_index == 0) | (col_index == 0) | (row_index == len(rows)-1) | (col_index == len(row)-1):
            tree_count+=1
        else:
            if all(num > c for c in column[row_index+1:]) | (all(num > c for c in column[:row_index])) | (all(num > x for x in row[:col_index])) | (all(num > x for x in row[col_index+1:])):
                tree_count+=1
        # get neighboring lists
        bottom_view = column[row_index+1:]
        top_view = list(reversed(column[:row_index]))
        left_view = list(reversed(row[:col_index]))
        right_view = row[col_index+1:]
        #multiply viz scores together
        viz_score = numpy.prod([count_visible_trees(lst, num) for lst in [bottom_view, top_view, left_view, right_view]])
        if viz_score > max_viz_score:
            max_viz_score = viz_score

        col_index+=1
        
    row_index+=1

print('Part 1 Answer: ' + str(tree_count))
print('Part 2 Answer: ' + str(max_viz_score))
"""
Consider your map; how many trees are visible from outside the grid?
A tree will only be visible if all its neighbors are shorter than it 

Approach for Part 1
For each tree 
- create a list of all the trees in the column
- create a list of all the trees in the row
if it satisfies one of these conditions:
    - greater than all the trees before or after it in the column
    - great than all of the trees before or after in its row
    - it's visible!
..

Approach for Part 2:
get a list of trees going out from each other tree.
loop through each of those lists + count up number of visible trees
multiply those visibility scores for each tree together.
Identify max score.

"""