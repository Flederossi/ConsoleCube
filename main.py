import os
import math
import time

def matrix_mult(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)

    res_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]

    if columns_a == rows_b:
        for x in range(rows_a):
            for y in range(columns_b):
                sum = 0
                for k in range(columns_a):
                    sum += a[x][k] * b[k][y]
                res_matrix[x][y] = sum
        return res_matrix
    else:
        return None

width, height = 50, 50
angle = 0
cube_position = [width//2, height//2]
scale = 50
speed = 0.04
points = [n for n in range(8)]
density = 1

curr_line = ""
changed = False

points[0] = [[-1], [-1], [1]]
points[1] = [[1], [-1], [1]]
points[2] = [[1], [1], [1]]
points[3] = [[-1], [1], [1]]
points[4] = [[-1], [-1], [-1]]
points[5] = [[1], [-1], [-1]]
points[6] = [[1], [1], [-1]]
points[7] = [[-1], [1], [-1]]

for i in range(-10, 10, density):
    #Kanten unten
    points.append([[i/10], [-1], [-1]])
    points.append([[i/10], [-1], [1]])
    points.append([[-1], [-1], [i/10]])
    points.append([[1], [-1], [i/10]])

    #Kanten mitte
    points.append([[-1], [i/10], [-1]])
    points.append([[1], [i/10], [-1]])
    points.append([[-1], [i/10], [1]])
    points.append([[1], [i/10], [1]])

    #Kanten oben
    points.append([[i/10], [1], [-1]])
    points.append([[i/10], [1], [1]])
    points.append([[-1], [1], [i/10]])
    points.append([[1], [1], [i/10]])

while True:
    index = 0
    projected_points = [j for j in range(len(points))]

    rotation_x = [[1, 0, 0],
                  [0, math.cos(angle), -math.sin(angle)],
                  [0, math.sin(angle), math.cos(angle)]]

    rotation_y = [[math.cos(angle), 0, -math.sin(angle)],
                  [0, 1, 0],
                  [math.sin(angle), 0, math.cos(angle)]]

    rotation_z = [[math.cos(angle), -math.sin(angle), 0],
                  [math.sin(angle), math.cos(angle), 0],
                  [0, 0, 1]]
    
    for point in points:
        rotated_2d = matrix_mult(rotation_y, point)
        rotated_2d = matrix_mult(rotation_x, rotated_2d)
        rotated_2d = matrix_mult(rotation_z, rotated_2d)

        distance = 5

        z = 1 / (distance - rotated_2d[2][0])
        projection_matrix = [[z, 0, 0],
                             [0, z, 0]]
        projected2d = matrix_mult(projection_matrix, rotated_2d)

        x = int(projected2d[0][0] * scale) + cube_position[0]
        y = int(projected2d[1][0] * scale) + cube_position[1]

        projected_points[index] = [x, y]

        index += 1
    
    os.system("cls")
    for h in range(height):
        curr_line = ""
        for w in range(width):
            for point in projected_points:
                if point == [w, h]:
                    if projected_points.index(point) > 7:
                        curr_line += " °"
                    else:
                        curr_line += " @"
                    changed = True
                    break
            if changed == False:
                curr_line += "  "
            changed = False
        print(curr_line)         

    angle += speed
    time.sleep(0.001)