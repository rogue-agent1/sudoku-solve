#!/usr/bin/env python3
"""Sudoku solver using backtracking."""
import sys

def solve(board):
    empty = find_empty(board)
    if not empty: return True
    r, c = empty
    for n in range(1, 10):
        if valid(board, r, c, n):
            board[r][c] = n
            if solve(board): return True
            board[r][c] = 0
    return False

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0: return r, c
    return None

def valid(board, r, c, n):
    if n in board[r]: return False
    if n in [board[i][c] for i in range(9)]: return False
    br, bc = 3*(r//3), 3*(c//3)
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if board[i][j] == n: return False
    return True

def parse(s):
    s = s.replace('.', '0').replace(' ', '').replace('\n', '')
    return [[int(s[i*9+j]) for j in range(9)] for i in range(9)]

def fmt(board):
    lines = []
    for i, row in enumerate(board):
        if i % 3 == 0 and i: lines.append('------+-------+------')
        nums = [str(n) if n else '.' for n in row]
        lines.append(f"{nums[0]} {nums[1]} {nums[2]} | {nums[3]} {nums[4]} {nums[5]} | {nums[6]} {nums[7]} {nums[8]}")
    return '\n'.join(lines)

if __name__ == '__main__':
    if len(sys.argv) < 2: print("Usage: sudoku_solve.py <81-char-puzzle>"); sys.exit(1)
    board = parse(sys.argv[1])
    print("Puzzle:"); print(fmt(board)); print()
    if solve(board): print("Solution:"); print(fmt(board))
    else: print("No solution found.")
