from random import randrange
from numpy import array, diagonal

try: size = int(input("Enter matrix size: "))
except ValueError: print("Enter correct matrix size")
else:
    print("Generated matrix:")
    matrix = [[randrange(10, 100) for j in range(size)] for i in range(size)]
    print(array(matrix), "\n")

    max_elem = max(diagonal(matrix))
    print("The maximum number of the main diagonal -", max_elem, "\n")

    new_array = array([[max_elem if i == j and matrix[i][j] == max_elem else matrix[i][j] / max_elem for i in range(size)] for j in range(size)])
    print("New matrix:\n", array([['%.2f' % elem for elem in a] for a in new_array]))
