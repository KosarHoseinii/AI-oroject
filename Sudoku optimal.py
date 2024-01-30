#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_valid(board, row, col, num):    #without changes
    # بررسی معتبر بودن عدد num در سطر و ستون
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    # بررسی معتبر بودن عدد num در بلوک 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def get_possible_values(board, row, col):   #additional method
    # مقادیر ممکن برای یک سلول با توجه به مقادیر قبلی در سطر، ستون و بلوک
    possible_values = set(range(1, 10))
    
    for i in range(9):
        possible_values.discard(board[row][i])
        possible_values.discard(board[i][col])
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            possible_values.discard(board[start_row + i][start_col + j])
    
    return list(possible_values)

def find_empty_location(board):
    # یافتن یک سلول خالی
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    # یافتن یک سلول خالی
    empty = find_empty_location(board)
    
    if not empty:
        # همه سلول‌ها پر شده و مسئله حل شده است
        return True
    
    row, col = empty
    
    possible_values = get_possible_values(board, row, col)     #using additional method
    
    for num in possible_values:
        if is_valid(board, row, col, num):
            # اگر عدد معتبر است، آن را در سلول قرار دهید
            board[row][col] = num
            
            # بازگشت به مرحله بعدی
            if solve_sudoku(board):
                return True
            
            # اگر به حل نرسید، عدد را حذف کنید و به عقب برگردید
            board[row][col] = 0
    
    # اگر هیچ عددی برای این سلول معتبر نبود، بازگشت به مرحله قبل
    return False


sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve_sudoku(sudoku_board)

for row in sudoku_board:
    print(row)

