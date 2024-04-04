def sum_up_diagonals(matrix):

    output = 0

    for i in range(len(matrix)):
        output += matrix[i][i]
        output += matrix[i][-1 - i]
    return output
"""Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:"""

m1 = [[1,   2],
      [30, 40],]

print(sum_up_diagonals(m1))
"73"

m2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      ]
print(sum_up_diagonals(m2))
"30"