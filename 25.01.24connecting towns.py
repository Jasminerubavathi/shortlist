#Cities on a map are connected by a number of roads. The number of roads between each city is in an array and city  is the starting location. The number of roads from city  to city  is the first value in the array, from city  to city  is the second, and so on.

#How many paths are there from city  to the last city in the list, modulo ?

#Example


#There are  roads to city ,  roads to city  and  roads to city . The total number of roads is .

#Note
#Pass all the towns Ti for i=1 to n-1 in numerical order to reach Tn.

#Function Description

#Complete the connectingTowns function in the editor below.

#connectingTowns has the following parameters:

#int n: the number of towns
#int routes[n-1]: the number of routes between towns
#Returns

#int: the total number of routes, modulo 1234567.
#Input Format
#The first line contains an integer T, T test-cases follow.

#Each test-case has 2 lines.
#The first line contains an integer N (the number of towns).
#The second line contains N - 1 space separated integers where the ith integer denotes the number of routes, Ni, from the town Ti to Ti+1

#Constraints
#1 <= T<=1000
#2< N <=100
#1 <= routes[i] <=1000

#Sample Input

#2
#3
#1 3
#4
#2 2 2
#Sample Output

#3
#8
#Explanation
#Case 1: 1 route from T1 to T2, 3 routes from T2 to T3, hence only 3 routes.
#case 2: There are 2 routes from each city to the next, hence 2 * 2 * 2 = 8.

#Submissions: 147
#Max Score: 10
#Difficulty: Easy
#Rate This Challenge:

    
#More
 
#1
#!/bin/python3
#2
​
#3
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
# Complete the 'connectingTowns' function below.
11
#
12
# The function is expected to return an INTEGER.
13
# The function accepts following parameters:
14
#  1. INTEGER n
15
#  2. INTEGER_ARRAY routes
16
#
17
​
18
def connectingTowns(n, routes):
19
    # Write your code here
20
    total_routes = 1
21
    for num_routes in routes:
22
        total_routes = (total_routes * num_routes) % 1234567
23
​
24
    return total_routes
25
​
26
​
27
if __name__ == '__main__':
28
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
29
​
30
    t = int(input().strip())
31
​
32
    for t_itr in range(t):
33
        n = int(input().strip())
34
​
35
        routes = list(map(int, input().rstrip().split()))
36
​
37
        result = connectingTowns(n, routes)
38
​
39
        fptr.write(str(result) + '\n')
40
​
41
    fptr.close()
