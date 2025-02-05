from os import system

sudoku_1="""
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
"""

sudoku_2="""
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
"""
sudoku_prueba="""
123456789
123456789
123456789
123456789
123456789
123456789
123456789
123456789
123456789
"""
def matrix_transpose(matrix):
    matrix_length = len(matrix)
    transpose_matrix = [[0 for i in range(matrix_length)] for j in range(matrix_length)]
    
    for i in range(matrix_length):
        for j in range(matrix_length):
            transpose_matrix[i][j] = matrix[j][i]
    return transpose_matrix

def total_sum(matrix):
    return sum([sum(i) for i in matrix])

def sub_matrix(matrix,i_start,i_end,j_start,j_end):
    submatrix = [[0 for i in range(3)]for i in range(3)]
    for i in range(i_start,i_end):
        for j in range(j_start, j_end):
            submatrix[i][j] = matrix[i][j]
    return submatrix
def check_sudoku (string):
    line_check = True
    #I create a list of lists here. Each original line is a list inside the sudoku list. I make every element to be an intenger:
    sudoku_matrix=[list([int(j) for j in i]) for i in string.split()]
    #print(sudoku_list)
    total_file = total_sum(sudoku_matrix)
    transposed_matrix = matrix_transpose(sudoku_matrix)
    total_column = total_sum(transposed_matrix)
    if total_column == 405 and total_file == 405:
        total_file = total_sum(sub_matrix(sudoku_matrix,0,2,0,2))
        total_column = total_sum(sub_matrix(matrix_transpose(sudoku_matrix),0,3,0,3))
        
        return total_file, total_column
        
    else:
        print("It is not a sudoku")
    return total_file , total_column
if __name__ == "__main__":
    system("cls || clear")
    #print(check_sudoku(sudoku_prueba))
    print(check_sudoku(sudoku_1))