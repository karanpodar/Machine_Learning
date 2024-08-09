'''
K Closest Points to Origin - less optimised 

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
'''

from math import sqrt

def k_closest_origin(arr, k):
    output = []
    dic = {}
    count = 0
    for i in arr:
        dist = sqrt( (0-i[0])**2 + (0-i[1])**2 )

        if dist in dic:
            count += 1
            dist += ( count / (10**4) )

        dic[dist] = i
    
    dic = dict(sorted(dic.items()))
    
    for i in range(k):

        output.append(list(dic.values())[i])
    
    return output

points = [[3,3],[5,-1],[-2,4]]
k = 2

print(k_closest_origin(points, k))

points = [[0,1],[1,0]]
k = 2

print(k_closest_origin(points, k))

points = [[2,2],[2,2],[3,3],[2,-2],[1,1]]
k = 4

print(k_closest_origin(points, k))