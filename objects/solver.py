__all__ = ('board', 'solve')

board = [
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(board):
  pos = find_empty(board)
  if not pos:
    return True
  else:
    row, col = pos
  
  for num in range(1, 10):
    if is_valid(board, num, pos):
      board[row][col] = num

      if solve(board):
        return True
      
      board[row][col] = 0
  return False


def is_valid(board, num, pos):
  # check the row
  for c in range(len(board[0])):
    if pos[1] != c and board[pos[0]][c] == num:
      return False

  # check the column
  for r in range(len(board)):
    if pos[0] != r and board[r][pos[1]] == num:
      return False
  
  # check the box itself
  box_r = pos[0] // 3
  box_c = pos[1] // 3
  
  for r in range(box_r*3, box_r*3 + 3):
    for c in range(box_c*3, box_c*3 + 3):
      if (r, c) != pos and board[r][c] == num:
        return False
  
  return True
      

def find_empty(board):
  for r in range(len(board)):
    for c in range(len(board[0])):
      if board[r][c] == 0:
        return (r, c)
