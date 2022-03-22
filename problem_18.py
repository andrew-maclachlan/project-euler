# Problem 18
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-18-maximum-path-sum-i

def maximumPathSumI(triangle) ->int:
    """
    Returns the maximum sum of a path of ints in a triangle where only adjacent numbers can be moved to.
    e.g.
       1
      1 0
     0 1 0
    0 0 1 0
    """

    for i in range(0, len(triangle)-1):
        row = triangle[i]
        next_row = triangle[i+1]

        new_row = []
        for i,number in enumerate(row):
            x = number + next_row[i]
            y = number + next_row[i+1]
            if i == 0:
                new_row.append(x)
            else:
                new_row[i] = max(new_row[i],x)
            new_row.append(y)
            triangle[i+1] = new_row

    return max(new_row)

testTriangle = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]

actualTriangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]
