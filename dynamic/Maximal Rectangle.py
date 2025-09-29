#Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# the idea is to find the maximal height on top of each element of array and see how many right and left columns have the same height in order to find the area
# Finally, the maximal rectabgle is one of the rectangles that we find with the above method. Clearly, it is not the problem of finding the maximal rectangle each element of the array belongs to that

# one approach to implement the above idea is to create a matrix height O(mn), and then find right and left -> O(m*n^2)

#the better approach is to consider an array of height, left and right and process row by row