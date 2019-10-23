import numpy as np
s1=raw_input("Enter the first string :")
s2=raw_input("Enter the second string :")

rows = len(s1)+1
cols = len(s2)+1
dist = [[0 for x in range(cols)] for x in range(rows)]

for i in range(1, rows):
    dist[i][0] = i

for i in range(1, cols):
    dist[0][i] = i

print "\nThe matrix before population is : \n", np.array(dist)

for col in range(1, cols):
    for row in range(1, rows):
        if s1[row-1] == s2[col-1]:
            cost = 0
        else:
            cost = 1
        dist[row][col] = min(dist[row-1][col] + 1,      # deletion
                             dist[row][col-1] + 1,      # insertion
                             dist[row-1][col-1] + cost) # substitution

print "\nThe matrix after population is : \n", np.array(dist)
print "\nThe edit distance to modify "+s1+" to "+s2+" is :"+str(dist[row][col])

"""
[00 01 02 03]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
"""