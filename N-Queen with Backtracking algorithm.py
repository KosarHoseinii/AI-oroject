#!/usr/bin/env python
# coding: utf-8

# In[29]:


from typing import List

class NQueensSolver:
    def __init__(self, n: int, verbose: bool = False) -> None:
        """
        Initialize the NQueensSolver class with the specified board size (n) and verbosity option (verbose).

        Args:
            n: The size of the chessboard and the number of queens to be placed.
            verbose: Whether to print verbose output during the solution process. Defaults to False.
        """
        self.n = n
        self.solution = []

        def place_queen(row: int, queens: List[int]) -> List[int]:
            """
            تابع بازگشتی برای جایگذاری وزیرها در صفحه شطرنج و پیدا کردن چینش معتبر

            Args:
                row: سطر درحال پردازش
                queens: لیستی که موقعیت وزیرها را ذخیره میکند

            Returns:
                موقعیت وزیرها در صورت وجود
            """
            if row == self.n:
                return queens

            for col in range(self.n):
                if all(
                    col != queens[c] and col != queens[c] + row - c and col != queens[c] - row + c
                    for c in range(row)
                ):
                    queens[row] = col
                    if verbose:
                        print(f"Placing Queen at Row {row} and Column {col}.")
                    if (result := place_queen(row + 1, queens)):
                        return result

            return None

        self.solution = place_queen(0, [None] * self.n)

    def get_chessboard(self) -> str:   #خروجی صفحه شطرنج بصورت یک رشته
        
        chessboard = ""
        for row in range(self.n):
            chessboard += "+---" * self.n + "+\n"
            for col in range(self.n):
                if self.solution[row] == col:
                    chessboard += "| Q "
                else:
                    chessboard += "|   "
            chessboard += "|\n"
        chessboard += "+---" * self.n + "+\n"
        return chessboard

    def display_chessboard(self) -> None:   #پرینت صفحه شطرنج
        
        print(self.get_chessboard())

    def get_solution_matrix(self) -> List[List[int]]:   #خروجی صفحه شطرنج بصورت ماتریس
        
        matrix = [[0] * self.n for _ in range(self.n)]
        for row, col in enumerate(self.solution):
            matrix[row][col] = 1
        return matrix

    def display_solution_matrix(self) -> None:   #پرینت صفحه شطرنج بصورت ماتریس
        
        for row in self.get_solution_matrix():
            print(' '.join(map(str, row)))
            
n = 4
solve = NQueensSolver(n, verbose=True)
#solve.display_chessboard()
#solve.display_solution_matrix()

