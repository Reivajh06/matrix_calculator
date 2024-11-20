def is_square(matrix):
    """
    Evaluates whether a matrix is square or not
    :param matrix:
    :return: True if it is square, else False
    """
    for index in range(len(matrix)):
        if len(matrix) != len(matrix[index]):
            return False

    return True


def print_matrix(matrix):
    matrix_printed = ""
    for row in matrix:
        matrix_printed += str(row) + "\n"

    print(matrix_printed)


def create_matrix(rows, columns, elements):
    """
    Creates the desired matrix
    :param rows: Amount of rows the user matrix will have
    :param columns: Amount of columns the user matrix will have
    :param elements: Amount of elements within the matrix
    :return: prints the matrix created with the characteristics the user desired, if the amount of elements does not match with
    the amount of rows and columns it has (it has more or less elements than rows * columns) it will print a message
    """
    if len(elements) is not rows * columns:
        print(f"The number of elements introduced should be {rows * columns} instead of {len(elements)}")

    matrix = []

    for i in range(0, rows):
        row = []

        for j in range(0, columns):
            row.append(int(elements[j]))

        matrix.append(row)
        elements = elements[j + 1:]

    print_matrix(matrix)


def sum(matrix1, matrix2):
    ''' Method which adds a matrix to another one using the normal procedure, the elements in the same position add to make the element in the result matrix'''


    rows = len(matrix1)
    columns = len(matrix1[0])
    sum_result = []

    for i in range(rows):
        result_row = []
        for j in range(columns):
            addition = matrix1[i][j] + matrix2[i][j]
            result_row.append(addition)
        sum_result.append(result_row)
    return sum_result


def subtraction(matrix1, matrix2):
    ''' Method which subtracts a matrix to another one using the normal procedure, the elements in the same position subtract to make the element in the result matrix'''


    rows = len(matrix1)
    columns = len(matrix1[0])
    subtract_result = []

    for i in range(rows):
        result_row = []
        for j in range(columns):
            difference = matrix1[i][j] - matrix2[i][j]
            result_row.append(difference)
        subtract_result.append(result_row)
    return subtract_result



def trace(matrix):
    """
    Method which evaluate the trace of a square matrix
    :param matrix:
    :return: diagonal sum if it is a square matrix, else return a string advice
    """
    trace_result = 0

    if is_square(matrix):

        for i in range(len(matrix)):
            trace_result += matrix[i][i]

        return trace_result

    return f"The given matrix: \n{print_matrix(matrix)}is not a square matrix!"


def determinant(matrix):
    """
    Method which calculates the determinant of a square matrix
    :param matrix:
    :return: determinant of a square matrix
    """

    if is_square(matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant_result: int = 0

        for j in range(len(matrix)):
            #Using the cofactors method, recursive is required, being the square matrix of 2 the base case
            cofactor_matrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
            determinant_result += (-1) ** j * matrix[0][j] * determinant(cofactor_matrix)

        return determinant_result

    return f"The given matrix: \n{print_matrix(matrix)}is not a square matrix!"
