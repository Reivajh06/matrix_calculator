import re


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
    print(matrix_to_string(matrix))


def matrix_to_string(matrix):
    matrix_str = ""

    for row in matrix:
        matrix_str += str(row) + "\n"

    return matrix_str


def create_matrix():
    """
    Creates the desired matrix
    :return: prints the matrix created with the characteristics the user desired, if the amount of elements does not match with
    the amount of rows and columns it has (it has more or less elements than rows * columns) it will print a message
    """
    rows = int(input("Introduce how many rows the matrix has: "))

    columns = int(input("Introduce how many columns the matrix has: "))

    elements = re.split(" +", input("Introduce each element within the matrix separated by single spaces: ").strip())

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
    print("----------------------\n")

    return matrix


def add(matrix1, matrix2):
    ''' Method which adds a matrix to another one using the normal procedure, the elements in the same position add to make the element in the result matrix'''
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: The dimensions of the matrices do not match, cannot add.")
        return None 

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


def subtract(matrix1, matrix2):
    ''' Method which subtracts a matrix to another one using the normal procedure, the elements in the same position subtract to make the element in the result matrix'''
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: The dimensions of the matrices do not match, cannot add.")
        return None 

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


def multiply(matrix1, matrix2):
    """
    Method which multiplies two matrices using the normal procedure.
    Method which multiplies two matrices using the normal procedure.
    There must be the same number of columns in matrix1 as there are rows in matrix2
    """
    rows_1 = len(matrix1)
    columns_1 = len(matrix1[0])
    rows_2 = len(matrix2)
    columns_2 = len(matrix2[0])
    if columns_1 != rows_2:
        result = 'These two matrices cannot be multiplied'
        return result
    result = [[0 for number_2 in range(columns_2)] for number_1 in range(rows_1)]
    for num_row1 in range(rows_1):
        for num_col2 in range(columns_2):
            for num_col1 in range(columns_1):
                result[num_row1][num_col2] += matrix1[num_row1][num_col1] * matrix2[num_col1][num_col2]
    return result


def transpose(matrix):
    """
    Method which calculates the transposed matrix of a matrix.
    """
    rows_trans = len(matrix[0])
    columns_trans = len(matrix)
    transposed_matrix = [[0] * columns_trans for number in range(rows_trans)]
    for num_row in range(rows_trans):
        for num_col in range(columns_trans):
            transposed_matrix[num_row][num_col] = matrix[num_col][num_row]
    return transposed_matrix


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



def multiply_scalar(matrix, scalar):
    """
    Method which calculates the multiplication of a matrix
    by a scalar number, returning a new matrix.
    """
    multipled_matrix = []
    
    for row in matrix:
        row_list = []
        for column in row:
            row_list.append(column * scalar)
        multipled_matrix.append(row_list)
        
    return multipled_matrix


def identity_matrix(matrix):
    """
    Method that creates a identity matrix, which has a 1 in the same position vertically 
    and horizontally and a 0 in the rest of the identity matrix. The size of the 
    identity matrix depends on the size of the matrix used as a parameter.
    """
    size = len(matrix)
    
    if not is_square(matrix):
        return "The matrix's columns and rows have different sizes"
    
    identity_matrix = []
    
    for row in range(size):
        row_identity = []
        for column in range(size):
            row_identity.append(0)
        identity_matrix.append(row_identity)

    for i in range(size):
        identity_matrix[i][i] = 1
        
    return identity_matrix
