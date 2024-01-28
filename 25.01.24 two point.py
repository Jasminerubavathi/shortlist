 #Consider two points,  and . We consider the inversion or point reflection, , of point  across point  to be a  rotation of point  around .

#Given  sets of points  and , find  for each pair of points and print two space-separated integers denoting the respective values of  and  on a new line.

#Function Description

#Complete the findPoint function in the editor below.

#findPoint has the following parameters:

#int px, py, qx, qy: x and y coordinates for points  and 
#Returns

#int[2]: x and y coordinates of the reflected point 
#Input Format

#The first line contains an integer, , denoting the number of sets of points.
#Each of the  subsequent lines contains four space-separated integers that describe the respective values of , , , and  defining points  and .

#Constraints

#Sample Input

2
0 0 1 1
1 1 2 2
#Sample Output

2 2
3 3
#Explanation

#The graphs below depict points , , and  for the  points given as Sample Input:

#find-point-0011.png
#find-point-1122.png
#Submissions: 149
#Max Score: 10
#Difficulty: Easy
#Rate This Challenge:

    
#More
 
1
#!/bin/python3
2
​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
​
9
#
10
# Complete the 'findPoint' function below.
11
#
12
# The function is expected to return an INTEGER_ARRAY.
13
# The function accepts following parameters:
14
#  1. INTEGER px
15
#  2. INTEGER py
16
#  3. INTEGER qx
17
#  4. INTEGER qy
18
#
19
​
20
def findPoint(px, py, qx, qy):
21
    # Write your code here
22
​
23
if __name__ == '__main__':
24
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
25
​
26
    n = int(input().strip())
27
​
28
    for n_itr in range(n):
29
        first_multiple_input = input().rstrip().split()
30
​
31
        px = int(first_multiple_input[0])
32
​
33
        py = int(first_multiple_input[1])
34
​
35
        qx = int(first_multiple_input[2])
36
​
37
        qy = int(first_multiple_input[3])
38
​
39
        result = findPoint(px, py, qx, qy)
40
​
41
        fptr.write(' '.join(map(str, result)))
42
        fptr.write('\n')
43
​
44
    fptr.close()
45
​
